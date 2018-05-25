# Synapse

A super simple way to convert your python function into a rest api.

**Falsk with better defaults**

> Not sure if this needed though. Might be micro optimizing. Most probably

## Model

- accepts json ( only json for now )
- passes each key to corresponding function arguments
- returns dict returned back as json

## Deps

- `flask`
- `flask_cors`

## Sample usage

```python
from synapse import Synapse

synapse = Synapse()

@synapse.connect('/robo')
def robo(name, robot=False):
    if robot:
        return f"{name} is a robot"
    else:
        return f"{name} is not a robot"

synapse.start()
```

### Ideal condition
For this if you send
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name": "meain", "robot": true}' \
  http://localhost:8080/robo
```
you get
```js
{
  "data": "meain is a robot",
  "success": true
}
```

### Error condition

It has basic error check for now. So if you send
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"nxame": "meain"}' \
  http://localhost:8080/robo
```

you get
```js
{
  "error": "Keys ['name'] not found",
  "success": false
}
```

## TODO
> For TODO check `todo/`
