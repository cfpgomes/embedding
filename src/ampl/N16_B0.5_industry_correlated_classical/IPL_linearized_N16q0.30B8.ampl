
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
minimize obj: sum{i in 1..n, j in 1..n} y[i,j] * sigma[i,j] * q - sum{i in 1..n} mu[i]*x[i];    

solve;
printf: "{ ""solution"": [%d", x[1] > "results/N16_B0.5_industry_correlated_classical/IPL_linearized_N16q0.30B8_solution.json";
printf{i in 2..n}: ",%d", x[i] >> "results/N16_B0.5_industry_correlated_classical/IPL_linearized_N16q0.30B8_solution.json";
printf: "]}" >> "results/N16_B0.5_industry_correlated_classical/IPL_linearized_N16q0.30B8_solution.json";

#data:
data;

param n := 16;
param q := 0.30000000000000004;
param B := 8;
param mu :=
1 0.002087286854557753
2 -0.0004008715924564684
3 -0.003693757359155897
4 -0.02817106565198864
5 -0.025372355446965155
6 -0.0009920552813279
7 0.0041832978934239
8 -0.005255273733632332
9 0.004702226069820461
10 0.0047780847758397355
11 0.0014125387536220752
12 -0.004900289926904143
13 -0.0029554087498819066
14 0.0033640561324092045
15 0.0016714038880011387
16 0.0009701599300816254;
param sigma : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 :=
1 0.00020992579641120822 9.019255164023667e-06 8.515996207015124e-05 -0.00029812801195985454 -0.00028577376740493877 0.00011254062002828193 0.00017255605903812398 1.6965975741111306e-05 0.00014288900663181968 0.00015471463947045036 -1.0911862660064101e-06 5.136553203080552e-05 -1.0768498369582159e-05 0.00015822192501372355 -4.703134113545217e-05 3.4581755436328286e-05
2 9.019255164023667e-06 0.0001709515338355733 6.353345497787761e-05 8.469269374847428e-05 0.00010305982724645175 -6.18567966374098e-05 6.151531519371367e-06 5.6241194729498835e-05 2.5071250621376617e-06 4.176370560654239e-06 -5.321515884796812e-05 -6.275002703265325e-05 -0.00016630923543463965 6.681780743600347e-05 -9.831733216999867e-05 2.264770268382433e-05
3 8.515996207015124e-05 6.353345497787761e-05 0.0001223051442794432 0.0001682559177087621 0.0001986663187663061 7.978735645340239e-05 6.661535626763871e-05 0.00013614494678744246 7.69732025851137e-05 8.334628217540298e-05 2.1646219906188896e-05 7.263227626972145e-05 1.9579583622237916e-05 7.101496746453227e-05 1.0437476936255065e-05 3.560073037350723e-05
4 -0.00029812801195985454 8.469269374847428e-05 0.0001682559177087621 0.005412189466872491 0.005582483578594521 5.176958038869723e-06 -0.0002032663016254572 0.0011405430038025728 0.00012468368020690523 0.00010550348426971214 0.00022289642419593536 0.0005397091736456971 -3.310721674144308e-05 0.0001299959812263684 0.000633169317486919 -8.686441179988514e-05
5 -0.00028577376740493877 0.00010305982724645175 0.0001986663187663061 0.005582483578594521 0.005910047772862706 5.5280985310420655e-05 -0.0001934581358370692 0.0011473693366687145 0.00014862295091585965 0.0001370100708774632 0.0002519962205605341 0.0005945772420845238 -0.00010423875032297269 0.00015050824381401267 0.0006346884755643417 -9.43612125594085e-05
6 0.00011254062002828193 -6.18567966374098e-05 7.978735645340239e-05 5.176958038869723e-06 5.5280985310420655e-05 0.0003048373630705137 7.606846701439034e-05 0.0001460355155302025 0.00011012424351258022 0.0001270701969430821 0.00018971425133210517 0.00022375656558796367 0.00015195226863410068 2.4318461153501666e-05 0.00012108887899562161 1.592713732927065e-05
7 0.00017255605903812398 6.151531519371367e-06 6.661535626763871e-05 -0.0002032663016254572 -0.0001934581358370692 7.606846701439034e-05 0.00019303559660260763 -2.99497994120888e-07 0.0001146045520440382 0.00012685300858241965 -1.9228916105746716e-05 5.127924852690628e-05 -2.9241348075866202e-05 0.00017235000124521881 -4.961027776276198e-05 3.591219360127775e-05
8 1.6965975741111306e-05 5.6241194729498835e-05 0.00013614494678744246 0.0011405430038025728 0.0011473693366687145 0.0001460355155302025 -2.99497994120888e-07 0.0005400755856364203 5.442409206935533e-05 6.223168114231095e-05 0.00012721365059090208 0.0002879721935482922 4.959869673284731e-05 -3.5198658624206786e-05 0.00024082459480254098 2.279230582710878e-05
9 0.00014288900663181968 2.5071250621376617e-06 7.69732025851137e-05 0.00012468368020690523 0.00014862295091585965 0.00011012424351258022 0.0001146045520440382 5.442409206935533e-05 0.00021738029236239773 0.00022141891414040365 -6.3852474280982405e-06 7.28786319734119e-06 -6.888945439528107e-07 0.00014877446952218755 2.097524775044692e-05 2.4635603780883672e-05
10 0.00015471463947045036 4.176370560654239e-06 8.334628217540298e-05 0.00010550348426971214 0.0001370100708774632 0.0001270701969430821 0.00012685300858241965 6.223168114231095e-05 0.00022141891414040365 0.00022914146511249619 -1.1459967415945827e-06 2.7769670322875736e-05 -1.0494299929050552e-05 0.0001549462230079903 1.152964109758703e-05 2.5913983667336595e-05
11 -1.0911862660064101e-06 -5.321515884796812e-05 2.1646219906188896e-05 0.00022289642419593536 0.0002519962205605341 0.00018971425133210517 -1.9228916105746716e-05 0.00012721365059090208 -6.3852474280982405e-06 -1.1459967415945827e-06 0.00024264582305744717 0.00019277146818585944 0.00013091586047303655 -7.698369752589851e-05 0.00016856840138638394 2.3249466130564855e-05
12 5.136553203080552e-05 -6.275002703265325e-05 7.263227626972145e-05 0.0005397091736456971 0.0005945772420845238 0.00022375656558796367 5.127924852690628e-05 0.0002879721935482922 7.28786319734119e-06 2.7769670322875736e-05 0.00019277146818585944 0.00046936911209953655 5.858446628126276e-05 -7.027440637937037e-05 8.833232056002092e-05 3.750029384295605e-05
13 -1.0768498369582159e-05 -0.00016630923543463965 1.9579583622237916e-05 -3.310721674144308e-05 -0.00010423875032297269 0.00015195226863410068 -2.9241348075866202e-05 4.959869673284731e-05 -6.888945439528107e-07 -1.0494299929050552e-05 0.00013091586047303655 5.858446628126276e-05 0.000455516017029062 -7.949088087006644e-05 0.00021611520347678754 1.548661411072566e-05
14 0.00015822192501372355 6.681780743600347e-05 7.101496746453227e-05 0.0001299959812263684 0.00015050824381401267 2.4318461153501666e-05 0.00017235000124521881 -3.5198658624206786e-05 0.00014877446952218755 0.0001549462230079903 -7.698369752589851e-05 -7.027440637937037e-05 -7.949088087006644e-05 0.00034941512295885295 -0.00011287024822441325 7.765210550778575e-06
15 -4.703134113545217e-05 -9.831733216999867e-05 1.0437476936255065e-05 0.000633169317486919 0.0006346884755643417 0.00012108887899562161 -4.961027776276198e-05 0.00024082459480254098 2.097524775044692e-05 1.152964109758703e-05 0.00016856840138638394 8.833232056002092e-05 0.00021611520347678754 -0.00011287024822441325 0.00036811586297687146 -1.0332353549642482e-05
16 3.4581755436328286e-05 2.264770268382433e-05 3.560073037350723e-05 -8.686441179988514e-05 -9.43612125594085e-05 1.592713732927065e-05 3.591219360127775e-05 2.279230582710878e-05 2.4635603780883672e-05 2.5913983667336595e-05 2.3249466130564855e-05 3.750029384295605e-05 1.548661411072566e-05 7.765210550778575e-06 -1.0332353549642482e-05 5.1793049285549746e-05;
end;
