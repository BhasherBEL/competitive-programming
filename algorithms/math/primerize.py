def primerize(n):
    factors = []
    d = 2

    while n**0.5+1 >= d:
        if n%d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
            print(d)
    
    if n > 1:
        factors.append(n)
    
    return factors


if __name__ == '__main__':
    print(primerize(25437))