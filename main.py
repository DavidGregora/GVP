import random
import os
import math
import timeit
import logging

logging.basicConfig(filename='test_prvociselnosti.log', level=logging.INFO, format='%(asctime)s - %(message)s')


"""
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




def arkinov_test(p, k):
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
"""
###################### READ WRITE FILE ####################################
def write_list_to_file(lst, filename):
    try:
        with open(filename, 'r'):
            pass
    except FileNotFoundError:
        open(filename, 'w').close()

    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

def read_value_from_file():
    while True:
        file_name = input("Zadejte název souboru: ")
        file_path = os.path.join(os.path.dirname(__file__), file_name)  # Získání úplné cesty k souboru
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) != 1:
                    print("Chyba - Soubor obsahuje více než jedno řádek")
                else:
                    value = lines[0].strip()
                    if not value.isdigit():  # Kontrola, zda se jedná o celé číslo
                        print("Chyba - Obsah souboru není celé číslo")
                    else:
                        return int(value)
        except FileNotFoundError:
            print("Chyba - Soubor nenalezen")
###################### READ WRITE FILE ####################################


######################### ERATOSTHENOVO SITO #####################################
def eratosthenovo_sito(do):
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

def prvocisloPoCisloRucne():
    zadanePrvocislo = int(input("Zadaj hodnotu cisla po ktore nasledne vypisem vsetky prvocisla: \n"))
    print("ZADANE CISLO:\n"+str(zadanePrvocislo))
    print(eratosthenovo_sito(zadanePrvocislo))
    write_list_to_file(eratosthenovo_sito(zadanePrvocislo), 'Eratosthenovo.txt')
    print("Vysledok zapisany do Eratosthenovo.txt")

def prvocisloPoCisloImport():
    
    zadanePrvocislo = read_value_from_file()
    print("Zadane prvocislo je: \n"+str(zadanePrvocislo)+"\n")
    print(eratosthenovo_sito(zadanePrvocislo))
    write_list_to_file(eratosthenovo_sito(zadanePrvocislo), 'Eratosthenovo.txt')
    print("Vysledok zapisany do Eratosthenovo.txt")


def prvocislaPoCislo():
    print("Chcete zadat cislo RUCNE alebo IMPORT zo suboru?")
    vyberAkcie = str(input("RUCNE // IMPORT\n")).lower()

    match vyberAkcie:
        case "rucne":
            prvocisloPoCisloRucne()

        case "import":
            prvocisloPoCisloImport()
        
        case _ :
            print("Nespravny vyber")
            prvocislaPoCislo()
######################### ERATOSTHENOVO SITO #####################################

######################### Miler rabin test #######################################
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

def testovanie_prvocisla(cislo, k):
    duration = timeit.timeit(lambda: je_prvocislo(cislo, k), number=1)  # Doba trvání testování v sekundách

    pocet_bitov = int(math.log2(cislo)) + 1  # Počet bitů čísla

    logging.info(f'Miller-Rabin test cisla {cislo}: Prvocislo: {je_prvocislo(cislo, k)}, Doba testovania: {duration:.10f} sekundy, Pocet bitov: {pocet_bitov}, Pocet iteracii: {k}')

    if je_prvocislo(cislo, k):
        print(cislo, "je prvočíslo.")
    else:
        print(cislo, "nie je prvočíslo.")

def testovanie_prvocisla_rucne():
    cislo_k_otestovaniu = int(input("Zadajte číslo k otestovaniu: "))
    pocet_iteraci = int(input("Zadajte počet iterácií: "))
    testovanie_prvocisla(cislo_k_otestovaniu, pocet_iteraci)

def testovanie_prvocisla_import():
    pocet_iteraci = int(input("Zadaj pocet iteracii: "))
    cislo_k_otestovaniu = read_value_from_file()
    print("Zadane prvocislo je: \n"+str(cislo_k_otestovaniu)+"\n")
    testovanie_prvocisla(cislo_k_otestovaniu, pocet_iteraci)

def vyber_moznosti():
    print("Chcete zadat cislo RUCNE alebo IMPORT zo suboru?")
    vyberAkcie = str(input("RUCNE // IMPORT\n")).lower()

    match vyberAkcie:
        case "rucne":
            testovanie_prvocisla_rucne()

        case "import":
            testovanie_prvocisla_import()
        
        case _ :
            print("Nespravny vyber")
            prvocislaPoCislo()

######################### Miler rabin test #######################################

#######################             MAIN          ###############################################


#Vyber akcie, ze co chceme robit z tychto troch veci
def zvolenie():
    while True:
        try:
            print("1..........Vypis vsetkych prvocisel po zadane cislo")
            print("2..........Test prvociselnosti zadaneho prvocisla")
            print("3..........Generovanie velkeho procisla na zaklade zadanej bitovej dlzky")
            volba = int(input("\nVyber akciu ktoru chces urobit podla cisla: "))
            if volba == 1:
                os.system('cls||clear')
                print("Vypis vsetkych prvocisel po zadane cislo")
                prvocislaPoCislo()
                break
            elif volba == 2:
                os.system('cls||clear')
                print("Testovanie prvocisla")
                vyber_moznosti()
                break
            elif volba == 3:
                os.system('cls||clear')
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