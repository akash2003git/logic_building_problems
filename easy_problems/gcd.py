# Time Complexity: O(min(a,b)) 
# Auxiliary Space: O(1)
# def gcd(a, b):
#     result = min(a, b)
#     while True:
#         if a % result == 0 and b % result == 0:
#             break
#         result -=1
#     return result

# Euclidean Algorithm
# Time Complexity: O(min(a,b))
# Auxiliary Space: O(min(a,b))
# def gcd(a ,b):
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     
#     if a == b:
#         return a
#
#     if a > b:
#         return gcd(a-b, b)
#     return gcd(a, b-a)

# Optimized Euclidean
# Time Complexity: O(min(a,b))
# Auxiliary Space: O(1)
# def gcd(a ,b):
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     
#     if a == b:
#         return a
#
#     if a > b:
#         if a % b == 0:
#             return b
#         return gcd(a - b, b)
#     else:
#         if b % a == 0:
#             return a
#         return gcd(a, b - a)

# Optimized Euclidean using division
# Time Complexity: O(log(min(a,b)))
# Auxiliary Space: O(log(min(a,b))
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# Euclidean algo using iterative implementation
# Time Complexity: O(log(min(a,b)))
# Auxiliary Space: O(1)
def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else: 
            b = b % a
    
    if a == 0:
        return b
    return a

# math.gcd(a, b) available
# Time Complexity: O(log(min(a, b)))
# Auxiliary Space: O(1)

# Other methods:
# binary GCD for bitwise hardware optimizations.
# prime factorization for small inputs or theoretical explorations.

print(gcd(36, 60))
print(gcd(20, 28))
print(gcd(98, 56))
print(gcd(48, 18))
print(gcd(101, 103))


