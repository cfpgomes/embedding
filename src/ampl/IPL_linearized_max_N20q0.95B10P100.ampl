
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
maximize obj: sum{i in 1..n, j in 1..n} y[i,j] * sigma[i,j] * q - sum{i in 1..n} mu[i]*x[i];    

solve;
printf: "{ ""solution"": [%d", x[1] > "results/IPL_linearized_max_N20q0.95B10P100_solution.json";
printf{i in 2..n}: ",%d", x[i] >> "results/IPL_linearized_max_N20q0.95B10P100_solution.json";
printf: "]}" >> "results/IPL_linearized_max_N20q0.95B10P100_solution.json";

#data:
data;

param n := 20;
param q := 0.9500000000000001;
param B := 10;
param mu :=
1 0.04919437256125079
2 0.0526041226528411
3 0.054479186033120484
4 0.06434335923846264
5 0.03599700948339685
6 0.01652681944156086
7 0.07699567301345857
8 0.03992174251707056
9 0.040322886308796185
10 0.03608895699477319
11 0.05503574339091402
12 0.04427420800012461
13 0.02150620735719001
14 0.060226810092595694
15 0.0008239903836207615
16 0.000772244881215689
17 0.06531198681756935
18 0.0360938687283117
19 0.0573576559605471
20 0.01788516892944324;
param sigma : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 :=
1 0.003174683513003251 -0.0013409735299333557 0.0023491949282553933 0.0021842900699640287 0.003733584798773341 0.0009969968871996766 0.003597244358324952 0.0012393442347047856 0.0029333583412517114 0.0019122050540559873 0.0015097854159310412 0.0012413074806906536 0.0002621368931894943 0.0029401830385665283 0.0009526023476132062 0.00020992684954226532 -0.0011610989405383659 0.002538117417777033 0.00355983696170607 -0.0003270629162205562
2 -0.0013409735299333557 0.01888213820390469 -0.003155716081705305 0.003635707562777463 0.00490549993708534 0.0011223842927259615 -0.00269564766776355 -0.001551767439231339 0.0027440255418747462 0.004207617240168365 0.004723658706175951 -0.0001506278074459091 0.002237172986842063 0.004101282581725816 -0.005800027482148545 -0.0073808183819315774 0.005974742549277746 0.006741419943759147 -0.0013962417534567177 0.0018078608912032647
3 0.0023491949282553933 -0.003155716081705305 0.009474886663414936 0.004435130732395157 0.003078860228813622 -0.00016150466265534756 0.008675164559883656 0.0030271706962505976 0.00466096609493093 0.0046213950074739845 0.004631986461542638 0.0016783249882067598 0.0006984203993623209 0.0059882926344004914 0.0011549649166300892 0.0007426552072158889 -0.0018683240284326854 0.0009753412379398995 0.0016726280867163672 -0.0008622631928657464
4 0.0021842900699640287 0.003635707562777463 0.004435130732395157 0.01036602511566258 0.0036275915888866277 -0.00026086977780547183 0.009724896269496387 0.003227432667221707 0.005298676586181091 0.006781387905266045 0.002020549509782527 0.0006869241274700139 -0.0005803865929164848 0.0049069089776351636 0.0009653526017621836 -0.0019955107349098017 0.0023676678684515125 0.0015421023533634787 -0.0013440532886799716 0.0030252245291879
5 0.003733584798773341 0.00490549993708534 0.003078860228813622 0.0036275915888866277 0.008090704546818293 0.0018845254770244496 0.004150024083477083 0.0001373173782296642 0.005494883822696073 0.004222647147898695 0.004856137353753583 0.0012878141616824758 0.002402114844219941 0.007074753976461715 -0.0012200847289012883 -0.002054793899112483 -0.0007258969019272229 0.0058895564963537955 0.005881056690065358 -0.00016781105855914874
6 0.0009969968871996766 0.0011223842927259615 -0.00016150466265534756 -0.00026086977780547183 0.0018845254770244496 0.0016529930265157722 0.00044057914046537926 0.00012679156265733098 0.0005758489197009294 0.00018060307440605927 0.000999236535296104 0.0001398496810198822 -9.242882332165192e-05 0.0009820952778817533 -0.0009063900606175121 -0.0005117473994541504 -0.0009568783269735779 0.0013669766602512905 0.002115694829601326 -0.0010142201129008837
7 0.003597244358324952 -0.00269564766776355 0.008675164559883656 0.009724896269496387 0.004150024083477083 0.00044057914046537926 0.017405438321715188 0.005861556839954406 0.005784368630292453 0.0050780792703878155 0.0033874343273442766 0.0006541870352270432 -0.0021796270778115215 0.005793432745776506 0.0024028465143491958 0.0009086306890069571 -0.0025654643374802277 0.0018472497889508472 0.0008422862316146371 0.0012418150884028133
8 0.0012393442347047856 -0.001551767439231339 0.0030271706962505976 0.003227432667221707 0.0001373173782296642 0.00012679156265733098 0.005861556839954406 0.004465264891489295 0.0012021900792865022 0.0010891218042716354 0.0008992397127501322 0.00019043507922463526 -0.0011207986853517015 0.0001325187262329202 0.0006361402926392805 7.21186310229716e-05 -0.0014228996699957904 0.0010239966169848793 -0.0013758209315868038 0.0008718282889432427
9 0.0029333583412517114 0.0027440255418747462 0.00466096609493093 0.005298676586181091 0.005494883822696073 0.0005758489197009294 0.005784368630292453 0.0012021900792865022 0.005281741808380219 0.004932171001394108 0.004101382102350877 0.0015449519118026429 0.0014339430632842637 0.006255748986968796 0.00019320559352417965 -0.0012206980917941566 0.00038827502743968387 0.003914822825049466 0.0029785125397308165 0.0005390115917766656
10 0.0019122050540559873 0.004207617240168365 0.0046213950074739845 0.006781387905266045 0.004222647147898695 0.00018060307440605927 0.0050780792703878155 0.0010891218042716354 0.004932171001394108 0.006526090041294011 0.003194444612717527 0.0013210122316809063 0.0007095362418653432 0.005572203701733689 -0.0003626905169709976 -0.002445635513197022 0.0019163886716631814 0.0020630368877500873 -4.3738853801347324e-05 0.0012292882812261592
11 0.0015097854159310412 0.004723658706175951 0.004631986461542638 0.002020549509782527 0.004856137353753583 0.000999236535296104 0.0033874343273442766 0.0008992397127501322 0.004101382102350877 0.003194444612717527 0.0066897181882460185 0.0010449054247435852 0.0032329758297863663 0.0065435264957391685 -0.0018688834770788712 -0.0013443877740355252 0.00033286212770116064 0.004911121344220996 0.0032115877548987218 -0.0006067983843041728
12 0.0012413074806906536 -0.0001506278074459091 0.0016783249882067598 0.0006869241274700139 0.0012878141616824758 0.0001398496810198822 0.0006541870352270432 0.00019043507922463526 0.0015449519118026429 0.0013210122316809063 0.0010449054247435852 0.0013607962745757643 -0.00011532184336314133 0.0015321709353835948 0.0005672129132130244 -0.00014736903600019708 0.0003743230873929087 0.0014770284523957457 0.0012410055664007446 -0.000698157662468904
13 0.0002621368931894943 0.002237172986842063 0.0006984203993623209 -0.0005803865929164848 0.002402114844219941 -9.242882332165192e-05 -0.0021796270778115215 -0.0011207986853517015 0.0014339430632842637 0.0007095362418653432 0.0032329758297863663 -0.00011532184336314133 0.004330458285384291 0.0032918160451897993 -0.0011396357851267609 -0.00018704031753051083 0.000680431637426465 0.0019217745320689482 0.0026632533111830845 0.0004942410646950327
14 0.0029401830385665283 0.004101282581725816 0.0059882926344004914 0.0049069089776351636 0.007074753976461715 0.0009820952778817533 0.005793432745776506 0.0001325187262329202 0.006255748986968796 0.005572203701733689 0.0065435264957391685 0.0015321709353835948 0.0032918160451897993 0.008957884393726682 -0.0007131625470789999 -0.0012598462483450047 0.0007598983558523755 0.004500815057302738 0.005019576583354035 -0.000216166457959439
15 0.0009526023476132062 -0.005800027482148545 0.0011549649166300892 0.0009653526017621836 -0.0012200847289012883 -0.0009063900606175121 0.0024028465143491958 0.0006361402926392805 0.00019320559352417965 -0.0003626905169709976 -0.0018688834770788712 0.0005672129132130244 -0.0011396357851267609 -0.0007131625470789999 0.003041267124669683 0.00244947633792001 -0.0007256234414719216 -0.0016891471115653826 0.0004450782809343759 0.00021202450438751816
16 0.00020992684954226532 -0.0073808183819315774 0.0007426552072158889 -0.0019955107349098017 -0.002054793899112483 -0.0005117473994541504 0.0009086306890069571 7.21186310229716e-05 -0.0012206980917941566 -0.002445635513197022 -0.0013443877740355252 -0.00014736903600019708 -0.00018704031753051083 -0.0012598462483450047 0.00244947633792001 0.003601566301552318 -0.002167787138490728 -0.0023447676615152694 0.0013093954753013394 -0.0007015784081159407
17 -0.0011610989405383659 0.005974742549277746 -0.0018683240284326854 0.0023676678684515125 -0.0007258969019272229 -0.0009568783269735779 -0.0025654643374802277 -0.0014228996699957904 0.00038827502743968387 0.0019163886716631814 0.00033286212770116064 0.0003743230873929087 0.000680431637426465 0.0007598983558523755 -0.0007256234414719216 -0.002167787138490728 0.006754292193423081 -0.00021673749776076852 -0.001849943148698829 0.0010675768796071575
18 0.002538117417777033 0.006741419943759147 0.0009753412379398995 0.0015421023533634787 0.0058895564963537955 0.0013669766602512905 0.0018472497889508472 0.0010239966169848793 0.003914822825049466 0.0020630368877500873 0.004911121344220996 0.0014770284523957457 0.0019217745320689482 0.004500815057302738 -0.0016891471115653826 -0.0023447676615152694 -0.00021673749776076852 0.008124999357891854 0.003381487543086098 0.00019720662523742911
19 0.00355983696170607 -0.0013962417534567177 0.0016726280867163672 -0.0013440532886799716 0.005881056690065358 0.002115694829601326 0.0008422862316146371 -0.0013758209315868038 0.0029785125397308165 -4.3738853801347324e-05 0.0032115877548987218 0.0012410055664007446 0.0026632533111830845 0.005019576583354035 0.0004450782809343759 0.0013093954753013394 -0.001849943148698829 0.003381487543086098 0.009546552659506624 -0.002559937043678229
20 -0.0003270629162205562 0.0018078608912032647 -0.0008622631928657464 0.0030252245291879 -0.00016781105855914874 -0.0010142201129008837 0.0012418150884028133 0.0008718282889432427 0.0005390115917766656 0.0012292882812261592 -0.0006067983843041728 -0.000698157662468904 0.0004942410646950327 -0.000216166457959439 0.00021202450438751816 -0.0007015784081159407 0.0010675768796071575 0.00019720662523742911 -0.002559937043678229 0.0027942194485957;
end;
