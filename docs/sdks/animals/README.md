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
    age=239780,
    color='maroon',
    id='<ID>',
    name='Buckinghamshire TLS',
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
                age=24488,
                color='sky blue',
                id='<ID>',
                name='loyalty Officer withdrawal',
            ),
        ],
        birds=shared.ComplexObjectDataBirds(
            food=[
                'ruddy',
            ],
            id='<ID>',
            name='Fantastic',
        ),
        created_date=[],
        updated_date=[],
    ),
    meta=[],
    name='Chicken',
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
    id='<ID>',
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
    age='Avon',
    color='turquoise',
    id='<ID>',
    name='plum',
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
        'qua',
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
        age=942154,
        color='plum',
        id='<ID>',
        name='enhance product',
    ),
    id='<ID>',
    per_page=208636,
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
        age=15412,
        color='ivory',
        id='<ID>',
        name='index Elizabeth Fish',
    ),
    id='<ID>',
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

