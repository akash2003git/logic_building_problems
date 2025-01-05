# def isTriangle(a, b, c):
#     if a + b > c:
#         if b + c > a:
#             if a + c > b:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False

# more elegant method
def isTriangle(a, b, c):
    if (a+b<=c or b+c<=a or a+c<=b):
        return False
    else:
        return True

print(isTriangle(7, 10, 5))
print(isTriangle(1, 10, 12))
