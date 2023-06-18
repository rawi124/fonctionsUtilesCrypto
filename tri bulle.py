def tri_bulle(L) :
    i = len(L) -1
    j = len(L)- 2
    while i >= 0 :
        j=i
        while j >= 0 :
            if L[i] < L[j] :
                L[i],L[j] = L[j],L[i]
            j=j-1
        i=i-1
    return L
l=[10,2,5,9,-1,10,0,100]
print(tri_bulle(l))
                
        
