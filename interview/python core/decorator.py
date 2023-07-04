def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator
def my_function():
    print("Inside my_function")


# Вызов функции
my_function()


def my_decorator(arg1, arg2):
    def decorator(func):
        def wrapper():
            print("Before function execution")
            print(f"Decorator arguments: {arg1}, {arg2}")
            func()
            print("After function execution")
        return wrapper
    return decorator


@my_decorator("arg1_value", "arg2_value")
def my_function():
    print("Inside my_function")


# Вызов функции
my_function()
