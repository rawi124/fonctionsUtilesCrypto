def inverse(a,p) :
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    r = 1
    x = p
    while ( a > 1 ) :
        q = p // a
        r = p % a
        p = a
        a = r
        s = u - u1*q
        u = u1
        u1 = s
        t = v -v1*q
        v = v1
        v1 = t
    return v1 % x
print(inverse(11,1665))
