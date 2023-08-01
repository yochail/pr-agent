import os
import shlex
import tempfile

from pr_agent.algo.utils import update_settings_from_args
from pr_agent.config_loader import get_settings
from pr_agent.git_providers import get_git_provider
from pr_agent.tools.pr_code_suggestions import PRCodeSuggestions
from pr_agent.tools.pr_description import PRDescription
from pr_agent.tools.pr_information_from_user import PRInformationFromUser
from pr_agent.tools.pr_questions import PRQuestions
from pr_agent.tools.pr_reviewer import PRReviewer
from pr_agent.tools.pr_update_changelog import PRUpdateChangelog

command2class = {
    "answer": PRReviewer,
    "review": PRReviewer,
    "review_pr": PRReviewer,
    "reflect": PRInformationFromUser,
    "reflect_and_review": PRInformationFromUser,
    "describe": PRDescription,
    "describe_pr": PRDescription,
    "improve": PRCodeSuggestions,
    "improve_code": PRCodeSuggestions,
    "ask": PRQuestions,
    "ask_question": PRQuestions,
    "update_changelog": PRUpdateChangelog,
}

commands = list(command2class.keys())

class PRAgent:
    def __init__(self):
        pass

    async def handle_request(self, pr_url, request) -> bool:
        # First, apply repo specific settings if exists
        if get_settings().config.use_repo_settings_file:
            repo_settings_file = None
            try:
                git_provider = get_git_provider()(pr_url)
                repo_settings = git_provider.get_repo_settings()
                if repo_settings:
                    repo_settings_file = None
                    fd, repo_settings_file = tempfile.mkstemp(suffix='.toml')
                    os.write(fd, repo_settings)
                    get_settings().load_file(repo_settings_file)
            finally:
                if repo_settings_file:
                    os.remove(repo_settings_file)

        # Then, apply user specific settings if exists
        request = request.replace("'", "\\'")
        lexer = shlex.shlex(request, posix=True)
        lexer.whitespace_split = True
        action, *args = list(lexer)
        args = update_settings_from_args(args)

        action = action.lstrip("/").lower()
        if action == "reflect_and_review" and not get_settings().pr_reviewer.ask_and_reflect:
            action = "review"
        if action == "answer":
            await PRReviewer(pr_url, is_answer=True, args=args).run()
        elif action in command2class:
            await command2class[action](pr_url, args=args).run()
        else:
            return False
        return True
