import time

from fastapi import Request

from app.infrastructure.logger import logger


async def log_requests(request: Request, call_next):
    start_time = time.time()

    route = request.url.path

    logger.info(f"Endpoint {request.method}: {route} called")

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000

    formatted_process_time = '{0:.2f}'.format(process_time)

    logger.info(f"Endpoint {request.method}: {route} returned with time {formatted_process_time}ms")

    return response
