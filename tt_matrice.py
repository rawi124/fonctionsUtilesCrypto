from random import *
import copy

def genmatrix(n,p,t) :
    i = 0
    l = []
    while i < n :
        j = 0
        s = []
        while j < p :
            s = s +[randrange(0,t)]
            j = j + 1
        l = l +[s]
        i = i + 1
    return l

def gendiag(n,t):
    l = []
    i = 0
    while i < n :
        tmp = [0]*n
        tmp[i] = randrange(0,t)
        l = l +[tmp]
        i = i + 1
    return l

def gentrianginf(n,t):
    i = 0
    l = []
    x = 1
    while i < n :
        j = 0
        tmp = [0]*n
        while j < x :
            tmp[j] = randrange(0,t)
            j = j + 1
        l = l + [tmp]
        x = x + 1
        i = i + 1
    return l

def gensym(n,t):
    l = gentrianginf(n,t)
    i = 0
    j=0
    while j < n :
        i = 0
        while i < n :
            l[j][i] = l[i][j]
            i = i + 1
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

def gensym(n,t):
    l = gentrianginf(n,t)
    i = 0
    j=0
    while j < n :
        i = 0
        while i < n :
            l[j][i] = -(l[i][j])
            i = i + 1
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

def gen_circulante(k,t) :
    n = t - 1
    i = 1
    l = [k]+[0]*n
    while i < t :
        if k & 1 == 1 :
            k = k >> 1
            s = 1 << n
            k=k^s
        else :
            k = k >> 1
        l[i]=k
        i = i + 1
    return l

def liste_perm(n) :
    l=[]
    i = 0
    l=[0]*n
    while i < n :
        l[i] = i
        i = i + 1
    n = n -1
    i = 0
    while i < n :
        j = randrange(0,n-i)
        l[j],l[n-i]=l[n-i],l[j]
        i = i + 1
    return l
print(liste_perm(3))
    





























