# petstore

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/petstore-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import pb
from pb.models import operations, shared

s = pb.Pb(
    security=shared.Security(
        key1="",
    ),
)

req = operations.CreateAnimalRequestBody(
    age=870013,
    color='at',
    id='f7cc78ca-1ba9-428f-8816-742cb7392059',
    name='Sheryl Fadel',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [Animals](docs/sdks/animals/README.md)

* [create_animal](docs/sdks/animals/README.md#create_animal) - create an animal
* [create_living_things](docs/sdks/animals/README.md#create_living_things) - create a living thing
* [delete_animals_by_id](docs/sdks/animals/README.md#delete_animals_by_id) - Delete Animal Object
* [get_all_animals](docs/sdks/animals/README.md#get_all_animals) - Your GET endpoint
* [get_all_living_things](docs/sdks/animals/README.md#get_all_living_things) - Get All living things
* [get_animals_by_id](docs/sdks/animals/README.md#get_animals_by_id) - Get Animal
* [update_animals_by_id](docs/sdks/animals/README.md#update_animals_by_id) - Update Animal

### [Birds](docs/sdks/birds/README.md)

* [create_living_things](docs/sdks/birds/README.md#create_living_things) - create a living thing
* [create_new_bird](docs/sdks/birds/README.md#create_new_bird) - Create new Bird
* [get_all_birds](docs/sdks/birds/README.md#get_all_birds) - Get Birds
* [get_all_living_things](docs/sdks/birds/README.md#get_all_living_things) - Get All living things
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
