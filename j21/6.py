import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

# @timer
# def slow_function():
#     sumNumbers = 0
#     for i in range(1, 1_000_000_001):
#       sumNumbers += i
#     return sumNumbers

# print(slow_function())

# @timer
# def fact(num):
#   time.sleep(1)
#   if num == 1:
#     return 1
#   else:
#     return fact(num - 1) * num


# print(fact(5))