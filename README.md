# Synapse

A super simple way to convert your python function into a rest api.

**Falsk with better defaults**

> Not sure if this needed though. Might be micro optimizing. Most probably

## Model

- accepts json ( only json for now )
- passes each key to corresponding function arguments
- returns dict returned back as json

## Deps

- flask ( or sanic? )

## Result

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
