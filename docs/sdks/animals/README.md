# Animals
(*animals*)

## Overview

Work with Animals.

### Available Operations

* [create_animal](#create_animal) - create an animal
* [create_living_things](#create_living_things) - create a living thing
* [delete_animals_by_id](#delete_animals_by_id) - Delete Animal Object
* [get_all_animals](#get_all_animals) - Your GET endpoint
* [get_all_living_things](#get_all_living_things) - Get All living things
* [get_animals_by_id](#get_animals_by_id) - Get Animal
* [update_animals_by_id](#update_animals_by_id) - Update Animal

## create_animal

Post animals description

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = operations.CreateAnimalRequestBody(
    age=943749,
    color='saepe',
    id='a7596eb1-0faa-4a23-92c5-955907aff1a3',
    name='Carlos Ziemann',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateAnimalRequestBody](../../models/operations/createanimalrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateAnimalResponse](../../models/operations/createanimalresponse.md)**


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
                age=253291,
                color='commodi',
                id='7739251a-a52c-43f5-ad01-9da1ffe78f09',
                name='Ms. Karla Aufderhar',
            ),
        ],
        birds=shared.ComplexObjectDataBirds(
            food=[
                'maiores',
            ],
            id='15471b5e-6e13-4b99-9488-e1e91e450ad2',
            name='Rudy Spencer',
        ),
        created_date=[],
        updated_date=[],
    ),
    meta=[],
    name='Beth McGlynn Sr.',
)

res = s.animals.create_living_things(req)

if res.complex_object is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.ComplexObject](../../models/shared/complexobject.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateLivingThingsResponse](../../models/operations/createlivingthingsresponse.md)**


## delete_animals_by_id

Delete the animal

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = operations.DeleteAnimalsByIDRequest(
    id='d502a94b-b4f6-43c9-a9e9-a3efa77dfb14',
)

res = s.animals.delete_animals_by_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteAnimalsByIDRequest](../../models/operations/deleteanimalsbyidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteAnimalsByIDResponse](../../models/operations/deleteanimalsbyidresponse.md)**


## get_all_animals

Get Animals Description

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = operations.GetAllAnimalsRequest(
    age='cumque',
    color='facere',
    id='66ae395e-fb9b-4a88-b3a6-6997074ba446',
    name='Robin Keebler',
)

res = s.animals.get_all_animals(req)

if res.animals is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAllAnimalsRequest](../../models/operations/getallanimalsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetAllAnimalsResponse](../../models/operations/getallanimalsresponse.md)**


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
        'architecto',
    ],
)

res = s.animals.get_all_living_things(req)

if res.get_all_living_things_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAllLivingThingsRequest](../../models/operations/getalllivingthingsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAllLivingThingsResponse](../../models/operations/getalllivingthingsresponse.md)**


## get_animals_by_id

Get an animal

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = operations.GetAnimalsByIDRequest(
    animals=shared.Animals(
        age=298282,
        color='et',
        id='959890af-a563-4e25-96fe-4c8b711e5b7f',
        name='Louis Turner Sr.',
    ),
    id='8921cddc-6926-401f-b576-b0d5f0d30c5f',
    per_page=729991,
)

res = s.animals.get_animals_by_id(req)

if res.animals is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAnimalsByIDRequest](../../models/operations/getanimalsbyidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetAnimalsByIDResponse](../../models/operations/getanimalsbyidresponse.md)**


## update_animals_by_id

Update the animal object

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = operations.UpdateAnimalsByIDRequest(
    animals=shared.Animals(
        age=749999,
        color='dolores',
        id='58705320-2c73-4d5f-a9b9-0c28909b3fe4',
        name='Omar Leuschke',
    ),
    id='cbf48633-323f-49b7-bf3a-4100674ebf69',
)

res = s.animals.update_animals_by_id(req)

if res.animals is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAnimalsByIDRequest](../../models/operations/updateanimalsbyidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateAnimalsByIDResponse](../../models/operations/updateanimalsbyidresponse.md)**

