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
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = shared.ComplexObject()

res = s.birds.create_living_things(req)

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

## create_new_bird

Create a new Bird

### Example Usage

```python
import pb
from pb.models import shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = shared.NestedBird()

res = s.birds.create_new_bird(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.NestedBird](../../models/shared/nestedbird.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateNewBirdResponse](../../models/operations/createnewbirdresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_all_birds

Get All birds

### Example Usage

```python
import pb
from pb.models import shared

s = pb.Pb(
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = [
    shared.Birds(),
]

res = s.birds.get_all_birds(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [List[shared.Birds]](../../models/.md)     | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.GetAllBirdsResponse](../../models/operations/getallbirdsresponse.md)**
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

res = s.birds.get_all_living_things(req)

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
