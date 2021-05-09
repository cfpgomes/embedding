
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
printf: "{ ""solution"": [%d", x[1] > "results/N32_B0.5_industry_correlated_classical/IPL_linearized_N32q70.00B16_solution.json";
printf{i in 2..n}: ",%d", x[i] >> "results/N32_B0.5_industry_correlated_classical/IPL_linearized_N32q70.00B16_solution.json";
printf: "]}" >> "results/N32_B0.5_industry_correlated_classical/IPL_linearized_N32q70.00B16_solution.json";

#data:
data;

param n := 32;
param q := 70;
param B := 16;
param mu :=
1 0.0019869319749943382
2 0.00496619514551215
3 -0.003185577493875713
4 0.002087286854557753
5 0.006180538910750509
6 0.003962724587566238
7 -0.0004670100789599659
8 -0.0027999631458458752
9 -0.0004008715924564684
10 -0.003693757359155897
11 -0.0031477757897214157
12 -0.0027549324925804555
13 -0.02817106565198864
14 -0.025372355446965155
15 -0.0009920552813279
16 0.0041832978934239
17 -0.005255273733632332
18 0.004702226069820461
19 0.0047780847758397355
20 0.0014125387536220752
21 -0.004900289926904143
22 -0.0029554087498819066
23 0.0033640561324092045
24 0.0004935972948424464
25 0.0016714038880011387
26 0.0018478838998237628
27 0.0009701599300816254
28 0.0021901286700046294
29 0.004165235382611254
30 0.0006812802233749214
31 -0.04166523911662343
32 0.002354520751951323;
param sigma : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 :=
1 0.00020952575196951008 -5.7334165291876917e-05 0.00017587991202027472 -4.9963699149825046e-05 9.351602380932966e-05 7.981008237827464e-05 5.274860743054161e-05 0.0002085126932007932 -6.072248568755683e-05 -4.140709092459637e-05 0.00011834846370890079 4.699762221807616e-05 -0.00015637509414280018 -0.0001405470964601446 3.6043603817901014e-05 -9.297512660208832e-05 2.31003448491735e-06 -8.022683627141183e-05 -8.550059796012071e-05 0.00011515299725806333 3.836780015023411e-05 9.449483325265975e-05 -0.00013336376342417804 5.976817442959612e-05 9.127877645861049e-05 9.045684706927493e-05 7.064928986155958e-06 -4.1596914660142066e-05 -8.037892468024077e-05 -8.35946623933959e-05 -0.0001416724788063719 6.243836642495918e-06
2 -5.7334165291876917e-05 0.00021136287575019606 4.735547790774274e-05 0.0001285637202858528 -4.9081340567751165e-05 5.460429994624626e-05 0.0001071088838621576 5.304314607409425e-05 3.0335101649949817e-05 4.830233361929577e-05 6.589068430425869e-05 5.490747964475227e-05 0.00011294296457707586 0.00017000792778583765 8.834889309386297e-05 0.00011866339379211698 2.0205830675625145e-05 0.00015433519426525638 0.00016429316189071666 -1.3011667215662087e-05 3.6631915292916216e-05 -0.00010326217726303367 0.0002135019592411543 -4.055707827580756e-05 -7.434783785927823e-05 -1.5452686501647098e-05 8.015472059944649e-06 7.02617564033253e-05 7.843152571115702e-05 0.00018301561435329816 0.00013069758777972974 -2.2436142367267108e-05
3 0.00017587991202027472 4.735547790774274e-05 0.0005298438129601772 -5.185011783577021e-06 -5.225895530919112e-07 0.00012083084280503107 0.0002445872372957699 0.00036456585754753745 -8.771267253544335e-05 3.193790600623701e-05 0.0005645899273036063 0.0001783822650585443 5.2681680423382635e-05 0.0001288923226959905 0.00025502981113663273 -5.875303506299981e-05 5.916191772493282e-05 4.008880202166964e-05 3.81941635217783e-05 0.0002314971218630553 0.00018580070336234023 0.00028009767621719323 -5.11693218181147e-05 0.00012494873019526425 0.00013003409602682805 0.00015698805775863644 2.9698012008265346e-05 8.449268869418784e-05 -0.00012508442952229658 0.00010069396262161388 0.0001642346680504984 -3.441625232428028e-05
4 -4.9963699149825046e-05 0.0001285637202858528 -5.185011783577021e-06 0.00020992579641120822 3.783434150352207e-05 5.010089982666202e-05 0.00011685264001517245 9.376984031912208e-05 9.019255164023667e-06 8.515996207015124e-05 2.614143721646398e-05 6.566830356219626e-05 -0.00029812801195985454 -0.00028577376740493877 0.00011254062002828193 0.00017255605903812398 1.6965975741111306e-05 0.00014288900663181968 0.00015471463947045036 -1.0911862660064101e-06 5.136553203080552e-05 -1.0768498369582159e-05 0.00015822192501372355 1.0406724577431688e-05 -4.703134113545217e-05 1.7222256815002487e-05 3.4581755436328286e-05 0.00013143622938265154 0.00013886658148493406 8.620465781567712e-05 -0.00023668312491079098 2.5933305827448636e-05
5 9.351602380932966e-05 -4.9081340567751165e-05 -5.225895530919112e-07 3.783434150352207e-05 0.0001461072041513274 6.85634522378724e-05 1.3170532890950995e-05 0.00012097858625764655 5.408430027442231e-06 2.576468657142134e-06 -3.639935530675885e-05 1.714902147999821e-05 -0.0004438597306872655 -0.0004970349630394978 -1.6080244660452845e-05 -8.199478577103286e-06 8.743033489158821e-06 -4.7988279464985653e-05 -4.891984923257448e-05 1.6089586962785113e-06 2.63826767037373e-07 2.8325171640001573e-05 -6.407885342355437e-05 -1.062281038633105e-05 -2.1511157778482138e-05 4.3463534074571515e-05 2.997699643156665e-05 -1.58378866578228e-05 2.566847623182062e-05 -8.01091970692154e-05 -0.00040473063377299075 3.9416646114122915e-05
6 7.981008237827464e-05 5.460429994624626e-05 0.00012083084280503107 5.010089982666202e-05 6.85634522378724e-05 0.0004501163946536061 -1.795173507436893e-05 0.0002481300844174547 -7.368077028437732e-05 -2.955645813058673e-06 0.00028121774377485887 0.00011248460405781855 9.062079211075962e-05 6.873288059179407e-05 0.00010037491400103245 6.652292044756002e-05 0.00016106847467050602 1.1458146402151903e-05 1.0550699855742068e-05 7.14155683401301e-05 0.00017005072446183925 8.225270200103696e-05 3.573022728766473e-05 0.0001330704409638229 0.0001649792753830661 8.495712566460918e-05 2.009414844702449e-05 5.228928499308287e-05 0.00011595957490886023 -4.840787930661587e-06 0.000582325643717046 1.590257045859825e-05
7 5.274860743054161e-05 0.0001071088838621576 0.0002445872372957699 0.00011685264001517245 1.3170532890950995e-05 -1.795173507436893e-05 0.0004068141624468038 0.00022950616875356582 -5.253501762467124e-05 4.151642467096833e-05 0.00036068288995477765 0.00011955629966489785 -0.0005667855290050555 -0.0005814363218682993 0.00015391452448424166 7.016042656626509e-05 -0.00011294621847191275 0.00013756263535459073 0.0001357797063378611 0.00010757714784888567 4.691587177834631e-06 0.00012235738189148162 5.999100308297259e-05 1.978590380749364e-05 -2.2322182683287274e-05 3.6254229472119965e-05 5.4107593204229135e-05 6.17711166228099e-05 1.482154205901503e-05 0.00023652387947540574 -0.0006516282989993196 1.1863747489706725e-05
8 0.0002085126932007932 5.304314607409425e-05 0.00036456585754753745 9.376984031912208e-05 0.00012097858625764655 0.0002481300844174547 0.00022950616875356582 0.000790294825899649 -0.00011171150224664308 -5.670400953087687e-05 0.000547594260899565 0.00015061328023495947 -0.0005810510587796864 -0.0006073112405277039 0.00028383741264281917 2.356929522949278e-05 -2.388102453832844e-05 -9.440340635508728e-06 -2.759504055323157e-06 0.00029828011126761876 0.00017709086577218823 0.00017044839507672577 -2.038229691506837e-05 0.00010192720928364098 0.00010505002066261911 0.00010032561050342795 1.675673436101072e-05 0.00010347650531830557 5.602734747031677e-06 0.0001871920304090003 -0.0003673385764185487 -1.541346036854224e-05
9 -6.072248568755683e-05 3.0335101649949817e-05 -8.771267253544335e-05 9.019255164023667e-06 5.408430027442231e-06 -7.368077028437732e-05 -5.253501762467124e-05 -0.00011171150224664308 0.0001709515338355733 6.353345497787761e-05 -0.00016326809117809437 -4.277561758640251e-05 8.469269374847428e-05 0.00010305982724645175 -6.18567966374098e-05 6.151531519371367e-06 5.6241194729498835e-05 2.5071250621376617e-06 4.176370560654239e-06 -5.321515884796812e-05 -6.275002703265325e-05 -0.00016630923543463965 6.681780743600347e-05 -5.756273055861066e-05 -9.831733216999867e-05 -9.565893703946043e-06 2.264770268382433e-05 4.280948020738861e-06 1.8945203823187046e-05 4.23282193591655e-05 -1.9810099735708914e-05 -3.899562147547078e-06
10 -4.140709092459637e-05 4.830233361929577e-05 3.193790600623701e-05 8.515996207015124e-05 2.576468657142134e-06 -2.955645813058673e-06 4.151642467096833e-05 -5.670400953087687e-05 6.353345497787761e-05 0.0001223051442794432 6.842228956429147e-05 5.889345522571385e-05 0.0001682559177087621 0.0001986663187663061 7.978735645340239e-05 6.661535626763871e-05 0.00013614494678744246 7.69732025851137e-05 8.334628217540298e-05 2.1646219906188896e-05 7.263227626972145e-05 1.9579583622237916e-05 7.101496746453227e-05 5.309908852788538e-05 1.0437476936255065e-05 6.519911611796554e-05 3.560073037350723e-05 9.216735507924724e-05 4.870351762003315e-05 5.1496600490711656e-05 0.00021551673357670528 2.1210871180445672e-07
11 0.00011834846370890079 6.589068430425869e-05 0.0005645899273036063 2.614143721646398e-05 -3.639935530675885e-05 0.00028121774377485887 0.00036068288995477765 0.000547594260899565 -0.00016326809117809437 6.842228956429147e-05 0.0011444070768633144 0.00024789068299786775 -7.914172745258247e-05 -9.145049133214492e-05 0.00040681509788976735 8.1658659316554e-06 7.940524193900453e-05 0.00010720754268636621 0.0001044864301477461 0.00030899235938625097 0.00019605689968572559 0.0004349635559906845 1.1108865658218059e-05 0.0002588351911307898 0.00025083076875992167 0.0001575837664169022 1.2778739370898252e-05 0.0001304900388130759 -2.477029353126301e-05 0.00031495786999458927 0.00022579385507006338 -8.29568972004676e-05
12 4.699762221807616e-05 5.490747964475227e-05 0.0001783822650585443 6.566830356219626e-05 1.714902147999821e-05 0.00011248460405781855 0.00011955629966489785 0.00015061328023495947 -4.277561758640251e-05 5.889345522571385e-05 0.00024789068299786775 0.00013193577201734297 0.00014128545788366135 0.00015521191828520717 0.0001255914781484391 4.7375042012473313e-05 0.00010451448818975366 5.488213018608925e-05 5.608502277253641e-05 9.884788220276644e-05 0.0001128862684148119 0.0001470042416694386 5.808546725005197e-05 8.541212336448464e-05 8.542413296703983e-05 9.901052592534977e-05 3.045258210275637e-05 8.147385866557922e-05 2.735350804745348e-05 8.902623754275883e-05 0.0003382214847793783 -3.2686773618567307e-06
13 -0.00015637509414280018 0.00011294296457707586 5.2681680423382635e-05 -0.00029812801195985454 -0.0004438597306872655 9.062079211075962e-05 -0.0005667855290050555 -0.0005810510587796864 8.469269374847428e-05 0.0001682559177087621 -7.914172745258247e-05 0.00014128545788366135 0.005412189466872491 0.005582483578594521 5.176958038869723e-06 -0.0002032663016254572 0.0011405430038025728 0.00012468368020690523 0.00010550348426971214 0.00022289642419593536 0.0005397091736456971 -3.310721674144308e-05 0.0001299959812263684 0.0004415323145446672 0.000633169317486919 0.0002465709084405062 -8.686441179988514e-05 0.00014348305849470213 -0.00011128833305198859 0.0002710999827606631 0.0056468469947302214 -0.0002048664509095143
14 -0.0001405470964601446 0.00017000792778583765 0.0001288923226959905 -0.00028577376740493877 -0.0004970349630394978 6.873288059179407e-05 -0.0005814363218682993 -0.0006073112405277039 0.00010305982724645175 0.0001986663187663061 -9.145049133214492e-05 0.00015521191828520717 0.005582483578594521 0.005910047772862706 5.5280985310420655e-05 -0.0001934581358370692 0.0011473693366687145 0.00014862295091585965 0.0001370100708774632 0.0002519962205605341 0.0005945772420845238 -0.00010423875032297269 0.00015050824381401267 0.0004491330187514353 0.0006346884755643417 0.0002600695895881752 -9.43612125594085e-05 0.00017422128505317655 -0.00016495390627837623 0.00022069098386368326 0.005853592667512893 -0.0002179509546133299
15 3.6043603817901014e-05 8.834889309386297e-05 0.00025502981113663273 0.00011254062002828193 -1.6080244660452845e-05 0.00010037491400103245 0.00015391452448424166 0.00028383741264281917 -6.18567966374098e-05 7.978735645340239e-05 0.00040681509788976735 0.0001255914781484391 5.176958038869723e-06 5.5280985310420655e-05 0.0003048373630705137 7.606846701439034e-05 0.0001460355155302025 0.00011012424351258022 0.0001270701969430821 0.00018971425133210517 0.00022375656558796367 0.00015195226863410068 2.4318461153501666e-05 0.00016046324852174085 0.00012108887899562161 0.0001151267994635131 1.592713732927065e-05 0.00016702506148041834 1.2913359194346248e-05 0.0001265442627344658 0.0001887922102331084 -2.920581053297263e-05
16 -9.297512660208832e-05 0.00011866339379211698 -5.875303506299981e-05 0.00017255605903812398 -8.199478577103286e-06 6.652292044756002e-05 7.016042656626509e-05 2.356929522949278e-05 6.151531519371367e-06 6.661535626763871e-05 8.1658659316554e-06 4.7375042012473313e-05 -0.0002032663016254572 -0.0001934581358370692 7.606846701439034e-05 0.00019303559660260763 -2.99497994120888e-07 0.0001146045520440382 0.00012685300858241965 -1.9228916105746716e-05 5.127924852690628e-05 -2.9241348075866202e-05 0.00017235000124521881 -5.76068157015827e-06 -4.961027776276198e-05 2.555132752602053e-06 3.591219360127775e-05 0.00011825400442781079 0.0001493305630539927 9.246467948714771e-05 -5.349283062692301e-05 3.1723424400092056e-05
17 2.31003448491735e-06 2.0205830675625145e-05 5.916191772493282e-05 1.6965975741111306e-05 8.743033489158821e-06 0.00016106847467050602 -0.00011294621847191275 -2.388102453832844e-05 5.6241194729498835e-05 0.00013614494678744246 7.940524193900453e-05 0.00010451448818975366 0.0011405430038025728 0.0011473693366687145 0.0001460355155302025 -2.99497994120888e-07 0.0005400755856364203 5.442409206935533e-05 6.223168114231095e-05 0.00012721365059090208 0.0002879721935482922 4.959869673284731e-05 -3.5198658624206786e-05 0.0002510298805463462 0.00024082459480254098 0.00019566088781919247 2.279230582710878e-05 0.00014291842791113135 3.642619142770355e-05 3.985613722907294e-05 0.001466731955023449 -2.7252332306193917e-05
18 -8.022683627141183e-05 0.00015433519426525638 4.008880202166964e-05 0.00014288900663181968 -4.7988279464985653e-05 1.1458146402151903e-05 0.00013756263535459073 -9.440340635508728e-06 2.5071250621376617e-06 7.69732025851137e-05 0.00010720754268636621 5.488213018608925e-05 0.00012468368020690523 0.00014862295091585965 0.00011012424351258022 0.0001146045520440382 5.442409206935533e-05 0.00021738029236239773 0.00022141891414040365 -6.3852474280982405e-06 7.28786319734119e-06 -6.888945439528107e-07 0.00014877446952218755 6.587429730236793e-05 2.097524775044692e-05 3.613304294972167e-06 2.4635603780883672e-05 0.00010965946778610177 0.00010227590404012707 0.00013320701683805657 7.070775658905932e-05 -6.337932927785826e-06
19 -8.550059796012071e-05 0.00016429316189071666 3.81941635217783e-05 0.00015471463947045036 -4.891984923257448e-05 1.0550699855742068e-05 0.0001357797063378611 -2.759504055323157e-06 4.176370560654239e-06 8.334628217540298e-05 0.0001044864301477461 5.608502277253641e-05 0.00010550348426971214 0.0001370100708774632 0.0001270701969430821 0.00012685300858241965 6.223168114231095e-05 0.00022141891414040365 0.00022914146511249619 -1.1459967415945827e-06 2.7769670322875736e-05 -1.0494299929050552e-05 0.0001549462230079903 6.251957609315018e-05 1.152964109758703e-05 4.430816028440611e-06 2.5913983667336595e-05 0.00012123389826196665 0.00010670222866519954 0.00013056751439555404 6.42664120415728e-05 -6.675029301467348e-06
20 0.00011515299725806333 -1.3011667215662087e-05 0.0002314971218630553 -1.0911862660064101e-06 1.6089586962785113e-06 7.14155683401301e-05 0.00010757714784888567 0.00029828011126761876 -5.321515884796812e-05 2.1646219906188896e-05 0.00030899235938625097 9.884788220276644e-05 0.00022289642419593536 0.0002519962205605341 0.00018971425133210517 -1.9228916105746716e-05 0.00012721365059090208 -6.3852474280982405e-06 -1.1459967415945827e-06 0.00024264582305744717 0.00019277146818585944 0.00013091586047303655 -7.698369752589851e-05 0.00015689829182747285 0.00016856840138638394 0.00012149196820069958 2.3249466130564855e-05 9.250421769611585e-05 -4.359977375557903e-05 7.9172088101461e-05 0.0003355623029790856 -1.5967765400454098e-05
21 3.836780015023411e-05 3.6631915292916216e-05 0.00018580070336234023 5.136553203080552e-05 2.63826767037373e-07 0.00017005072446183925 4.691587177834631e-06 0.00017709086577218823 -6.275002703265325e-05 7.263227626972145e-05 0.00019605689968572559 0.0001128862684148119 0.0005397091736456971 0.0005945772420845238 0.00022375656558796367 5.127924852690628e-05 0.0002879721935482922 7.28786319734119e-06 2.7769670322875736e-05 0.00019277146818585944 0.00046936911209953655 5.858446628126276e-05 -7.027440637937037e-05 8.20055804017957e-05 8.833232056002092e-05 0.0001328663367472883 3.750029384295605e-05 0.00013091241498764886 -2.9875468509380794e-05 6.144702763634084e-05 0.0008743749964394037 1.3374573222202982e-05
22 9.449483325265975e-05 -0.00010326217726303367 0.00028009767621719323 -1.0768498369582159e-05 2.8325171640001573e-05 8.225270200103696e-05 0.00012235738189148162 0.00017044839507672577 -0.00016630923543463965 1.9579583622237916e-05 0.0004349635559906845 0.0001470042416694386 -3.310721674144308e-05 -0.00010423875032297269 0.00015195226863410068 -2.9241348075866202e-05 4.959869673284731e-05 -6.888945439528107e-07 -1.0494299929050552e-05 0.00013091586047303655 5.858446628126276e-05 0.000455516017029062 -7.949088087006644e-05 0.0001886448016170161 0.00021611520347678754 0.0001431991849166349 1.548661411072566e-05 7.200671761249657e-05 -2.4688883893221695e-05 -2.4822576196569194e-05 0.00015803241787471737 -4.454322407452055e-06
23 -0.00013336376342417804 0.0002135019592411543 -5.11693218181147e-05 0.00015822192501372355 -6.407885342355437e-05 3.573022728766473e-05 5.999100308297259e-05 -2.038229691506837e-05 6.681780743600347e-05 7.101496746453227e-05 1.1108865658218059e-05 5.808546725005197e-05 0.0001299959812263684 0.00015050824381401267 2.4318461153501666e-05 0.00017235000124521881 -3.5198658624206786e-05 0.00014877446952218755 0.0001549462230079903 -7.698369752589851e-05 -7.027440637937037e-05 -7.949088087006644e-05 0.00034941512295885295 -8.28226828289513e-05 -0.00011287024822441325 -4.569790419779864e-05 7.765210550778575e-06 7.8624570879356e-05 0.00015400280169118748 0.00021502138454813582 0.0001579839062901139 -2.5193729853587558e-05
24 5.976817442959612e-05 -4.055707827580756e-05 0.00012494873019526425 1.0406724577431688e-05 -1.062281038633105e-05 0.0001330704409638229 1.978590380749364e-05 0.00010192720928364098 -5.756273055861066e-05 5.309908852788538e-05 0.0002588351911307898 8.541212336448464e-05 0.0004415323145446672 0.0004491330187514353 0.00016046324852174085 -5.76068157015827e-06 0.0002510298805463462 6.587429730236793e-05 6.251957609315018e-05 0.00015689829182747285 8.20055804017957e-05 0.0001886448016170161 -8.28226828289513e-05 0.0003228962189462593 0.0003244688701070312 0.00014154320389256545 2.5036037713725482e-06 0.0001247643179579969 3.819076094912131e-05 -3.6139950181301554e-05 0.0006447269500588872 -1.9983826072312244e-05
25 9.127877645861049e-05 -7.434783785927823e-05 0.00013003409602682805 -4.703134113545217e-05 -2.1511157778482138e-05 0.0001649792753830661 -2.2322182683287274e-05 0.00010505002066261911 -9.831733216999867e-05 1.0437476936255065e-05 0.00025083076875992167 8.542413296703983e-05 0.000633169317486919 0.0006346884755643417 0.00012108887899562161 -4.961027776276198e-05 0.00024082459480254098 2.097524775044692e-05 1.152964109758703e-05 0.00016856840138638394 8.833232056002092e-05 0.00021611520347678754 -0.00011287024822441325 0.0003244688701070312 0.00036811586297687146 0.00013920218109073014 -1.0332353549642482e-05 8.18374126845653e-05 8.889700194239978e-06 -5.7880576705000074e-05 0.0008666578064458252 -2.242667533576498e-05
26 9.045684706927493e-05 -1.5452686501647098e-05 0.00015698805775863644 1.7222256815002487e-05 4.3463534074571515e-05 8.495712566460918e-05 3.6254229472119965e-05 0.00010032561050342795 -9.565893703946043e-06 6.519911611796554e-05 0.0001575837664169022 9.901052592534977e-05 0.0002465709084405062 0.0002600695895881752 0.0001151267994635131 2.555132752602053e-06 0.00019566088781919247 3.613304294972167e-06 4.430816028440611e-06 0.00012149196820069958 0.0001328663367472883 0.0001431991849166349 -4.569790419779864e-05 0.00014154320389256545 0.00013920218109073014 0.00016416846348448117 3.863472921142776e-05 7.848445805732345e-05 -1.1789402530413083e-05 1.8189241748524693e-05 0.00044053889480680567 7.866822047124455e-06
27 7.064928986155958e-06 8.015472059944649e-06 2.9698012008265346e-05 3.4581755436328286e-05 2.997699643156665e-05 2.009414844702449e-05 5.4107593204229135e-05 1.675673436101072e-05 2.264770268382433e-05 3.560073037350723e-05 1.2778739370898252e-05 3.045258210275637e-05 -8.686441179988514e-05 -9.43612125594085e-05 1.592713732927065e-05 3.591219360127775e-05 2.279230582710878e-05 2.4635603780883672e-05 2.5913983667336595e-05 2.3249466130564855e-05 3.750029384295605e-05 1.548661411072566e-05 7.765210550778575e-06 2.5036037713725482e-06 -1.0332353549642482e-05 3.863472921142776e-05 5.1793049285549746e-05 3.0682285907667796e-05 3.0364137392621703e-05 1.287937463764356e-05 -5.5729619555859254e-05 3.3030903939884174e-05
28 -4.1596914660142066e-05 7.02617564033253e-05 8.449268869418784e-05 0.00013143622938265154 -1.58378866578228e-05 5.228928499308287e-05 6.17711166228099e-05 0.00010347650531830557 4.280948020738861e-06 9.216735507924724e-05 0.0001304900388130759 8.147385866557922e-05 0.00014348305849470213 0.00017422128505317655 0.00016702506148041834 0.00011825400442781079 0.00014291842791113135 0.00010965946778610177 0.00012123389826196665 9.250421769611585e-05 0.00013091241498764886 7.200671761249657e-05 7.8624570879356e-05 0.0001247643179579969 8.18374126845653e-05 7.848445805732345e-05 3.0682285907667796e-05 0.00017265140968001394 8.504003891032013e-05 6.108054455243543e-05 0.00028335950370214635 2.6259951703742916e-06
29 -8.037892468024077e-05 7.843152571115702e-05 -0.00012508442952229658 0.00013886658148493406 2.566847623182062e-05 0.00011595957490886023 1.482154205901503e-05 5.602734747031677e-06 1.8945203823187046e-05 4.870351762003315e-05 -2.477029353126301e-05 2.735350804745348e-05 -0.00011128833305198859 -0.00016495390627837623 1.2913359194346248e-05 0.0001493305630539927 3.642619142770355e-05 0.00010227590404012707 0.00010670222866519954 -4.359977375557903e-05 -2.9875468509380794e-05 -2.4688883893221695e-05 0.00015400280169118748 3.819076094912131e-05 8.889700194239978e-06 -1.1789402530413083e-05 3.0364137392621703e-05 8.504003891032013e-05 0.00019045810277160198 3.731980134439825e-05 -3.911663777368511e-06 2.6036093529928654e-05
30 -8.35946623933959e-05 0.00018301561435329816 0.00010069396262161388 8.620465781567712e-05 -8.01091970692154e-05 -4.840787930661587e-06 0.00023652387947540574 0.0001871920304090003 4.23282193591655e-05 5.1496600490711656e-05 0.00031495786999458927 8.902623754275883e-05 0.0002710999827606631 0.00022069098386368326 0.0001265442627344658 9.246467948714771e-05 3.985613722907294e-05 0.00013320701683805657 0.00013056751439555404 7.9172088101461e-05 6.144702763634084e-05 -2.4822576196569194e-05 0.00021502138454813582 -3.6139950181301554e-05 -5.7880576705000074e-05 1.8189241748524693e-05 1.287937463764356e-05 6.108054455243543e-05 3.731980134439825e-05 0.000523753114943102 0.0002580573407217782 -4.5517170773243804e-05
31 -0.0001416724788063719 0.00013069758777972974 0.0001642346680504984 -0.00023668312491079098 -0.00040473063377299075 0.000582325643717046 -0.0006516282989993196 -0.0003673385764185487 -1.9810099735708914e-05 0.00021551673357670528 0.00022579385507006338 0.0003382214847793783 0.0056468469947302214 0.005853592667512893 0.0001887922102331084 -5.349283062692301e-05 0.001466731955023449 7.070775658905932e-05 6.42664120415728e-05 0.0003355623029790856 0.0008743749964394037 0.00015803241787471737 0.0001579839062901139 0.0006447269500588872 0.0008666578064458252 0.00044053889480680567 -5.5729619555859254e-05 0.00028335950370214635 -3.911663777368511e-06 0.0002580573407217782 0.006939397000869956 -0.00017039954548423074
32 6.243836642495918e-06 -2.2436142367267108e-05 -3.441625232428028e-05 2.5933305827448636e-05 3.9416646114122915e-05 1.590257045859825e-05 1.1863747489706725e-05 -1.541346036854224e-05 -3.899562147547078e-06 2.1210871180445672e-07 -8.29568972004676e-05 -3.2686773618567307e-06 -0.0002048664509095143 -0.0002179509546133299 -2.920581053297263e-05 3.1723424400092056e-05 -2.7252332306193917e-05 -6.337932927785826e-06 -6.675029301467348e-06 -1.5967765400454098e-05 1.3374573222202982e-05 -4.454322407452055e-06 -2.5193729853587558e-05 -1.9983826072312244e-05 -2.242667533576498e-05 7.866822047124455e-06 3.3030903939884174e-05 2.6259951703742916e-06 2.6036093529928654e-05 -4.5517170773243804e-05 -0.00017039954548423074 4.50456023691093e-05;
end;
