def somme_ind_pair(L) :
    i = 0
    s = 0
    while i < len(L) :
        s = s + L[i]
        i += 2
    return s
l=[3,2,3,7,10,1]
print(somme_ind_pair(l))
