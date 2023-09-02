def som_div_propres(n) :
    d = 2
    s = 1
    if n == 1 :
        return 0
    else : 
        while d < (n**0.5)  :
            if n%d == 0 :
                s=s+d
                x = n//d
                s=s+x
            d = d +1
        m = int(n**0.5)
        if n == (m**2):
            s = s + m
    return s
print(som_div_propres(1))
