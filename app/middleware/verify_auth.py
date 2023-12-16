from fastapi import (
    Request,
)

from app.infrastructure.logger import logger



async def verify_auth(request: Request, call_next):
    try:
        logger.info("Verifying authentication")

        # no authentication implemented yet

        return await call_next(request)
    except Exception as e:
        logger.error(f"Error during authentication: {str(e)}")
