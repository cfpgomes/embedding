
#parameters
param n, integer, > 0; /* number of assets */
param B, >= 0;	
param mu{i in 1..n};
param sigma{i in 1..n, j in 1..n};
param q;
param P;	

#variables
var y{i in 1..n, j in 1..n}, binary;
var x{i in 1..n}, binary;

#constraints to link x and y
s.t. card1{i in 1..n,j in 1..n}: y[i,j] <= x[i] ;
s.t. card2{i in 1..n,j in 1..n}: y[i,j] <= x[j] ;
s.t. card3{i in 1..n,j in 1..n}: y[i,j] >= x[i]+x[j]-1 ;

#objective function
minimize obj: sum{i in 1..n, j in 1..n} y[i,j] * sigma[i,j] * q - sum{i in 1..n} mu[i]*x[i] + P*(sum{i in 1..n} x[i] + 2*sum{i in 1..n, j in i+1..n} y[i,j] - 2*B*sum{i in 1..n} x[i] + B*B);

solve;

#data:
data;

param q := 1;
param n := 20;
param B := 10;
param P := 100;
param mu :=
1 0.8
2 0.4
3 0.3
4 0.4
5 0.5
6 0.6
7 0.1
8 0.2 
9 0.7
10 0.1
11 0.8
12 0.4
13 0.2
14 0.9
15 0.1
16 0.4
17 0.5
18 0.9
19 0.6
20 0.4;
param sigma : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 :=
1 2 0 8 1 0 6 3 2 2 0 9 0 3 5 7 7 4 3 8 3
2 0 6 7 0 7 4 4 0 8 7 3 4 2 5 0 0 7 8 2 2
3 8 7 3 9 3 2 6 3 0 0 7 5 4 8 1 0 5 0 7 6
4 1 0 9 9 9 9 6 3 8 7 2 8 1 0 2 6 6 6 6 9
5 0 7 3 9 7 4 6 6 2 7 5 4 5 2 9 8 8 0 5 0
6 6 4 2 9 4 0 7 3 2 7 8 1 0 4 3 3 1 5 3 6
7 3 4 6 6 6 7 3 7 5 3 2 9 3 6 2 2 7 5 8 8
8 2 0 3 3 6 3 7 3 4 8 3 9 8 0 1 5 7 3 2 1
9 2 8 0 8 2 2 5 4 9 0 9 6 9 7 1 4 9 6 2 9
10 0 7 0 7 7 7 3 8 0 0 7 2 1 3 6 6 5 9 3 0
11 9 3 7 2 5 8 2 3 9 7 4 2 4 9 1 4 4 2 6 0
12 0 4 5 8 4 1 9 9 6 2 2 4 4 1 6 4 7 6 0 6
13 3 2 4 1 5 0 3 8 9 1 4 4 3 2 3 7 9 4 7 0
14 5 5 8 0 2 4 6 0 7 3 9 1 2 1 9 2 7 4 4 9
15 7 0 1 2 9 3 2 1 1 6 1 6 3 9 4 4 4 3 1 1
16 7 0 0 6 8 3 2 5 4 6 4 4 7 2 4 6 9 0 4 9
17 4 7 5 6 8 1 7 7 9 5 4 7 9 7 4 9 0 9 8 9
18 3 8 0 6 0 5 5 3 6 9 2 6 4 4 3 0 9 6 0 9
19 8 2 7 6 5 3 8 2 2 3 6 0 7 4 1 4 8 0 3 9
20 3 2 6 9 0 6 8 1 9 0 0 6 0 9 1 9 9 9 9 3;
end;

