<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->