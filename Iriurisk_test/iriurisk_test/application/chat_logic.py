from iriurisk_test.clients import gpt_client
from typing import Optional
from iriurisk_test.prompts import Prompt
from iriurisk_test.app_config import get_config
from iriurisk_test.app_logging import get_logger

from fastapi import HTTPException, status

CONFIG = get_config()
logger = get_logger()


def get_chat_response(
    client: gpt_client.GPTClient, user_message: str, prompt: Prompt
) -> Optional[str]:
    """
    Retrieves a response from a GPT client based on the user's message and a given prompt.

    This function attempts to obtain a response from a GPT model by sending the user's
    message and a system prompt to the provided GPT client. It includes a retry mechanism
    to handle potential failures in communication with the GPT model. If the maximum number
    of retries is exceeded and no response is obtained, an HTTP 500 error is raised.

    Args:
        client (gpt_client.GPTClient): An instance of the GPT client used to interact with the GPT model.
        user_message (str): The message input from the user.
        prompt (Prompt): The system prompt to guide the GPT model's response.

    Returns:
        Optional[str]: The response from the GPT model if successful.

    Raises:
        HTTPException: If the GPT model is busy and a response cannot be obtained after
                       the maximum number of retries.
    """

    retry = 0
    response = None
    while retry <= CONFIG.gpt_max_retries:
        try:
            response = client.get_response(
                user_message=user_message, system_message=prompt
            )
        except Exception as err:
            logger.info(f"retry: {retry}")
            retry += 1
            logger.error(err)
    if response:
        return response
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="LLM MODEL BUSY"
    )
