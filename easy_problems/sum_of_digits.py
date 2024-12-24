# def sumOfDigits(n):
#     sum = 0
#     while (n != 0):
#         r = n % 10
#         sum += r
#         n = int(n/10)
#     return sum

# Sample dry run

# 1] n = 687, r = 7, sum = 7, n = 68
# 2] n = 68, r = 8, sum = 15, n = 6
# 3] n = 6, r = 6, sum = 21, n = 0


# Time Complexity: O(log n)
# Auxiliary Space: O(1)

# def sumOfDigits(n):
#     return 0 if n == 0 else int(n%10) + sumOfDigits((int(n/10)))

# Sameple dry run
# 1] n = 687, 7 + sumOfDigits(68)
# 2] n = 68, 7 + (8 + sumOfDigits(6))
# 3] n = 6, 7 + (8 + (6 + sumOfDigits(0)))
# 4] n = 0, 7 + (8 + (6 + 0)) = 21

# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

# def sumOfDigits(n, val):
#     if (n < 10):
#         val = val + n
#         return val
#     return sumOfDigits(n // 10, (n % 10) + val)

# Sample dry run

# sumOfDigits(687, 0)
#   sumOfDigits(68, 7)
#     sumOfDigits(6, 15)
#       21
    
# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

def sumOfDigits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

# Time Complexity: O(n)
# Auxiliary Space: O(1)



if __name__ == "__main__":
    # n = int(input("Input: "))
    # print(sumOfDigits(n, 0))
    n = input("Input: ")
    print(sumOfDigits(n))

