def factorial(n):
    r = 1
    for i in range(2, n):
        r *= i
    return r


if __name__ == '__main__':
    print(factorial(5))