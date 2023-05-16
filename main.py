from math import log2, floor


def main():
    x = 262149
    p = 47
    bits = decimal_to_binary(x)

    modulo_function(bits, p)


# zamiana liczby dziesiętnej na wektor binarny
def decimal_to_binary(decimal_x):
    result = []
    while decimal_x > 1:
        result.append(decimal_x % 2)
        decimal_x = decimal_x // 2
    result.append(decimal_x)

    return result


def split_into_subvectors(binary_x, r):
    result = []
    while binary_x:
        result.append(binary_x[:r])
        binary_x = binary_x[r+1:]

    return result


# funkcja wykonująca operację X(mod P)
def modulo_function(bits, p, r):
    r = floor(log2(p) - 1)

    #dodanie zer na początek żeby utworzyć subwektory równej długości
    while len(bits) % r != 0:
        bits.insert(0, 0)

    #podział wektora bitów na subwektory
    subvectors = split_into_subvectors(bits)

    x = []
    for subv in subvectors:
        x = binary_to_decimal(subv)