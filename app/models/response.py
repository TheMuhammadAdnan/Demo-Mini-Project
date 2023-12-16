import http
from typing import Any

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.utils.helpers import camelize


class CustomJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return super().render(self.camel_keys(content))

    @staticmethod
    def camel_keys(data):
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                new_key = camelize(key)
                new_dict[new_key] = CustomJSONResponse.camel_keys(value)
            return new_dict
        elif isinstance(data, list):
            return [CustomJSONResponse.camel_keys(value) for value in data]
        else:
            return data


class Response(BaseModel):
    status: str
    errors: str
    data: Any | None = {}

    def build_success_response(data=None, status_code=http.HTTPStatus.OK):
        if data is None:
            data = {}

        response = Response(
            status="success",
            errors="",
            data=data,
        )

        body = jsonable_encoder(response)

        return CustomJSONResponse(
            status_code=status_code,
            content=body,
        )

    @staticmethod
    def build_error_response(errors="something went wrong", status_code=http.HTTPStatus.BAD_REQUEST):
        response = Response(
            status="error",
            errors=errors,
            data={}
        )

        body = jsonable_encoder(response)

        return CustomJSONResponse(
            status_code=status_code,
            content=body,
        )
