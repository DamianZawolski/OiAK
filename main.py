from binary_operations import *

def main():
    x = 7
    p = 3
    print("x = ", x)
    bits_x = decimal_to_binary(x)
    print("Zamiana na binarny x: ", bits_x)
    print("p = ", p)
    bits_p = decimal_to_binary(p)
    print("Zamiana na binarny p: ", bits_p)
    modulo_xp = modulo_function(bits_x, bits_p)
    print("Wynik modulo: ", modulo_xp)
    print("X = ", binary_to_decimal(bits_x))
    print("P = ", binary_to_decimal(bits_p))
    #print("Wynik modulo: ", binary_to_decimal(modulo_xp))
main()