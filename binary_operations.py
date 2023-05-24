from math import log2, floor

# zamiana liczby dziesiętnej na wektor binarny
def decimal_to_binary(decimal_x):
    result = []
    while decimal_x > 0:
        result.insert(0, decimal_x % 2)
        decimal_x = decimal_x // 2
    
    return result

# Funkcja wypełniająca wektory bitowe zerami, aby miały taką samą długość równej długości wektora o największej długości
def fill_with_zeros(binary_a, binary_b):
    length_a = len(binary_a)
    length_b = len(binary_b)
    if length_a > length_b:
        binary_b = [0] * (length_a - length_b) + binary_b
    elif length_b > length_a:
        binary_a = [0] * (length_b - length_a) + binary_a
    return binary_a, binary_b


# Funkcja porównująca dwa wektory bitowe (gdzie False oznacza 0, a Trye oznacza 1) i zwracająca True, jeśli pierwszy wektor jest większy lub równy drugiemu, a False w przeciwnym wypadku.
def compare_binary(binary_a, binary_b):
    # Sprawdzenie, który wektor jest dłuższy
    length_a = len(binary_a)
    length_b = len(binary_b)
    if length_a > length_b:
        binary_b = [0] * (length_a - length_b) + binary_b
    elif length_b > length_a:
        binary_a = [0] * (length_b - length_a) + binary_a

    # Iteracja od końca wektorów
    for bit_a, bit_b in zip(binary_a[::-1], binary_b[::-1]):
        # Jeśli bit_a jest większy od bit_b, to zwróć True
        if bit_a > bit_b:
            return True
        # Jeśli bit_b jest większy od bit_a, to zwróć False
        elif bit_b > bit_a:
            return False

    # Jeśli oba wektory są takie same, to zwróć True
    return True

# Funkcja konwertująca wektor bitowy na liczbę dziesiętną
def binary_to_decimal(binary_x):
    result = 0
    for i in range(len(binary_x)):
        result += binary_x[i] * 2 ** (len(binary_x) - i - 1)
    return result

# funkcja wykonująca operację X(mod P) na dwóch wektorach bitowych (gdzie X to binary_x, a P to binary_p)
def modulo_function(X, P):
    X, P = fill_with_zeros(X, P)
    print("X = ", X)
    print("P = ", P)
    r = len(P)
    k = len(X) // r
    n = len(X)

    if len(X) < k * r:
        X = [0] * (k * r - n) + X

    X_parts = [X[i*r:(i+1)*r] for i in range(k, 0, -1)]
    X_parts.reverse()

    S = sum([(int("".join(map(str, X_i)), 2) * (2 ** ((i+1) * (r-1)))) % int("".join(map(str, P)), 2) for i, X_i in enumerate(X_parts)])

    while S > (2 * int("".join(map(str, P)), 2)):
        n_temp = len(str(bin(S))) - 2
        k_temp = n_temp // r

        if len(str(bin(S))) - 2 < k_temp * r:
            S = int(bin(S)[(k_temp * r) - n_temp:], 2)

        S_parts = [str(bin(S))[i*r:(i+1)*r] for i in range(k_temp, 0, -1)]
        S_parts.reverse()

        S = sum([(int(S_i, 2) * (2 ** ((i+1) * (r-1)))) % int("".join(map(str, P)), 2) for i, S_i in enumerate(S_parts)])

        if int("".join(map(str, P)), 2) <= S:
            S -= int("".join(map(str, P)), 2)
        else:
            break

    return S

