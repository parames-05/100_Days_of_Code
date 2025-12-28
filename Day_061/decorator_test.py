import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

def speed_calc_decorator(function):
    def wrapper():
        start = time.time()
        function()
        end_time = time.time()
        time_taken = end_time - start
        print(f"run speed : {time_taken}")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()