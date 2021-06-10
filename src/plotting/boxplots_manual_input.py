import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['CMU Serif']
from datetime import datetime
import os

scenario_name = 'scenarioA3'

# A1
labels = ['8', '16', '32', '64']
title = 'A1'
list_set_epsilons = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.069745339063699, 1.092361554481774, 1.0401612648181484, 1.024987806680736, 1.092361554481774, 1.0673737373191567, 1.0697773251747045, 1.0721887251507554, 1.0984542789970648, 1.032063813494498],
    [1.9672283318399104, 2.000208156727025, 1.5057984665883457, 1.7313780537119778, 1.7583356077077361, 1.583550495324147, 1.7515512359533156, 1.8688823793978162, 1.863895563897313, 1.6631307077366522],
    [2.0219766490363518, 2.0083955641477678, 2.050651504630772, 1.9425289723714714, 2.0143853558614717, 1.9996298119483003, 2.0348651357355068, 1.907129840169096, 1.9210138346236325, 2.034906949518788]
]

# A2B3N32B0.2
# labels = ['lessDmoreS', 'mediumDmediumS', 'moreDlessS']
# title = 'A2B3N32B0.2'
# list_set_epsilons = [
#     [1.3499979263151332, 1.4052383661831214, 1.3767810617925065, 1.2246383166488921, 1.305776027695795, 1.3084124650329483, 1.132134976118413, 1.2910842615206186, 1.3067941249864734, 1.2876399869178907],
#     [1.2995504139539467, 1.404756216444296, 1.2508234046861144, 1.2726522028350036, 1.3711890363293475, 1.4745478053134664, 1.400490306063234, 1.297083582690216, 1.2758397745108707, 1.3959217933866106],
#     [1.190339028084757, 1.1777285234088037, 1.3251138101252673, 1.239663511129278, 1.3387415243139376, 1.5842374530495735, 1.3688516255800733, 1.379150152956782, 1.340757194685381, 1.2198027127569138]
#     ]

# A2B3N32B0.5
# labels = ['lessDmoreS', 'mediumDmediumS', 'moreDlessS']
# title = 'A2B3N32B0.5'
# list_set_epsilons = [
#     [1.3223924568287806, 1.2687432067032371, 1.220955076787497, 1.254966363250258, 1.2938492909112813, 1.3256707583772473, 1.2040490053282122, 1.1819631969153142, 1.3282177152185588, 1.2887856515113894],
#     [1.2019484617437721, 1.2624076702069662, 1.1803388633948861, 1.2035769093379443, 1.2273742495494546, 1.1501530862431293, 1.2224423858280125, 1.2143619613673462, 1.2553964940050566, 1.2193490137433176],
#     [1.2443007122010312, 1.196461316049709, 1.2400360986124226, 1.1842034194065967, 1.2859427569109037, 1.3400791236063267, 1.3139169442373335, 1.2249150091725682, 1.2445937643135445, 1.259655318329354]
#     ]

# A2B3N32B0.8
# labels = ['lessDmoreS', 'mediumDmediumS', 'moreDlessS']
# title = 'A2B3N32B0.8'
# list_set_epsilons = [
#     [11.64880622819096, 3.218488975672744, 4.19978909323371, 2.4222216462067827, 1.3945702864495817, 1.3938204360664423, 2.96026521135779, 1.3291389438470973, 3.132559987296749, 1.23512476930302],
#     [1.556664032973834, 1.3663118105123084, 1.5586430764381378, 1.680835551796745, 1.5913162723285534, 1.501892745376455, 1.3087531667410865, 1.449283674627408, 1.4847002599501813, 1.2183353846734502],
#     [1.4042623555013878, 1.762925100716513, 5.616428969987258, 1.4656917356032806, 1.154926574216331, 1.3776272084021526, 1.2252770713096917, 1.2846944076373747, 4.7196783391463715, 1.144661538942052]]

# A2B3N64B0.2
# labels = ['lessDmoreS', 'mediumDmediumS', 'moreDlessS']
# title = 'A2B3N64B0.2'
# list_set_epsilons = [
#     [6.2822047738081395, 1.8638804611036361, 1.9047437553733515, 2.422472141548823, 2.2032959794790696, 1.6386958153297015, 3.063416583984287, 2.625420696002434, 1.7552233893401767, 2.60671559850603],
#     [1.5575930523578907, 2.0030329838314995, 3.1676934778763344, 2.9871419348114188, 2.7198452481964237, 3.0346991000143655, 2.778619963862992, 2.219290022394909, 2.0002451717105925, 2.6288289803010523],
#     [3.095781529782441, 2.6553700990395632, 2.361810872572806, 1.9441985959597363, 3.3874699973609315, 2.581202380730777, 1.7481341700460693, 2.9323582591612896, 2.131735008717141, 3.9206302398077018]
#     ]

# A2B3N64B0.5
# labels = ['lessDmoreS', 'mediumDmediumS', 'moreDlessS']
# title = 'A2B3N64B0.5'
# list_set_epsilons = [
#     [1.5047783802519876, 1.5424474973680935, 1.5397188105542317, 1.4446165311565198, 1.4851902111804731, 1.6006473186665091, 1.5837164068658742, 1.4911725746520827, 1.5194618121989951, 1.589209303793632],
#     [1.4858362812934982, 1.4889654752248092, 1.504781330353911, 1.4098188899588118, 1.4602483148388254, 1.481326947321431, 1.5172997720691475, 1.5515222397966384, 1.522140684961688, 1.5918113131308156],
#     [1.5801374259874152, 1.528434198773743, 1.618441431572883, 1.3962855707332278, 1.5321040040763054, 1.5452556642464619, 1.5196346291550682, 1.5973291501536233, 1.5846994430061343, 1.519257982440362]
#     ]

# A2B3N64B0.8
# labels = ['lessDmoreS', 'mediumDmediumS', 'moreDlessS']
# title = 'A2B3N64B0.8'
# list_set_epsilons = [
#     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
#     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
#     [float('inf'), float('inf'), float('inf'), 1.9884989104451705, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
#     ]

# A2B3N32lessDmoreS
# labels = ['0.2', '0.5', '0.8']
# title = 'A2B3N32lessDmoreS'
# list_set_epsilons = [
#     [1.3499979263151332, 1.4052383661831214, 1.3767810617925065, 1.2246383166488921, 1.305776027695795, 1.3084124650329483, 1.132134976118413, 1.2910842615206186, 1.3067941249864734, 1.2876399869178907],
#     [1.3223924568287806, 1.2687432067032371, 1.220955076787497, 1.254966363250258, 1.2938492909112813, 1.3256707583772473, 1.2040490053282122, 1.1819631969153142, 1.3282177152185588, 1.2887856515113894],
#     [11.64880622819096, 3.218488975672744, 4.19978909323371, 2.4222216462067827, 1.3945702864495817, 1.3938204360664423, 2.96026521135779, 1.3291389438470973, 3.132559987296749, 1.23512476930302]
#     ]

# A2B3N32mediumDmediumS
# labels = ['0.2', '0.5', '0.8']
# title = 'A2B3N32mediumDmediumS'
# list_set_epsilons = [
#     [1.2995504139539467, 1.404756216444296, 1.2508234046861144, 1.2726522028350036, 1.3711890363293475, 1.4745478053134664, 1.400490306063234, 1.297083582690216, 1.2758397745108707, 1.3959217933866106],
#     [1.2019484617437721, 1.2624076702069662, 1.1803388633948861, 1.2035769093379443, 1.2273742495494546, 1.1501530862431293, 1.2224423858280125, 1.2143619613673462, 1.2553964940050566, 1.2193490137433176],
#     [1.556664032973834, 1.3663118105123084, 1.5586430764381378, 1.680835551796745, 1.5913162723285534, 1.501892745376455, 1.3087531667410865, 1.449283674627408, 1.4847002599501813, 1.2183353846734502]
#     ]

# A2B3N32moreDlessS
# labels = ['0.2', '0.5', '0.8']
# title = 'A2B3N32moreDlessS'
# list_set_epsilons = [
#     [1.190339028084757, 1.1777285234088037, 1.3251138101252673, 1.239663511129278, 1.3387415243139376, 1.5842374530495735, 1.3688516255800733, 1.379150152956782, 1.340757194685381, 1.2198027127569138],
#     [1.2443007122010312, 1.196461316049709, 1.2400360986124226, 1.1842034194065967, 1.2859427569109037, 1.3400791236063267, 1.3139169442373335, 1.2249150091725682, 1.2445937643135445, 1.259655318329354],
#     [1.4042623555013878, 1.762925100716513, 5.616428969987258, 1.4656917356032806, 1.154926574216331, 1.3776272084021526, 1.2252770713096917, 1.2846944076373747, 4.7196783391463715, 1.144661538942052]
#     ]

# A2B3N64lessDmoreS
# labels = ['0.2', '0.5', '0.8']
# title = 'A2B3N64lessDmoreS'
# list_set_epsilons = [
#     [6.2822047738081395, 1.8638804611036361, 1.9047437553733515, 2.422472141548823, 2.2032959794790696, 1.6386958153297015, 3.063416583984287, 2.625420696002434, 1.7552233893401767, 2.60671559850603],
#     [1.5047783802519876, 1.5424474973680935, 1.5397188105542317, 1.4446165311565198, 1.4851902111804731, 1.6006473186665091, 1.5837164068658742, 1.4911725746520827, 1.5194618121989951, 1.589209303793632],
#     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
#     ]

# A2B3N64mediumDmediumS
# labels = ['0.2', '0.5', '0.8']
# title = 'A2B3N64mediumDmediumS'
# list_set_epsilons = [
#     [1.5575930523578907, 2.0030329838314995, 3.1676934778763344, 2.9871419348114188, 2.7198452481964237, 3.0346991000143655, 2.778619963862992, 2.219290022394909, 2.0002451717105925, 2.6288289803010523],
#     [1.4858362812934982, 1.4889654752248092, 1.504781330353911, 1.4098188899588118, 1.4602483148388254, 1.481326947321431, 1.5172997720691475, 1.5515222397966384, 1.522140684961688, 1.5918113131308156],
#     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
#     ]

# A2B3N64moreDlessS
# labels = ['0.2', '0.5', '0.8']
# title = 'A2B3N64moreDlessS'
# list_set_epsilons = [
#     [3.095781529782441, 2.6553700990395632, 2.361810872572806, 1.9441985959597363, 3.3874699973609315, 2.581202380730777, 1.7481341700460693, 2.9323582591612896, 2.131735008717141, 3.9206302398077018],
#     [1.5801374259874152, 1.528434198773743, 1.618441431572883, 1.3962855707332278, 1.5321040040763054, 1.5452556642464619, 1.5196346291550682, 1.5973291501536233, 1.5846994430061343, 1.519257982440362],
#     [float('inf'), float('inf'), float('inf'), 1.9884989104451705, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
#     ]

# B2N16
# labels = ['default', 'clique', 'layout']
# title = 'B2N16'
# list_set_epsilons = [
#     [1.0568713785067598, 1.0393077920791243, 1.0717989664330105, 1.0174972218859963, 1.0984542789970648, 1.0995747506079512, 1.076422956935955, 1.0697773251747045, 1.0721887251507554, 1.0617306209896549],
#     [1.092361554481774, 1.092361554481774, 1.1550046370248923, 1.1263482082890073, 1.092361554481774, 1.0984880050061543, 1.069745339063699, 1.069745339063699, 1.0995747506079512, 1.0995747506079512],
#     [1.069745339063699, 1.0717989664330105, 1.0617306209896549, 1.092361554481774, 1.1263482082890073, 1.069745339063699, 1.069745339063699, 1.0697773251747045, 1.092361554481774, 1.0697773251747045]
#     ]

# B2N32
# labels = ['default', 'clique', 'layout']
# title = 'B2N32'
# list_set_epsilons = [
#     [1.1648830986803027, 1.274607461666451, 1.2746124354082478, 1.2901197218104328, 1.251599560259116, 1.2966670118398864, 1.2903095087971328, 1.3777056814792898, 1.222093089331546, 1.2902120762068712],
#     [1.3164838774831533, 1.3204491225105135, 1.3812107507228906, 1.3163825613411466, 1.253686482337723, 1.2803191079140395, 1.2971555390423612, 1.2634572690874404, 1.419810219406164, 1.4388482257124797],
#     [1.250487660661036, 1.3262523046942487, 1.3013875124919834, 1.2479030749457698, 1.275322497071187, 1.1807935842935766, 1.22685897368455, 1.2190974889561597, 1.4201631396046004, 1.2793441303424395]
#     ]

# B2N64
# labels = ['default', 'clique', 'layout']
# title = 'B2N64'
# list_set_epsilons = [
#     [1.59319592598288, 1.5475698605999058, 1.5676345089256754, 1.4870048002959697, 1.3348663638196163, 1.5204390528232812, 1.537824821724261, 1.4244844927545859, 1.5400031976660937, 1.4124097728107203],
#     [1.5463019291059412, 1.5097302754928548, 1.427913587624222, 1.576689006928445, 1.517809459126627, 1.4481040496827902, 1.4918742091579653, 1.6171187430696579, 1.5388614382659418, 1.601552508853652],
#     [1.453708008958359, 1.3892770097800016, 1.4641989171658787, 1.4721139985246516, 1.4594746118799953, 1.5256476711642588, 1.5097507810625204, 1.5354449972668835, 1.3093249020285496, 1.5449070742850397]
#     ]

# B4N16
# labels = ['default', 'long', 'pause', 'quench']
# title = 'B4N16'
# list_set_epsilons = [
#     [1.092361554481774, 1.0174972218859963, 1.092361554481774, 1.0717989664330105, 1.0984542789970648, 1.1024229279374809, 1.069745339063699, 1.1263482082890073, 1.0, 1.069745339063699],
#     [1.0745464054191984, 1.0, 1.0697773251747045, 1.1024229279374809, 1.0717989664330105, 1.100811836367349, 1.092361554481774, 1.0995747506079512, 1.092361554481774, 1.0566486241847508],
#     [1.0617306209896549, 1.0721887251507554, 1.0070189250799315, 1.069745339063699, 1.0743999075141863, 1.092361554481774, 1.0984880050061543, 1.092361554481774, 1.0697773251747045, 1.0984542789970648],
#     [1.069745339063699, 1.092361554481774, 1.0995747506079512, 1.135479930116604, 1.069745339063699, 1.0697773251747045, 1.069745339063699, 1.0995747506079512, 1.092361554481774, 1.0984542789970648]
#     ]

# B4N32
# labels = ['default', 'long', 'pause', 'quench']
# title = 'B4N32'
# list_set_epsilons = [
#     [1.3517850518147483, 1.2351620051331451, 1.2419806167336755, 1.253449932867132, 1.2972976373744176, 1.2010223096471366, 1.3379527477527187, 1.1526497228445969, 1.3131195168854548, 1.2883396222450554],
#     [1.2773084389374618, 1.2685859412167662, 1.282440675632727, 1.2993723060342706, 1.2698253194462126, 1.2047029430996907, 1.2393684119584454, 1.2075308260897635, 1.2298278821145505, 1.3908615817709569],
#     [1.2235341061967722, 1.226120904434251, 1.2279227738062093, 1.1846873126415314, 1.2562894271342242, 1.3240568135082378, 1.293774410299287, 1.2744502298042917, 1.2786287143344317, 1.3288088026162883],
#     [1.2811447849206972, 1.3075712381393696, 1.3033753143749904, 1.2859913292662528, 1.3053195063580334, 1.2538988070385046, 1.3230107185848823, 1.2727247959766292, 1.2255688962641433, 1.2668091494859914]
#     ]

# B4N64
# labels = ['default', 'long', 'pause', 'quench']
# title = 'B4N64'
# list_set_epsilons = [
#     [1.5172127715152381, 1.4650921665719863, 1.578786888567411, 1.5375728717289225, 1.4263595347128148, 1.4419254705861224, 1.403621202857771, 1.4945997714148278, 1.3795272469199982, 1.4925379966852075],
#     [1.478730296108486, 1.3949736950202156, 1.5101094100342656, 1.4832660350964741, 1.5477821575078923, 1.4492128589588629, 1.4908634396896399, 1.4578976423659322, 1.4145406018256872, 1.4807595033726906],
#     [1.4376387082399167, 1.5470916940262103, 1.5018400284840752, 1.4852721388950165, 1.5165228682120504, 1.4784011759331945, 1.5059733828686297, 1.490752688638682, 1.4683297544762237, 1.5252631643163925],
#     [1.4690634250105148, 1.3928715064121016, 1.4791407298039705, 1.3740265914395953, 1.4686016146384933, 1.361015832280519, 1.3334789168583425, 1.450581174749839, 1.4859500686376994, 1.4853328806921704]
#     ]

# A3N16
# labels = ['diversified', 'correlated', 'industry_diversified', 'industry_correlated']
# title = 'A3N16'
# list_set_epsilons = [
#     [1.0252990521071133, 1.0, 1.0252990521071133, 1.0398904698739035, 1.0252990521071133, 1.0, 1.044078926786686, 1.0, 1.0252990521071133, 1.0],
#     [1.0184926535860195, 1.0138186993022122, 1.0183204025272334, 1.0146279197185049, 1.0099975432282287, 1.0116525232431057, 1.0131428285948059, 1.0209184382692877, 1.0108127936689362, 1.0229865243638439],
#     [1.024987806680736, 1.0717989664330105, 1.0, 1.0, 1.0617306209896549, 1.0717989664330105, 1.1187067404228423, 1.0617306209896549, 1.0568713785067598, 1.0995747506079512],
#     [1.0807158822709637, 1.0628970589064997, 1.0355813783849832, 1.0017552368401965, 1.0628970589064997, 1.0628970589064997, 1.0807158822709637, 1.0628970589064997, 1.1010632114409609, 1.0864442097157865]
#     ]

# A3N32
# labels = ['diversified', 'correlated', 'industry_diversified', 'industry_correlated']
# title = 'A3N32'
# list_set_epsilons = [
#     [1.2742794349447089, 1.2884689100696118, 1.2773672514016263, 1.2753373162832464, 1.2330931799174467, 1.2796396380232535, 1.2166893951238382, 1.212711791220173, 1.1795924280178165, 1.2663753671790334],
#     [1.1022627340052333, 1.1040043866764444, 1.107290257993464, 1.1095633593648768, 1.1030412770134137, 1.079307231420843, 1.0887219540762665, 1.1108069626397188, 1.0850448168079752, 1.1034182745023535],
#     [1.3211551275053297, 1.3375576459869927, 1.3547221236814633, 1.273461244430681, 1.3830779041288135, 1.3043527411881481, 1.3276152141861295, 1.325934861500814, 1.260888231927054, 1.2569944259788486],
#     [1.3999197317543246, 1.3725234793287475, 1.3100230533839459, 1.268457109826973, 1.317538884521333, 1.4232197588990068, 1.267293530521767, 1.544633488006858, 1.4009284319753958, 1.3420678679554765]
#     ]

# A3N64
# labels = ['diversified', 'correlated', 'industry_diversified', 'industry_correlated']
# title = 'A3N64'
# list_set_epsilons = [
#     [1.5896707140453368, 1.692115874229774, 1.5797159691954805, 1.544775608544733, 1.6306603596458091, 1.4931610333677243, 1.482970767797879, 1.5659992029242256, 1.4697099089637102, 1.6240157684697236],
#     [1.1543709462719736, 1.1808555712929112, 1.1965189175682915, 1.2054586123321147, 1.1451164825300342, 1.1596348091861888, 1.1806645396154591, 1.1340653715120215, 1.1749899569337423, 1.1649997731351296],
#     [1.480961077552874, 1.439785049594824, 1.49521532395618, 1.4271771706844985, 1.4703703494825286, 1.4632080571787447, 1.4721727955026187, 1.5664902809960106, 1.5195807860850508, 1.443112731331886],
#     [1.712487317392762, 1.8350719836858504, 1.8867041380744307, 1.6599045066687057, 1.8170283525044424, 1.6158099698537383, 1.8063585809979532, 1.772285044123278, 1.892957682435774, 1.8983968042954449]
#     ]

# B5N8
# labels = ['Pegasus', 'Chimera']
# title = 'B5N8'
# list_set_epsilons = [
#     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
#     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#     ]

# B5N16
# labels = ['Pegasus', 'Chimera']
# title = 'B5N16'
# list_set_epsilons = [
#     [1.069745339063699, 1.058972091907241, 1.0568713785067598, 1.0457946233055313, 1.092361554481774, 1.1021014347352187, 1.069745339063699, 1.100811836367349, 1.0743999075141863, 1.069745339063699],
#     [1.0984542789970648, 1.092361554481774, 1.129929803310457, 1.092361554481774, 1.0984542789970648, 1.0984880050061543, 1.0984880050061543, 1.0568713785067598, 1.100811836367349, 1.129929803310457]
#     ]

# B5N32
# labels = ['Pegasus', 'Chimera']
# title = 'B5N32'
# list_set_epsilons = [
#     [1.2851101191209349, 1.1700255332799216, 1.3411442493278372, 1.284471106279312, 1.2492237847194403, 1.2014593617831402, 1.1909883692297452, 1.2756655373153891, 1.2601553919718655, 1.2291356718165953],
#     [1.3254404151162924, 1.2669876639143147, 1.357630375379645, 1.3263453714191362, 1.2659731560125795, 1.3749176679661628, 1.2486672435065347, 1.3774269123039369, 1.2389962416351232, 1.3608293029818523]
#     ]

# B5N64
# labels = ['Pegasus', 'Chimera']
# title = 'B5N64'
# list_set_epsilons = [
#     [1.608612141506866, 1.5582521132573601, 1.6412515681828963, 1.5353913265287034, 1.59049440852764, 1.5410829979560219, 1.6271800009255297, 1.4488658522113367, 1.4867540245815873, 1.499736164674981],
#     [1.5248641235660008, 1.452756789976252, 1.501390261971793, 1.5498291907630495, 1.436759456506447, 1.4654370420439464, 1.5509652018290958, 1.5355213042360858, 1.4405828403131256, 1.4724404549331098]
#     ]

# 2 columns, 9 per 6 inches figure
fig, ax1 = plt.subplots(figsize=(4, 4))
ax1.boxplot(list_set_epsilons, notch=True, labels=labels)

# Tidy up the figure
(ax1_bottom, ax1_top) = ax1.get_ylim()

ax1.grid(True)
# ax1.set_title(title)
ax1.set_ylim(1, ax1_top)
ax1.set_ylabel('Epsilon Indicator')
ax1.set_xlabel('Universe Size')


# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

folder_name = 'boxplots_manual_input'

# Check if folder exists and creates if not
if not os.path.exists('images/' + folder_name):
    os.makedirs('images/' + folder_name)

# fig.text(0.5, 0.005, 'How to interpret: The epsilon indicator is the minimum factor by which the annealer set has to be multiplied in the objective so as to weakly dominate the classical set.\nHence, the closer to 1 is the epsilon indicator, the better the annealer set.',
#          ha='center', size='xx-small')

output_name = f'{scenario_name}{date}'
# fig.suptitle('Boxplots - ' + output_name)

# Save as 2 1 6 0p image
plt.savefig(
    f'images/{folder_name}/{output_name}.pdf', dpi=360)
plt.show()
