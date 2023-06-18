def minimum_posi(L) :
    i = 0
    u = []
    mini=L[0]
    while i < len(L) :
        if L[i] <= mini and len(u) == 0 :
            mini=L[i]
            u = u +[i]
        elif len(u) != 0 and L[i] == mini  :
            mini=L[i]
            u = u +[i]
        elif L[i] < mini and len(u) != 0 :
            u=[]
            mini=L[i]
            u=u+[i] 
        i = i +1
    return u
l=[1,1,-1,0,0]
print(minimum_posi(l))
    
