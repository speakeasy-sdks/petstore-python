"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import animals as shared_animals
from ...models.shared import birds as shared_birds
from ...models.shared import pagination as shared_pagination
from dataclasses_json import Undefined, dataclass_json
from pb import utils
from typing import Any, List, Optional, Union


@dataclasses.dataclass
class GetAllLivingThingsRequest:
    filter_: Optional[List[Any]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter', 'style': 'form', 'explode': True }})
    r"""include all filters"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllLivingThingsPagination:
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllLivingThings2:
    pagination: Optional[GetAllLivingThingsPagination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllLivingThings1:
    pagination: Optional[shared_pagination.Pagination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Two:
    animals: Optional[List[shared_animals.Animals]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('animals'), 'exclude': lambda f: f is None }})
    meta: Optional[Union[GetAllLivingThings1, GetAllLivingThings2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Pagination:
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllLivingThingsAnimalsMeta:
    pagination: Optional[Pagination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class One:
    birds: Optional[List[shared_birds.Birds]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('birds'), 'exclude': lambda f: f is None }})
    meta: Optional[GetAllLivingThingsAnimalsMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetAllLivingThingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    one_of: Optional[Union[One, Two]] = dataclasses.field(default=None)
    r"""OK"""
    

