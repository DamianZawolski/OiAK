module mul6ABmod47(A, B, R);
    input [6:1] A, B;
    output [6:1] R;
    wire [6:1] r1, r2, r3, r4, r5, r6;
    wire [8:1] temp_R1; 
    wire [7:1] temp_R2;
    reg [8:1] temp_R;

    mul3x3 label1 (.a1(A[3]),.a2(A[2]),.a3(A[1]),
                    .b1(B[3]),.b2(B[2]),.b3(B[1]),
                    .r1(r1[6]),.r2(r1[5]),.r3(r1[4]),
                    .r4(r1[3]),.r5(r1[2]),.r6(r1[1]));

    mul3x3_8 label2 (.a1(A[6]),.a2(A[5]),.a3(A[4]),
                    .b1(B[3]),.b2(B[2]),.b3(B[1]),
                    .r1(r2[6]),.r2(r2[5]),.r3(r2[4]),
                    .r4(r2[3]),.r5(r2[2]),.r6(r2[1]));

    mul3x3_8 label3 (.a1(A[3]),.a2(A[2]),.a3(A[1]),
                    .b1(B[6]),.b2(B[5]),.b3(B[4]),
                    .r1(r3[6]),.r2(r3[5]),.r3(r3[4]),
                    .r4(r3[3]),.r5(r3[2]),.r6(r3[1]));

    mul3x3_17 label4 (.a1(A[6]),.a2(A[5]),.a3(A[4]),
                    .b1(B[6]),.b2(B[5]),.b3(B[4]),
                    .r1(r4[6]),.r2(r4[5]),.r3(r4[4]),
                    .r4(r4[3]),.r5(r4[2]),.r6(r4[1]));

    assign temp_R1 = r1 + r2 + r3 + r4;

    mul3_8 label5 (.a1(temp_R1[6]),.a2(temp_R1[5]),.a3(temp_R1[4]),
                    .r1(r5[6]),.r2(r5[5]),.r3(r5[4]),
                    .r4(r5[3]),.r5(r5[2]),.r6(r5[1]));

    mul2_17 label6 (.a1(temp_R1[8]),.a2(temp_R1[7]),
                    .r1(r6[6]),.r2(r6[5]),.r3(r6[4]),
                    .r4(r6[3]),.r5(r6[2]),.r6(r6[1]));

    assign temp_R2 = temp_R1[3:1] + r5 + r6;

    always @(*) begin
        if (temp_R2 >= 47)
            temp_R = temp_R2 - 47;
        else
            temp_R = temp_R2;
    end

    assign R = temp_R;

endmodule