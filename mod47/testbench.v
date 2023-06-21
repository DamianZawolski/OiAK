module testbench;
    reg[6:1] tb_A;
    reg[6:1] tb_B;
    wire [6:1] tb_mul;

    initial begin
        tb_A = 'd45;
        tb_B = 'd15;
        $monitor("%0b * %0b mod 47 = %0d\n", tb_A, tb_B, multiplication.temp_R);
        #3;
    end

    mul6ABmod47 multiplication (.A(tb_A), .B(tb_B), .R(tb_mul));

endmodule

def mul6ABmod47(A, B):
    r1 = mul3x3(A[3], A[2], A[1], B[3], B[2], B[1])
    r2 = mul3x3_8(A[6], A[5], A[4], B[3], B[2], B[1])
    r3 = mul3x3_8(A[3], A[2], A[1], B[6], B[5], B[4])
    r4 = mul3x3_17(A[6], A[5], A[4], B[6], B[5], B[4])

    temp_R1 = [r1[i] + r2[i] + r3[i] + r4[i] for i in range(7, 0, -1)]

    r5 = mul3_8(temp_R1[6], temp_R1[5], temp_R1[4])
    r6 = mul2_17(temp_R1[8], temp_R1[7])

    temp_R2 = [temp_R1[i] for i in range(3, 0, -1)] + r5 + r6

    if temp_R2 >= 47:
        temp_R = temp_R2 - 47
    else:
        temp_R = temp_R2

    R = temp_R

    return R

class Mul6ABMod47:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.R = (A * B) % 47

class Testbench:
    def __init__(self):
        self.tb_A = 45
        self.tb_B = 15
        self.tb_mul = None

    def simulate(self):
        self.tb_mul = Mul6ABMod47(self.tb_A, self.tb_B)
        print(f"{self.tb_A:06b} * {self.tb_B:06b} mod 47 = {self.tb_mul.R}")

testbench = Testbench()
testbench.simulate()
