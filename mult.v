module ModuloMultiplication #(parameter mulN=6, DELTA=2, mulP=47) (A,
                                                        B,
                                                        R);

    localparam out_size = $clog2(mulP);                                     //rozmiar liczby wyjściowej

    input [mulN-1:0] A;
    input [mulN-1:0] B;

    reg [mulN/DELTA-1:0] A_vec [1:DELTA];                                   //podział liczby na mniejsze wektory
    reg [mulN/DELTA-1:0] B_vec [1:DELTA];

    output reg [out_size-1:0] R;

    reg [2**(3*DELTA+4): 0] S_temp = 0;

    initial begin : block
        integer i, j;
        #1

        for (i = 1; i < DELTA + 1; i = i + 1) begin
            A_vec[i] = A[(i)*(mulN/DELTA) - 1 -: (mulN/DELTA)];             //podział liczby na mniejsze wektory
            B_vec[i] = B[(i)*(mulN/DELTA) - 1 -: (mulN/DELTA)];
        end

        for (i = 1; i < DELTA + 1; i = i + 1) begin
            for (j = 1; j < DELTA + 1; j = j + 1) begin
                S_temp = S_temp + (A_vec[i] * B_vec[j] * 2**((i+j-2)*3)) % mulP;
            end
        end

        while (S_temp > mulP)
            S_temp = S_temp - mulP;

        R = S_temp;
    end

endmodule