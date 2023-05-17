from math import log2, floor
from binary_operations import *

def main():
    x = 262149
    p = 47
    bits = decimal_to_binary(x)

    modulo_function(bits, p)


def split_into_subvectors(binary_x, r):
    result = []
    while binary_x:
        result.append(binary_x[:r])
        binary_x = binary_x[r+1:]

    return result


# funkcja wykonująca operację X(mod P)
def modulo_function(bits, p):
    r = floor(log2(p) - 1)

    # dodanie zer na początek żeby utworzyć subwektory równej długości
    while len(bits) % r != 0:
        bits.insert(0, 0)

    # podział wektora bitów na subwektory
    subvectors = split_into_subvectors(bits, r)
    k = len(subvectors)

    x = []
    for i in range(0, k):
        subv = subvectors[i]
        x = binary_addition(x, binary_multiplication(subv, pow(2, r*(i-1)) % p))

    s = x
    s_temp = s

    p_binary = decimal_to_binary(p)
    while compare_binary(s_temp, binary_multiplication(p_binary, [1, 0])):
        k_temp = len(s_temp) // r

        pad_with_zeros(s_temp, k_temp * r)

        subvectors_temp = split_into_subvectors(s_temp, r)

        s_temp = []

        for i in range(0, k_temp):
            subv = subvectors_temp[i]
            s_temp = binary_addition(s_temp, binary_multiplication(subv, pow(2, r*(i-1)) % p))


    if not compare_binary(p, s_temp):
        s = s_temp - p
    else:
        s = s_temp