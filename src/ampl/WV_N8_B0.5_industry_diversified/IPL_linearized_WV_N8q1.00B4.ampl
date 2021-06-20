
#parameters    
param n, integer, > 0; /* number of assets */    
param B, >= 0;      
param mu{i in 1..n};                          
param sigma{i in 1..n, j in 1..n};    
param q;    
                                              
#variables                                    
var y{i in 1..n, j in 1..n}, binary;    
var x{i in 1..n}, binary;                     
    
#capacity constraint    
s.t. card0: sum{i in 1..n} x[i] = B ;    
#constraints to link x and y                   
s.t. card1{i in 1..n,j in 1..n}: y[i,j] <= x[i] ;    
s.t. card2{i in 1..n,j in 1..n}: y[i,j] <= x[j] ;    
s.t. card3{i in 1..n,j in 1..n}: y[i,j] >= x[i]+x[j]-1 ;    
    
#objective function    
maximize obj: sum{i in 1..n, j in 1..n} y[i,j] * sigma[i,j];    

solve;
printf: "{ ""solution"": [%d", x[1] > "results/WV_N8_B0.5_industry_diversified/IPL_linearized_WV_N8q1.00B4_solution.json";
printf{i in 2..n}: ",%d", x[i] >> "results/WV_N8_B0.5_industry_diversified/IPL_linearized_WV_N8q1.00B4_solution.json";
printf: "]}" >> "results/WV_N8_B0.5_industry_diversified/IPL_linearized_WV_N8q1.00B4_solution.json";

#data:
data;

param n := 8;
param q := 1;
param B := 4;
param mu :=
1 0.006672863194472878
2 9.56132732858106e-05
3 0.0043423003530233765
4 0.002564918493923302
5 -0.0033595961943244878
6 -0.002350103358567751
7 0.005176210986128543
8 0.008707260961317515;
param sigma : 1 2 3 4 5 6 7 8 :=
1 0.0003137773405389041 -2.2288003777661456e-05 -2.7551962579440446e-05 0.0002142941990439731 0.0003322607469930468 -0.00014219127309026458 0.0001238401911435847 0.00015752445307690223
2 -2.2288003777661456e-05 0.00020910177359636546 0.00015864470108219468 3.462492399510674e-06 -5.582744324430413e-05 0.00019227739402338377 -6.532181201544937e-06 9.444475695522827e-05
3 -2.7551962579440446e-05 0.00015864470108219468 0.0002770642917077778 5.5092283677561686e-05 -4.7295727439014374e-05 0.0001578350031259019 3.869323492967693e-05 0.00012642937714091106
4 0.0002142941990439731 3.462492399510674e-06 5.5092283677561686e-05 0.0002088151815624795 0.00028797026007839217 -5.287171345205252e-05 0.00011963262549362719 0.00013956825627060995
5 0.0003322607469930468 -5.582744324430413e-05 -4.7295727439014374e-05 0.00028797026007839217 0.0018062431008579437 -8.312910398699437e-05 0.00015500642163106468 4.223920550062787e-05
6 -0.00014219127309026458 0.00019227739402338377 0.0001578350031259019 -5.287171345205252e-05 -8.312910398699437e-05 0.0003807183212128199 -9.135393399205827e-05 1.5830421336397021e-06
7 0.0001238401911435847 -6.532181201544937e-06 3.869323492967693e-05 0.00011963262549362719 0.00015500642163106468 -9.135393399205827e-05 0.0001217823947044265 0.0001021907745067146
8 0.00015752445307690223 9.444475695522827e-05 0.00012642937714091106 0.00013956825627060995 4.223920550062787e-05 1.5830421336397021e-06 0.0001021907745067146 0.00031153944337819885;
end;
