# lst = [(8,9), (6, 7), (4, 7), (2, 3),(2, 1) , (2, -8)]
# print(lst)
# ln = len(lst)
# for i in range(ln):
#     for j in range(ln -i -1):
#         if lst[j][0] + lst[j][1] > lst[j+1][0] + lst[j+1][1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print("\nThe answer is ")
# print(lst)

from time import perf_counter_ns
def measure(data, find):
    start = perf_counter_ns()
    find in data
    return perf_counter_ns() - start
