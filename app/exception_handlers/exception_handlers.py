import sys
from typing import Union

from fastapi import Request
from fastapi.exceptions import (
    RequestValidationError,
    HTTPException
)
from fastapi.responses import (
    JSONResponse,
    PlainTextResponse,
    Response
)

from app.infrastructure.logger import logger
from app.models.response import Response as CustomResponse


async def request_validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    This is a wrapper to the default RequestValidationException handler of FastAPI.
    This function will be called when client input is not valid.
    """
    route = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
    logger.error(f"Endpoint {request.method}: {route} Request validation failed error: {exc.__str__()}")
    return CustomResponse.build_error_response(exc.__str__())


async def http_exception_handler(request: Request, exc: HTTPException) -> Union[JSONResponse, Response]:
    """
    This is a wrapper to the default HTTPException handler of FastAPI.
    This function will be called when a HTTPException is explicitly raised.
    """
    return CustomResponse.build_error_response(errors=exc.detail, status_code=exc.status_code)


async def unhandled_exception_handler(request: Request, exc: Exception) -> PlainTextResponse:
    """
    This middleware will log all unhandled exceptions.
    Unhandled exceptions are all exceptions that are not HTTPExceptions or RequestValidationErrors.
    """
    url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
    exception_type, exception_value, exception_traceback = sys.exc_info()
    exception_name = getattr(exception_type, "__name__", None)
    logger.error(f"Endpoint {request.method}: {url} 500 Internal Server Error <{exception_name}: {exception_value}>")
    for exc_exception in exc.args:
        logger.error(exc_exception)
    return CustomResponse.build_error_response()
