module mul2_17 (input a1,
                a2,
                output r1,
                r2,
                r3,
                r4,
                r5,
                r6);

    assign r1 = (a1&!a2);

    assign r2 = (!a1&a2);

    assign r3 = (0);

    assign r4 = (a1&a2);

    assign r5 = (a1&!a2);

    assign r6 = (!a1&a2);


endmodule