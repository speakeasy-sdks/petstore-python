# Birds

## Overview

Birds information.

### Available Operations

* [create_living_things](#create_living_things) - create a living thing
* [create_new_bird](#create_new_bird) - Create new Bird
* [get_all_birds](#get_all_birds) - Get Birds
* [get_all_living_things](#get_all_living_things) - Get All living things

## create_living_things

Create a living thing

### Example Usage

```python
import pb
from pb.models import shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = shared.ComplexObject(
    data=shared.ComplexObjectData(
        animal=[
            shared.Animals(
                age=743835,
                color='dolorum',
                id='77a89ebf-737a-4e42-83ce-5e6a95d8a0d4',
                name='Gina Schmeler',
            ),
        ],
        birds=shared.ComplexObjectDataBirds(
            food=[
                'dolorum',
            ],
            id='f7a73cf3-be45-43f8-b0b3-26b5a73429cd',
            name='Keith Padberg',
        ),
        created_date=174909,
        updated_date=7044.74,
    ),
    meta=shared.Pagination(
        has_more=False,
        page_number=463150,
    ),
    name='Marty Deckow',
)

res = s.birds.create_living_things(req)

if res.complex_object is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.ComplexObject](../../models/shared/complexobject.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateLivingThingsResponse](../../models/operations/createlivingthingsresponse.md)**


## create_new_bird

Create a new Bird

### Example Usage

```python
import pb
from pb.models import shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = shared.NestedBird(
    age=shared.NestedBirdAge(
        amount=1649.59,
        unit=shared.NestedBirdAgeUnit.YEARS,
    ),
    flight=shared.NestedBirdFlight(
        can_fly=False,
        wings=shared.NestedBirdFlightWings(
            count=124833,
            span=shared.NestedBirdFlightWingsSpan(
                amount=3556.13,
                unit='nam',
            ),
        ),
    ),
    food=[
        'hic',
    ],
    id='0cbb1e31-b8b9-40f3-843a-1108e0adcf4b',
    location=[
        shared.NestedBirdLocation(
            geography=shared.NestedBirdLocationGeography(
                latitude='cupiditate',
                longitutde='qui',
            ),
        ),
    ],
    name='Marsha Kuhic',
)

res = s.birds.create_new_bird(req)

if res.create_new_bird_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.NestedBird](../../models/shared/nestedbird.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateNewBirdResponse](../../models/operations/createnewbirdresponse.md)**


## get_all_birds

Get All birds

### Example Usage

```python
import pb
from pb.models import shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = [
    shared.Birds(
        can_fly=False,
        id='ce953f73-ef7f-4bc7-abd7-4dd39c0f5d2c',
        name='Domingo Kris',
        wing_span=4048,
    ),
]

res = s.birds.get_all_birds(req)

if res.birds is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [list[shared.Birds]](../../models//.md)    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.GetAllBirdsResponse](../../models/operations/getallbirdsresponse.md)**


## get_all_living_things

get All living things data

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = operations.GetAllLivingThingsRequest(
    filter=[
        'officia',
    ],
)

res = s.birds.get_all_living_things(req)

if res.get_all_living_things_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAllLivingThingsRequest](../../models/operations/getalllivingthingsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAllLivingThingsResponse](../../models/operations/getalllivingthingsresponse.md)**

