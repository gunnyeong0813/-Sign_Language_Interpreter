import numpy as np

question = np.array([
[ 65.56808472, -49.14525986, -59.82063293, -27.86125183,  49.68679047,
  -6.14654875, -46.79391861,  10.61275578, -31.31301308,  -3.3896575 ,
 -55.41078186,  14.1761055 ,  -3.74878526, -52.99801636,  21.44675064,
 -14.68338203, -41.29887772,  36.89996338],
[ 67.90460968, -50.84015656, -60.65609741, -26.50147629,  50.60770035,
  -4.39759827, -46.63100052,  14.19095898, -30.11599541,  -1.91328418,
 -55.89545822,  12.44360828,  -4.35419178, -53.71385193,  19.45943832,
 -15.64694881, -42.31855011,  35.31458282],
[ 67.27265167, -49.43388367, -61.0162735 , -27.66176414,  49.96373749,
  -4.61069298, -46.97768402,  13.71495247, -29.79603767,   0.14498162,
 -55.88728333,  12.6252594 ,  -3.57353997, -53.81473541,  19.33934212,
 -14.76223278, -42.65771484,  35.28742218],
[ 65.35688019, -47.52728271, -61.03776169, -29.29787445,  48.88275146,
  -5.90910673, -48.27588272,  11.24831676, -28.73535728,   1.81296527,
 -55.35801315,  14.66320896,  -2.25688148, -53.08914566,  21.43025208,
 -12.97277451, -41.75421906,  37.02835464],
[ 64.86978912, -47.30160141, -60.87804413, -29.49888039,  48.7130394 ,
  -6.29777956, -48.76866531,  10.62555599, -28.13399124,   1.70306623,
 -55.20165253,  15.25396919,  -2.94948077, -52.77450562,  22.11240578,
 -14.20640564, -41.58669281,  36.76317978],
[ 64.13891602, -47.16747665, -60.78224945, -29.72988129,  48.47883224,
  -6.98164368, -49.44495392,   9.04814529, -27.49789047,   1.87264729,
 -54.7690506 ,  16.72276306,  -2.44503403, -52.060215  ,  23.80256844,
 -13.56608486, -40.64764023,  38.03337097],
[ 64.27585602, -47.36312866, -60.63996506, -29.52962685,  48.61264801,
  -6.90055752, -49.28022003,   8.79496956, -27.87319374,   2.04612136,
 -54.80000305,  16.60059357,  -2.44165254, -52.00009918,  23.93395996,
 -13.78090763, -40.88966751,  37.69519806],
[ 64.60222626, -47.30806732, -60.6517067 , -29.4834919 ,  48.69025421,
  -6.54136229, -49.18026733,   9.61419582, -27.77904129,   1.8489542 ,
 -55.05815887,  15.74760532,  -2.700562  , -52.36258698,  23.10136414,
 -13.15650845, -41.65491104,  37.0753479 ],
[ 64.67500305, -47.62059402, -60.51428223, -29.23135948,  48.83749771,
  -6.57514763, -49.00091934,   9.32740974, -28.19070244,   0.95440292,
 -55.06650925,  15.79794407,  -2.99139118, -52.25923157,  23.29872894,
 -13.30836868, -41.4889183 ,  37.20703125],
[ 64.28833008, -47.55621338, -60.17191315, -29.25138474,  48.78171158,
  -6.89257717, -48.63593674,   8.63637638, -29.03041458,   2.02142644,
 -54.8506546 ,  16.43551064,  -2.72727799, -51.98575592,  23.93427658,
 -13.38479233, -41.2174263 ,  37.48036194],
[ 64.71086121, -47.97358322, -60.34507751, -28.95255661,  48.99196243,
  -6.65909863, -48.58935547,   8.9194746 , -29.0228157 ,   1.80378044,
 -54.87964249,  16.36391068,  -2.91398573, -51.98184204,  23.92076683,
 -13.35172749, -41.0901947 ,  37.63155365],
[ 66.70095825, -51.15906906, -58.76897812, -25.99718285,  50.75703812,
  -5.53859043, -47.01842117,  13.08351231, -30.01493263,  -2.88930488,
 -55.5648613 ,  13.67496204,  -5.64975643, -52.71340942,  21.72977257,
 -16.42455292, -41.61220932,  35.7975502 ],
[ 68.59044647, -53.69615555, -58.42993927, -23.83264351,  51.92624664,
  -4.29841089, -46.27759552,  15.94848156, -29.77980232,  -3.36551857,
 -55.84636688,  12.35569382,  -5.60090923, -53.04689789,  20.91561127,
 -16.56098366, -41.78385925,  35.53377533],
[ 67.73920441, -52.08485031, -59.38312531, -25.34381866,  51.15690994,
  -4.84436274, -46.84075546,  13.80153561, -29.9711132 ,   1.40706766,
 -55.53542709,  14.02293396,  -2.91225171, -52.69981384,  22.29472923,
 -13.51963806, -41.39395905,  37.23662186],
[ 66.74962616, -49.95256805, -60.43184662, -27.25703812,  50.11740494,
  -5.30150318, -46.9615593 ,  11.12289619, -30.88202858,   3.67193747,
 -55.19674301,  14.92121601,  -1.00905752, -52.39748001,  23.15799141,
 -11.80474091, -41.30530167,  37.9120903 ],
[ 72.2232132 , -52.25886917, -64.27513123, -25.72565079,  51.1929512 ,
  -0.52811605, -45.15124512,  17.09830093, -30.85157585,   0.48055857,
 -56.71419144,   8.12870598,  -3.99094415, -54.74607849,  16.42393684,
 -15.01802063, -45.23855209,  31.79211998],
[ 68.35145569, -51.34383392, -59.92489624, -25.87381172,  50.96863937,
  -3.94338584, -45.22962952,  15.19441032, -31.72092628,   1.28303456,
 -56.00847626,  12.00877476,  -2.41682482, -53.59425354,  20.11520195,
 -12.22982216, -43.68925095,  34.99267578],
[ 67.01383972, -50.78633499, -58.77325439, -26.17050362,  50.71876144,
  -5.05156803, -44.8721199 ,  14.02646255, -32.74992752,   2.13174152,
 -55.70172882,  13.25064182,  -0.84510696, -53.18490601,  21.29454803,
 -10.54107475, -43.42960358,  35.85472488],
[ 69.20872498, -52.4329567 , -59.9315033 , -24.98377609,  51.45215225,
  -3.36051583, -44.34025574,  15.97011662, -32.58378983,   1.6487602 ,
 -56.09943008,  11.53003597,  -0.71367019, -53.88599014,  19.45757294,
 -10.81632519, -44.63556671,  34.25609207],
[ 71.05782318, -53.91759491, -60.41987991, -23.80370903,  52.08691025,
  -1.77304649, -43.1677742 ,  18.43616295, -32.85510254,   0.6153248 ,
 -56.56121826,   9.12449837,  -1.63919151, -54.69356918,  16.992136  ,
 -12.31991005, -45.98648071,  31.87899017],
[ 71.39477539, -54.04748917, -60.66275024, -23.73102188,  52.13004684,
  -1.45028305, -43.65032578,  18.9196167 , -31.92966652,   1.55235636,
 -56.58274841,   8.87632179,  -0.66056859, -54.79123688,  16.74188614,
 -11.39295101, -46.3715477 ,  31.66522598],
[ 69.06319427, -52.96406555, -58.31493378, -24.22970963,  51.80499268,
  -3.45979238, -45.01774597,  17.20864487, -30.98501778,   4.39286804,
 -55.95671463,  11.50456619,   0.30883661, -54.06476593,  18.96608162,
  -9.66154861, -45.13650131,  33.9434433 ],
[ 67.14109039, -51.25068283, -57.72164154, -25.53330994,  51.05322647,
  -4.94211054, -45.38241196,  13.99347305, -32.05348206,   5.420156  ,
 -55.48814774,  13.20961857,   1.93793643, -53.33914948,  20.83232307,
  -8.38123512, -44.15436935,  35.53804779],
[ 66.84345245, -50.06255722, -58.21291733, -26.49934387,  50.56071472,
  -4.91986799, -44.4392395 ,  12.40409184, -33.97203064,   5.09514236,
 -55.63122559,  12.72841644,   1.46805561, -53.58655548,  20.22701263,
  -8.30157471, -44.55768204,  35.05001068],
[ 66.55680084, -49.04197311, -58.74710846, -27.3655014 ,  50.09550858,
  -4.93721056, -43.31037521,  10.71757698, -35.94651031,   4.70022011,
 -55.68479919,  12.64585495,   0.64196026, -53.88114548,  19.47347641,
  -8.84647942, -44.76859665,  34.64561844],
[ 68.44033813, -49.83405304, -59.61858368, -26.79122734,  50.53829956,
  -3.30407119, -41.59787369,  12.72525597, -37.28928757,   2.55314136,
 -56.43094635,   9.58311939,  -2.67251778, -55.06092453,  15.619174  ,
 -13.491786  , -46.32881927,  30.89366722],
[ 69.40724945, -49.75074387, -60.63264847, -26.99962807,  50.48069763,
  -2.35068893, -41.68203735,  14.02326965, -36.72550201,   0.29399481,
 -56.87740326,   6.90514088,  -3.87775755, -55.55603027,  13.46464348,
 -16.81504059, -47.14753723,  27.87777901],
[ 69.75709534, -49.57048035, -61.17870331, -27.22963333,  50.37304688,
  -1.97726274, -41.95811844,  14.78190422, -36.10842133,  -1.32764053,
 -57.0271759 ,   5.38004255,  -4.10204268, -55.71052933,  12.74034882,
 -17.59181595, -47.49647903,  26.78467751],

[ 73.08979034, -52.13613129, -62.37685394, -25.50143814,  51.30123901,
   0.81621355, -40.31668854,  21.58477402, -34.51765442,  -3.36362648,
 -57.19649124,  -0.23247345, -11.30575752, -55.95248032,   4.93012285,
 -23.26628113, -48.58943176,  19.50778008],
[ 74.58177948, -53.98637009, -63.10372925, -24.29610634,  51.8512001 ,
   1.98960018, -39.81915283,  24.07517052, -33.43093491,  -5.34281015,
 -57.00056076,  -2.27973771, -14.03283501, -55.48739624,   2.65232801,
 -25.32367516, -48.27057648,  17.64850044],
[ 74.8392334 , -55.52026749, -61.81954575, -22.89179802,  52.48395538,
   2.05095172, -39.70014572,  25.75421906, -32.30208969,  -6.80085182,
 -56.8249855 ,  -2.73418498, -15.67941666, -55.06608963,   2.16525078,
 -26.98718452, -47.6158371 ,  16.94786644],
[ 74.31221008, -55.58227539, -59.92885208, -22.4610405 ,  52.68676758,
   1.55324352, -39.96507263,  26.68810844, -31.19846344,  -6.75850487,
 -56.81433105,  -3.04315591, -16.85716057, -54.74782562,   1.14805663,
 -28.1643734 , -47.51581955,  15.22568226],
[ 74.7071991 , -56.35638809, -60.38443375, -21.97948074,  52.88058853,
   1.83085787, -39.88523865,  26.22789383, -31.68709183,  -7.3633666 ,
 -56.75287628,  -2.77460957, -17.47469139, -54.54117966,   1.64364409,
 -28.19765472, -47.30442429,  15.81107235],
[ 74.56074524, -56.98147202, -59.8527565 , -21.38047409,  53.133461  ,
   1.58662772, -39.79626465,  25.49255371, -32.39125824,  -8.20322037,
 -56.67109299,  -1.97499239, -17.76926231, -54.39520645,   2.86724854,
 -28.3499012 , -46.84500122,  16.87114334],
[ 77.69467163, -59.16688156, -64.39740753, -20.66757584,  53.25620651,
   4.40839291, -38.35100555,  26.84027672, -33.03946686,  -9.65748692,
 -56.24310684,  -5.12366962, -17.70261002, -54.48865891,   0.64037251,
 -27.28329849, -48.15172577,  14.82699203],
[ 77.44991302, -58.94147873, -64.01268768, -20.77220154,  53.23246002,
   4.19848394, -37.80578232,  26.33110619, -34.06174088,  -7.93833685,
 -56.57024002,  -4.42685461, -16.65958595, -54.80748749,   1.18479776,
 -25.86976242, -48.85122681,  15.07048512],
[ 76.10716248, -57.86248016, -61.9092865 , -21.18113136,  53.15119934,
   3.01932168, -37.92689514,  25.51033592, -34.54822922,  -5.81585598,
 -56.92918015,  -2.83737683, -15.50992584, -55.10930252,   2.28326511,
 -25.09719086, -49.13651276,  15.44475555],
[ 75.80065155, -57.9405098 , -60.7516861 , -20.91570854,  53.27168274,
   2.73269677, -37.97121048,  25.73882294, -34.32938004,  -5.74723291,
 -56.93588257,  -2.84269786, -15.91578007, -55.00611115,   1.95500505,
 -25.25243568, -49.28874207,  14.68811321],
[ 75.21898651, -58.3637886 , -58.39180756, -20.13954544,  53.59718323,
   2.13244987, -36.99514771,  26.02826881, -35.16667557,  -6.37404203,
 -56.87548447,  -2.71240091, -17.35083389, -54.58187103,   1.6045543 ,
 -26.24578857, -48.95901108,  14.03495884],
[ 74.95046997, -58.7080307 , -57.1307373 , -19.63319588,  53.79571915,
   1.83433998, -36.70797348,  26.0411911 , -35.4568367 ,  -7.2019887 ,
 -56.77355576,  -2.77512717, -18.8275528 , -54.10071182,   1.20107186,
 -27.21315002, -48.57203293,  13.52806282],
[ 74.40721893, -58.87582016, -55.41051483, -19.15247154,  53.98474121,
   1.27943337, -36.54788971,  25.82244492, -35.78071594,  -8.00684929,
 -56.67899704,  -2.48759007, -19.59263611, -53.82213211,   1.45357478,
 -27.93749046, -48.12228394,  13.65828705],
[ 74.20632172, -59.3104248 , -54.12447357, -18.58145523,  54.18914032,
   1.03590643, -36.5147171 ,  25.8659668 , -35.7831459 ,  -9.15020466,
 -56.50101089,  -2.59145117, -20.60503006, -53.4413414 ,   1.50407553,
 -29.01831245, -47.58899689,  13.26768398],
[ 74.40055847, -59.68042374, -53.85026169, -18.27727699,  54.28922272,
   1.19485211, -36.26189804,  26.12255669, -35.85377502, -10.02016544,
 -56.32203293,  -3.19861054, -21.38642693, -53.14449692,   1.04378748,
 -29.58634186, -47.44239807,  12.51693439],
[ 74.91434479, -60.14260864, -54.25436401, -18.05944252,  54.34967041,
   1.66619265, -35.77770996,  26.52739143, -36.04246902, -10.47431755,
 -56.19202423,  -3.94350839, -21.74505234, -53.00746155,   0.40997449,
 -29.81565094, -47.53514862,  11.58632374],
[ 79.50878906, -63.20541763, -63.27988052, -17.68883324,  54.16922379,
   5.96715069, -33.49916458,  28.23799706, -36.92191696, -10.99042892,
 -55.69859695,  -7.72547579, -21.33125496, -53.12699509,  -2.30359173,
 -28.75271988, -48.7264328 ,   9.04557514],
[ 79.93058014, -63.19917297, -65.01177979, -17.8882122 ,  54.06146622,
   6.33846474, -31.55084038,  26.92049408, -39.53021622,  -9.57648277,
 -56.08308792,  -6.76643753, -18.65257454, -54.17415619,  -0.2213107 ,
 -26.60466194, -49.70008469,  10.24207783],
[ 80.02641296, -62.99758148, -65.67861176, -18.11429977,  53.97575378,
   6.426229  , -31.03060913,  26.34144783, -40.32413483,  -8.15574265,
 -56.38411331,  -6.09278202, -17.19493103, -54.65102005,   0.6377542 ,
 -25.40030098, -50.22832489,  10.71198273],

[ 81.64280701, -63.99629211, -69.2870636 , -17.95062447,  53.8331871 ,
   7.91008043, -30.64591789,  26.85944366, -40.27659988,  -8.26245975,
 -56.22434235,  -7.30491066, -16.55376816, -54.85215759,  -0.14154135,
 -24.06193924, -51.08834076,   9.68561172],
[ 81.19180298, -63.72078705, -68.14228821, -18.03229523,  53.8622551 ,
   7.51665831, -30.92927551,  26.9113884 , -40.02453613,  -8.21400928,
 -56.23840714,  -7.2510705 , -16.80281448, -54.77525711,  -0.37845093,
 -23.91463089, -51.23436356,   9.27021599],
[ 79.67992401, -63.21959686, -64.03000641, -17.75345612,  54.13162231,
   6.11461306, -30.95098305,  26.88747787, -40.0238266 ,  -6.39018822,
 -56.68263245,  -5.38990259, -17.25024033, -54.63711166,   0.14671822,
 -23.77525711, -51.31416702,   9.18694115]
], "float32")
print np.shape(question)