from functools import wraps
from typing import Any, Callable


def log_action(
    function: Callable[..., Any]
) -> Callable[..., Any]:
    """
    Decorator used for logging actions.
    """

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        print(f"\n[LOG] Starting: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"[LOG] Completed: {function.__name__}")

        return result

    return wrapper