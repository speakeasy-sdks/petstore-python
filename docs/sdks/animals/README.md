# Animals

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
from pb.models import operations

s = pb.Pb()

req = operations.CreateAnimalRequestBody(
    age=870013,
    color='at',
    id='f7cc78ca-1ba9-428f-8816-742cb7392059',
    name='Sheryl Fadel',
)

res = s.animals.create_animal(req, operations.CreateAnimalSecurity(
    key1="",
))

if res.animals is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateAnimalRequestBody](../../models/operations/createanimalrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.CreateAnimalSecurity](../../models/operations/createanimalsecurity.md)       | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.CreateAnimalResponse](../../models/operations/createanimalresponse.md)**


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
                age=943749,
                color='saepe',
                id='a7596eb1-0faa-4a23-92c5-955907aff1a3',
                name='Carlos Ziemann',
            ),
        ],
        birds=shared.ComplexObjectDataBirds(
            food=[
                'numquam',
            ],
            id='67739251-aa52-4c3f-9ad0-19da1ffe78f0',
            name='Mr. Jared Ritchie',
        ),
        created_date=979587,
        updated_date=359444,
    ),
    meta=shared.Pagination(
        has_more=False,
        page_number=480894,
    ),
    name='Maryann Hamill',
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
from pb.models import operations

s = pb.Pb()

req = operations.DeleteAnimalsByIDRequest(
    id='e13b99d4-88e1-4e91-a450-ad2abd442698',
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
from pb.models import operations

s = pb.Pb()

req = operations.GetAllAnimalsRequest(
    age='perferendis',
    color='magni',
    id='d502a94b-b4f6-43c9-a9e9-a3efa77dfb14',
    name='Irving Jenkins',
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
from pb.models import operations

s = pb.Pb()

req = operations.GetAllLivingThingsRequest(
    filter=[
        'accusamus',
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

s = pb.Pb()

req = operations.GetAnimalsByIDRequest(
    animals=shared.Animals(
        age=249796,
        color='occaecati',
        id='5efb9ba8-8f3a-4669-9707-4ba4469b6e21',
        name='Frances Marks',
    ),
    id='890afa56-3e25-416f-a4c8-b711e5b7fd2e',
    per_page=868126,
)

res = s.animals.get_animals_by_id(req, operations.GetAnimalsByIDSecurity(
    key1="",
))

if res.animals is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAnimalsByIDRequest](../../models/operations/getanimalsbyidrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetAnimalsByIDSecurity](../../models/operations/getanimalsbyidsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetAnimalsByIDResponse](../../models/operations/getanimalsbyidresponse.md)**


## update_animals_by_id

Update the animal object

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb()

req = operations.UpdateAnimalsByIDRequest(
    animals=shared.Animals(
        age=37559,
        color='consequuntur',
        id='8921cddc-6926-401f-b576-b0d5f0d30c5f',
        name='Robin D'Amore',
    ),
    id='7053202c-73d5-4fe9-b90c-28909b3fe49a',
)

res = s.animals.update_animals_by_id(req, operations.UpdateAnimalsByIDSecurity(
    key1="",
))

if res.animals is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAnimalsByIDRequest](../../models/operations/updateanimalsbyidrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateAnimalsByIDSecurity](../../models/operations/updateanimalsbyidsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateAnimalsByIDResponse](../../models/operations/updateanimalsbyidresponse.md)**

