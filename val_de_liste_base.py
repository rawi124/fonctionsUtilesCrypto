def valeur(L,b) :
    i = len(L)-1
    s = 0
    j = 0
    t=1
    while i >= 0 :
        s = s + L[i]*(t)
        t=t*b
        j = j + 1
        i = i -1
    return s
print(valeur([3,2,1],5))
