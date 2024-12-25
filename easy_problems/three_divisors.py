# Given a number N, print all numbers in the range from 1 to N having exactly 3 divisors. 

# Input: N = 16
# Output: 4 9
# Explanation: 4 and 9 have exactly three divisors.
#
# Input: N = 49
# Output: 4 9 25 49
# Explanation: 4, 9, 25 and 49 have exactly three divisors.
     
def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, (int(n**0.5) + 1)):
        if n % i == 0:
            return False
    return True

def threeDivisors(n):
    result = []
    for i in range (4, n+1):
        sqrt_i = int(i**0.5)
        if (sqrt_i**2 == i and isPrime(sqrt_i)):
            result.append(i)
    return result

if __name__ == "__main__":
    n = int(input("Input: "))
    print(threeDivisors(n))


