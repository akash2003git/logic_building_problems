import math

# O(√n) time and O(1) space
# def isPrime(n):
#     if (n <= 1):
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         # better than (2, n - 1) 
#         # O(n) time and O(1) space for that approach
#         if (n % i == 0):
#             return False 
#     return True 

# We know that any integer number can be written in the form of 6k+i,  
# where k is a nonnegative integer (like 0, 1, 2, 3,...)  
# and i is a number between 0 and 5 (so i can be 0, 1, 2, 3, 4, or 5).  
#
# If we look closely, we’ll notice that when i is 0, 2, 3, or 4,  
# the numbers 6k, 6k+2, 6k+3, and 6k+4 are all divisible by either 2 or 3.  
#
# But prime numbers greater than 3 can't be divisible by 2 or 3.  
#
# Therefore, the only forms left that a prime number can have are 6k+1 or 6k+5  
# (since these forms are not divisible by 2 or 3).  
#
# Instead of checking every number up to the √n to see if it divides n,  
# we only check numbers of the form 6k+1 and 6k+5.  
#
# This reduces the number of checks needed.

# O(√n) time and O(1) space
def isPrime(n):
    # Check if n is 1 or 0
    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    n = int(input("Input: "))
    print(isPrime(n))
