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
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateAnimalRequestBody(
    color='white',
    id='<id>',
    name='<value>',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateAnimalRequestBody](../../models/operations/createanimalrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateAnimalResponse](../../models/operations/createanimalresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## create_living_things

Create a living thing

### Example Usage

```python
import pb
from pb.models import shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = shared.ComplexObject()

res = s.animals.create_living_things(req)

if res.complex_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.ComplexObject](../../models/shared/complexobject.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateLivingThingsResponse](../../models/operations/createlivingthingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## delete_animals_by_id

Delete the animal

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.DeleteAnimalsByIDRequest(
    id='<id>',
)

res = s.animals.delete_animals_by_id(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteAnimalsByIDRequest](../../models/operations/deleteanimalsbyidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteAnimalsByIDResponse](../../models/operations/deleteanimalsbyidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get_all_animals

Get Animals Description

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetAllAnimalsRequest()

res = s.animals.get_all_animals(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAllAnimalsRequest](../../models/operations/getallanimalsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetAllAnimalsResponse](../../models/operations/getallanimalsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get_all_living_things

get All living things data

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetAllLivingThingsRequest()

res = s.animals.get_all_living_things(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAllLivingThingsRequest](../../models/operations/getalllivingthingsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAllLivingThingsResponse](../../models/operations/getalllivingthingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_animals_by_id

Get an animal

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.GetAnimalsByIDRequest(
    id='<id>',
)

res = s.animals.get_animals_by_id(req)

if res.animals is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAnimalsByIDRequest](../../models/operations/getanimalsbyidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetAnimalsByIDResponse](../../models/operations/getanimalsbyidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## update_animals_by_id

Update the animal object

### Example Usage

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.UpdateAnimalsByIDRequest(
    id='<id>',
)

res = s.animals.update_animals_by_id(req)

if res.animals is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAnimalsByIDRequest](../../models/operations/updateanimalsbyidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateAnimalsByIDResponse](../../models/operations/updateanimalsbyidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
