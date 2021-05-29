import time


def time_decorator(some_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = some_function(*args, **kwargs)
        print(time.time() - start_time)
        return result

    return wrapper


@time_decorator
def factor(number):
    res = 1
    for numb in range(1, number):
        res *= numb
    return res


number = 100
# start_time = time.time()
result = factor(number)
# print(time.time() - start_time)
print(result)
