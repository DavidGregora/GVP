import random
import os
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

def najblizsie_mensie_prvocislo(cislo):
    prvocisla = eratosthenovo_sito(cislo)
    for p in reversed(prvocisla):
        if p <= cislo:
            return p

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
######### Jednotka z programu ###########

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



#######################             MAIN          ###############################################


#Vyber akcie, ze co chceme robit z tychto troch veci
def zaciatok():
    print("1..........Vypis vsetkych prvocisel po zadane cislo")
    print("2..........Generovanie velkeho procisla na zaklade zadanej bitovej dlzky")
    print("3..........Test prvociselnosti zadaneho prvocisla")
    vyberAkcie = int(input("Vyber akciu ktoru chces urobit podla cisla: "))


    match vyberAkcie :  
        case 1  : 
            os.system('cls||clear')
            print("Vypis vsetkych prvocisel po zadane cislo")
            prvocislaPoCislo()
        
        case 2 :
            os.system('cls||clear')
            print("Generovanie velkeho procisla na zaklade zadanej bitovej dlzky")
            

        case 3 :
            os.system('cls||clear')
            print("Test prvociselnosti zadaneho prvocisla")
            

        case _ : 
            os.system('cls||clear')
            print("Zadaj jedno z vyššie uvedených čísel.\n\n")
            zaciatok()
zaciatok()