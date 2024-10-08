
def suite_Fibonacci(n):
    a, b = 1, 1
    if n >= 1:
        yield a
    if n >= 2:
        yield b
    for _ in range(2, n):
        a, b = b, a + b
        yield b

def chiffres_pairs(k):
    return [int(chiffre) for chiffre in str(k) if int(chiffre) % 2 == 0]

def est_super_impair(k):
    return len(chiffres_pairs(k)) == 0

def super_impairs_fibonacci(n):
    return (fibo for fibo in suite_Fibonacci(n) if est_super_impair(fibo))

if __name__ == "__main__":
    n = 10
    print("Les premiers termes de la suite de Fibonacci :")
    print(list(suite_Fibonacci(n)))

    k = 13579
    print(f"Chiffres pairs dans {k} :", chiffres_pairs(k))
    print(f"{k} est super-impair :", est_super_impair(k))

    print("Nombres super-impairs parmi les premiers termes de la suite de Fibonacci :")
    print(list(super_impairs_fibonacci(n)))