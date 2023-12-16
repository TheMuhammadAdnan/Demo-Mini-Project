from fastapi import APIRouter

from app.api.handlers import (
    health,
    orders
)
from app.configs.env import env

# Route: /conversation-management-service/api/v1/
router = APIRouter(prefix=f"/{env.APP_NAME}/api/v1", tags=["root"])

# Route: /health/
health.router.get("/")(health.get_health)

router.include_router(health.router, prefix="/health", tags=["health"])

# Route: /orders/
orders.router.get("/{customer_id}")(orders.get_orders)

router.include_router(orders.router, prefix="/orders", tags=["orders"])
