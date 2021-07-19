import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import scikit_posthocs as sp

# S1
# labels = ['8', '16', '32', '64']
# title = 'S1'
# list_set_epsilons = [
#     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
#     [1.0629485594831503, 1.0923615544817737, 1.028943213531982, 1.0180817613156488, 1.0629485594831503, 1.0482023127639382, 1.0629485594831503, 1.0721887251507554, 1.0984542789970648, 1.0231579407518554],
#     [1.9672283318399109, 2.0002081567270245, 1.5057984665883457, 1.7313780537119778, 1.7583356077077361, 1.583550495324147, 1.7515512359533152, 1.868882379397816, 1.863895563897313, 1.6631307077366522],
#     [2.021976649036352, 2.008395564147768, 2.050651504630773, 1.942528972371472, 2.0143853558614717, 1.9996298119483005, 2.0348651357355068, 1.9071298401690961, 1.9210138346236332, 2.034906949518788]
# ]

# S3N16
# labels = ['1000 $\\times$ |directions|', '15000']
# title = 'S3N16'
# list_set_epsilons = [
#     [1.115346226262037, 1.0976885846407207, 1.1338825419641678, 1.10098951378513, 1.1526659530608883, 1.1263482082890075, 1.1263482082890075, 1.0717086909513749, 1.1263127498737597, 1.133918478610877],
#     [1.050306607555603, 1.0717086909513749, 1.078642972376386, 1.1024229279374806, 1.1137820992060656, 1.078642972376386, 1.05128426385391, 1.1263127498737597, 1.0957846400736082, 1.0697453390636988]
#     ]

# S3N32
# labels = ['1000 $\\times$ |directions|', '15000']
# title = 'S3N32'
# list_set_epsilons = [
#     [1.249906129579693, 1.3495624087686078, 1.2522750616411138, 1.3508130597113208, 1.2992162005757446, 1.321292006518581, 1.2509829143514453, 1.209022726220185, 1.4380596599578508, 1.269298582294037],
#     [1.2279835151895546, 1.2803781729412032, 1.239198347017118, 1.2526071891137016, 1.2776522997601503, 1.132631316498451, 1.2480196302767232, 1.1826304951220747, 1.1858830054545102, 1.2981227328890228]
#     ]

# S3N64
# labels = ['1000 $\\times$ |directions|', '15000']
# title = 'S3N64'
# list_set_epsilons = [
#     [1.5258955507796164, 1.4851753489907469, 1.5363441111928835, 1.4501267073439699, 1.6737423960970934, 1.4915379820168673, 1.638673354144739, 1.5360592595479707, 1.4566925671442394, 1.4730056937178895],
#     [1.4902995240915766, 1.5139109644708177, 1.6091374333500401, 1.6062090958097235, 1.5651248696491584, 1.4388694508088091, 1.5730012367944612, 1.5522292625827643, 1.5292050511867405, 1.6151815644907437]
#     ]

# S4N32
# labels = ['minimal set', '6', '15', '30']
# title = 'S4N32'
# xlabel = 'Directions'
# list_set_epsilons = [
#     [1.2279835151895546, 1.2803781729412032, 1.239198347017118, 1.2526071891137016, 1.2776522997601503, 1.132631316498451, 1.2480196302767232, 1.1826304951220747, 1.1858830054545102, 1.2981227328890228],
#     [1.3223924568287804, 1.2687432067032371, 1.220955076787497, 1.254966363250258, 1.293849290911281, 1.3256707583772473, 1.1935112678414648, 1.1686450188908628, 1.3282177152185588, 1.2887856515113894],
#     [1.2019484617437721, 1.2624076702069662, 1.1803388633948861, 1.1888649286139934, 1.2273742495494546, 1.1395473681360064, 1.2224423858280125, 1.2143619613673462, 1.2553964940050566, 1.2193490137433176],
#     [1.2443007122010312, 1.196461316049709, 1.2400360986124226, 1.1842034194065967, 1.2859427569109037, 1.3400791236063267, 1.3139169442373335, 1.2249150091725682, 1.2445937643135443, 1.259655318329354]
#     ]

# S4N64
# labels = ['minimal set', '6', '15', '30']
# title = 'S4N64'
# xlabel = 'Directions'
# list_set_epsilons = [
#     [1.4902995240915766, 1.5139109644708177, 1.6091374333500401, 1.6062090958097235, 1.5651248696491584, 1.4388694508088091, 1.5730012367944612, 1.5522292625827643, 1.5292050511867405, 1.6151815644907437],
#     [1.5047783802519878, 1.5424474973680935, 1.5397188105542317, 1.44461653115652, 1.485190211180473, 1.6006473186665093, 1.5588026478870995, 1.491172574652083, 1.5194618121989956, 1.5892093037936321],
#     [1.4858362812934984, 1.4889654752248094, 1.5047813303539113, 1.4098188899588122, 1.4602483148388257, 1.4813269473214312, 1.5172997720691477, 1.5515222397966386, 1.5221406849616883, 1.591811313130816],
#     [1.5801374259874155, 1.5284341987737433, 1.6184414315728834, 1.3944405492660419, 1.5321040040763056, 1.545255664246462, 1.5196346291550684, 1.5973291501536235, 1.5846994430061345, 1.4811888599881178]
#     ]

# S5N32
# labels = ['0.2', '0.5', '0.8']
# title = 'S5N32'
# xlabel = 'Budget size as a ratio of N'
# list_set_epsilons = [
#     [1.2995504139539467, 1.4047562164442957, 1.2508234046861142, 1.2726522028350036, 1.3711890363293475, 1.4745478053134662, 1.4004903060632339, 1.2970835826902156, 1.2758397745108707, 1.3959217933866106],
#     [1.2019484617437721, 1.2624076702069662, 1.1803388633948861, 1.1888649286139934, 1.2273742495494546, 1.1395473681360064, 1.2224423858280125, 1.2143619613673462, 1.2553964940050566, 1.2193490137433176],
#     [1.556664032973834, 1.3663118105123084, 1.6692207493652609, 1.1489170120126047, 1.5913162723285534, 1.522342985279589, 1.3680345449029585, 1.4783493754100259, 1.4847002599501815, 1.4220223169471704],
#     ]

# S5N64 - Note: 0.8 removed because of not having any result
# labels = ['0.2', '0.5']
# title = 'S5N64'
# xlabel = 'Budget size as a ratio of N'
# list_set_epsilons = [
#     [1.5575930523578907, 2.0030329838314995, 3.167693477876335, 2.9871419348114188, 2.719845248196423, 3.0346991000143655, 2.778619963862992, 2.219290022394909, 2.0002451717105925, 2.6288289803010523],
#     [1.4858362812934984, 1.4889654752248094, 1.5047813303539113, 1.4098188899588122, 1.4602483148388257, 1.4813269473214312, 1.5172997720691477, 1.5515222397966386, 1.5221406849616883, 1.591811313130816]
#     ]

# S6N16
# labels = ['general', 'clique', 'layout']
# title = 'S6N16'
# xlabel = 'Embedding'
# list_set_epsilons = [
#     [1.0404363454609564, 1.0283898707248533, 1.05128426385391, 1.0119569658170224, 1.0629485594831503, 1.084077285625739, 1.05128426385391, 1.0697773251747045, 1.0721887251507554, 1.061730620989655],
#     [1.0923615544817737, 1.0629485594831503, 1.1549673514293395, 1.1263482082890075, 1.0923615544817737, 1.0984880050061543, 1.0697453390636988, 1.0697453390636988, 1.099574750607951, 1.099574750607951],
#     [1.0629485594831503, 1.0629485594831503, 1.05128426385391, 1.0923615544817737, 1.1263482082890075, 1.0697453390636988, 1.0697453390636988, 1.0697773251747045, 1.0629485594831503, 1.0697773251747045]
#     ]

# S6N32
# labels = ['general', 'clique', 'layout']
# title = 'S6N32'
# xlabel = 'Embedding'
# list_set_epsilons = [
#     [1.1648830986803027, 1.2746074616664507, 1.2586096749756641, 1.275287647430814, 1.2515995602591157, 1.2966670118398864, 1.2903095087971328, 1.3777056814792898, 1.222093089331546, 1.2902120762068712],
#     [1.3164838774831533, 1.3204491225105133, 1.3812107507228903, 1.3163825613411466, 1.253686482337723, 1.2803191079140395, 1.2971555390423615, 1.2634572690874404, 1.419810219406164, 1.4388482257124795],
#     [1.250487660661036, 1.3262523046942485, 1.3013875124919834, 1.2479030749457698, 1.275322497071187, 1.1569673236003652, 1.2268589736845505, 1.2190974889561597, 1.4201631396046004, 1.2793441303424395]
#     ]

# S6N64
# labels = ['general', 'clique', 'layout']
# title = 'S6N64'
# xlabel = 'Embedding'
# list_set_epsilons = [
#     [1.5931959259828803, 1.547569860599906, 1.5676345089256756, 1.48700480029597, 1.3348663638196165, 1.5204390528232814, 1.537824821724261, 1.424484492754586, 1.540003197666094, 1.4124097728107206],
#     [1.5463019291059414, 1.509730275492855, 1.4279135876242224, 1.5766890069284454, 1.5178094591266271, 1.4481040496827904, 1.4918742091579658, 1.617118743069658, 1.538861438265942, 1.6015525088536522],
#     [1.4537080089583592, 1.3892770097800018, 1.4641989171658791, 1.4721139985246519, 1.4594746118799955, 1.525647671164259, 1.5097507810625206, 1.535444997266884, 1.3093249020285498, 1.5449070742850397]
#     ]

# S7N16
# labels = ['standard', 'long', 'pause', 'quench']
# title = 'S7N16'
# xlabel = 'Anneal schedule'
# list_set_epsilons = [
#     [1.0923615544817737, 1.0119569658170224, 1.0923615544817737, 1.0629485594831503, 1.0984542789970648, 1.1024229279374806, 1.0697453390636988, 1.1263482082890075, 1.0, 1.0697453390636988],
#     [1.0647482646071107, 1.0, 1.0697773251747045, 1.1024229279374806, 1.0697453390636988, 1.0629485594831503, 1.0923615544817737, 1.099574750607951, 1.0923615544817737, 1.0382456431431355],
#     [1.0544341068371788, 1.0629485594831503, 1.0051135115749124, 1.0629485594831503, 1.0597442705745803, 1.0923615544817737, 1.0984880050061543, 1.0923615544817737, 1.0697773251747045, 1.0984542789970648],
#     [1.0697453390636988, 1.0629485594831503, 1.099574750607951, 1.0955765438881906, 1.0629485594831503, 1.0697773251747045, 1.0697453390636988, 1.099574750607951, 1.0923615544817737, 1.0984542789970648]
#     ]

# S7N32
# labels = ['standard', 'long', 'pause', 'quench']
# title = 'S7N32'
# xlabel = 'Anneal schedule'
# list_set_epsilons = [
#     [1.3517850518147478, 1.235162005133145, 1.2419806167336758, 1.2534499328671318, 1.2972976373744176, 1.2010223096471366, 1.3379527477527187, 1.1526497228445969, 1.3131195168854548, 1.2883396222450554],
#     [1.2773084389374618, 1.2685859412167662, 1.282440675632727, 1.2815781351997102, 1.2698253194462128, 1.2047029430996905, 1.2393684119584452, 1.2075308260897635, 1.2029245261943176, 1.3908615817709566],
#     [1.2235341061967722, 1.226120904434251, 1.221098656380994, 1.1846873126415314, 1.2562894271342242, 1.3240568135082378, 1.293774410299287, 1.2744502298042917, 1.2786287143344317, 1.3288088026162883],
#     [1.2811447849206972, 1.3075712381393696, 1.3033753143749904, 1.2859913292662528, 1.3053195063580334, 1.2538988070385046, 1.3230107185848823, 1.272724795976629, 1.2255688962641433, 1.2668091494859914]
#     ]

# S7N64
# labels = ['standard', 'long', 'pause', 'quench']
# title = 'S7N64'
# xlabel = 'Anneal schedule'
# list_set_epsilons = [
#     [1.5172127715152384, 1.4650921665719865, 1.5787868885674112, 1.5375728717289228, 1.4263595347128148, 1.4321437809693391, 1.4036212028577713, 1.494599771414828, 1.379527246919998, 1.4925379966852077],
#     [1.4787302961084863, 1.3949736950202158, 1.5101094100342658, 1.4832660350964741, 1.5477821575078925, 1.4492128589588633, 1.4908634396896399, 1.4578976423659327, 1.4145406018256874, 1.4807595033726906],
#     [1.437638708239917, 1.5470916940262103, 1.5018400284840754, 1.4702696693013044, 1.5165228682120506, 1.4784011759331945, 1.50597338286863, 1.4907526886386822, 1.468329754476224, 1.5252631643163927],
#     [1.469063425010515, 1.3928715064121018, 1.4791407298039707, 1.3740265914395955, 1.4686016146384935, 1.3610158322805193, 1.3334789168583427, 1.4505811747498392, 1.4859500686376994, 1.4853328806921708]
#     ]


# S8N16
# labels = ['diversified', 'correlated', 'industry\ndiversified', 'industry\ncorrelated']
# title = 'S8N16'
# xlabel = 'Anneal schedule'
# list_set_epsilons = [
#     [1.044078926786686, 1.041416582016792, 1.044078926786686, 1.0657949785006744, 1.0592137120160172, 1.0469085450368754, 1.044078926786686, 1.0389745321155137, 1.0596923282895578, 1.05749590934194],
#     [1.0291722045955074, 1.0322752735121847, 1.0209184382692877, 1.028849769220871, 1.0133911069057577, 1.0271384560083836, 1.0306693861114955, 1.0306693861114955, 1.0228086135201593, 1.0302079966084552],
#     [1.0180817613156485, 1.05128426385391, 1.0, 1.0, 1.05128426385391, 1.0544341068371783, 1.078642972376386, 1.0617306209896549, 1.0404363454609564, 1.0995747506079512],
#     [1.0628970589064997, 1.0628970589064997, 1.0142556439244375, 1.0007172761192669, 1.0628970589064997, 1.0628970589064997, 1.0306256443837767, 1.0628970589064997, 1.0379030770398543, 1.0326915823639555]
#     ]

# S8N32
# labels = ['diversified', 'correlated', 'industry\ndiversified', 'industry\ncorrelated']
# title = 'S8N32'
# xlabel = 'Anneal schedule'
# list_set_epsilons = [
#     [1.19273182803684, 1.1743255030311621, 1.1918808382633905, 1.1851044655855745, 1.1446397643960284, 1.1974642071208985, 1.1350510133665708, 1.1830630391823211, 1.1795924280178165, 1.1634143885742592],
#     [1.1645663002085818, 1.1543976051828826, 1.1659505442792977, 1.163789618432745, 1.165890556774585, 1.1192509514635458, 1.1417151549487292, 1.1357388082012554, 1.1213650610744095, 1.1287009142931657],
#     [1.3211551275053297, 1.3375576459869927, 1.3547221236814633, 1.273461244430681, 1.3830779041288135, 1.3043527411881481, 1.3276152141861295, 1.325934861500814, 1.260888231927054, 1.2405811712688435],
#     [1.3999197317543246, 1.3725234793287475, 1.3100230533839459, 1.268457109826973, 1.317538884521333, 1.4232197588990068, 1.267293530521767, 1.544633488006858, 1.4009284319753958, 1.3420678679554765]
#     ]

# S8N64
# labels = ['diversified', 'correlated', 'industry\ndiversified', 'industry\ncorrelated']
# title = 'S8N64'
# xlabel = 'Anneal schedule'
# list_set_epsilons = [
#     [1.5896707140453368, 1.692115874229774, 1.5797159691954805, 1.544775608544733, 1.6306603596458091, 1.4931610333677243, 1.482970767797879, 1.5659992029242256, 1.4697099089637102, 1.6240157684697236],
#     [1.2340291263107832, 1.2774651904082464, 1.3036471195671726, 1.3187583705215216, 1.219092837010016, 1.2425800305337429, 1.2771481630316672, 1.201417277842347, 1.2677558086925917, 1.251336773935054],
#     [1.4750953804904727, 1.439785049594824, 1.49521532395618, 1.4133384596886653, 1.454697934837426, 1.4632080571787447, 1.4721727955026187, 1.5664902809960106, 1.5195807860850508, 1.443112731331886],
#     [1.712487317392762, 1.8350719836858504, 1.8867041380744307, 1.6599045066687057, 1.8170283525044424, 1.6158099698537383, 1.8063585809979532, 1.772285044123278, 1.892957682435774, 1.8983968042954449]
#     ]

# S9N8
# labels = ['Pegasus', 'Chimera']
# title = 'S9N8'
# xlabel = 'Annealing system'
# list_set_epsilons = [
#     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
#     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#     ]

# S9N16
# labels = ['Pegasus', 'Chimera']
# title = 'S9N16'
# xlabel = 'Annealing system'
# list_set_epsilons = [
#     [1.0629485594831503, 1.0419059109202746, 1.0404363454609564, 1.0330177149063273, 1.0629485594831503, 1.0717086909513749, 1.0629485594831503, 1.0629485594831503, 1.0597442705745803, 1.0629485594831503],
#     [1.0629485594831503, 1.0923615544817737, 1.129929803310457, 1.0923615544817737, 1.0629485594831503, 1.0984880050061543, 1.0984880050061543, 1.0404363454609564, 1.0629485594831503, 1.1263127498737597]
#     ]

# S9N32
# labels = ['Pegasus', 'Chimera']
# title = 'S9N32'
# xlabel = 'Annealing system'
# list_set_epsilons = [
#     [1.285110119120935, 1.1482482551658113, 1.3411442493278372, 1.284471106279312, 1.2492237847194403, 1.2014593617831402, 1.1661448522088238, 1.2756655373153891, 1.2601553919718653, 1.2291356718165953],
#     [1.3254404151162924, 1.2669876639143147, 1.357630375379645, 1.2855571176686424, 1.2659731560125793, 1.374917667966163, 1.2486672435065347, 1.377426912303937, 1.2389962416351232, 1.3608293029818523]
#     ]

# S9N64
# labels = ['Pegasus', 'Chimera']
# title = 'S9N64'
# xlabel = 'Annealing system'
# list_set_epsilons = [
#     [1.6086121415068662, 1.5582521132573603, 1.641251568182897, 1.5353913265287036, 1.5904944085276402, 1.541082997956022, 1.62718000092553, 1.448865852211337, 1.4867540245815876, 1.4997361646749812],
#     [1.524864123566001, 1.4527567899762521, 1.5013902619717931, 1.5498291907630497, 1.4367594565064472, 1.4654370420439466, 1.550965201829096, 1.535521304236086, 1.3868792335532125, 1.47244045493311]
#     ]

# Check assumptions for each group.
assumptions_met = True

# Print median value of each group.
for set in list_set_epsilons:
    print('median:')
    print(np.median(set))

# Shapiro-Wilk test
for set in list_set_epsilons:
    test = stats.shapiro(set)
    print('Shapiro-Wilk test p-value:')
    print(test.pvalue)
    if test.pvalue < 0.05:
        assumptions_met = False

# Levene's test

_, pvalue = stats.levene(*list_set_epsilons)
print('Levene\'s test p-value:')
print(pvalue)
if pvalue < 0.05:
    assumptions_met = False

dict = {'tries': [], 'groups': [], 'y': []}

for i in range(len(list_set_epsilons)):
    for j in range(len(list_set_epsilons[i])):
        dict['tries'].append(j)
        dict['groups'].append(labels[i])
        dict['y'].append(list_set_epsilons[i][j])

df = pd.DataFrame.from_dict(dict)
# print(df)

if assumptions_met:
    # If assumptions are met, we perform parametric one-way ANOVA
    print('Assumptions MET! Performing one-way ANOVA:')

    anova_result = stats.f_oneway(*list_set_epsilons)
    print('one-way ANOVA p-value:')
    print(anova_result.pvalue)

    if anova_result.pvalue > 0.05:
        print('The null hypothesis was not rejected!')
        exit(0)

    results = sp.posthoc_ttest(df, val_col='y', group_col='groups', p_adjust='bonferroni', sort=False)
    print(results)
    for i in range(len(labels)):
        for j in range(i+1, len(labels)):
            x = labels[i]
            y = labels[j]
            if results[x][y] < 0.05:
                print(f'{x} and {y} ARE significantly different!')
            if results[x][y] > 0.05:
                print(f'{x} and {y} are NOT!')
else:
    # If assumptions are not met, we perform kruskal-wallis one-way ANOVA
    print('Assumptions NOT MET! Performing Kruskal-Wallis One-way ANOVA:')

    H, p = stats.kruskal(*list_set_epsilons)
    print(f'p-value:\t{p}')

    if p > 0.05:
        print('The null hypothesis was not rejected!')
        exit(0)


    print('Null hypothesis rejected! Now performing pairwise comparison with Conover-Iman\'s test')

    results = sp.posthoc_conover(
        df, val_col='y', group_col='groups', p_adjust='bonferroni', sort=False)

    print(results)

    for i in range(len(labels)):
        for j in range(i+1, len(labels)):
            x = labels[i]
            y = labels[j]
            if results[x][y] < 0.05:
                print(f'{x} and {y} ARE significantly different!')
            if results[x][y] > 0.05:
                print(f'{x} and {y} are NOT!')