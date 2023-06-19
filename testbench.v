module testbench;
    reg [17:0] tb_X;
    wire [5:0] tb_mod;
    
    reg[5:0] tb_A;
    reg[5:0] tb_B;
    wire [5:0] tb_mul;

    initial begin
        tb_X = 'd131073;

        tb_A = 'd45;
        tb_B = 'd15;

        $monitor("%0d mod %0d = %0d\n(%0d * %0d) mod %0d = %0d", tb_X, 47, tb_mod, tb_A, tb_B, 47, tb_mul);
        #5;
    end

    ModuloComputation mod (.X (tb_X),
                            .out_vec (tb_mod));

    ModuloMultiplication mul (.A (tb_A),
                                .B (tb_B),
                                .R (tb_mul));

endmodule
