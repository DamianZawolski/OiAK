import math

def int_to_bit_vector(num, width):
    binary_str = bin(num)[2:].zfill(width)
    return [int(bit) for bit in binary_str]

def modulo_computation(X, N, P):
    DELTA = (P-1).bit_length()  # liczba bitów potrzebna do zapisania liczby modP
    K = (N + DELTA - 1) // DELTA  # K subwektorów
    padding = DELTA * K - N

    paddedX = X << padding

    subvectors = []

    for i in range(K):
        subvector = (paddedX >> (i * DELTA)) & ((1 << DELTA) - 1)  # podział X na DELTA-bitowe liczby
        subvectors.append(subvector)
        # print("subv[{}]: {}".format(i, bin(subvector)))  # do testowania podziału

    S = 0  # suma

    for i in range(K):
        S += subvectors[i] * ((2 ** (DELTA * i)) % P)
        # print("S: {}".format(S))

    while S > 2 * P:
        n = S.bit_length()
        k_temp = n // DELTA

        if n % DELTA != 0:
            k_temp += 1  # nie da się bezpośrednio zrobić ceil(n/DELTA)

        subvectors = []

        for i in range(k_temp):
            subvector = (S >> (i * DELTA)) & ((1 << DELTA) - 1)  # podział S na DELTA-bitowe liczby
            subvectors.append(subvector)
            # print("subv[{}]: {}".format(i, bin(subvector)))

        S = 0

        for i in range(k_temp):
            S += subvectors[i] * ((2 ** (DELTA * i)) % P)
            # print("S: {}; i: {}".format(bin(S), i))

    if S > P:
        S -= P

    # print("Final S: {}".format(S))

    out_vec = S

    return out_vec

def modulo_multiplication(A, B, mulN, DELTA, mulP):
    out_size = mulP.bit_length()  # rozmiar liczby wyjściowej

    A_vec = [0] * (DELTA + 1)  # podział liczby na mniejsze wektory
    B_vec = [0] * (DELTA + 1)

    R = 0

    S_temp = 0

    for i in range(1, DELTA + 1):
        A_vec[i] = (A >> ((i - 1) * (mulN // DELTA))) & ((1 << (mulN // DELTA)) - 1)
        B_vec[i] = (B >> ((i - 1) * (mulN // DELTA))) & ((1 << (mulN // DELTA)) - 1)

    for i in range(1, DELTA + 1):
        for j in range(1, DELTA + 1):
            S_temp += (A_vec[i] * B_vec[j] * (2 ** ((i + j - 2) * 3))) % mulP

    while S_temp > mulP:
        S_temp -= mulP

    R = S_temp

    return R