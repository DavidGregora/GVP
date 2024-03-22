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
            iteracie = int(input("Kolko iteracii ma byt prevedenych? "))
            if (iteracie >= cis_cislo):
                print(f"Maximalny pocet prevedenych iteracii bol: {cis_cislo - 1}.")
            print(Algoritmus.eratosthenovo_sito(cis_cislo))
            print(Algoritmus.arkinov_test(cis_cislo, iteracie))
            break
        except ValueError:
            print("Musite zadat cele cislo!")

zvolenie()
