"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import complexobject as shared_complexobject
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class CreateLivingThingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    complex_object: Optional[shared_complexobject.ComplexObject] = dataclasses.field(default=None)
    r"""OK"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

