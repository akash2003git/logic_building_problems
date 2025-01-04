import math

# def countPairs(n):
#     count = 0
#     for i in range(1, n):
#         for j in range(1, n):
#             if (pow(i, 3) + pow(j, 3) == n):
#                 count += 1
#     return count

def countPairs(n):
    count = 0
    for i in range(1, int(math.pow(n, 1/3)) + 1):
        cb = math.pow(i, 3)
        diff = n - cb
        cb_diff = round(math.pow(diff, 1/3))
        if (math.pow(cb_diff, 3) == diff):
            count += 1
    return count


print(countPairs(9))
print(countPairs(28))

