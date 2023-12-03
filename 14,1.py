def logger(func):
    def wrapper(*args, **kwargs):
        arg_str = ', '.join(map(repr, args))
        kwarg_str = ', '.join(f'{key}={value!r}' for key, value in kwargs.items())
        print(f"{func.__name__} called with {arg_str}{', ' if arg_str and kwarg_str else ''}{kwarg_str}")
        return func(*args, **kwargs)

    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3)
