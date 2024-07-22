from fastapi import FastAPI
import uvicorn
from iriurisk_test.app_config import get_config
from iriurisk_test.api.routes import health_check
from iriurisk_test.api.routes import chat_route

app = FastAPI(title="iriurisk tech test",debug=True)

app.include_router(health_check.router, prefix="/health_check", tags=["health_check"])
app.include_router(chat_route.router, prefix="/chat", tags=["GPT CHAT"])

def run() -> None:
    """
    Run uvicorn server ro serve Fastapi application
    """
    config = get_config()

    uvicorn.run(
        "iriurisk_test.main:app",
        host=config.api_host,
        port=config.api_port,
        workers=2,
        reload=config.api_reload,
    )


if __name__ == "__main__":
    run()
