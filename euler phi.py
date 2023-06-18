
def euler_phi(n) :
    cpt = 0
    i = 1
    x = n
    p=1
    while i < n :
        while n != 0 :
            r = p % n
            p,n = n,r
        if p == 1:
            cpt = cpt + 1
        n=x
        p=i
        i = i + 1
    return cpt
print(euler_phi(27))
