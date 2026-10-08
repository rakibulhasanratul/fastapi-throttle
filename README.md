# FastAPI Throttle

Rate limiting for FastAPI applications.

## Getting Started

Install with `uv`:

```bash
uv add git+https://github.com/rakibulhasanratul/fastapi-throttle
```

Or clone the repo:

```bash
git clone https://github.com/rakibulhasanratul/fastapi-throttle
```

Import the `limit` decorator and apply it to your endpoints.

## Features

- Decorator-based rate limiting
- Configurable parameters:
  - `max_calls`: Maximum calls allowed within `interval_seconds`
  - `interval_seconds`: Time window for the `max_calls` limit
  - `request_per_seconds`: Token bucket refill rate (tokens per second)
  - `burst`: Token bucket capacity (max accumulated tokens)
  - `clean_up_interval_seconds`: How often to clean up old usage records
- Sync and async compatible
- Request object is optional

## Usage

```python
from fastapi import FastAPI, Request
from fastapi_throttle import limit

app = FastAPI()

@app.get("/endpoint1")
@limit(max_calls=10, interval_seconds=1, request_per_seconds=1)
async def endpoint_1(request: Request):
    return {"message": "Return from endpoint 1"}

@app.get("/endpoint-2")
@limit(max_calls=1, interval_seconds=1, request_per_seconds=1)
def endpoint_2():
    return {"status": "ok"}

@app.get("/another-async")
@limit(max_calls=5, interval_seconds=5)
async def another_async_endpoint():
    return {"data": "This is another async endpoint"}
```
