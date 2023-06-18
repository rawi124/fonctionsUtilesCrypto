def pgcd(a,b) :
    if b == 0 :
        return a
    while b > 0 :
        tmp = b
        b=a%b
        if b == 0 :
            b = tmp
            break
        a = tmp
    return b
def pgcd1(a,b) :
    while b != 0 :
        r = a % b
        a,b=b,r
    return a
print(pgcd1(56,42))
