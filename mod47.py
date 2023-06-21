def mul2_17(a1, a2):
    r1 = a1 and (not a2)
    r2 = (not a1) and a2
    r3 = 0
    r4 = a1 and a2
    r5 = a1 and (not a2)
    r6 = (not a1) and a2
    return r1, r2, r3, r4, r5, r6


def mul3_8(a1, a2, a3):
    r1 = a1 and (not a2)
    r2 = (not a1) and a2
    r3 = a3
    r4 = 0
    r5 = 0
    r6 = a1 and a2
    return r1, r2, r3, r4, r5, r6

def mul3x3_8(a1, a2, a3, b1, b2, b3):
    p = [a1 * b1, a2 * b2, a3 * b3]

    r1 = (not p[0] and p[1] and p[2] and p[3] and not p[4]) or \
         (not p[0] and p[1] and not p[2] and p[3] and p[4]) or \
         (not p[0] and p[1] and not p[2] and not p[3] and not p[4]) or \
         (not p[0] and not p[1] and not p[2] and p[3] and not p[4]) or \
         (p[0] and not p[1] and p[2] and p[3] and p[4] and not p[5]) or \
         (not p[0] and not p[1] and p[2] and not p[3] and p[4]) or \
         (p[0] and not p[1] and p[2] and not p[3] and not p[4]) or \
         (p[0] and not p[1] and not p[2] and not p[3] and p[4])

    r2 = (not p[0] and p[1] and p[2] and not p[3] and p[4]) or \
         (not p[0] and not p[1] and not p[2] and not p[3] and p[4]) or \
         (p[0] and not p[1] and p[2] and p[3] and not p[4]) or \
         (not p[0] and not p[1] and p[2] and not p[3] and not p[4]) or \
         (not p[0] and not p[1] and p[2] and p[3] and p[4]) or \
         (p[0] and not p[1] and not p[2] and not p[3] and not p[4]) or \
         (not p[0] and p[1] and not p[2] and p[3] and not p[4]) or \
         (p[0] and not p[1] and not p[2] and p[3] and p[4])

    r3 = (not p[1] and not p[3] and p[5]) or \
         (not p[1] and not p[2] and p[5]) or \
         (not p[1] and not p[4] and p[5]) or \
         (not p[0] and p[5])

    r4 = (p[0] and not p[1] and p[2] and p[3] and p[4] and not p[5]) or \
         (p[0] and not p[1] and p[2] and not p[3] and not p[4]) or \
         (p[0] and not p[1] and not p[2] and not p[3] and not p[4]) or \
         (p[0] and not p[1] and not p[2] and not p[3] and p[4]) or \
         (p[0] and not p[1] and not p[2] and p[3] and p[4]) or \
         (p[0] and not p[1] and p[2] and not p[3] and p[4]) or \
         (not p[0] and p[1] and p[2] and not p[3] and p[4]) or \
         (p[0] and not p[1] and p[3] and not p[4])

    r5 = (not p[0] and p[1] and not p[2] and not p[3] and not p[4]) or \
         (p[0] and not p[1] and p[2] and p[3] and p[4] and not p[5]) or \
         (p[0] and not p[1] and p[2] and not p[3] and not p[4]) or \
         (not p[0] and not p[1] and p[2] and p[3] and p[4]) or \
         (not p[0] and p[1] and not p[2] and p[3] and not p[4]) or \
         (not p[1] and p[2] and p[3] and not p[4]) or \
         (p[0] and not p[1] and not p[2] and p[3] and p[4]) or \
         (p[0] and not p[1] and p[2] and not p[3] and p[4])

    r6 = (p[0] and not p[1] and p[2] and p[3] and p[4] and not p[5]) or \
         (p[0] and not p[1] and p[2] and p[3] and not p[4]) or \
         (not p[0] and not p[1] and p[2] and not p[3] and not p[4]) or \
         (not p[0] and not p[1] and p[2] and not p[3] and p[4]) or \
         (not p[0] and p[1] and p[3] and p[4]) or \
         (p[0] and not p[1] and not p[2] and not p[3] and not p[4]) or \
         (not p[0] and p[1] and not p[2] and p[3] and not p[4]) or \
         (p[0] and not p[1] and not p[2] and not p[3] and p[4]) or \
         (not p[0] and not p[1] and p[3] and p[4]) or \
         (p[0] and not p[1] and p[2] and not p[3] and p[4]) or \
         (not p[0] and p[1] and not p[2] and p[4])

    return r1, r2, r3, r4, r5, r6

def mul3x3_17(a1, a2, a3, b1, b2, b3):
    p = [0] * 7
    p[1] = a1 * b1
    p[2] = a2 * b2
    p[3] = a3 * b3

    r1 = (not p[1] and p[2] and not p[4] and not p[5] and not p[6]) or \
         (not p[1] and not p[2] and not p[3] and not p[4] and p[5] and not p[6]) or \
         (p[1] and not p[2] and not p[3] and p[4] and p[5] and not p[6]) or \
         (not p[1] and p[2] and not p[3] and not p[4] and p[5] and p[6]) or \
         (not p[1] and p[2] and p[4] and p[5] and not p[6]) or \
         (not p[1] and not p[2] and p[3] and not p[4] and not p[5] and not p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and not p[5] and not p[6]) or \
         (not p[1] and not p[2] and p[4] and not p[5] and p[6]) or \
         (p[1] and not p[2] and not p[4] and not p[5] and p[6]) or \
         (not p[1] and p[3] and not p[4] and p[5] and p[6])

    r2 = (not p[1] and p[2] and not p[3] and not p[4] and p[5] and not p[6]) or \
         (p[1] and not p[2] and not p[3] and p[4] and not p[5] and p[6]) or \
         (not p[1] and not p[2] and p[3] and not p[4] and p[5] and not p[6]) or \
         (not p[1] and p[2] and p[3] and not p[4] and p[5] and not p[6]) or \
         (not p[1] and p[2] and p[4] and not p[5] and p[6]) or \
         (not p[1] and not p[2] and not p[3] and not p[4] and not p[5] and p[6]) or \
         (not p[1] and not p[2] and p[4] and not p[5] and not p[6]) or \
         (p[1] and not p[2] and not p[4] and not p[5] and not p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and p[5] and not p[6]) or \
         (not p[1] and not p[2] and p[4] and p[5] and p[6]) or \
         (p[1] and not p[2] and not p[4] and p[5] and p[6])

    r3 = (not p[1] and p[2] and not p[3] and not p[4] and p[5] and not p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and not p[5] and p[6]) or \
         (not p[1] and p[2] and not p[3] and not p[4] and p[5] and p[6]) or \
         (not p[1] and p[2] and not p[3] and p[4] and not p[5] and not p[6]) or \
         (not p[1] and p[2] and p[4] and p[5] and not p[6]) or \
         (not p[1] and not p[2] and p[3] and not p[4] and not p[5] and not p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and not p[5] and not p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and p[5] and not p[6]) or \
         (p[1] and not p[2] and not p[4] and p[5] and p[6]) or \
         (not p[1] and p[2] and not p[3] and p[4] and p[6]) or \
         (not p[2] and p[3] and not p[4] and p[5] and not p[6]) or \
         (not p[1] and p[2] and p[4] and p[5] and p[6]) or \
         (p[1] and not p[2] and not p[3] and not p[4]) or \
         (not p[1] and not p[2] and p[3] and not p[4] and p[6]) or \
         (not p[1] and not p[3] and p[4] and p[5])

    r4 = (p[1] and not p[2] and p[3] and p[4] and not p[5] and p[6]) or \
         (not p[1] and not p[2] and p[3] and not p[4] and p[5] and not p[6]) or \
         (not p[1] and not p[2] and not p[3] and p[4] and not p[5] and not p[6]) or \
         (not p[1] and not p[2] and not p[3] and p[4] and not p[5] and p[6]) or \
         (not p[2] and not p[3] and not p[4] and p[5] and p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and p[5] and not p[6]) or \
         (p[1] and not p[2] and not p[4] and not p[5] and p[6]) or \
         (not p[1] and p[2] and p[3] and p[4] and not p[5]) or \
         (not p[1] and not p[2] and p[3] and p[5] and p[6]) or \
         (p[1] and not p[2] and p[3] and not p[4] and not p[5]) or \
         (not p[1] and p[2] and not p[3] and p[4] and p[6]) or \
         (not p[1] and p[2] and not p[3] and not p[4] and not p[5]) or \
         (not p[1] and p[3] and not p[4] and p[5] and p[6]) or \
         (not p[1] and p[2] and not p[3] and p[4] and p[5]) or \
         (p[1] and not p[2] and not p[3] and not p[4] and p[5]) or \
         (p[1] and not p[2] and not p[3] and p[5] and p[6]) or \
         (not p[1] and not p[2] and p[3] and not p[4] and p[6])

    r5 = (p[1] and not p[2] and not p[3] and p[4] and not p[5] and p[6]) or \
         (not p[1] and p[2] and p[3] and not p[4] and p[5] and not p[6]) or \
         (not p[1] and not p[2] and not p[3] and not p[4] and p[5] and not p[6]) or \
         (p[1] and not p[2] and not p[3] and p[4] and p[5] and not p[6]) or \
         (not p[1] and not p[2] and p[3] and p[4] and p[5] and not p[6]) or \
         (not p[1] and p[2] and not p[3] and p[4] and not p[5] and not p[6]) or \
         (not p[1] and p[2] and not p[4] and not p[5] and p[6]) or \
         (not p[2] and p[3] and not p[4] and p[5] and p[6]) or \
         (not p[1] and not p[2] and p[3] and not p[4] and not p[5] and not p[6]) or \
         (not p[1] and not p[2] and not p[3] and p[4] and not p[5] and p[6]) or \
         (p[1] and not p[2] and not p[4] and not p[5] and not p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and not p[5] and not p[6]) or \
         (p[1] and not p[2] and p[3] and p[4] and p[5] and p[6]) or \
         (p[1] and not p[2] and not p[3] and not p[4] and not p[5] and not p[6])

    return [r1, r2, r3, r4, r5]

def mul3x3(a1, a2, a3, b1, b2, b3):
    p = [a1*a2, a1*a3, a1*b1, a1*b2, a1*b3, a2*b1, a2*b2, a2*b3, a3*b1, a3*b2, a3*b3]

    r1 = (p[0] and not p[1] and p[2] and not p[3] and p[4] and p[5]) or \
         (p[0] and not p[1] and not p[2] and p[4] and p[5]) or \
         (p[0] and not p[1] and not p[4] and p[5]) or \
         (p[0] and not p[1] and not p[5])

    r2 = (not p[0] and p[1])

    r3 = (p[0] and not p[1] and p[2] and not p[3] and p[4] and p[5]) or \
         (not p[1] and p[2] and not p[4]) or \
         (not p[1] and p[2] and not p[5]) or \
         (not p[0] and p[2])

    r4 = (not p[1] and p[3] and not p[4]) or \
         (not p[1] and not p[2] and p[3]) or \
         (not p[1] and p[3] and not p[5]) or \
         (not p[0] and p[3])

    r5 = (p[0] and not p[1] and p[2] and not p[3] and p[4] and p[5]) or \
         (p[0] and not p[1] and not p[2] and p[4] and p[5]) or \
         (not p[1] and p[4] and not p[5]) or \
         (not p[0] and p[4])

    r6 = (p[0] and not p[1] and p[2] and not p[3] and p[4] and p[5]) or \
         (p[0] and not p[1] and not p[2] and p[4] and p[5]) or \
         (p[0] and not p[1] and not p[4] and p[5]) or \
         (not p[0] and p[5])

    return [r1, r2, r3, r4, r5, r6]

class Mul6ABMod47:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.R = (A * B) % 47

class Test3x3:
    def __init__(self, A, B):
        self.tb_A = A
        self.tb_B = B
        self.tb_mul = None

    def simulate(self):
        self.tb_mul = Mul6ABMod47(self.tb_A, self.tb_B)
        print(f"{self.tb_A:06b} * {self.tb_B:06b} mod 47 = {self.tb_mul.R}")
