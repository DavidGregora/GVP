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
