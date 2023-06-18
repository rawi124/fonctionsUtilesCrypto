def minimum2(L) :
    min1=L[0]
    min2=L[1]
    if min1 > min2 :
        min1,min2=min2,min1
    i = 2
    while i < len(L) :
        if L[i] < min1  :
            min1,min2=L[i],min1
        elif L[i] > min1 and L[i] < min2 :
            min2=L[i]
        i=i+1
    return min2
l=[3,2,5,1,0,4]
print(minimum2(l))
    
            
