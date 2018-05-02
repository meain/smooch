# Smooch

A super simple way to convert your python function into a rest api.

> Not sure if this needed though. Might be micro optimizing

## Model

- accepts json ( only json for now )
- passes each key to corresponding function arguments
- returns dict returned back as json

## Deps

- flask ( or sanic? )

## Result

```python
import smooch

@smooch
def infer(input=None):
    result = work_on(input)
    return result
```
