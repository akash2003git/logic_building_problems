# Given two integers n and m (m != 0). Find the number closest to n and divisible by m.
# If there is more than one such number, then output the one having maximum absolute value.

# Input: n = 13, m = 4
# Output: 12
# Explanation: 12 is the closest to 13, divisible by 4.

# Input: n = -15, m = 6
# Output: -18
# Explanation: Both -12 and -18 are closest to -15, but-18 has the maximum absolute value

# def closest_number(n, m):
#     i = 1
#     high, low = 0, 0
#     while high == 0:
#         if (((n + i) % m) == 0):
#             high = n + i
#         i = i + 1
#     i = 1
#     while low == 0:
#         if (((n - i) % m) == 0):
#             low = n - i
#         i = i + 1
#     highDiff = high - n
#     lowDiff = n - low
#     if(highDiff > lowDiff):
#         return low
#     elif(highDiff == lowDiff):
#         if(abs(high) > abs(low)):
#             return high
#         else:
#             return low
#     else:
#         return high

# def closest_number(n, m):
#     # find the quotient
#     closest = 0
#     min_difference = float('inf')
#
#     # Check numbers around n
#     for i in range(n - abs(m), n + abs(m) + 1):
#         if i % m == 0:
#             difference = abs(n - i)
#
#             if (difference < min_difference) or (difference == min_difference and abs(i) > abs(closest)):
#                 closest = i
#                 min_difference = difference
#     return closest

def closest_number(n, m) :
    # Find the quotient
    q = int(n / m)
    
    # 1st possible closest number
    n1 = m * q
    
    # 2nd possible closest number
    if((n * m) > 0) :
        n2 = (m * (q + 1)) 
    else :
        n2 = (m * (q - 1))
    
    # if true, then n1 is the required closest number
    if (abs(n - n1) < abs(n - n2)) :
        return n1
    
    # else n2 is the required closest number 
    return n2

if __name__ == "__main__":
  print(closest_number(13, 4))
  print(closest_number(-15, 6))

