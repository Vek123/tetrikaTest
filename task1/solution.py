from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for var, arg in zip(func.__annotations__.values(), args):
            if var != type(arg):
                raise TypeError
        for key, val in kwargs.items():
            if func.__annotations__.get(key) != type(val):
                raise TypeError
        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int = 2) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(2, 2.5))  # >>> TypeError
