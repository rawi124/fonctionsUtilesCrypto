def det(l) :
    i = 0
    n = len(l)
    while i < n and l[0][i] == 0 :
        i = i +1
    


def gauss(l):
    j = 1
    z = 0
    n=len(l[z])
    while z < len(l)-1:
        x = l[z][z]
        while j < len(l):
            s = l[j][0]
            y = 0
            while y < n  :
                l[j][y] = x*l[j][y]-s*l[z][y]
                y = y + 1
            j = j + 1
        j = 2
        z = z + 1 
    return l
def matvec(M,V):
    n = len(V)
    m = len(M)
    s = 0
    i = 0
    l = []
    while i < m :
        j = 0
        s = 0
        while j < n :
            s = s + V[j]*M[i][j]
            j = j + 1
        l = l +[s]
        i = i + 1
    return l
print(matvec([[2,0,0,0],[0,2,0,0],[0,2,1,0],[1,0,2,2]],[0.5,1,1,0.75]))
