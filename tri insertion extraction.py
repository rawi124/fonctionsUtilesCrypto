def tri(L) :
    mini = L[0]
    i=0
    tmp=0
    while i < len(L)-1 :
        mini=L[i]
        ind=i
        j=i
        while j < len(L) :
            if L[j] < mini :
                mini = L[j]
                ind=j
            j = j + 1
        L[i],L[ind]=L[ind],L[i]
        
        i=i+1
    return L
l=[2,7,1,8,12,0]
print(tri(l))
