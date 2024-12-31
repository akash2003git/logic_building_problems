import math

# Time Complexity: O(log y)
# Space Complexity: O(1)

# def isPower(x, y):
#     if x == 1:
#         return y == 1
#     if y == 1:
#         return True
#     while y % x == 0:
#         y //= x
#     return y == 1

# Time Complexity: O(1)
# Space Complexity: O(1)
def isPower(x, y):
    if x == 1:
        return y == 1
    if y == 1:
        return True
    res = math.log(y) / math.log(x)
    return res.is_integer()

print(isPower(10, 1))
print(isPower(10, 1000))
print(isPower(10, 1001))
print(isPower(1, 1))
print(isPower(1, 100))
