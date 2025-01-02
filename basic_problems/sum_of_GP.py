# def sumOfGP(a, r, n):
#     if n == 1: return a
#     sum = 0
#     for i in range(0, n):
#         sum += pow(r, i)
#     return a*sum

def sumOfGP(a, r, n):
    return a * ((1 - pow(r, n)) / (1 - r))

print("%.5f" % sumOfGP(1, 0.5, 10))
print("%.5f" % sumOfGP(2, 2, 15))
