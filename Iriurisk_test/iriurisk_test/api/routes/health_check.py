from fastapi import APIRouter, status
from typing import Dict, Optional

router = APIRouter()


@router.get(path="", status_code=status.HTTP_200_OK)
async def health_check() -> Optional[Dict[str, str]]:
    return {"msg": "API is running .."}
