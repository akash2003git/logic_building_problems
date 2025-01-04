# Recursive Apporach
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Iterative Apporach
# def factorial(n):
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     return res

print(factorial(5))
print(factorial(4))
print(factorial(1))
print(factorial(0))
