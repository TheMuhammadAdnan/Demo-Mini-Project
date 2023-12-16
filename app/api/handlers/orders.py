import httpx
from fastapi import (
    APIRouter,
    Query,
    HTTPException,
    Depends
)
from http import HTTPStatus
from app.infrastructure.logger import logger

from app.models.response import (
    Response,
)
from app.clients.shopify_client.shopify_client import get_orders_by_customer_id

router = APIRouter()

def validate_status(status: str = 'any'):
    allowed_statuses = ['any', 'shipped', 'pending', 'completed']
    if status not in allowed_statuses:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY.value, detail='Invalid status parameter')
    return status

def get_orders(customer_id: int,
               status: str = Depends(validate_status)
               ) -> Response:
    logger.info(f"Getting Orders for customer id {customer_id}")
    orders_response = get_orders_by_customer_id(customer_id, status)
    response = {
        "result": orders_response.json(),
    }
    return Response.build_success_response(response)
