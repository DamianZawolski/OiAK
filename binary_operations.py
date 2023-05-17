# zamiana liczby dziesiętnej na wektor binarny
def decimal_to_binary(decimal_x):
    result = []
    while decimal_x > 1:
        result.insert(0, decimal_x % 2 == 1)
        decimal_x = decimal_x // 2
    result.append(decimal_x)

    return result


def pad_with_zeros(x, total_length):
    while len(x) < total_length:
        x.insert(0, False)


# mnożenie dwóch wektorów bitowych
def binary_multiplication(v_a, v_b):
    if len(v_a) < len(v_b):
        pad_with_zeros(v_a, len(v_b))
    elif len(v_b) < len(v_a):
        pad_with_zeros(v_b, len(v_a))

    result = []

    # TODO

    return result


def binary_addition(v_a, v_b):
    if len(v_a) < len(v_b):
        pad_with_zeros(v_a, len(v_b))
    elif len(v_b) < len(v_a):
        pad_with_zeros(v_b, len(v_a))

    result = []
    carry = False
    for i in reversed(range(0, len(v_a))):
        # 1 1
        if v_a[i] & v_b[i]:
            result.insert(0, False ^ carry)
            carry = True
        # 1 0 albo 0 1
        elif v_a[i] | v_b[i]:
            result.insert(0, True ^ carry)
        # 0 0
        else:
            result.insert(0, 0 ^ carry)
            carry = False

    if carry:
        result.insert(0, True)

    return result


# v_a > v_b
def compare_binary(v_a, v_b):
    if len(v_a) < len(v_b):
        pad_with_zeros(v_a, len(v_b))
    elif len(v_b) < len(v_a):
        pad_with_zeros(v_b, len(v_a))

    for i in range(len(v_a)):
        if v_a[i] and not v_b[i]:
            return True
        elif v_b[i] and not v_a[i]:
            return False

    return False
