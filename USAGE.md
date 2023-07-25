<!-- Start SDK Example Usage -->


```python
import pb
from pb.models import operations

s = pb.Pb()

req = operations.CreateAnimalRequestBody(
    age=548814,
    color='provident',
    id='bd9d8d69-a674-4e0f-867c-c8796ed151a0',
    name='Estelle Will',
)

res = s.animals.create_animal(req, operations.CreateAnimalSecurity(
    key1="",
))

if res.animals is not None:
    # handle response
```
<!-- End SDK Example Usage -->