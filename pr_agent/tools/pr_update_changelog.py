import copy
import json
import logging
import textwrap
from datetime import date
from typing import Tuple

from jinja2 import Environment, StrictUndefined

from pr_agent.algo.ai_handler import AiHandler
from pr_agent.algo.pr_processing import get_pr_diff, retry_with_fallback_models
from pr_agent.algo.token_handler import TokenHandler
from pr_agent.config_loader import settings
from pr_agent.git_providers import get_git_provider, GithubProvider
from pr_agent.git_providers.git_provider import get_main_pr_language

CHANGELOG_LINES = 50


class PRUpdateChangelog:
    def __init__(self, pr_url: str, cli_mode=False):

        self.git_provider = get_git_provider()(pr_url)
        self.main_language = get_main_pr_language(
            self.git_provider.get_languages(), self.git_provider.get_files()
        )
        try:
            self.changelog_file = self.git_provider.repo_obj.get_contents("CHANGELOG.md",
                                                                          ref=self.git_provider.get_pr_branch())
            changelog_file_lines = self.changelog_file.decoded_content.decode().splitlines()
            changelog_file_lines = changelog_file_lines[:CHANGELOG_LINES]
            self.changelog_file_str = "\n".join(changelog_file_lines)
        except:
            raise Exception("No CHANGELOG.md file found in the repository")

        today = date.today()
        print("Today's date:", today)

        self.ai_handler = AiHandler()
        self.patches_diff = None
        self.prediction = None
        self.cli_mode = cli_mode
        self.vars = {
            "title": self.git_provider.pr.title,
            "branch": self.git_provider.get_pr_branch(),
            "description": self.git_provider.get_pr_description(),
            "language": self.main_language,
            "diff": "",  # empty diff for initial calculation
            "changelog_file": self.changelog_file_str,
            "today": today,
        }
        self.token_handler = TokenHandler(self.git_provider.pr,
                                          self.vars,
                                          settings.pr_update_changelog_prompt.system,
                                          settings.pr_update_changelog_prompt.user)

    async def update_changelog(self):
        assert type(self.git_provider) == GithubProvider, "Currently only Github is supported"

        logging.info('Updating the changelog...')
        if settings.config.publish_output:
            self.git_provider.publish_comment("Preparing changelog updates...", is_temporary=True)
        await retry_with_fallback_models(self._prepare_prediction)
        logging.info('Preparing PR changelog updates...')
        new_file_content, answer = self._prepare_changelog_update()
        if settings.config.publish_output:
            self.git_provider.remove_initial_comment()
            logging.info('publishing changelog updates...')
            self.git_provider.publish_comment(f"**Changelog updates:**\n\n{answer}")
            if settings.pr_update_changelog.push_changelog_changes:
                logging.info('Pushing PR changelog updates...')
                self.push_changelog_update(new_file_content)

    async def _prepare_prediction(self, model: str):
        logging.info('Getting PR diff...')
        # we are using extended hunk with line numbers for code suggestions
        self.patches_diff = get_pr_diff(self.git_provider,
                                        self.token_handler,
                                        model,
                                        add_line_numbers_to_hunks=True,
                                        disable_extra_lines=True)
        logging.info('Getting AI prediction...')
        self.prediction = await self._get_prediction(model)

    async def _get_prediction(self, model: str):
        variables = copy.deepcopy(self.vars)
        variables["diff"] = self.patches_diff  # update diff
        environment = Environment(undefined=StrictUndefined)
        system_prompt = environment.from_string(settings.pr_update_changelog_prompt.system).render(variables)
        user_prompt = environment.from_string(settings.pr_update_changelog_prompt.user).render(variables)
        if settings.config.verbosity_level >= 2:
            logging.info(f"\nSystem prompt:\n{system_prompt}")
            logging.info(f"\nUser prompt:\n{user_prompt}")
        response, finish_reason = await self.ai_handler.chat_completion(model=model, temperature=0.2,
                                                                        system=system_prompt, user=user_prompt)

        return response

    def _prepare_changelog_update(self) -> Tuple[str, str]:
        answer = self.prediction.strip().strip("```").strip()
        new_file_content = answer + "\n\n" + self.changelog_file.decoded_content.decode()
        if settings.config.verbosity_level >= 2:
            logging.info(f"answer:\n{answer}")
        return new_file_content, answer

    def push_changelog_update(self, new_file_content):
        self.git_provider.repo_obj.update_file(path=self.changelog_file.path,
                                               message="Update CHANGELOG.md",
                                               content=new_file_content,
                                               sha=self.changelog_file.sha,
                                               branch=self.git_provider.get_pr_branch())
