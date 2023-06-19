module ModuloComputation #(parameter N=18, parameter P=64) ( X,
												out_vec);

	localparam DELTA = $clog2(P);									//liczba bitów potrzebna do zapisania liczby modP
	localparam K = $ceil(N/DELTA + 1);									//K subwektorów
	localparam padding = (DELTA * K) - N;


	input [N-1:0] X;												//wejście - liczba N-bitowa
	reg [DELTA * K:0] paddedX;

	output reg [DELTA-1:0] out_vec; 								//wyjście - XmodP, więc liczba DELTA-bitowa

	reg [DELTA-1:0] subvectors[0:K-1];								//do podziału X na K DELTA-bitowych liczb

	reg [N:0] S;

	initial begin : block
		integer i, n, k_temp, padding;
		#1

		paddedX = X;

		repeat(padding)
			paddedX <= {1'b0, paddedX};

		for (i = 0; i < K; i = i+1) begin							//podział X na DELTA-bitowe liczby
			subvectors[i] = paddedX[(i+1)*DELTA - 1 -: DELTA];
			$display("subv[%0d]: %0b", i, subvectors[i]);
		end

		S = 'b0;													//suma 

		for (i = 0; i < K; i = i + 1) begin
			S = S + (subvectors[i] * (2**(DELTA*(i)) % P));
			$display("S: %0d", S);
		end



		while (S > 2 * P) begin
			n = $clog2(S);
			k_temp = n/DELTA;

			if (n % DELTA != 0)
				k_temp = k_temp + 1;									//nie da się bezpośrednio zrobić $ceil(n/DELTA)

			for (i = 0; i < k_temp; i = i+1) begin						//podział S na DELTA-bitowe liczby
				subvectors[i] = S[(i+1)*DELTA - 1 -: DELTA];
				//$display("subv[%0d]: %0b", i, subvectors[i]);
				end

			S = 'b0;

			for (i = 0; i < k_temp; i = i+1) begin
				S = S + (subvectors[i] * (2**(DELTA*(i)) % P));
				//$display("S: %0b; i: %0d", S, i);
			end
		end

		if (S > P)
			S = S - P;

		//$display("Final S: %0d", S);

		assign out_vec = S;
	end


endmodule
