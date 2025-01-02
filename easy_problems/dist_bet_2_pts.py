import math

# def distance(x1, y1, x2, y2):
#     x = x1 - x2
#     y = y1 - y2
#     sum = pow(x, 2) + pow(y, 2)
#     return pow(sum ,0.5)

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2-x1, 2)+ math.pow(y2-y1, 2))

print(distance(3, 4, 7, 7))
print("%.5f"%distance(3, 4, 4, 3))
