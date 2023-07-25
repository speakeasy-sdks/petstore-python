# animals

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
                age=902599,
                color='fuga',
                id='7596eb10-faaa-4235-ac59-55907aff1a3a',
                name='Jaime O'Hara',
            ),
            shared.Animals(
                age=414369,
                color='quam',
                id='739251aa-52c3-4f5a-9019-da1ffe78f097',
                name='Thomas Batz',
            ),
            shared.Animals(
                age=979587,
                color='dicta',
                id='5471b5e6-e13b-499d-888e-1e91e450ad2a',
                name='Marty Green',
            ),
            shared.Animals(
                age=397821,
                color='cupiditate',
                id='802d502a-94bb-44f6-bc96-9e9a3efa77df',
                name='Keith Gulgowski',
            ),
        ],
        birds=shared.ComplexObjectDataBirds(
            food=[
                'aliquid',
                'laborum',
            ],
            id='e395efb9-ba88-4f3a-a699-7074ba4469b6',
            name='Brandon Brakus V',
        ),
        created_date=590873,
        updated_date=5743.25,
    ),
    meta=shared.Pagination(
        has_more=False,
        page_number=653201,
    ),
    name='Shaun Hammes',
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
    id='e2516fe4-c8b7-411e-9b7f-d2ed028921cd',
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
    age='pariatur',
    color='maxime',
    id='692601fb-576b-40d5-b0d3-0c5fbb258705',
    name='Ruby Auer',
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
        'dolor',
        'vero',
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
        age=345352,
        color='hic',
        id='e9b90c28-909b-43fe-89a8-d9cbf4863332',
        name='Mindy Marks',
    ),
    id='7f3a4100-674e-4bf6-9280-d1ba77a89ebf',
    per_page=469497,
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
        age=216897,
        color='voluptate',
        id='ae4203ce-5e6a-495d-8a0d-446ce2af7a73',
        name='Saul Fay',
    ),
    id='453f870b-326b-45a7-b429-cdb1a8422bb6',
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

