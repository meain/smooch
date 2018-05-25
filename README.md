# Synapse [WIP]

A super simple way to convert your python function into a rest api.

**Falsk with better defaults**

> Not sure if this needed though. Might be micro optimizing

## Why

- auth
- check for needed keys ( give correct error message back )
- use function name as path


## Model

- accepts json ( only json for now )
- passes each key to corresponding function arguments
- returns dict returned back as json

## Deps

- flask ( or sanic? )

## Result

```python
import synapse

@synapse
def infer(input=None): # will be available at /infer
    result = work_on(input)
    return result
```
