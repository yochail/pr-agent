# This file contains the code for the Azure DevOps Server webhook server.
<<<<<<< HEAD
#   The server listens for incoming webhooks from Azure DevOps Server and forwards them to the PR Agent.
#   ADO webhook documentation: https://learn.microsoft.com/en-us/azure/devops/service-hooks/services/webhooks?view=azure-devops
=======
# The server listens for incoming webhooks from Azure DevOps Server and forwards them to the PR Agent.
# ADO webhook documentation: https://learn.microsoft.com/en-us/azure/devops/service-hooks/services/webhooks?view=azure-devops
>>>>>>> yochail/support_azure_devops_webhook_pr

import json
import os
import re
<<<<<<< HEAD

import uvicorn
from fastapi import APIRouter, FastAPI
=======
import secrets
import uvicorn
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
>>>>>>> yochail/support_azure_devops_webhook_pr
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.background import BackgroundTasks
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette_context.middleware import RawContextMiddleware

from pr_agent.agent.pr_agent import PRAgent, command2class
from pr_agent.config_loader import get_settings
from pr_agent.log import get_logger
<<<<<<< HEAD
import base64

router = APIRouter()
available_commands_rgx = re.compile(r"^\/(" + "|".join(command2class.keys()) + r")\s*")
azuredevops_server = get_settings().get("azure_devops")
=======
from fastapi import Request, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pr_agent.log import get_logger

security = HTTPBasic()
router = APIRouter()
available_commands_rgx = re.compile(r"^\/(" + "|".join(command2class.keys()) + r")\s*")
azuredevops_server = get_settings().get("azure_devops_server")
>>>>>>> yochail/support_azure_devops_webhook_pr
WEBHOOK_USERNAME = azuredevops_server.get("webhook_username")
WEBHOOK_PASSWORD = azuredevops_server.get("webhook_password")

def handle_request(
    background_tasks: BackgroundTasks, url: str, body: str, log_context: dict
):
    log_context["action"] = body
    log_context["api_url"] = url
    with get_logger().contextualize(**log_context):
        background_tasks.add_task(PRAgent().handle_request, url, body)


<<<<<<< HEAD
@router.post("/")
=======
# currently only basic auth is supported with azure webhooks
# for this reason, https must be enabled to ensure the credentials are not sent in clear text
def authorize(credentials: HTTPBasicCredentials = Depends(security)):
        is_user_ok = secrets.compare_digest(credentials.username, WEBHOOK_USERNAME)
        is_pass_ok = secrets.compare_digest(credentials.password, WEBHOOK_PASSWORD)
        if not (is_user_ok and is_pass_ok):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorrect username or password.',
                headers={'WWW-Authenticate': 'Basic'},
            )
        
@router.post("/", dependencies=[Depends(authorize)])
>>>>>>> yochail/support_azure_devops_webhook_pr
async def handle_webhook(background_tasks: BackgroundTasks, request: Request):
    log_context = {"server_type": "azuredevops_server"}
    data = await request.json()
    get_logger().info(json.dumps(data))

<<<<<<< HEAD
    if not validate_basic_auth(request):
        get_logger().error("Unauthorized webhook request")
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=json.dumps({"message": "unauthorized"}),
        )

    if data["eventType"] == "git.pullrequest.created": 
        body = "review"
        # API V1 (latest)
        pr_url = data["resource"]["_links"]["web"]["href"].replace("_apis/git/repositories", "_git")
=======
    actions = []
    if data["eventType"] == "git.pullrequest.created": 
        # API V1 (latest)
        pr_url = data["resource"]["_links"]["web"]["href"].replace("_apis/git/repositories", "_git")
        if get_settings().get("github_action_config").get("auto_review") == True:
            actions.append("review")
        if get_settings().get("github_action_config").get("auto_improve") == True:
            actions.append("improve")
        if get_settings().get("github_action_config").get("describe") == True:
            actions.append("describe")
            
>>>>>>> yochail/support_azure_devops_webhook_pr
    elif data["eventType"] == "ms.vss-code.git-pullrequest-comment-event":
        if available_commands_rgx.match(data["resource"]["comment"]["content"]):
            if(data["resourceVersion"] == "2.0"):
                repo = data["resource"]["pullRequest"]["repository"]["webUrl"]
                pr_url = f'{repo}/pullrequest/{data["resource"]["pullRequest"]["pullRequestId"]}'
<<<<<<< HEAD
                body = data["resource"]["comment"]["content"]
=======
                actions = [data["resource"]["comment"]["content"]]
>>>>>>> yochail/support_azure_devops_webhook_pr
            else: 
                # API V1 not supported as it does not contain the PR URL
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content=json.dumps({"message": "version 1.0 webhook for Azure Devops PR comment is not supported. please upgrade to version 2.0"})),
        else:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=json.dumps({"message": "Unsupported command"}),
            )
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=json.dumps({"message": "Unsupported event"}),
        )

    log_context["event"] = data["eventType"]
    log_context["api_url"] = pr_url
    
<<<<<<< HEAD
    try:
        handle_request(background_tasks, pr_url, body, log_context)
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder({"message": "success"})
        )
    except Exception as e:
        get_logger().error("Azure DevOps Trigger failed. Error:" + str(e))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=json.dumps({"message": "Internal server error"}),
        )

# currently only basic auth is supported with azure webhooks
def validate_basic_auth(request: Request):
    auth = request.headers.get("Authorization")
    if not auth:
        return False
    if not auth.startswith("Basic "):
        return False
    decoded_auth = base64.b64decode(auth.split(" ")[1]).decode()
    username, password = decoded_auth.split(":")
    return username == WEBHOOK_USERNAME and password == WEBHOOK_PASSWORD

=======
    for action in actions:
        try:
            handle_request(background_tasks, pr_url, action, log_context)
        except Exception as e:
            get_logger().error("Azure DevOps Trigger failed. Error:" + str(e))
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps({"message": "Internal server error"}),
            )
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder({"message": "webhook triggerd successfully"})
    )

        
>>>>>>> yochail/support_azure_devops_webhook_pr
def start():
    app = FastAPI(middleware=[Middleware(RawContextMiddleware)])
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "3000")))

if __name__ == "__main__":
    start()