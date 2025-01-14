def function_with_uncommon_error(x, y):
    if x == 0:
        return 1 / x  # ZeroDivisionError, but could be masked by other exceptions
    elif y < 0:
        raise ValueError("y must be non-negative")
    else:
        return x + y

# Example usage that might mask the ZeroDivisionError
try:
    result = function_with_uncommon_error(0, 5)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Caught an error: {e}")
#The ZeroDivisionError is masked because the ValueError is raised first when 0 is passed as x