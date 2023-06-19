from math import log2, ceil
from binary_operations import *

def main():
    x = 51
    p = 1000
    r = 4
    k = 3
    S= modulus_function_computation(x, p, r, k)
    print(S)


def modulus_function_computation(x, p, r, k):
    # zmiana liczby dziesietnej na wektor binarny
    x = int_to_binary(x)
    n = len(x)+1
    # r = log2 P
    r = ceil(log2(p))
    k = ceil(n / r)

    if len(x) < k * r:
        x= add_zeros_to_binary_list(x, k*r-n)
    X = []
    
    for i in range(k):
        Xi = int(''.join(map(str, X[i-1])), 2)
        S += Xi * (2**(i * (r - 1)))
        X.append(Xi)

    Stemp = S

    while Stemp > 2 * p:
        ntemp = len(Stemp)
        ktemp = ceil(ntemp / r)

        if len(Stemp) < ktemp * r:
            Stemp= add_zeros_to_binary_list(Stemp, ktemp * r - ntemp)

        S_parts = []
        for i in range(k):
            start = i * r
            end = start + r
            S_parts.append(bin(Stemp)[2:][start:end])

        Stemp = 0
        for i in range(1, k + 1):
            Si = int(S_parts[i-1], 2)
            Stemp += Si * (2**(i * (r - 1)))

    if p <= Stemp:
        S = Stemp - p
    else:
        S = Stemp

    return S


main()