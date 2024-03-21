import Algoritmus

def zvolenie():
    while True:
        try:
            volba = int(input("Pre bitovu dlzku zadajte 1, pre cislo 2: "))
            if volba == 1:
                bity()
                break
            elif volba == 2:
                cislo()
                break
            else:
                print("Zle brasko/sestra")
            zvolenie()
        except ValueError:
            print("Mimo si, skus este raz")

def bity():
    while True:
        try:
            bitova_dlzka = int(input("Kolko bitov ma mat cislo: "))
            bit_cislo = 2 ** bitova_dlzka
            print(Algoritmus.eratosthenovo_sito(bit_cislo))
            break
        except ValueError:
            print("Mimo si, skus este raz")

def cislo():
    while True:
        try:
            cis_cislo = int(input("Zadajte cislo: "))
            print(je_prvocislo(cis_cislo))
            print(Algoritmus.eratosthenovo_sito(cis_cislo))
            break
        except ValueError:
            print("Mimo si, skus este raz")

def je_prvocislo(cislo):
    if cislo <= 1:
        return "Cislo nie je prvocislo!"
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return "Cislo nie je prvocislo!"
    return "Zvolene cislo je prvocislo!"

zvolenie()
