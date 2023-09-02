def decompose(n,b) :
    l = []
    while n > 0 :
        r = n % b
        q = n // b
        l = [r]+l
        n = q
    return l
print(decompose(25,2))
