import numpy as np

question = np.array([
[  10.72896862,  177.68974304,    1.39846241,   29.93799591,   16.65709686,
  -45.92454529,    5.45777082,   22.61013985,  -52.36220932,   -2.20680594,
   20.27735519,  -53.54218292,   -1.7395581 ,   17.4285965 ,  -54.55295181,
   -4.64284325,   16.04725266,  -54.80635071],
[  10.25674629,  177.62532043,    1.67368519,   30.1503334 ,   15.87689114,
  -46.06178665,    5.7445612 ,   21.99376488,  -52.59354401,   -2.01003361,
   19.36508751,  -53.88654327,   -1.54295111,   16.58706284,  -54.8205719 ,
   -4.41946888,   15.18438816,  -55.07003784],
[   9.91742706,  177.44432068,    1.83924878,   30.47485352,   15.03984261,
  -46.12908936,    5.82754707,   20.77774239,  -53.07665634,   -1.89193892,
   18.6373539 ,  -54.14680099,   -1.56266844,   15.47174454,  -55.1451683 ,
   -4.16195536,   14.21505642,  -55.34814072],
[   9.38387966,  177.32473755,    2.00240445,   30.64561081,   14.30095482,
  -46.25078964,    5.78234196,   19.68769836,  -53.49547195,   -1.72568583,
   18.09572029,  -54.33574677,   -1.38666713,   14.75632477,  -55.34558868,
   -3.924757  ,   13.58618736,  -55.52313232],
[  10.72896862,  177.68974304,    1.39846241,   29.93799591,   16.65709686,
  -45.92454529,    5.45777082,   22.61013985,  -52.36220932,   -2.20680594,
   20.27735519,  -53.54218292,   -1.7395581 ,   17.4285965 ,  -54.55295181,
   -4.64284325,   16.04725266,  -54.80635071],
[  10.25674629,  177.62532043,    1.67368519,   30.1503334 ,   15.87689114,
  -46.06178665,    5.7445612 ,   21.99376488,  -52.59354401,   -2.01003361,
   19.36508751,  -53.88654327,   -1.54295111,   16.58706284,  -54.8205719 ,
   -4.41946888,   15.18438816,  -55.07003784],
[   9.91742706,  177.44432068,    1.83924878,   30.47485352,   15.03984261,
  -46.12908936,    5.82754707,   20.77774239,  -53.07665634,   -1.89193892,
   18.6373539 ,  -54.14680099,   -1.56266844,   15.47174454,  -55.1451683 ,
   -4.16195536,   14.21505642,  -55.34814072],
[   9.38387966,  177.32473755,    2.00240445,   30.64561081,   14.30095482,
  -46.25078964,    5.78234196,   19.68769836,  -53.49547195,   -1.72568583,
   18.09572029,  -54.33574677,   -1.38666713,   14.75632477,  -55.34558868,
   -3.924757  ,   13.58618736,  -55.52313232],
[   8.70297432,  177.19264221,    2.18104744,   30.8557663 ,   13.59702396,
  -46.32331085,    5.90937281,   18.91997528,  -53.75797653,   -1.61672986,
   17.54245186,  -54.52022552,   -1.2567457 ,   13.9895525 ,  -55.54745483,
   -3.7550621 ,   12.8980341 ,  -55.69871521],
[   8.17061138,  177.08847046,    2.32640195,   31.1072464 ,   13.02093697,
  -46.32063293,    6.00456429,   18.39014626,  -53.93101501,   -1.59587729,
   16.99128342,  -54.69511795,   -1.27290237,   13.67476463,  -55.6254158 ,
   -3.68360591,   12.45093441,  -55.80512238],
[   7.71395493,  176.99765015,    2.38076735,   31.16343117,   12.59971809,
  -46.39928818,    6.02212381,   18.05582237,  -54.04190826,   -1.51944244,
   16.79233932,  -54.75870132,   -1.2598418 ,   13.56711483,  -55.65206909,
   -3.71776891,   12.42886543,  -55.8077774 ],
[   7.39572811,  176.85409546,    2.40881467,   31.32793045,   12.42867661,
  -46.33459854,    6.0272584 ,   17.80540276,  -54.12435913,   -1.47915518,
   16.74776268,  -54.77345276,   -1.15795636,   13.81727314,  -55.59270477,
   -3.67071581,   12.79533291,  -55.7280159 ],
[   7.13897848,  176.78569031,    2.37236857,   31.57227707,   12.27938557,
  -46.20838165,    6.00423384,   17.85396576,  -54.11091614,   -1.4091475 ,
   16.84038544,  -54.74689484,   -1.13832319,   13.91367817,  -55.56905746,
   -3.74053478,   12.66064262,  -55.7541275 ],
[   6.93306446,  176.84492493,    2.31509042,   31.71092224,   12.18602943,
  -46.13810349,    6.17908716,   18.41093063,  -53.90420151,   -1.35454631,
   16.94155121,  -54.71704865,   -1.15374339,   14.04855728,  -55.53479385,
   -3.78654981,   12.70303631,  -55.74137878],
[   6.80461121,  176.89329529,    2.27055526,   31.9793148 ,   12.14023972,
  -45.96460342,    6.29632902,   18.66275406,  -53.80393982,   -1.21974838,
   17.17442894,  -54.64757538,   -1.19015729,   14.09947395,  -55.52111816,
   -3.78911281,   12.87954426,  -55.70068359],
[   6.71142864,  176.91542053,    2.24126601,   32.18444824,   12.18307781,
  -45.8098259 ,    6.29227448,   18.60729218,  -53.82362366,   -1.10155201,
   17.32675362,  -54.60198593,   -1.10325789,   14.24736118,  -55.4851532 ,
   -3.7321794 ,   12.9131937 ,  -55.69673538],
[   6.61177492,  176.94876099,    2.18604708,   32.30731964,   12.23736   ,
  -45.70875549,    6.23014498,   18.62161446,  -53.82589722,   -1.06883597,
   17.31043625,  -54.60781097,   -1.04420865,   14.19864464,  -55.49878311,
   -3.61946082,   12.93852997,  -55.69829941],
[   6.5315609 ,  176.90090942,    2.19921446,   32.39546967,   12.19383526,
  -45.65797043,    6.20798016,   18.53624535,  -53.85791397,   -1.05898261,
   17.20736313,  -54.64056778,   -0.99893975,   13.97629929,  -55.55602264,
   -3.57646322,   12.94143772,  -55.70039749],
[   6.53336573,  176.72911072,    2.23745775,   32.47756195,   12.10029984,
  -45.62452316,    6.05127239,   18.09803009,  -54.0245285 ,   -1.06748569,
   17.01973534,  -54.69913864,   -0.89753288,   13.38063622,  -55.70421219,
   -3.57417178,   12.7208786 ,  -55.75133133],
[   6.80067301,  176.690979  ,    2.21676707,   32.69108963,   12.31925583,
  -45.41294098,    6.08015394,   18.26700783,  -53.96438217,   -1.33496404,
   17.30932426,  -54.60230637,   -0.94681919,   13.18877602,  -55.74913406,
   -3.73206115,   12.56831551,  -55.77558136],
[   6.90937042,  176.78311157,    2.17077971,   32.68795395,   12.56872177,
  -45.34679031,    6.16004181,   18.5828495 ,  -53.8473587 ,   -1.03831136,
   17.09420967,  -54.67647171,   -0.87941837,   13.30187988,  -55.72336197,
   -3.75332952,   12.73996258,  -55.73519897],
[   7.02326393,  176.88336182,    2.05658984,   32.57772064,   12.73795891,
  -45.37888336,    6.21360302,   18.72015762,  -53.79361725,   -0.75585145,
   16.78295326,  -54.77743912,   -0.74203771,   13.28123379,  -55.73028183,
   -3.67115927,   12.79184914,  -55.72878647],
[   7.08563185,  176.91908264,    2.04591513,   32.63593674,   12.65780449,
  -45.35947418,    6.34454298,   18.66369438,  -53.79795074,   -0.62611085,
   16.7133007 ,  -54.80036545,   -0.59473652,   12.99588871,  -55.79927826,
   -3.53532672,   12.687253  ,  -55.76147079],
[   7.17930937,  176.94210815,    2.05006146,   32.69524765,   12.61793518,
  -45.32785797,    6.34782743,   18.80921936,  -53.74685669,   -0.69704843,
   16.89954948,  -54.74235916,   -0.55235434,   13.02099037,  -55.79386139,
   -3.48441672,   12.63082886,  -55.77748108],
[   7.20144224,  176.94937134,    2.05264854,   32.72360992,   12.4891634 ,
  -45.34305191,    6.31258297,   18.84158897,  -53.7396698 ,   -0.55627465,
   13.02039433,  -55.79396057,   -3.38225079,   12.6522131 ,  -55.77892303,
   -0.66105795,   17.26648521,  -54.62817764],
[   7.23114014,  176.95271301,    2.1315999 ,   32.81779099,   12.44333553,
  -45.28755188,    6.33480024,   18.90879822,  -53.71344376,   -0.6162805 ,
   17.18889999,  -54.65316391,   -0.51858509,   13.09887791,  -55.7759552 ,
   -3.29475474,   12.69892693,  -55.77354431],
[   7.25086069,  176.94241333,    2.17674065,   32.90003204,   12.26486778,
  -45.27656555,    6.25608969,   19.06494141,  -53.66745758,   -0.48815796,
   17.38139343,  -54.59354401,   -0.44244128,   13.26632881,  -55.73701859,
   -3.22634315,   12.81003571,  -55.7521286 ],
[   7.21610928,  177.004776  ,    2.1768198 ,   33.11640549,   12.08924484,
  -45.16592026,    5.99684095,   19.11941528,  -53.67767334,   -0.35618448,
   17.78813934,  -54.46339798,   -0.34879011,   13.58714104,  -55.6603508 ,
   -3.20976758,   12.99784184,  -55.70960236],
[   7.18385649,  176.94328308,    2.30212593,   33.30002213,   12.00983524,
  -45.05195999,    5.95573807,   19.23531342,  -53.64082718,   -0.33197531,
   18.06969261,  -54.37078476,   -0.29604146,   13.8534832 ,  -55.59495926,
   -3.06197286,   13.31179428,  -55.64374924],

[   6.99621773,  176.76295471,    2.59723449,   33.30969238,   12.09930706,
  -45.02085876,    6.03652334,   19.13311195,  -53.66834259,   -0.26107284,
   14.29409504,  -55.48348618,   -2.7383585 ,   13.81271553,  -55.53842545,
   -0.27610475,   18.15698242,  -54.3420105 ],
[   7.01478577,  176.74882507,    2.71969438,   33.31359863,   12.18991661,
  -44.99351501,    5.89451694,   19.31340218,  -53.61952591,   -0.30802661,
   18.37682915,  -54.26788712,   -0.17734534,   14.44076538,  -55.44582367,
   -2.72218633,   14.11799526,  -55.46240234],
[   7.04443264,  176.76998901,    2.80669761,   33.27124786,   12.27220821,
  -45.00247955,    5.86996603,   19.41635895,  -53.58502579,   -0.31052703,
   18.56332397,  -54.20436096,   -0.40333492,   14.41540813,  -55.45123672,
   -2.84459853,   14.1954422 ,  -55.43648529],
[   7.02300358,  176.77618408,    2.88574791,   33.13138199,   12.34557915,
  -45.08552551,    5.95963001,   19.41104698,  -53.57705307,   -0.38883096,
   18.73263359,  -54.14557648,   -0.41390806,   14.52410889,  -55.42278671,
   -2.96923947,   14.42525005,  -55.37059021],
[   7.01531744,  176.76803589,    2.96322227,   33.01385498,   12.45615768,
  -45.14128876,    5.96942282,   19.40087128,  -53.57964706,   -0.43366757,
   18.69320297,  -54.15886307,   -0.60173398,   14.26230812,  -55.48901749,
   -2.97082305,   14.42004108,  -55.37186432],
[   6.90995455,  176.68717957,    3.13179946,   32.51773834,   12.73278809,
  -45.42333221,    5.96823883,   19.21715355,  -53.6459465 ,   -0.47095302,
   14.28230858,  -55.48513412,   -3.051651  ,   14.37622833,  -55.37885666,
   -0.39660364,   18.59093857,  -54.19433975],
[   6.7997961 ,  176.61505127,    3.21413612,   32.62921906,   12.65353489,
  -45.36549759,    5.70324612,   19.26792145,  -53.65656281,   -0.3482978 ,
   18.54756927,  -54.20952988,   -0.30964655,   14.3534565 ,  -55.46790695,
   -3.01344013,   14.7385664 ,  -55.28562546],
[   6.73104858,  176.52757263,    3.32048154,   32.72002029,   12.61332512,
  -45.31126404,    5.66834068,   19.47344398,  -53.58601761,   -0.27305424,
   18.52688217,  -54.21702957,   -0.20208691,   14.25821018,  -55.4929657 ,
   -2.99726868,   14.72598171,  -55.28985596],

[   6.09680414,  176.12145996,    3.1724596 ,   32.7799263 ,   12.3153286 ,
  -45.34992218,    6.62273121,   19.83559608,  -53.34318161,    0.2741724 ,
   18.96094894,  -54.06675339,    0.36596251,   14.22592926,  -55.50041199,
   -2.41599131,   14.40617847,  -55.40244675],
[   6.00866032,  176.12858582,    3.15226197,   32.8514328 ,   12.29072475,
  -45.30482864,    6.92640018,   19.99258041,  -53.24592209,    0.42951417,
   14.35914421,  -55.46563721,   -2.50113463,   14.38657951,  -55.40376282,
    0.47507825,   19.14348221,  -54.00099945],
[   5.91892815,  176.19700623,    3.14518118,   33.274189  ,   12.16462421,
  -45.02950668,    7.23710299,   20.2124939 ,  -53.12142563,    0.51455009,
   19.06601715,  -54.02803802,    0.53014517,   14.44959641,  -55.44127274,
   -2.58058071,   14.40686512,  -55.39484787],
[   5.86966085,  176.29022217,    3.11882234,   33.34783173,   12.17635536,
  -44.97182465,    7.20584774,   20.24205589,  -53.11441803,    0.48636827,
   19.03500748,  -54.03922653,    0.5677616 ,   14.5214386 ,  -55.42212677,
   -2.52230597,   14.56585884,  -55.35594177],
[   5.83013678,  176.37574768,    3.08817387,   33.23003769,   12.22092247,
  -45.04686737,    6.93478632,   20.03212929,  -53.2299614 ,    0.60018736,
   14.57147312,  -55.40864944,   -2.35949183,   14.82133865,  -55.29527283,
    0.45861614,   18.98914146,  -54.05560684],
[   5.82499552,  176.43173218,    3.10834718,   33.23665237,   12.26611614,
  -45.02970123,    7.07714558,   19.97598839,  -53.23232269,    0.65755492,
   14.71043682,  -55.37126541,   -2.29651976,   14.88388252,  -55.28112411,
    0.47914451,   18.99150085,  -54.05459976],
[   5.83195925,  176.47561646,    3.08668303,   33.14317322,   12.38058853,
  -45.06725693,    6.98236752,   19.97912788,  -53.24365997,    0.71959406,
   14.69587612,  -55.37436295,   -2.28838634,   15.00831985,  -55.24780655,
    0.45923734,   19.04669189,  -54.0353508 ],
[   5.78423071,  176.48190308,    3.0304203 ,   33.05461121,   12.46473694,
  -45.10908508,    6.83196354,   19.91684532,  -53.28649139,    0.78311461,
   15.01749992,  -55.28713989,   -2.27249575,   15.10156059,  -55.22304916,
    0.4782778 ,   19.0910244 ,  -54.01953506],
[   5.59057713,  176.55233765,    2.92913079,   33.09799957,   12.40445042,
  -45.09388733,    6.75187969,   19.86894226,  -53.31457138,    0.46647659,
   19.10025597,  -54.0163765 ,    0.68074751,   14.94315624,  -55.30863571,
   -2.26671338,   15.10634995,  -55.22197342],
[   5.45630074,  176.63383484,    2.82581854,   32.93784332,   12.41294193,
  -45.20867157,    6.74860811,   19.73178482,  -53.36590195,    0.75210172,
   14.48808479,  -55.42865753,   -2.25000596,   15.05656147,  -55.23625565,
    0.39502254,   18.98179817,  -54.0586853 ],
[   5.41780853,  176.68377686,    2.76463723,   32.74010086,   12.47472   ,
  -45.33512497,    6.9453311 ,   19.88410378,  -53.28406143,    0.78931522,
   14.32966042,  -55.46931076,   -2.28755736,   14.94073009,  -55.26615906,
    0.39642549,   18.87907028,  -54.09463882],
[   5.53168488,  176.75912476,    2.68949628,   32.60248184,   12.63590431,
  -45.38962936,    6.91279745,   20.02789497,  -53.23441696,    0.83691472,
   14.110075  ,  -55.52487564,   -2.2533989 ,   14.90074444,  -55.27835464,
    0.48965445,   18.5283947 ,  -54.21499252],
[   5.66458273,  176.76463318,    2.63324928,   32.4471817 ,   12.49426174,
  -45.53987503,    7.12624359,   20.05578995,  -53.195755  ,    0.65478802,
   18.38022614,  -54.26366043,    0.74284762,   14.18954182,  -55.50595856,
   -2.17514277,   14.72236347,  -55.32926178]
], "float32")
print np.shape(question)
#a = np.ones((50,1), dtype=np.int)*3

#target_data = np.array([[0], [1], [2]], "float32")

#print np.reshape(np.append(training_data10,two),(53,18))
