
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
printf: "{ ""solution"": [%d", x[1] > "results/scenarioA2_N16_B0.8_classical/IPL_linearized_N16q10.00B12_solution.json";
printf{i in 2..n}: ",%d", x[i] >> "results/scenarioA2_N16_B0.8_classical/IPL_linearized_N16q10.00B12_solution.json";
printf: "]}" >> "results/scenarioA2_N16_B0.8_classical/IPL_linearized_N16q10.00B12_solution.json";

#data:
data;

param n := 16;
param q := 10;
param B := 12;
param mu :=
1 0.006672863194472878
2 9.56132732858106e-05
3 0.0043423003530233765
4 9.667140929613405e-05
5 -0.0013502236473571182
6 0.002564918493923302
7 0.003489847958281456
8 -0.0011796755440926232
9 -0.0033595961943244878
10 0.004566694088427104
11 0.002337570869249178
12 -0.002350103358567751
13 -0.005366814548175702
14 -0.0008633775255719011
15 0.005176210986128543
16 0.008707260961317515;
param sigma : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 :=
1 0.0003137773405389041 -2.2288003777661456e-05 -2.7551962579440446e-05 0.00012409239083781658 1.1601658415451156e-05 0.0002142941990439731 0.00015436400482111292 -0.00013848442579565928 0.0003322607469930468 8.974576109845859e-05 1.4242332855320428e-05 -0.00014219127309026458 0.00017933066651777392 -0.0001366516116612839 0.0001238401911435847 0.00015752445307690223
2 -2.2288003777661456e-05 0.00020910177359636546 0.00015864470108219468 8.401796038338673e-05 0.00010948079210212963 3.462492399510674e-06 -2.0119403211920685e-05 0.00012239665044298676 -5.582744324430413e-05 0.00012966788716374148 2.8438402458719333e-05 0.00019227739402338377 -1.6795693293429096e-05 0.00010754974458011581 -6.532181201544937e-06 9.444475695522827e-05
3 -2.7551962579440446e-05 0.00015864470108219468 0.0002770642917077778 0.00013953963251856985 0.00015260546844902278 5.5092283677561686e-05 5.444189632899072e-05 9.871979179947745e-05 -4.7295727439014374e-05 0.00013049276260729907 3.741047999431138e-05 0.0001578350031259019 0.00012375123081880752 8.002790171509322e-05 3.869323492967693e-05 0.00012642937714091106
4 0.00012409239083781658 8.401796038338673e-05 0.00013953963251856985 0.00019543889138266924 0.00012832604145476508 0.0001543265153882274 0.00012043254419377768 5.12281101814542e-06 0.0002217009847183163 0.00013167451621964347 4.9041099272375395e-05 6.256569910257534e-05 0.0001325092040396317 4.2969918918656447e-05 8.432435075675439e-05 0.00014387485004928012
5 1.1601658415451156e-05 0.00010948079210212963 0.00015260546844902278 0.00012832604145476508 0.0004412248739170243 7.333357963643814e-05 4.8612554750590837e-05 0.00012949194590203592 -2.822219696345094e-05 0.00013038468456347924 6.794367208783689e-05 0.00020799765178260838 4.978147551102448e-05 5.430180338211267e-05 -2.0125358983416535e-05 0.00012060237476330578
6 0.0002142941990439731 3.462492399510674e-06 5.5092283677561686e-05 0.0001543265153882274 7.333357963643814e-05 0.0002088151815624795 0.0001583951268517934 -7.774049049115695e-05 0.00028797026007839217 6.25510493355035e-05 2.8950245412762275e-05 -5.287171345205252e-05 0.00018748545095671572 -5.303450969897586e-05 0.00011963262549362719 0.00013956825627060995
7 0.00015436400482111292 -2.0119403211920685e-05 5.444189632899072e-05 0.00012043254419377768 4.8612554750590837e-05 0.0001583951268517934 0.0001762957623765608 -0.00010800786841446589 0.00015242695681902128 4.140240251665428e-05 3.0998123840995385e-05 -7.523747788732413e-05 0.00014558462821432337 -8.274747133057452e-05 0.00011705607997230814 0.00011070854071795572
8 -0.00013848442579565928 0.00012239665044298676 9.871979179947745e-05 5.12281101814542e-06 0.00012949194590203592 -7.774049049115695e-05 -0.00010800786841446589 0.00029436951076713995 -9.276780559297144e-06 4.5437382453236065e-05 1.5437258559809326e-06 0.0002765356558405098 4.930452999590598e-05 0.00022036340879907275 -9.453303612595935e-05 -3.455498918294886e-05
9 0.0003322607469930468 -5.582744324430413e-05 -4.7295727439014374e-05 0.0002217009847183163 -2.822219696345094e-05 0.00028797026007839217 0.00015242695681902128 -9.276780559297144e-06 0.0018062431008579437 0.00018911272566352603 -0.00010738572221834053 -8.312910398699437e-05 0.0004909526234725875 0.00026466464838896574 0.00015500642163106468 4.223920550062787e-05
10 8.974576109845859e-05 0.00012966788716374148 0.00013049276260729907 0.00013167451621964347 0.00013038468456347924 6.25510493355035e-05 4.140240251665428e-05 4.5437382453236065e-05 0.00018911272566352603 0.00023808478318023633 1.3998293108725903e-05 0.00010164636032980153 9.904832041865854e-05 3.665815626593124e-05 2.7745300803534695e-05 0.00014566238736309938
11 1.4242332855320428e-05 2.8438402458719333e-05 3.741047999431138e-05 4.9041099272375395e-05 6.794367208783689e-05 2.8950245412762275e-05 3.0998123840995385e-05 1.5437258559809326e-06 -0.00010738572221834053 1.3998293108725903e-05 0.00010663122576437231 2.7521685196056106e-05 -6.399901297163906e-05 -2.5834465903895152e-06 1.5777761908271705e-05 7.183850641962147e-05
12 -0.00014219127309026458 0.00019227739402338377 0.0001578350031259019 6.256569910257534e-05 0.00020799765178260838 -5.287171345205252e-05 -7.523747788732413e-05 0.0002765356558405098 -8.312910398699437e-05 0.00010164636032980153 2.7521685196056106e-05 0.0003807183212128199 2.428269315743898e-05 0.00024572509720470714 -9.135393399205827e-05 1.5830421336397021e-06
13 0.00017933066651777392 -1.6795693293429096e-05 0.00012375123081880752 0.0001325092040396317 4.978147551102448e-05 0.00018748545095671572 0.00014558462821432337 4.930452999590598e-05 0.0004909526234725875 9.904832041865854e-05 -6.399901297163906e-05 2.428269315743898e-05 0.0005654397643596026 -3.3326623051803244e-05 0.00011178438482920259 0.00016395345552628414
14 -0.0001366516116612839 0.00010754974458011581 8.002790171509322e-05 4.2969918918656447e-05 5.430180338211267e-05 -5.303450969897586e-05 -8.274747133057452e-05 0.00022036340879907275 0.00026466464838896574 3.665815626593124e-05 -2.5834465903895152e-06 0.00024572509720470714 -3.3326623051803244e-05 0.0003449731015793036 -6.585247549858028e-05 -0.0001344201855345699
15 0.0001238401911435847 -6.532181201544937e-06 3.869323492967693e-05 8.432435075675439e-05 -2.0125358983416535e-05 0.00011963262549362719 0.00011705607997230814 -9.453303612595935e-05 0.00015500642163106468 2.7745300803534695e-05 1.5777761908271705e-05 -9.135393399205827e-05 0.00011178438482920259 -6.585247549858028e-05 0.0001217823947044265 0.0001021907745067146
16 0.00015752445307690223 9.444475695522827e-05 0.00012642937714091106 0.00014387485004928012 0.00012060237476330578 0.00013956825627060995 0.00011070854071795572 -3.455498918294886e-05 4.223920550062787e-05 0.00014566238736309938 7.183850641962147e-05 1.5830421336397021e-06 0.00016395345552628414 -0.0001344201855345699 0.0001021907745067146 0.00031153944337819885;
end;
