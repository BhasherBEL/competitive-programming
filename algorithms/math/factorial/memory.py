def factorial(n, mem={1: 1}):
    if n not in mem:
        mem[n] = n*factorial(n-1)
    return mem[n]
    

if __name__ == '__main__':
    print(factorial(5))