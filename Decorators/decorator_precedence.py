import functools

# Mock newrelic.agent.function_trace decorator
def function_trace(func):
    """Mock of New Relic's function trace decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Tracing Start] Function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[Tracing End] Function: {func.__name__}")
        return result
    return wrapper

class MyClass:
    # Scenario 1: Correct order with @staticmethod on the outside
    @staticmethod
    @function_trace
    def my_function_correct():
        print("Executing my_function_correct (static method).")

    # Scenario 2: Incorrect order with @function_trace on the outside
    @function_trace
    @staticmethod
    def my_function_incorrect():
        print("Executing my_function_incorrect (static method).")


# Testing both scenarios
print("=== Scenario 1: Correct Order ===")
MyClass.my_function_correct()  # Should work as expected

print("\n=== Scenario 2: Incorrect Order ===")
MyClass.my_function_incorrect()  # May produce unexpected behavior
