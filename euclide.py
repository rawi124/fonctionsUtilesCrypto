def euclide(a,n) :
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    r = 1
    l  =[]
    while ( n > 0 ) :
        q = a // n
        r = a % n
        a = n
        n = r
        s = u - u1*q
        u = u1
        u1 = s
        t = v -v1*q
        v = v1
        v1 = t
    l =[u]+[v]+[a]
    return l
print(euclide(54,39))
