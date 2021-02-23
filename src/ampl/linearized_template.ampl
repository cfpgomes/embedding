
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
