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
def gcd(a ,b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    if a == b:
        return a

    if a > b:
        if a % b == 0:
            return b
        return gcd(a - b, b)
    else:
        if b % a == 0:
            return a
        return gcd(a, b - a)
    

print(gcd(36, 60))
print(gcd(20, 28))
print(gcd(98, 56))


