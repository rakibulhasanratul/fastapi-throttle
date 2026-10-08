from typing_extensions import Any, Callable

def limit(
    max_calls: int = 10,
    interval_seconds: int = 1,
    request_per_seconds: float = 1.0,
    burst: int = 10,
    clean_up_interval_seconds: int = 60,
) -> Callable[..., Any]: ...
