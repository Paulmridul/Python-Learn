# from numpy import *

# arr = array([7, 8, 9, 4])

# print(arr)

# for i in range(1, 10):
#     print(i)

# arr = ones(8)
# print(arr)

def sum_add(x, y):
    return x+y, x-y


print(sum_add(8, 5))


def sumall(*b):
    x = 0
    for i in b:
        x = x + i
    return x


print(sumall(5, 8, 9))

