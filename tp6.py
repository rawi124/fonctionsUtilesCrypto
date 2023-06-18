import random
import copy

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

def matmat(A,B):
    n = len(A)
    m = len(A[0])
    w = len(B[0])
    j = 0
    l=[]
    k = []
    while j < n:
        i = 0
        while i < w :
            y = 0
            s = 0
            while y < m :
                s = s +A[j][y]*B[y][i]
                y = y + 1
            i = i + 1
            k = k+[s]
        l = l + [k]
        k=[]
        j = j + 1
    return l

def transpose(M) :
    n = len(M)
    t = len(M[0])
    p = []
    s= []
    j = 0
    while j < t :
        i = 0
        while i < n :
            p = p +[M[i][j]]
            i = i + 1
        s = s + [p]
        p = []
        j = j + 1
    return s

def gentrianginf_inv(n,t):
    i = 0
    l = []
    x = 1
    while i < n :
        j = 0
        tmp = [0]*n
        while j < x :
            tmp[j] = random.randrange(1,t)
            j = j + 1
        l = l + [tmp]
        x = x + 1
        i = i + 1
    return l

def gentrianginf_mod26(n):
    i = 0
    l = []
    x = 1
    p= 0
    while i < n :
        j = 0
        tmp = [0]*n
        while j < x :
            tmp[j] = random.randrange(1,26)
            j = j + 1
        a = random.randrange(1,26)
        while ( a %2 == 0 ) or ( a %13 == 0):
            a = random.randrange(1,26)
        tmp[p] = a
        p = p + 1
        l = l + [tmp]
        x = x + 1
        i = i + 1
    return l
def genmatrix_inv(n) :
    A = gentrianginf_inv(n,10)
    D = gentrianginf_inv(n,10)
    B= transpose(D)
    n = len(A)
    m = len(A[0])
    w = len(B[0])
    j = 0
    l=[]
    k = []
    while j < n:
        i = 0
        while i < w :
            y = 0
            s = 0
            while y < m :
                s = s +A[j][y]*B[y][i]
                y = y + 1
            i = i + 1
            k = k+[s]
        l = l + [k]
        k=[]
        j = j + 1
    return l

def genmatrixinv_mod26(n) :
    A =gentrianginf_mod26(n)
    D =gentrianginf_mod26(n)
    B= transpose(D)
    n = len(A)
    m = len(A[0])
    w = len(B[0])
    j = 0
    l=[]
    k = []
    while j < n:
        i = 0
        while i < w :
            y = 0
            s = 0
            while y < m :
                s = s +A[j][y]*B[y][i]
                y = y + 1
            i = i + 1
            s = s % 26
            k = k+[s]
        l = l + [k]
        k=[]
        j = j + 1
    return l

def gencirculante(L) :
    i = 1
    t = copy.copy(L)
    s=[]
    s = s + [L]
    x=len(L)-1
    z = x 
    while i < len(L) :
        t=[t[x]]+t[:x]
        i = i + 1
        t = copy.copy(t)
        s=s+[t]
    return s
def fct(V,Y) :
    M = gencirculante(V)
    Z = gencirculante(Y)
    return matmat(M,Z)
print(fct([1,2,3],[6,6,2]))
print('oui')
def circmultvec(V,Y):
    i = 0
    n=len(V)
    l=[]
    s = 0
    while i < n :
        j = 0
        while j < n :
            s = s +Y[j]*V[j]
            j = j+1
        V=[V[-1]]+V[:(n-1)]
        l = l +[s]
        s = 0
        i = i + 1
    return l
def cirmultmat(A,B):
    n = len(A)
    m = len(A)
    w = len(B)
    j = 0
    l=[]
    k = []
    while j < n:
        i = 0
        while i < w :
            y = 0
            s = 0
            while y < m :
                print(B)
                s = s +A[y]*B[y]
                y = y + 1
                B=[B[-1]]+B[:(n-1)]
            i = i + 1
            k = k+[s]
        print(A)
        print("\n")
        A=[A[-1]]+A[:(n-1)]
        l = l + [k]
        k=[]
        j = j + 1
    return l
print(cirmultmat([1,2,3],[6,6,2]))


def cirmultmat2(A,B):
    n = len(A)
    m = len(A)
    w = len(B)
    j = 0
    l=[]
    k = []
    while j < n:
        i = 0
        while i < w :
            y = 0
            s = 0
            B=[B[-1]]+B[:(n-1)]
            while y < m :
                s = s +A[y]*B[y]
                y = y + 1
            i = i + 1
            k = k+[s]
        print(A,B)
        A=[A[-1]]+A[:(n-1)]
        l = l + [k]
        k=[]
        j = j + 1
    return l

        




















    
