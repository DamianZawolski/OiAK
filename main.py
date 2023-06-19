from binary_operations import modulo_computation, modulo_multiplication
from test import measure_modulo_operation_time, measure_modulo_multiply_operation_time
X = 57
N = 18
P = 47
R = modulo_computation(X, N, P)
print("Wynik dzialania modulo:", R)

A = 45
B = 2
mulN=6
DELTA=2
mulP=47
out_vec = modulo_multiplication(A, B, mulN, DELTA, mulP)
print("Wynik mnożenia modulo:", out_vec)

amount_of_operations = 100000
measure_modulo_operation_time([100, 1000, 10000, 100000], amount_of_operations)
measure_modulo_multiply_operation_time([100, 1000, 10000, 100000], amount_of_operations)
