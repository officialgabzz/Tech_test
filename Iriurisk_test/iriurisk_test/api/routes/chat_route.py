from fastapi import APIRouter, status
from typing import Dict, Optional
from iriurisk_test.app_logging import get_logger
from iriurisk_test.clients.gpt_client import GPTClient
from iriurisk_test.application.chat_logic import get_chat_response
from iriurisk_test.prompts import custom_prompt

from pydantic import BaseModel


class UserMessage(BaseModel):
    content: str = ""


router = APIRouter()
logger = get_logger()


@router.post(path="", status_code=status.HTTP_200_OK)
async def chat(user_message: UserMessage) -> Optional[Dict[str, str]]:
    client = GPTClient()
    logger.info("request sent to gpt")
    response = get_chat_response(
        client=client, user_message=user_message.content, prompt=custom_prompt
    )
    logger.info("response received from gpt")
    return {"msg": response}
