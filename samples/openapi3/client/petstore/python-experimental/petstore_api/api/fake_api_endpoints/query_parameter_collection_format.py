# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3

from petstore_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from petstore_api.model.string_with_validation import StringWithValidation

# query params


class PipeSchema(
    ListSchema
):
    _items = StrSchema


class IoutilSchema(
    ListSchema
):
    _items = StrSchema


class HttpSchema(
    ListSchema
):
    _items = StrSchema


class UrlSchema(
    ListSchema
):
    _items = StrSchema


class ContextSchema(
    ListSchema
):
    _items = StrSchema
RefParamSchema = StringWithValidation
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
        'pipe': PipeSchema,
        'ioutil': IoutilSchema,
        'http': HttpSchema,
        'url': UrlSchema,
        'context': ContextSchema,
        'refParam': RefParamSchema,
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_pipe = api_client.QueryParameter(
    name="pipe",
    style=api_client.ParameterStyle.FORM,
    schema=PipeSchema,
    required=True,
    explode=True,
)
request_query_ioutil = api_client.QueryParameter(
    name="ioutil",
    style=api_client.ParameterStyle.FORM,
    schema=IoutilSchema,
    required=True,
)
request_query_http = api_client.QueryParameter(
    name="http",
    style=api_client.ParameterStyle.SPACE_DELIMITED,
    schema=HttpSchema,
    required=True,
)
request_query_url = api_client.QueryParameter(
    name="url",
    style=api_client.ParameterStyle.FORM,
    schema=UrlSchema,
    required=True,
)
request_query_context = api_client.QueryParameter(
    name="context",
    style=api_client.ParameterStyle.FORM,
    schema=ContextSchema,
    required=True,
    explode=True,
)
request_query_ref_param = api_client.QueryParameter(
    name="refParam",
    style=api_client.ParameterStyle.FORM,
    schema=RefParamSchema,
    required=True,
    explode=True,
)
_path = '/fake/test-query-paramters'
_method = 'PUT'


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: Unset = unset
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
)
_status_code_to_response = {
    '200': _response_for_200,
}


class QueryParameterCollectionFormat(api_client.Api):

    def query_parameter_collection_format(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)

        _query_params = []
        for parameter in (
            request_query_pipe,
            request_query_ioutil,
            request_query_http,
            request_query_url,
            request_query_context,
            request_query_ref_param,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _query_params.extend(serialized_data)
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=_path,
            method=_method,
            query_params=tuple(_query_params),
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
