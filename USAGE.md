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
    age=239780,
    color='maroon',
    id='<ID>',
    name='Buckinghamshire TLS',
)

res = s.animals.create_animal(req)

if res.animals is not None:
    # handle response
```
<!-- End SDK Example Usage -->