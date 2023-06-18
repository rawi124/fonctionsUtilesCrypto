"""
recherche deux nombres amicaux a et b
deux nombres entiers positifs a et b sont considérés comme des nombres amicaux :
==>La somme des diviseurs propres de a est égale à b
==>La somme des diviseurs propres de b est égale à a
"""
def som_div_propres(nombre) :
    """
    calcule la somme des diviseurs propres d'un nombre
    un diviseur propre de n est un diviseur de n inferieur a n et qui exclut n
    """
    diviseur, somme = 2, 1
    if nombre == 1 :
        return 0
    else :
        racine = nombre**0.5
        while diviseur < racine  :
            if nombre%diviseur == 0 :
                somme += diviseur
                div_pr = nombre//diviseur
                somme += div_pr
            diviseur = diviseur +1
        #partie pour verifier si nombre**0.5 est un carre parfait, si c est la cas
        #il est ajouté a la somme des diviseurs propres
        parfait = int(racine)
        if nombre == (parfait**2):
            somme += parfait
    return somme
def amicaux(bits) :
    """
    recherche les nombres amicaux inferieur a 2**bits
    """
    amicaux, traite = [], []
    i = 2
    maxi = 2**bits
    while nb1 < maxi:
        somme_d_p = som_div_propres(nb1)
        if nb1 == som_div_propres(somme_d_p) and nb1 != somme_d_p and somme_d_p not in traite :
            traite += [nb1]
            amicaux += [(nb1,somme_d_p),]
        nb1 += 1
    return amicaux
