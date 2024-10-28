# import functools

def repeat(num_times):
    def decorator_repeat(func):
        #@functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
#
# # @repeat(5)
# # def greet(name, mark=100):
# #     print(f"Hello {name}, your mark is {mark}")
# #
# # greet("DevOps")
# #
# lst = [2, -4, True, "a", 12.5]
# it = iter(lst)
# @repeat(6)
# def next_print(it):
#     print(next(it))
#
# next_print(it)

# import tracemalloc
# def measure_mem_usage(func):
#     def wrapper(*args, **kwargs):
#         tracemalloc.start()
#         res = func(*args, **kwargs)
#
#         snapshot = tracemalloc.take_snapshot()
#         top_stats = snapshot.statistics("lineno")
#
#         print(f"Memory usage of {func.__name__}: ")
#         for stat in top_stats[:3]:
#             print(stat)
#
#         return res
#     return wrapper

# @measure_mem_usage
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n -1)
# # print(measure_mem_usage(factorial(5)))
# print("Factorial: ", factorial(25))



# @measure_mem_usage
# @repeat(3)
# def create_list(num):
#     ls = [i**3 for i in range(num)]
#
#     return ls
#
# print(create_list(1000))

def cache_result(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())

        if key in cache:
            print("Retrieving result from cache...")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache_result
def calc_mul_with_cache(x, y):
    print("Calculating the product of two numbers...")
    return x * y

print(calc_mul_with_cache(4,5))
print(calc_mul_with_cache(4,5))
print(calc_mul_with_cache(14,5))
print(calc_mul_with_cache(4,5))
print(calc_mul_with_cache(4,25))
print(calc_mul_with_cache(2,0))
print(calc_mul_with_cache(4,5))
print(calc_mul_with_cache(4,5))

