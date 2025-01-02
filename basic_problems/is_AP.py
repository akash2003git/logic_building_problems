# def isAP(arr):
#     n = len(arr)
#     if n == 1: return True
#     d = arr[1] - arr[0]
#     for i in range(1, n):
#         if (arr[i] != (arr[0] + (i) * d)):
#             return False
#     return True

def isAP(arr):
    n = len(arr)
    if n == 1: return True
    d = arr[1] - arr[0]
    if (arr[-1] - arr[0] != (n - 1) * d):
        return False
    return True

arr1 = [1, 4, 7, 10, 13]
arr2 = [13, 10, 7, 4, 1]
print(isAP(arr1))
print(isAP(arr2))
