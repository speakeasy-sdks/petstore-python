"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import animals as shared_animals
from ..shared import birds as shared_birds
from ..shared import pagination as shared_pagination
from dataclasses_json import Undefined, dataclass_json
from pb import utils
from typing import Any, Optional



@dataclasses.dataclass
class GetAllLivingThingsRequest:
    filter: Optional[list[Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter', 'style': 'form', 'explode': True }})
    r"""include all filters"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAllLivingThings200ApplicationJSON2Meta2Pagination:
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAllLivingThings200ApplicationJSON2Meta2:
    pagination: Optional[GetAllLivingThings200ApplicationJSON2Meta2Pagination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAllLivingThings200ApplicationJSON2Meta1:
    pagination: Optional[shared_pagination.Pagination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAllLivingThings200ApplicationJSON2:
    animals: Optional[list[shared_animals.Animals]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('animals'), 'exclude': lambda f: f is None }})
    meta: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAllLivingThings200ApplicationJSON1MetaPagination:
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAllLivingThings200ApplicationJSON1Meta:
    pagination: Optional[GetAllLivingThings200ApplicationJSON1MetaPagination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAllLivingThings200ApplicationJSON1:
    birds: Optional[list[shared_birds.Birds]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('birds'), 'exclude': lambda f: f is None }})
    meta: Optional[GetAllLivingThings200ApplicationJSON1Meta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetAllLivingThingsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_all_living_things_200_application_json_object: Optional[Any] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

