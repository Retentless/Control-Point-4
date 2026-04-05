# 1
# BEGIN (write your solution here)
def barchart(data):
    max_val = max(max(data), 0)
    min_val = min(min(data), 0)
    width = len(data)
    lines = []

    for level in range(max_val, 0, -1):
        row = ''.join('*' if val >= level else ' ' for val in data)
        lines.append(row.ljust(width))

    for level in range(-1, min_val - 1, -1):
        row = ''.join('#' if val <= level else ' ' for val in data)
        lines.append(row.ljust(width))

    return '\n'.join(lines)
# END

# 2
from functools import wraps


def format_error(error):
    """Format type violation message."""
    argument, value, expected_type = error
    return (
        f'Bad argument type for argument "{argument}":'
        f' {type(value)} instead of {expected_type}'
    )


def throw_error(*args):
    """Raise one typing violation."""
    raise TypeError(format_error(args))


def throw_errors(errors):
    """Raise one error for all typing violations."""
    raise TypeError('\n'.join(map(format_error, errors)))


def typecheck(error_callback=throw_error):
    def decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            annotations = func.__annotations__
            for arg_name, expected_type in annotations.items():
                if arg_name in kwargs and not isinstance(kwargs[arg_name], expected_type):
                    error_callback(arg_name, kwargs[arg_name], expected_type)
                    return None
            return func(**kwargs)
        return wrapper
    return decorator


def typecheck_all(error_callback=throw_errors):
    def decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            annotations = func.__annotations__
            errors = []
            for arg_name, expected_type in annotations.items():
                if arg_name in kwargs and not isinstance(kwargs[arg_name], expected_type):
                    errors.append((arg_name, kwargs[arg_name], expected_type))
            if errors:
                error_callback(errors)
                return None
            return func(**kwargs)
        return wrapper
    return decorator

if __name__ == '__main__':
    @typecheck_all()
    def multiply(times: int, value: (str, tuple)):
        return value * times

    print(multiply(times=10, value=(42,)))
    print(multiply(times=10, value='1'))

    # оба аргумента — не того типа
    print(multiply(times='12', value=None))

# 3
# BEGIN (write your solution here)
def decode(signal):
    result = []
    i = 0
    while i < len(signal):
        if signal[i] == '|':
            result.append('1')
            i += 2  # пропускаем и |, и следующий символ
        else:
            result.append('0')
            i += 1
    return ''.join(result)
# END

# 4
# BEGIN (write your solution here)
def ip2int(ip):
    parts = ip.split('.')
    return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])


def int2ip(n):
    return f'{(n >> 24) & 255}.{(n >> 16) & 255}.{(n >> 8) & 255}.{n & 255}'
# END

# 5
# BEGIN (write your solution here)
def find_index_of_nearest(number, items):
    if not items:
        return None
    nearest_index = 0
    nearest_diff = abs(items[0] - number)
    for i, val in enumerate(items[1:], 1):
        diff = abs(val - number)
        if diff < nearest_diff:
            nearest_diff = diff
            nearest_index = i
    return nearest_index
# END
