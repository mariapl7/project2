from typing import Any


# def log(my_function):
#     def wrapper(*args, **kwargs):
#         result = my_function(*args, **kwargs)
#         print(f'тип ошибки. Inputs: (1, 2), {result}')
#         return result
#     return wrapper


def log(filename: Any):
    """Декоратор логирует начало и конец выполнения декорируемой функции, ее результаты и ошибки"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # time_1 = time()
                result = func(*args, **kwargs)
                # time_2 = time()
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator
