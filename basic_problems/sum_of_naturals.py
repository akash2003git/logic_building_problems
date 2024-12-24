# def getSum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

def getSum(n):
    return n * (n+1) / 2

if __name__ == "__main__":
    n = int(input("Input: "))
    sum = int(getSum(n))
    print(sum)


