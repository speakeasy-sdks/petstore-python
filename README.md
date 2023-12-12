# petstore

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/petstore-python.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
    id='<ID>',
    name='string',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [animals](docs/sdks/animals/README.md)

* [create_animal](docs/sdks/animals/README.md#create_animal) - create an animal
* [create_living_things](docs/sdks/animals/README.md#create_living_things) - create a living thing
* [delete_animals_by_id](docs/sdks/animals/README.md#delete_animals_by_id) - Delete Animal Object
* [get_all_animals](docs/sdks/animals/README.md#get_all_animals) - Your GET endpoint
* [get_all_living_things](docs/sdks/animals/README.md#get_all_living_things) - Get All living things
* [get_animals_by_id](docs/sdks/animals/README.md#get_animals_by_id) - Get Animal
* [update_animals_by_id](docs/sdks/animals/README.md#update_animals_by_id) - Update Animal

### [birds](docs/sdks/birds/README.md)

* [create_living_things](docs/sdks/birds/README.md#create_living_things) - create a living thing
* [create_new_bird](docs/sdks/birds/README.md#create_new_bird) - Create new Bird
* [get_all_birds](docs/sdks/birds/README.md#get_all_birds) - Get Birds
* [get_all_living_things](docs/sdks/birds/README.md#get_all_living_things) - Get All living things
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 400-600          | */*              |

### Example

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
    id='<ID>',
    name='string',
)

res = None
try:
    res = s.animals.create_animal(req)
except errors.Error as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.animals is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.petstore.com` | None |
| 1 | `https://sandbox-api.petstore.com` | None |

#### Example

```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    server_idx=1,
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateAnimalRequestBody(
    color='white',
    id='<ID>',
    name='string',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    server_url="https://api.petstore.com",
    security=shared.Security(
        key1="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.CreateAnimalRequestBody(
    color='white',
    id='<ID>',
    name='string',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import pb
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = pb.Pb(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name         | Type         | Scheme       |
| ------------ | ------------ | ------------ |
| `key1`       | oauth2       | OAuth2 token |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
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
    id='<ID>',
    name='string',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
