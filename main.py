import random

def mocnina(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def miller_rabin(d, n):
    a = 2 + random.randint(1, n - 4)
    x = mocnina(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def je_prvocislo(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not miller_rabin(d, n):
            return False
    return True

def vypis_prvocisla(do_cisla, k):
    print("Prvočísla do", do_cisla, ":")
    for i in range(2, do_cisla + 1):
        if je_prvocislo(i, k):
            print(i, end=" ")

def testovanie_prvocisla(cislo, k):
    if je_prvocislo(cislo, k):
        print(cislo, "je prvočíslo.")
    else:
        print(cislo, "nie je prvočíslo.")

def zvolenie():
    while True:
        try:
            volba = int(input("Pre výpis všetkých prvočísel do zadaného čísla zadajte 1, pre otestovanie, či je číslo prvočíslo, zadajte 2, pre zadanie bitovej dĺžky, zadajte 3: "))
            if volba == 1:
                konecne_cislo = int(input("Zadajte konečné číslo: "))
                pocet_iteraci = int(input("Zadajte počet iterácií: "))
                vypis_prvocisla(konecne_cislo, pocet_iteraci)
                break
            elif volba == 2:
                cislo_k_otestovaniu = int(input("Zadajte číslo k otestovaniu: "))
                pocet_iteraci = int(input("Zadajte počet iterácií: "))
                testovanie_prvocisla(cislo_k_otestovaniu, pocet_iteraci)
                break
            elif volba == 3:
                bitova_dlzka = int(input("Zadajte dĺžku bitu: "))
                pocet_iteraci = int(input("Zadajte počet iterácií: "))
                bit_cislo = 2 ** bitova_dlzka
                vypis_prvocisla(bit_cislo, pocet_iteraci)
                break
            else:
                print("Musíte zadať 1, 2 alebo 3!")
        except ValueError:
            print("Musíte zadať celé číslo!")

zvolenie()
