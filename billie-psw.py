import random
import time

def miller_rabin(n, k=5): # k = iteracie (ak treba, kludne sa daju zvysit, ale dlhsie to bude trvat)
    # Urcili sme male prvocisla a cele cisla priamo, na setrenie casu
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(2, min(1000, n)):
        if n % i == 0:
            return False

    # Napise n ako 2^r*d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Miller-Rabin test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def lucas_selfridge(n):    #nasiel som na internete, ze s tymto je to najlepsie
    # "Lucas sequence" parametre podla Selfridga
    D = 5
    P, Q = 1, (1 - D) // 4

    # Inicializalia hodnot
    u, v, k = 0, 2, n

    # Prevedenie Lucas-Selfridge test
    while k > 0:
        if k & 1:
            u, v = (u * P + v * Q) % n, (v * P + u * Q) % n
        u, v, k = (u * v) % n, (v * v + 2 * (u * u) * Q) % n, k // 2

    if u == 0 or v == 0:
        return True
    else:
        return False

def generate_large_prime(bits):
    while True:
        candidate = random.getrandbits(bits) | (1 << bits - 1) | 1  # Pozmeni posledny bit, aby vzdy bolo cislo neparne
        if miller_rabin(candidate) and lucas_selfridge(candidate):
            return candidate

def main():
    while True:
        try:
            bits = int(input("Zadejte pocet bitov pozadovaneho cisla: "))
            if bits <= 0:
                print("Pocet bitov musi byt kladne cislo.")
            else:
                start_time = time.time()
                prime = generate_large_prime(bits)
                end_time = time.time()
                duration = end_time - start_time
                print("Vygenerovane prvocislo o dlzke", bits, "bitov:", prime, "za cas", duration)
                break
        except ValueError:
            print("Zadajte prosim cele cislo")

'''
def generate_prime():
    start_time = time.time()
    while True:
        candidate = random.getrandbits(bits) | (1 << bits - 1) | 1
        if miller_rabin(candidate) and lucas_selfridge(candidate):
            end_time = time.time()
            duration = end_time - start_time
            return candidate,duration
'''
main()
# generate_prime()