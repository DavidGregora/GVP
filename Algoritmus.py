import random

def eratosthenovo_sito(do): #algoritmus na eratosthenovo sito (z internetu)
    do += 1
    sito = [True] * do

    for i in range(2, do):
        if sito[i]:
            for j in range(i ** 2, do, i):
                sito[j] = False

    prvocisla = []
    for i in range(2, do):
        if sito[i]:
            prvocisla.append(i)
    return prvocisla

def najblizsie_mensie_prvocislo(cislo): #algoritmus na zistenie najlbizsieho mensieho prvocisla po generovani, ak zadane nie je
    prvocisla = eratosthenovo_sito(cislo)
    for p in reversed(prvocisla):
        if p <= cislo:
            return p

def arkinov_test(p, k):  #test prvociselnosti 2
    if p <= 1:
        return "Cislo nie je prvocislo!"
    if p <= 3:
        return "Cislo je prvocislo!"

    def kontrola(a, p):
        return pow(a, p - 1, p) == 1

    for _ in range(k):
        a = random.randint(2, p - 1)
        if not kontrola(a, p):
            return "Cislo nie je prvocislo!"
    return "Cislo je prvocislo!"
