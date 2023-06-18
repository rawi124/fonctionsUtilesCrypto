def decompose(n) :
    l = []
    i = 0
    if n % 2 == 0 :
        l=l+[2]
        while n % 2 == 0 :
            n = n // 2
    i = 3
    while n != 1 :
        if n % i == 0 :
            l=l+[i]
            while n % i == 0 :
                n=n//i
        i = i + 2
    return l
print(decompose(15552))
