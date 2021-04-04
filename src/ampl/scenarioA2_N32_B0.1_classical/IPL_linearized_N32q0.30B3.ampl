
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
printf: "{ ""solution"": [%d", x[1] > "results/scenarioA2_N32_B0.1_classical/IPL_linearized_N32q0.30B3_solution.json";
printf{i in 2..n}: ",%d", x[i] >> "results/scenarioA2_N32_B0.1_classical/IPL_linearized_N32q0.30B3_solution.json";
printf: "]}" >> "results/scenarioA2_N32_B0.1_classical/IPL_linearized_N32q0.30B3_solution.json";

#data:
data;

param n := 32;
param q := 0.30000000000000004;
param B := 3;
param mu :=
1 0.006672863194472878
2 -0.0005657719597152611
3 9.56132732858106e-05
4 0.0043423003530233765
5 9.163352244409562e-05
6 9.667140929613405e-05
7 -0.0013502236473571182
8 0.002564918493923302
9 -0.0018301496411297913
10 -0.004712361595109215
11 0.0017170712217501384
12 0.003489847958281456
13 0.007147740896610022
14 0.0021259089662375497
15 -0.005415057018813707
16 0.005964006043966902
17 -0.0011796755440926232
18 -0.0033595961943244878
19 0.004566694088427104
20 -0.005965365925735949
21 0.002337570869249178
22 -0.002350103358567751
23 0.002744681055228582
24 0.001028279087513434
25 -0.001516429900924665
26 -0.005366814548175702
27 0.0023468359083123
28 -0.0008633775255719011
29 0.007466162717324426
30 0.005176210986128543
31 0.008707260961317515
32 0.003992522253681197;
param sigma : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 :=
1 0.0003137773405389041 -3.397586440000851e-05 -2.2288003777661456e-05 -2.7551962579440446e-05 -0.00022016846133650575 0.00012409239083781658 1.1601658415451156e-05 0.0002142941990439731 1.6721406782219745e-06 -6.891395864226503e-05 0.0003510253588091557 0.00015436400482111292 0.00014086605577226673 0.0001465673852126817 -0.00019134330707746422 -0.00015314636926057522 -0.00013848442579565928 0.0003322607469930468 8.974576109845859e-05 0.00015183613818268277 1.4242332855320428e-05 -0.00014219127309026458 0.00012149190786716242 0.00024134714574660962 -4.021374516857892e-07 0.00017933066651777392 0.0001453028162048566 -0.0001366516116612839 7.469145836292205e-05 0.0001238401911435847 0.00015752445307690223 9.3016738993861e-05
2 -3.397586440000851e-05 0.0002805810190156016 0.00012164335594080983 8.245767042162997e-05 0.0001583823208990194 6.0976916496970764e-05 0.0001515219506696335 -3.0399047058759557e-06 0.0001239947356829563 0.0002014471016109546 -3.8929995190796036e-05 3.386883529373954e-05 5.0306139352219524e-05 4.958244782718809e-05 0.00019828079300114747 0.0001389267059943598 4.385183132336219e-05 -2.7702311507634253e-05 0.00012453099874482017 -5.4728007022296544e-05 4.468319741094683e-05 0.00015125366097427999 5.284992725868713e-05 -3.2936032912771085e-05 0.00015454250648250237 -6.922283752757339e-05 7.303742063780716e-06 6.189080795110786e-05 8.803739947597197e-05 1.6916360011137043e-05 0.00010752161343391666 1.7103351871458388e-05
3 -2.2288003777661456e-05 0.00012164335594080983 0.00020910177359636546 0.00015864470108219468 0.0002541955766220094 8.401796038338673e-05 0.00010948079210212963 3.462492399510674e-06 0.0002261043555222418 0.0003721082605224064 1.1115042375751751e-05 -2.0119403211920685e-05 1.2505725138216937e-05 3.964983875291454e-05 0.00030061275323494475 0.0001804242727502659 0.00012239665044298676 -5.582744324430413e-05 0.00012966788716374148 5.1713341407755525e-05 2.8438402458719333e-05 0.00019227739402338377 -3.723276177296145e-05 -5.9417856109133e-05 0.00010021931470375407 -1.6795693293429096e-05 -4.2138162920723545e-05 0.00010754974458011581 -1.1468226586676904e-05 -6.532181201544937e-06 9.444475695522827e-05 -4.668612348833635e-05
4 -2.7551962579440446e-05 8.245767042162997e-05 0.00015864470108219468 0.0002770642917077778 0.00026056330830209024 0.00013953963251856985 0.00015260546844902278 5.5092283677561686e-05 0.0003359981109940112 0.0003097545411735929 -1.3086727184919385e-05 5.444189632899072e-05 4.667054171049113e-05 5.736468501918507e-05 0.00026804952489095494 0.00023820382583915708 9.871979179947745e-05 -4.7295727439014374e-05 0.00013049276260729907 0.00015759444764834097 3.741047999431138e-05 0.0001578350031259019 5.80096276016477e-05 1.1148939832583257e-05 0.0001238007368666585 0.00012375123081880752 4.775920993906742e-05 8.002790171509322e-05 -1.5432398784172907e-05 3.869323492967693e-05 0.00012642937714091106 -4.508785446242219e-05
5 -0.00022016846133650575 0.0001583823208990194 0.0002541955766220094 0.00026056330830209024 0.0005679751426197252 6.317730540254257e-05 0.00017544447049601652 -0.00010284065874604404 0.0003970052978319672 0.0006716430485273866 -0.00017744662384606676 -0.0001039767840179027 -6.123970953737796e-05 2.1332134295167934e-05 0.0006379849500068805 0.00038107219165340223 0.00033217064054614224 -9.485142468690862e-05 0.00011485961113968385 5.432410647528249e-05 3.363590775731775e-05 0.00040391909526279877 -0.00010231753295454968 -0.00018671968823432585 0.0002084583288779341 1.9985693447100336e-05 -1.3595387095717753e-05 0.00030775248610056085 -5.176094420333206e-05 -9.445106632560117e-05 1.4146575852252118e-05 -9.895954031431078e-05
6 0.00012409239083781658 6.0976916496970764e-05 8.401796038338673e-05 0.00013953963251856985 6.317730540254257e-05 0.00019543889138266924 0.00012832604145476508 0.0001543265153882274 0.00022499187505682495 0.00017482607538820585 0.00013482947370814188 0.00012043254419377768 0.00011871515240541776 0.00014121216360706883 0.00011070221471785143 3.348756640131006e-05 5.12281101814542e-06 0.0002217009847183163 0.00013167451621964347 0.0001876493026308764 4.9041099272375395e-05 6.256569910257534e-05 8.0307935947162e-05 0.00015464765345827376 0.00012777831118528524 0.0001325092040396317 0.00013985079057838754 4.2969918918656447e-05 2.8467924359450816e-05 8.432435075675439e-05 0.00014387485004928012 4.22443296490541e-05
7 1.1601658415451156e-05 0.0001515219506696335 0.00010948079210212963 0.00015260546844902278 0.00017544447049601652 0.00012832604145476508 0.0004412248739170243 7.333357963643814e-05 0.0003136322815087571 0.00034773092620634906 0.00014876902277578488 4.8612554750590837e-05 -1.3830009001074213e-05 8.750229737864404e-05 0.00036671176600302423 0.00011004429988116903 0.00012949194590203592 -2.822219696345094e-05 0.00013038468456347924 0.0001654254078023113 6.794367208783689e-05 0.00020799765178260838 8.17438826031087e-05 3.46680037193572e-05 6.638751375097209e-05 4.978147551102448e-05 9.566523572399876e-05 5.430180338211267e-05 5.23347379425829e-05 -2.0125358983416535e-05 0.00012060237476330578 -5.003429547483909e-05
8 0.0002142941990439731 -3.0399047058759557e-06 3.462492399510674e-06 5.5092283677561686e-05 -0.00010284065874604404 0.0001543265153882274 7.333357963643814e-05 0.0002088151815624795 0.00012417623498565966 4.234498158047595e-05 0.0002696862876812955 0.0001583951268517934 0.0001199434056090127 0.00014226892724870965 -4.5110644972346466e-05 -5.4376469649481546e-05 -7.774049049115695e-05 0.00028797026007839217 6.25510493355035e-05 0.00021849978418671126 2.8950245412762275e-05 -5.287171345205252e-05 0.0001334345779426864 0.0002350273685204802 5.084128519340825e-05 0.00018748545095671572 0.00014953581623560348 -5.303450969897586e-05 4.222329570258302e-05 0.00011963262549362719 0.00013956825627060995 6.926986621138339e-05
9 1.6721406782219745e-06 0.0001239947356829563 0.0002261043555222418 0.0003359981109940112 0.0003970052978319672 0.00022499187505682495 0.0003136322815087571 0.00012417623498565966 0.0008155747829608139 0.0007884046622015402 9.42605280267054e-05 5.007724878008414e-05 8.42693146267717e-06 0.00011822795729924422 0.0005998364828745227 0.0002692204552707326 0.00024050206030668464 0.00016148001728193452 0.00019969971431614284 0.0004867141073308885 7.182659178069431e-05 0.00027664315799960193 5.889018098165326e-05 8.6040411105556e-05 0.00019740820329617844 0.00016275321816156262 0.00012211109373984629 0.00027481931900169164 -7.937446724789783e-05 5.784309042315914e-05 0.00011904793327036495 -8.151052387280696e-05
10 -6.891395864226503e-05 0.0002014471016109546 0.0003721082605224064 0.0003097545411735929 0.0006716430485273866 0.00017482607538820585 0.00034773092620634906 4.234498158047595e-05 0.0007884046622015402 0.0013432374446205415 0.00011636115068296457 -7.577700738971963e-05 -0.00012610289343643264 8.512857429473468e-05 0.0009556762515433552 0.0003885822732544845 0.00040812269047804526 0.0004100331495482823 0.00018650351342549743 0.00030960712124960545 6.105119355319513e-05 0.0005003123948007246 -0.00012018130328003793 -3.959967036320949e-05 0.000241484717284843 7.947571581158052e-05 9.514825251885755e-05 0.0005044161586832227 -4.13670544990112e-05 -3.456117957570964e-05 3.925441365994769e-05 -0.00013113788623654813
11 0.0003510253588091557 -3.8929995190796036e-05 1.1115042375751751e-05 -1.3086727184919385e-05 -0.00017744662384606676 0.00013482947370814188 0.00014876902277578488 0.0002696862876812955 9.42605280267054e-05 0.00011636115068296457 0.0008242640943190924 0.00019728642373139976 0.00018726924472623065 0.00020744447742953968 -4.381398276488326e-06 -9.186185141869503e-05 -8.484076384179702e-05 0.0003934752178475849 5.5598785704255216e-05 0.00037627773009700515 0.00011608307501685583 -0.00011602509807446206 0.0002484581309860141 0.0002840736876369321 -7.246980699819693e-05 0.0002884621362386819 0.0001319432467234239 -0.00017052037794566125 9.022564580831488e-05 0.00015550827569575266 0.0002721489205135106 8.265645857656492e-05
12 0.00015436400482111292 3.386883529373954e-05 -2.0119403211920685e-05 5.444189632899072e-05 -0.0001039767840179027 0.00012043254419377768 4.8612554750590837e-05 0.0001583951268517934 5.007724878008414e-05 -7.577700738971963e-05 0.00019728642373139976 0.0001762957623765608 0.00013021502923230076 0.00011937601014109627 -0.00010094364349622755 -3.9889157450883823e-05 -0.00010800786841446589 0.00015242695681902128 4.140240251665428e-05 0.0001702599158795967 3.0998123840995385e-05 -7.523747788732413e-05 0.00016288039493609225 0.00017537790860013624 7.082464091022753e-05 0.00014558462821432337 0.00011268092876993363 -8.274747133057452e-05 7.404443617627092e-05 0.00011705607997230814 0.00011070854071795572 7.520294128280805e-05
13 0.00014086605577226673 5.0306139352219524e-05 1.2505725138216937e-05 4.667054171049113e-05 -6.123970953737796e-05 0.00011871515240541776 -1.3830009001074213e-05 0.0001199434056090127 8.42693146267717e-06 -0.00012610289343643264 0.00018726924472623065 0.00013021502923230076 0.00024740916878731895 0.0001088227428798927 -7.182631420959511e-05 1.215642200007786e-05 -6.591021007706037e-05 0.0001343816765369139 0.00011286777085404374 7.454860222189773e-05 6.63872277249368e-05 -1.590404787143811e-05 0.00011244901265811549 0.0001368509263885027 0.00010114153307317653 0.00012523170837188522 9.61292445115402e-05 -5.5017886398452574e-05 5.4555582424557275e-05 7.992187065405861e-05 0.00012684901877845422 8.042973851529379e-05
14 0.0001465673852126817 4.958244782718809e-05 3.964983875291454e-05 5.736468501918507e-05 2.1332134295167934e-05 0.00014121216360706883 8.750229737864404e-05 0.00014226892724870965 0.00011822795729924422 8.512857429473468e-05 0.00020744447742953968 0.00011937601014109627 0.0001088227428798927 0.0002229829226066151 3.4138650085431325e-05 -3.564836944593615e-05 1.36915835402129e-05 0.00026589860341615616 0.00010402990419567157 0.0001887100177859481 1.5614900060308904e-05 2.5334048902152708e-05 0.00011746861615532778 0.00017682577282903655 0.00010369805873133317 0.00019681463706794835 0.000173979096979684 -1.2574851591166166e-05 4.29514976330298e-05 7.808818784745362e-05 0.00014571195648431157 8.630734862192003e-05
15 -0.00019134330707746422 0.00019828079300114747 0.00030061275323494475 0.00026804952489095494 0.0006379849500068805 0.00011070221471785143 0.00036671176600302423 -4.5110644972346466e-05 0.0005998364828745227 0.0009556762515433552 -4.381398276488326e-06 -0.00010094364349622755 -7.182631420959511e-05 3.4138650085431325e-05 0.0009481774679392229 0.00040702405991609544 0.00044451156515587417 -3.4065332654776954e-06 0.00014025396568061882 0.0002295413764740515 7.38015880170719e-05 0.0005467816165515841 -0.00010269224582323113 -0.00015869396254132378 0.00023989159549365644 8.397355918393466e-05 1.7304415537301155e-05 0.0003990816086308815 -7.480347405319719e-05 -0.00010983097623476498 4.2009448676956e-05 -0.00012159568662124692
16 -0.00015314636926057522 0.0001389267059943598 0.0001804242727502659 0.00023820382583915708 0.00038107219165340223 3.348756640131006e-05 0.00011004429988116903 -5.4376469649481546e-05 0.0002692204552707326 0.0003885822732544845 -9.186185141869503e-05 -3.9889157450883823e-05 1.215642200007786e-05 -3.564836944593615e-05 0.00040702405991609544 0.00039566059647436024 0.00019982820147374292 -0.000147867990109654 7.203787825800116e-05 2.2212150614551606e-05 3.6838992172824736e-05 0.00025487347445025526 -2.8938497001815103e-06 -0.00012510698900947362 0.00013954099645583344 3.849410040875849e-05 -5.113060259287931e-05 0.0001535348529908321 -7.50675115924553e-06 -3.9567154586000876e-05 5.822677628601335e-05 -7.610886659309684e-05
17 -0.00013848442579565928 4.385183132336219e-05 0.00012239665044298676 9.871979179947745e-05 0.00033217064054614224 5.12281101814542e-06 0.00012949194590203592 -7.774049049115695e-05 0.00024050206030668464 0.00040812269047804526 -8.484076384179702e-05 -0.00010800786841446589 -6.591021007706037e-05 1.36915835402129e-05 0.00044451156515587417 0.00019982820147374292 0.00029436951076713995 -9.276780559297144e-06 4.5437382453236065e-05 4.1659957750482e-05 1.5437258559809326e-06 0.0002765356558405098 -0.00010446189549782397 -0.00014014439339298738 0.000130988701632163 4.930452999590598e-05 8.772147100803821e-06 0.00022036340879907275 -2.875151601029167e-05 -9.453303612595935e-05 -3.455498918294886e-05 -6.267148763030835e-05
18 0.0003322607469930468 -2.7702311507634253e-05 -5.582744324430413e-05 -4.7295727439014374e-05 -9.485142468690862e-05 0.0002217009847183163 -2.822219696345094e-05 0.00028797026007839217 0.00016148001728193452 0.0004100331495482823 0.0003934752178475849 0.00015242695681902128 0.0001343816765369139 0.00026589860341615616 -3.4065332654776954e-06 -0.000147867990109654 -9.276780559297144e-06 0.0018062431008579437 0.00018911272566352603 0.00020575536498811993 -0.00010738572221834053 -8.312910398699437e-05 2.535654178916103e-05 0.0005418390848798798 7.890279686154714e-05 0.0004909526234725875 0.0005776746361048063 0.00026466464838896574 6.791604664337031e-05 0.00015500642163106468 4.223920550062787e-05 0.00021192592991323391
19 8.974576109845859e-05 0.00012453099874482017 0.00012966788716374148 0.00013049276260729907 0.00011485961113968385 0.00013167451621964347 0.00013038468456347924 6.25510493355035e-05 0.00019969971431614284 0.00018650351342549743 5.5598785704255216e-05 4.140240251665428e-05 0.00011286777085404374 0.00010402990419567157 0.00014025396568061882 7.203787825800116e-05 4.5437382453236065e-05 0.00018911272566352603 0.00023808478318023633 6.287078777497539e-05 1.3998293108725903e-05 0.00010164636032980153 2.691875849101419e-05 7.371862160453158e-05 8.939377406883589e-05 9.904832041865854e-05 0.0001119584063978271 3.665815626593124e-05 1.5323365826150475e-05 2.7745300803534695e-05 0.00014566238736309938 1.977660613714991e-05
20 0.00015183613818268277 -5.4728007022296544e-05 5.1713341407755525e-05 0.00015759444764834097 5.432410647528249e-05 0.0001876493026308764 0.0001654254078023113 0.00021849978418671126 0.0004867141073308885 0.00030960712124960545 0.00037627773009700515 0.0001702599158795967 7.454860222189773e-05 0.0001887100177859481 0.0002295413764740515 2.2212150614551606e-05 4.1659957750482e-05 0.00020575536498811993 6.287078777497539e-05 0.0006496508359871533 4.038516697286195e-05 2.0304683470219938e-05 0.00019842676906787406 0.0002489884131798107 3.680365865467171e-05 0.0003158018885630815 0.00013589047660046266 1.806167578711559e-05 -8.760067120990321e-05 0.00013637755906356402 0.00013761763007210835 1.9038968634742497e-05
21 1.4242332855320428e-05 4.468319741094683e-05 2.8438402458719333e-05 3.741047999431138e-05 3.363590775731775e-05 4.9041099272375395e-05 6.794367208783689e-05 2.8950245412762275e-05 7.182659178069431e-05 6.105119355319513e-05 0.00011608307501685583 3.0998123840995385e-05 6.63872277249368e-05 1.5614900060308904e-05 7.38015880170719e-05 3.6838992172824736e-05 1.5437258559809326e-06 -0.00010738572221834053 1.3998293108725903e-05 4.038516697286195e-05 0.00010663122576437231 2.7521685196056106e-05 6.688386107242439e-05 -5.873038198711414e-06 4.339405710507344e-05 -6.399901297163906e-05 -2.7452150063605443e-05 -2.5834465903895152e-06 3.510393883630429e-05 1.5777761908271705e-05 7.183850641962147e-05 -5.716076493289002e-06
22 -0.00014219127309026458 0.00015125366097427999 0.00019227739402338377 0.0001578350031259019 0.00040391909526279877 6.256569910257534e-05 0.00020799765178260838 -5.287171345205252e-05 0.00027664315799960193 0.0005003123948007246 -0.00011602509807446206 -7.523747788732413e-05 -1.590404787143811e-05 2.5334048902152708e-05 0.0005467816165515841 0.00025487347445025526 0.0002765356558405098 -8.312910398699437e-05 0.00010164636032980153 2.0304683470219938e-05 2.7521685196056106e-05 0.0003807183212128199 -0.00010721685383999483 -0.00012924738722312792 0.0001884213283112007 2.428269315743898e-05 1.1334636767039064e-05 0.00024572509720470714 -2.8394037083021488e-05 -9.135393399205827e-05 1.5830421336397021e-06 -7.009394116254947e-05
23 0.00012149190786716242 5.284992725868713e-05 -3.723276177296145e-05 5.80096276016477e-05 -0.00010231753295454968 8.0307935947162e-05 8.17438826031087e-05 0.0001334345779426864 5.889018098165326e-05 -0.00012018130328003793 0.0002484581309860141 0.00016288039493609225 0.00011244901265811549 0.00011746861615532778 -0.00010269224582323113 -2.8938497001815103e-06 -0.00010446189549782397 2.535654178916103e-05 2.691875849101419e-05 0.00019842676906787406 6.688386107242439e-05 -0.00010721685383999483 0.00025733624234428265 0.00016588096624568676 1.300566964115608e-05 0.00012113115957294943 7.193302645908871e-05 -0.00015408958175622245 6.923879406799203e-05 0.00011063154309352355 0.00016952673245858272 6.814492570632573e-05
24 0.00024134714574660962 -3.2936032912771085e-05 -5.9417856109133e-05 1.1148939832583257e-05 -0.00018671968823432585 0.00015464765345827376 3.46680037193572e-05 0.0002350273685204802 8.6040411105556e-05 -3.959967036320949e-05 0.0002840736876369321 0.00017537790860013624 0.0001368509263885027 0.00017682577282903655 -0.00015869396254132378 -0.00012510698900947362 -0.00014014439339298738 0.0005418390848798798 7.371862160453158e-05 0.0002489884131798107 -5.873038198711414e-06 -0.00012924738722312792 0.00016588096624568676 0.00036518182754718666 -2.1893649007626096e-05 0.0002435101649679188 0.00024026581599575274 -6.515119576165096e-05 8.661286112095617e-08 0.00013298860766641397 0.00012079476248470878 0.00010921682446068534
25 -4.021374516857892e-07 0.00015454250648250237 0.00010021931470375407 0.0001238007368666585 0.0002084583288779341 0.00012777831118528524 6.638751375097209e-05 5.084128519340825e-05 0.00019740820329617844 0.000241484717284843 -7.246980699819693e-05 7.082464091022753e-05 0.00010114153307317653 0.00010369805873133317 0.00023989159549365644 0.00013954099645583344 0.000130988701632163 7.890279686154714e-05 8.939377406883589e-05 3.680365865467171e-05 4.339405710507344e-05 0.0001884213283112007 1.300566964115608e-05 -2.1893649007626096e-05 0.0003080699152158738 6.0235612657546306e-05 8.792029924168664e-05 0.00016617712675282267 0.00010383032881001277 3.5527368325895466e-05 4.430074007419381e-05 4.040514909116676e-05
26 0.00017933066651777392 -6.922283752757339e-05 -1.6795693293429096e-05 0.00012375123081880752 1.9985693447100336e-05 0.0001325092040396317 4.978147551102448e-05 0.00018748545095671572 0.00016275321816156262 7.947571581158052e-05 0.0002884621362386819 0.00014558462821432337 0.00012523170837188522 0.00019681463706794835 8.397355918393466e-05 3.849410040875849e-05 4.930452999590598e-05 0.0004909526234725875 9.904832041865854e-05 0.0003158018885630815 -6.399901297163906e-05 2.428269315743898e-05 0.00012113115957294943 0.0002435101649679188 6.0235612657546306e-05 0.0005654397643596026 0.00029146851046358245 -3.3326623051803244e-05 -2.088736888098653e-05 0.00011178438482920259 0.00016395345552628414 8.90379418372676e-05
27 0.0001453028162048566 7.303742063780716e-06 -4.2138162920723545e-05 4.775920993906742e-05 -1.3595387095717753e-05 0.00013985079057838754 9.566523572399876e-05 0.00014953581623560348 0.00012211109373984629 9.514825251885755e-05 0.0001319432467234239 0.00011268092876993363 9.61292445115402e-05 0.000173979096979684 1.7304415537301155e-05 -5.113060259287931e-05 8.772147100803821e-06 0.0005776746361048063 0.0001119584063978271 0.00013589047660046266 -2.7452150063605443e-05 1.1334636767039064e-05 7.193302645908871e-05 0.00024026581599575274 8.792029924168664e-05 0.00029146851046358245 0.0003055354781229315 5.755284720145954e-05 3.918009425924195e-05 6.580751790085632e-05 6.748876269165045e-05 9.178453956883005e-05
28 -0.0001366516116612839 6.189080795110786e-05 0.00010754974458011581 8.002790171509322e-05 0.00030775248610056085 4.2969918918656447e-05 5.430180338211267e-05 -5.303450969897586e-05 0.00027481931900169164 0.0005044161586832227 -0.00017052037794566125 -8.274747133057452e-05 -5.5017886398452574e-05 -1.2574851591166166e-05 0.0003990816086308815 0.0001535348529908321 0.00022036340879907275 0.00026466464838896574 3.665815626593124e-05 1.806167578711559e-05 -2.5834465903895152e-06 0.00024572509720470714 -0.00015408958175622245 -6.515119576165096e-05 0.00016617712675282267 -3.3326623051803244e-05 5.755284720145954e-05 0.0003449731015793036 -3.505134170705418e-05 -6.585247549858028e-05 -0.0001344201855345699 -4.5984454394373906e-05
29 7.469145836292205e-05 8.803739947597197e-05 -1.1468226586676904e-05 -1.5432398784172907e-05 -5.176094420333206e-05 2.8467924359450816e-05 5.23347379425829e-05 4.222329570258302e-05 -7.937446724789783e-05 -4.13670544990112e-05 9.022564580831488e-05 7.404443617627092e-05 5.4555582424557275e-05 4.29514976330298e-05 -7.480347405319719e-05 -7.50675115924553e-06 -2.875151601029167e-05 6.791604664337031e-05 1.5323365826150475e-05 -8.760067120990321e-05 3.510393883630429e-05 -2.8394037083021488e-05 6.923879406799203e-05 8.661286112095617e-08 0.00010383032881001277 -2.088736888098653e-05 3.918009425924195e-05 -3.505134170705418e-05 0.00018334009560456066 4.898602697703454e-05 4.255517776135017e-05 4.2422286118634015e-05
30 0.0001238401911435847 1.6916360011137043e-05 -6.532181201544937e-06 3.869323492967693e-05 -9.445106632560117e-05 8.432435075675439e-05 -2.0125358983416535e-05 0.00011963262549362719 5.784309042315914e-05 -3.456117957570964e-05 0.00015550827569575266 0.00011705607997230814 7.992187065405861e-05 7.808818784745362e-05 -0.00010983097623476498 -3.9567154586000876e-05 -9.453303612595935e-05 0.00015500642163106468 2.7745300803534695e-05 0.00013637755906356402 1.5777761908271705e-05 -9.135393399205827e-05 0.00011063154309352355 0.00013298860766641397 3.5527368325895466e-05 0.00011178438482920259 6.580751790085632e-05 -6.585247549858028e-05 4.898602697703454e-05 0.0001217823947044265 0.0001021907745067146 5.2684315328596594e-05
31 0.00015752445307690223 0.00010752161343391666 9.444475695522827e-05 0.00012642937714091106 1.4146575852252118e-05 0.00014387485004928012 0.00012060237476330578 0.00013956825627060995 0.00011904793327036495 3.925441365994769e-05 0.0002721489205135106 0.00011070854071795572 0.00012684901877845422 0.00014571195648431157 4.2009448676956e-05 5.822677628601335e-05 -3.455498918294886e-05 4.223920550062787e-05 0.00014566238736309938 0.00013761763007210835 7.183850641962147e-05 1.5830421336397021e-06 0.00016952673245858272 0.00012079476248470878 4.430074007419381e-05 0.00016395345552628414 6.748876269165045e-05 -0.0001344201855345699 4.255517776135017e-05 0.0001021907745067146 0.00031153944337819885 5.7264390843588084e-05
32 9.3016738993861e-05 1.7103351871458388e-05 -4.668612348833635e-05 -4.508785446242219e-05 -9.895954031431078e-05 4.22443296490541e-05 -5.003429547483909e-05 6.926986621138339e-05 -8.151052387280696e-05 -0.00013113788623654813 8.265645857656492e-05 7.520294128280805e-05 8.042973851529379e-05 8.630734862192003e-05 -0.00012159568662124692 -7.610886659309684e-05 -6.267148763030835e-05 0.00021192592991323391 1.977660613714991e-05 1.9038968634742497e-05 -5.716076493289002e-06 -7.009394116254947e-05 6.814492570632573e-05 0.00010921682446068534 4.040514909116676e-05 8.90379418372676e-05 9.178453956883005e-05 -4.5984454394373906e-05 4.2422286118634015e-05 5.2684315328596594e-05 5.7264390843588084e-05 8.769497924250623e-05;
end;
