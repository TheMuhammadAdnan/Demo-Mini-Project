from fastapi import APIRouter

from app.infrastructure.logger import logger
from app.models.response import Response

router = APIRouter()


def get_health():
    logger.info(f"Getting health of service")

    data = {'status': 'UP'}

    return Response.build_success_response(data)
