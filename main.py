from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError


from app.api.router import router
from app.models.response import CustomJSONResponse
from app.middleware.log_requests import log_requests

from app.exception_handlers.exception_handlers import (
    request_validation_exception_handler,
    http_exception_handler,
    unhandled_exception_handler,
)


def create_application() -> FastAPI:
    application = FastAPI(default_response_class=CustomJSONResponse)
    application.include_router(router)

    return application


app = create_application()


@app.on_event("startup")
def startup():
    pass


@app.on_event("shutdown")
def shutdown():
    pass


app.add_middleware(
    BaseHTTPMiddleware,
    dispatch=log_requests
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)
