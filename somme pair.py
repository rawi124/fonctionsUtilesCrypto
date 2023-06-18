def somme_pair(L) :
    i = 0
    s = 0
    while i < len(L) :
        if (L[i] % 2) == 0 :
            s = s + L[i]
        i += 1
    return s
l = [3,2,5,7,4,1]
print(somme_pair(l))
    
