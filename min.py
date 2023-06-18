def minimum(L) :
    min = L[0]
    i = 0
    while i < len(L) :
        if min > L[i] :
            min = L[i]
        i += 1
    return min
l=[3,2,5,7,2]
print(minimum(l))
