# Birds
(*birds*)

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
                age=24488,
                color='sky blue',
                id='<ID>',
                name='loyalty Officer withdrawal',
            ),
        ],
        birds=[],
        created_date=[],
        updated_date=[],
    ),
    meta=[],
    name='female Fantastic B2B',
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
        amount=5601.46,
        unit=shared.NestedBirdAgeUnit.YEARS,
    ),
    flight=shared.NestedBirdFlight(
        can_fly=False,
        wings=shared.NestedBirdFlightWings(
            count=959530,
            span=shared.NestedBirdFlightWingsSpan(
                amount=7898.44,
                unit='katal',
            ),
        ),
    ),
    food=[
        'digital',
    ],
    id='<ID>',
    location=[
        shared.NestedBirdLocation(
            geography=shared.NestedBirdLocationGeography(
                latitude='-69.7312',
                longitutde='Response',
            ),
        ),
    ],
    name='wipe Southwest',
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
        id='<ID>',
        name='Creative',
        wing_span=956031,
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
        'qua',
    ],
)

res = s.birds.get_all_living_things(req)

if res.get_all_living_things_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAllLivingThingsRequest](../../models/operations/getalllivingthingsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAllLivingThingsResponse](../../models/operations/getalllivingthingsresponse.md)**

