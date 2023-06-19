import random
import time
import matplotlib.pyplot as plt
from binary_operations import modulo_computation, modulo_multiplication
from matplotlib.pyplot import figure
from qbstyles import mpl_style

def measure_modulo_operation_time(list_of_operations, amount_of_operations):
    execution_times = []
    list_of_operations = sorted(list_of_operations)
    plot_x_axis_info = []
    first = True
    for i in range(len(list_of_operations)):
        if first:
            first = False
            plot_x_axis_info.append(f"0 - {list_of_operations[i]}")
        else:
            plot_x_axis_info.append(f"{list_of_operations[i-1]} - {list_of_operations[i]}")
    for i in range(len(list_of_operations)):
        start_time = time.time()
        # Wykonaj operacje modulo_computation n razy
        first = True
        for _ in range(amount_of_operations):
            if first:
                X=random.randint(0, list_of_operations[i])
            else:
                X = random.randint(list_of_operations[i-1], list_of_operations[i])
            N = 18
            P = 47
            modulo_computation(X, N, P)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        first = False

    # Tworzenie wykresu
    mpl_style(True)
    figure(figsize=(10, 6), dpi=80)
    plt.plot(plot_x_axis_info, execution_times)
    plt.xlabel('Zakres z którego losowane są liczby')
    plt.ylabel('Czas wykonania (s)')
    plt.title(f'Czas wykonania modulo w zależności od rozmiaru liczby (dla {amount_of_operations} operacji)')
    plt.savefig('Czasy_obliczania_modulo.png')
    plt.show()

def measure_modulo_multiply_operation_time(list_of_operations, amount_of_operations):
    execution_times = []
    list_of_operations = sorted(list_of_operations)
    plot_x_axis_info = []
    first = True
    for i in range(len(list_of_operations)):
        if first:
            first = False
            plot_x_axis_info.append(f"0 - {list_of_operations[i]}")
        else:
            plot_x_axis_info.append(f"{list_of_operations[i-1]} - {list_of_operations[i]}")
    for i in range(len(list_of_operations)):
        start_time = time.time()
        # Wykonaj operacje modulo_computation n razy
        first = True
        for _ in range(amount_of_operations):
            if first:
                A=random.randint(1, list_of_operations[i])
                B=random.randint(1, A)
            else:
                A=random.randint(list_of_operations[i-1], list_of_operations[i])
                B=random.randint(1, A)
            mulN=6
            DELTA=2
            mulP=47
            modulo_multiplication(A, B, mulN, DELTA, mulP)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        first = False

    # Tworzenie wykresu
    mpl_style(True)
    figure(figsize=(10, 6), dpi=80)
    plt.plot(plot_x_axis_info, execution_times)
    plt.xlabel('Zakres z którego losowane są liczby')
    plt.ylabel('Czas wykonania (s)')
    plt.title(f'Czas wykonania mnożenia modulo w zależności od rozmiaru liczby (dla {amount_of_operations} operacji)')
    plt.savefig('Czasy_obliczania_mnozenia_modulo.png')
    plt.show()