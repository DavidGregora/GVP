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
                print("Musite zadat 1 alebo 2!")
            zvolenie()
        except ValueError:
            print("Musite zadat 1 alebo 2!")

def bity():
    while True:
        try:
            bitova_dlzka = int(input("Kolko bitov ma mat cislo: "))
            bit_cislo = 2 ** bitova_dlzka
            print(Algoritmus.eratosthenovo_sito(bit_cislo))
            najblizsie_prvocislo = Algoritmus.najblizsie_mensie_prvocislo(bit_cislo)
            print("Najvacsie prvocislo je:", najblizsie_prvocislo)
            break
        except ValueError:
            print("Musite zadat cele cislo!")

def cislo():
    while True:
        try:
            cis_cislo = int(input("Zadajte cislo: "))
            iteracie = int(input("Kolko iteracii ma byt prevedenych? "))
            if (iteracie >= cis_cislo):
                print(f"Maximalny pocet prevedenych iteracii bol: {cis_cislo - 1}.")
            print(Algoritmus.eratosthenovo_sito(cis_cislo))
            print(Algoritmus.arkinov_test(cis_cislo, iteracie))
            if (Algoritmus.arkinov_test(cis_cislo, iteracie) == "Cislo nie je prvocislo!" and cis_cislo > 1):
                najblizsie_prvocislo = Algoritmus.najblizsie_mensie_prvocislo(cis_cislo)
                print("Najbližšie menšie prvočíslo k číslu", cis_cislo, "je", najblizsie_prvocislo)
            break
        except ValueError:
            print("Musite zadat cele cislo!")


zvolenie()
