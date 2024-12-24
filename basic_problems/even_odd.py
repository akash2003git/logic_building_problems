def isEven(n):
    return n % 2 == 0


if __name__ == "__main__":
    n = int(input("Input: "))
    if isEven(n):
        print("true")
    else:
        print("false")
