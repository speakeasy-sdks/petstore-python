# birds

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
                age=565421,
                color='temporibus',
                id='2322715b-f0cb-4b1e-b1b8-b90f3443a110',
                name='Percy Altenwerth',
            ),
            shared.Animals(
                age=785153,
                color='doloribus',
                id='4b921879-fce9-453f-b3ef-7fbc7abd74dd',
                name='Dr. Faye Rutherford',
            ),
        ],
        birds=shared.ComplexObjectDataBirds(
            food=[
                'fugit',
                'porro',
                'maiores',
                'doloribus',
            ],
            id='7c70a456-26d4-4368-93f1-6d9f5fce6c55',
            name='Stephanie Gutkowski',
        ),
        created_date=926213,
        updated_date=325310,
    ),
    meta=shared.Pagination(
        has_more=False,
        page_number=952871,
    ),
    name='Richard Anderson',
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
        amount=3045.82,
        unit=shared.NestedBirdAgeUnit.MONTHS,
    ),
    flight=shared.NestedBirdFlight(
        can_fly=False,
        wings=shared.NestedBirdFlightWings(
            count=882860,
            span=shared.NestedBirdFlightWingsSpan(
                amount=795.22,
                unit='non',
            ),
        ),
    ),
    food=[
        'dolorum',
    ],
    id='ac366c8d-d6b1-4442-9074-74778a7bd466',
    location=[
        shared.NestedBirdLocation(
            geography=shared.NestedBirdLocationGeography(
                latitude='eos',
                longitutde='praesentium',
            ),
        ),
        shared.NestedBirdLocation(
            geography=shared.NestedBirdLocationGeography(
                latitude='quisquam',
                longitutde='veritatis',
            ),
        ),
        shared.NestedBirdLocation(
            geography=shared.NestedBirdLocationGeography(
                latitude='ipsa',
                longitutde='id',
            ),
        ),
        shared.NestedBirdLocation(
            geography=shared.NestedBirdLocationGeography(
                latitude='quidem',
                longitutde='neque',
            ),
        ),
    ],
    name='Dallas Sanford',
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
        id='51904e52-3c7e-40bc-b178-e4796f2a70c6',
        name='Dwayne Cronin',
        wing_span=681393,
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
        'incidunt',
        'atque',
        'explicabo',
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

