
# zamiana liczby dziesiętnej na wektor binarny
def int_to_binary(number):
    binary_list = []
    
    while number > 0:
        binary_list.insert(0, number % 2)
        number = number // 2
    
    return binary_list

def add_zeros_to_binary_list(binary_list, n):
    return ['0'] * n + binary_list