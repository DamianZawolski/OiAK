module mul3_8 (input a1,
                a2,
                a3,
                output r1,
                r2,
                r3,
                r4,
                r5,
                r6);

    assign r1 = (a1&!a2);

    assign r2 = (!a1&a2);

    assign r3 = (a3);

    assign r4 = (0);

    assign r5 = (0);

    assign r6 = (a1&a2);


endmodule