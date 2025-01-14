def function_with_uncommon_error(x, y):
    if x == 0:
        return 1 / x  # ZeroDivisionError, but could be masked by other exceptions
    elif y < 0:
        raise ValueError("y must be non-negative")
    else:
        return x + y

# Example usage that handles both exceptions
try:
    result = function_with_uncommon_error(0, 5)
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
except ValueError as e:
    print(f"Caught a ValueError: {e}")

try:
    result = function_with_uncommon_error(5, -1)
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
except ValueError as e:
    print(f"Caught a ValueError: {e}")
    