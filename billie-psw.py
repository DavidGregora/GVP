import random
import time

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67,
                    71, 73, 79, 83, 89, 97, 101, 103,
                    107, 109, 113, 127, 131, 137, 139,
                    149, 151, 157, 163, 167, 173, 179,
                    181, 191, 193, 197, 199, 211, 223,
                    227, 229, 233, 239, 241, 251, 257,
                    263, 269, 271, 277, 281, 283, 293,
                    307, 311, 313, 317, 331, 337, 347, 349]


def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)


def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
    by first primes'''
    start_time = time.time()
    while True:
        # Obtain a random number
        pc = nBitRandom(n)

        # Test divisibility by pre-generated
        # primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            end_time = time.time()
            duration = end_time - start_time
            if duration > 30:
                return "Generovanie prvocisla trvalo prilis dlho", duration
            return pc, duration


def isMillerRabinPassed(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


def generate_prime(bits):
    start_time = time.time()
    while True:
        n = bits
        prime_candidate, duration = getLowLevelPrime(n)
        if isinstance(prime_candidate, str):  # Ak vráti reťazec, časový limit bol prekročený
            return prime_candidate, duration
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            end_time = time.time()
            total_duration = end_time - start_time
            return prime_candidate, total_duration

"""
bits = int(input("Zadaj pocet bitov pre generovanie prvocisla: "))
prime, duration = generate_prime(bits)
print(f"Vygenerovane prvocislo: {prime}, cas trvania: {duration} sekund")
"""

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

# Hlavny zdroj: https://faculty.lynchburg.edu/~nicely/misc/bpsw.html
