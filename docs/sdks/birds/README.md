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

s = pb.Pb()

req = shared.ComplexObject(
    data=shared.ComplexObjectData(
        animal=[
            shared.Animals(
                age=535633,
                color='pariatur',
                id='9cbf4863-3323-4f9b-b7f3-a4100674ebf6',
                name='Dr. Craig Littel DDS',
            ),
        ],
        birds=shared.ComplexObjectDataBirds(
            food=[
                'dolorum',
            ],
            id='77a89ebf-737a-4e42-83ce-5e6a95d8a0d4',
            name='Gina Schmeler',
        ),
        created_date='a',
        updated_date=687488,
    ),
    meta=shared.Pagination(
        has_more=False,
        page_number=215507,
    ),
    name='Saul Fay',
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

s = pb.Pb()

req = shared.NestedBird(
    age=shared.NestedBirdAge(
        amount=2539.41,
        unit=shared.NestedBirdAgeUnit.MONTHS,
    ),
    flight=shared.NestedBirdFlight(
        can_fly=False,
        wings=shared.NestedBirdFlightWings(
            count=213312,
            span=shared.NestedBirdFlightWingsSpan(
                amount=9574.51,
                unit='totam',
            ),
        ),
    ),
    food=[
        'nihil',
    ],
    id='0b326b5a-7342-49cd-b1a8-422bb679d232',
    location=[
        shared.NestedBirdLocation(
            geography=shared.NestedBirdLocationGeography(
                latitude='magni',
                longitutde='odio',
            ),
        ),
    ],
    name='Marion Reichert DDS',
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

s = pb.Pb()

req = [
    shared.Birds(
        can_fly=False,
        id='bb1e31b8-b90f-4344-ba11-08e0adcf4b92',
        name='Marsha Kuhic',
        wing_span=787542,
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
from pb.models import operations

s = pb.Pb()

req = operations.GetAllLivingThingsRequest(
    filter=[
        'vero',
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

