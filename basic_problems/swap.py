def swap(a, b):
    return b, a

if __name__ == "__main__":

    a = 1
    b = 2

    print("Before swap: ")
    print(f"a = {a}\nb = {b}")

    # a = a + b
    # b = a - b
    # a = a - b

    # a ,b = b, a

    a, b = swap(a, b)

    print("After swap: ")
    print(f"a = {a}\nb = {b}")
