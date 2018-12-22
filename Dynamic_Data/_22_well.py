import numpy as np

well = np.array([[ -0.88663656,  -4.22871542,  35.25028992,  11.53482914, -28.23905373,
 -48.50061798, -40.90236282,  -4.57418299,  39.86075592, -32.05692291,
  -2.10790539,  47.44172287, -24.14751816,  -3.54841185,  51.83736801,
 -21.48852921,  -8.6789093 ,  52.39967346, -50.74279404,  18.59794235,
  19.0287075 , -52.30810928,  16.21541405,  16.844244  , -49.39572906,
  28.12890244,   7.18565178, -56.48254013,   9.37128353,  -2.16983604,
 -56.28691483,  -2.45657873, -10.41897678,  80.3409729 , -11.35525131,
 -87.7479248 ],
[ -1.80806911,  -4.51301718,  35.07726288,  10.9684763 , -28.96953011,
 -48.20026398, -41.06578445,  -5.21951389,  39.61267853, -31.705616  ,
  -1.68805504,  47.69392776, -23.87557411,  -3.23083353,  51.98389435,
 -21.19474602,  -8.03209877,  52.62199783, -52.02811813,  14.6467104 ,
  19.00934792, -53.13987732,  14.84253216,  15.44859219, -55.15101242,
  15.42729568,   1.78066432, -55.25374222,  -8.1198616 , -12.8022728 ,
 -52.48609924,  22.20303535,   5.9195509 ,  80.3409729 , -11.35525131,
 -87.7479248 ],
[ -1.80806911,  -4.51301718,  35.07726288,  10.9684763 , -28.96953011,
 -48.20026398, -41.06578445,  -5.21951389,  39.61267853, -31.705616  ,
  -1.68805504,  47.69392776, -23.87557411,  -3.23083353,  51.98389435,
 -21.19474602,  -8.03209877,  52.62199783, -52.02811813,  14.6467104 ,
  19.00934792, -53.13987732,  14.84253216,  15.44859219, -55.15101242,
  15.42729568,   1.78066432, -55.25374222,  -8.1198616 , -12.8022728 ,
 -52.48609924,  22.20303535,   5.9195509 ,  57.17825699,  -3.1055963 ,
 -85.70101929],
[ -2.0692625 ,  -5.39247704,  35.40306473,  11.28423119, -28.04364586,
 -48.67264557, -41.15253448,  -4.89706039,  39.56380081, -31.84690094,
  -1.68083584,  47.59995651, -24.37070847,  -2.82775211,  51.77720261,
 -21.96509552,  -7.08015871,  52.44246674, -52.46911621,  13.24739742,
  18.82298279, -54.14269638,  12.44125271,  14.02105808, -55.2585907 ,
  14.72332668,   3.53810358, -56.47509384,  -1.86914468,  -9.48032856,
 -53.08151245,  20.71675491,   5.99797344,  57.17825699,  -3.1055963 ,
 -85.70101929],
[ -2.0692625 ,  -5.39247704,  35.40306473,  11.28423119, -28.04364586,
 -48.67264557, -41.15253448,  -4.89706039,  39.56380081, -31.84690094,
  -1.68083584,  47.59995651, -24.37070847,  -2.82775211,  51.77720261,
 -21.96509552,  -7.08015871,  52.44246674, -52.46911621,  13.24739742,
  18.82298279, -54.14269638,  12.44125271,  14.02105808, -55.2585907 ,
  14.72332668,   3.53810358, -56.47509384,  -1.86914468,  -9.48032856,
 -53.08151245,  20.71675491,   5.99797344,  50.4857254 ,  -1.44934022,
 -86.26094055],
[ -2.30874324,  -6.02943373,  35.57158279,  11.547966  , -27.84121895,
 -48.72697067, -41.26091385,  -3.87341619,  39.56438065, -32.004776  ,
  -1.3053112 ,  47.50575638, -24.51981544,  -3.12342668,  51.68973923,
 -22.23165321,  -7.25582027,  52.30595779, -52.3516655 ,  12.89141655,
  19.38867569, -54.21548843,  11.85933781,  14.24231529, -55.82788849,
  -5.83979607, -11.48696709, -52.57262421,  22.13598824,   5.37808895,
 -55.23091507,  14.70905113,   3.99951339,  50.4857254 ,  -1.44934022,
 -86.26094055],
[ -2.30874324,  -6.02943373,  35.57158279,  11.547966  , -27.84121895,
 -48.72697067, -41.26091385,  -3.87341619,  39.56438065, -32.004776  ,
  -1.3053112 ,  47.50575638, -24.51981544,  -3.12342668,  51.68973923,
 -22.23165321,  -7.25582027,  52.30595779, -52.3516655 ,  12.89141655,
  19.38867569, -54.21548843,  11.85933781,  14.24231529, -55.82788849,
  -5.83979607, -11.48696709, -52.57262421,  22.13598824,   5.37808895,
 -55.23091507,  14.70905113,   3.99951339,  56.45069504,  -2.23575306,
 -86.37802887],
[ -2.20296001,  -6.40410089,  35.45726395,  11.70705128, -27.56315804,
 -48.8469429 , -41.4436264 ,  -3.71027327,  39.3886528 , -31.90091515,
  -1.41529691,  47.57241821, -24.40646935,  -3.54574966,  51.71613312,
 -22.09951591,  -8.08158112,  52.24084473, -52.18990326,  12.89629078,
  19.81681442, -54.36478043,  10.05984974,  15.03584671, -55.71812057,
  -5.99541473, -11.93115997, -52.52264404,  22.49973106,   4.23564816,
 -55.69075775,  13.0154562 ,   3.45600152,  56.45069504,  -2.23575306,
 -86.37802887],
[ -2.20296001,  -6.40410089,  35.45726395,  11.70705128, -27.56315804,
 -48.8469429 , -41.4436264 ,  -3.71027327,  39.3886528 , -31.90091515,
  -1.41529691,  47.57241821, -24.40646935,  -3.54574966,  51.71613312,
 -22.09951591,  -8.08158112,  52.24084473, -52.18990326,  12.89629078,
  19.81681442, -54.36478043,  10.05984974,  15.03584671, -55.71812057,
  -5.99541473, -11.93115997, -52.52264404,  22.49973106,   4.23564816,
 -55.69075775,  13.0154562 ,   3.45600152,  55.64630127,  -2.21561623,
 -86.08596802],
[ -2.10011935,  -6.60458708,  35.76330185,  11.52046108, -27.32893181,
 -49.02259445, -41.73961258,  -4.78126669,  38.9583168 , -32.05870819,
  -2.31357431,  47.43092728, -24.51066589,  -4.64699221,  51.57944489,
 -22.29248428,  -8.73801708,  52.052845  , -53.80495071,   7.64928436,
  18.14724159, -55.49012756,   4.86314535,  13.41648483, -55.76527786,
  -6.94572973, -11.17125034, -54.46292496,  17.72627068,   1.54122436,
 -56.31389236,  10.11889076,   3.02653003,  55.64630127,  -2.21561623,
 -86.08596802],
[ -2.10011935,  -6.60458708,  35.76330185,  11.52046108, -27.32893181,
 -49.02259445, -41.73961258,  -4.78126669,  38.9583168 , -32.05870819,
  -2.31357431,  47.43092728, -24.51066589,  -4.64699221,  51.57944489,
 -22.29248428,  -8.73801708,  52.052845  , -53.80495071,   7.64928436,
  18.14724159, -55.49012756,   4.86314535,  13.41648483, -55.76527786,
  -6.94572973, -11.17125034, -54.46292496,  17.72627068,   1.54122436,
 -56.31389236,  10.11889076,   3.02653003,   1.65383506,   4.88095284,
 -84.48429108],
[ -3.17861223,  -6.56163931,  35.45288086,  11.33876324, -28.32600975,
 -48.49614334, -41.3439064 ,  -4.35993671,  39.42687988, -32.11367416,
  -0.49498719,  47.44758224, -24.43656731,  -1.98726368,  51.78524017,
 -22.24997902,  -6.19007397,  52.43498611, -54.00201035,   7.50565386,
  17.61404419, -55.51426697,   6.699965  ,  12.49333477, -56.07873154,
  -5.05269957, -10.60435867, -53.92613602,  17.54540253,  -8.18151188,
 -56.40623856,   9.74109173,   2.5007453 ,   1.65383506,   4.88095284,
 -84.48429108],

[ -3.60874629,  -6.09728241,  35.89585876,  11.64116859, -28.7285881 ,
 -48.1866951 , -41.53497314,  -2.27379823,  39.40155029, -32.61017227,
   0.4850015 ,  47.10783386, -24.97657394,  -1.16524076,  51.55210495,
 -22.47461319,  -5.62473059,  52.40286636, -52.30432892,  14.27336121,
  18.52929878, -54.99066925,  11.10873604,  11.63738441, -56.5377388 ,
   7.84571362,  -4.97347307, -52.35540009,  21.13510323,  -9.74811268,
 -55.82134247,  12.51315212,   3.19455028,  54.70813751,  -2.63798022,
 -86.21485138],
[ -3.48697448,  -6.1761694 ,  35.71576691,  11.68697453, -28.45684433,
 -48.33662033, -41.45796967,  -2.30755258,  39.48060608, -32.51072693,
   0.4037821 ,  47.17728043, -25.00550079,  -1.02265453,  51.54110718,
 -22.29156494,  -5.88626385,  52.45230865, -54.758358  ,  -4.52749395,
  16.24285507, -56.83037949,   3.63083506,   6.31913805, -56.97734833,
   3.49228954,  -4.91851854, -56.6240387 ,   6.94846058,  -5.31448126,
 -56.61155701,   8.17865944,   3.32382965,  54.70813751,  -2.63798022,
 -86.21485138],
[ -3.48697448,  -6.1761694 ,  35.71576691,  11.68697453, -28.45684433,
 -48.33662033, -41.45796967,  -2.30755258,  39.48060608, -32.51072693,
   0.4037821 ,  47.17728043, -25.00550079,  -1.02265453,  51.54110718,
 -22.29156494,  -5.88626385,  52.45230865, -54.758358  ,  -4.52749395,
  16.24285507, -56.83037949,   3.63083506,   6.31913805, -56.97734833,
   3.49228954,  -4.91851854, -56.6240387 ,   6.94846058,  -5.31448126,
 -56.61155701,   8.17865944,   3.32382965, -70.54382324,  11.12308788,
 -86.80673218],
[ -2.6275866 ,  -6.42040873,  36.13643646,  12.72851562, -27.85990906,
 -48.42124176, -42.10291672,  -2.34303117,  38.78996277, -32.95313263,
  -0.28111511,  46.87023163, -25.60280991,  -1.74829555,  51.22739792,
 -22.70185089,  -7.1782012 ,  52.11435318, -55.14968491,  -4.5484786 ,
  14.85361958, -57.02946091,   4.45103884,   3.26114845, -56.67206573,
   5.32524061,  -6.53646326, -56.32943344,   7.03987646,  -7.76152563,
 -56.55647659,   9.10842896,   1.09896052, -58.22879028,   6.64581585,
 -86.94622803],
[ -2.6275866 ,  -6.42040873,  36.13643646,  12.72851562, -27.85990906,
 -48.42124176, -42.10291672,  -2.34303117,  38.78996277, -32.95313263,
  -0.28111511,  46.87023163, -25.60280991,  -1.74829555,  51.22739792,
 -22.70185089,  -7.1782012 ,  52.11435318, -55.14968491,  -4.5484786 ,
  14.85361958, -57.02946091,   4.45103884,   3.26114845, -56.67206573,
   5.32524061,  -6.53646326, -56.32943344,   7.03987646,  -7.76152563,
 -56.55647659,   9.10842896,   1.09896052, -62.56797409,  10.5716362 ,
 -85.6813736 ],
[ -1.94343626,  -5.81532478,  35.04920578,  11.796031  , -27.47717667,
 -48.87397003, -41.13089752,  -2.33475137,  39.81965256, -32.1319809 ,
  -0.22121347,  47.43725586, -24.74501801,  -1.58917105,  51.65234756,
 -21.91533852,  -6.7404356 ,  52.50800705, -54.92624664,  -6.10166407,
  15.12228012, -56.94433975,   5.30412722,   3.46626759, -56.68263245,
   5.48011589,  -6.31297541, -56.30334854,   7.06943798,  -7.92226839,
 -56.67390823,   8.39065266,   0.68666869, -62.56797409,  10.5716362 ,
 -85.6813736 ],
[ -1.94343626,  -5.81532478,  35.04920578,  11.796031  , -27.47717667,
 -48.87397003, -41.13089752,  -2.33475137,  39.81965256, -32.1319809 ,
  -0.22121347,  47.43725586, -24.74501801,  -1.58917105,  51.65234756,
 -21.91533852,  -6.7404356 ,  52.50800705, -54.92624664,  -6.10166407,
  15.12228012, -56.94433975,   5.30412722,   3.46626759, -56.68263245,
   5.48011589,  -6.31297541, -56.30334854,   7.06943798,  -7.92226839,
 -56.67390823,   8.39065266,   0.68666869, -64.49655151,   9.7767601 ,
 -86.19190216],
[ -3.08446288,  -6.31139755,  35.43953705,  12.13425732, -28.09199333,
 -48.43971634, -41.3705101 ,  -1.0638808 ,  39.62518692, -32.51218414,
   0.80007678,  47.17122269, -25.054842  ,  -0.55119139,  51.52433777,
 -22.64360809,  -4.81405592,  52.41085815, -55.14600372,  -5.15621805,
  14.66758537, -56.84912109,   6.90839767,   1.80503094, -56.62697983,
   5.69054985,  -6.61883545, -56.35815048,   7.46702051,  -7.12805748,
 -56.61006165,   8.83666801,   0.14272901, -64.49655151,   9.7767601 ,
 -86.19190216],
[ -3.08446288,  -6.31139755,  35.43953705,  12.13425732, -28.09199333,
 -48.43971634, -41.3705101 ,  -1.0638808 ,  39.62518692, -32.51218414,
   0.80007678,  47.17122269, -25.054842  ,  -0.55119139,  51.52433777,
 -22.64360809,  -4.81405592,  52.41085815, -55.14600372,  -5.15621805,
  14.66758537, -56.84912109,   6.90839767,   1.80503094, -56.62697983,
   5.69054985,  -6.61883545, -56.35815048,   7.46702051,  -7.12805748,
 -56.61006165,   8.83666801,   0.14272901, -67.96513367,   9.05914497,
 -86.93943024],
[ -3.40009928,  -6.55012226,  35.68513489,  12.14904881, -28.01518631,
 -48.48047638, -41.95137787,  -1.55076635,  38.9933815 , -32.67606354,
   1.23637748,  47.04840469, -25.18352509,   0.2242118 ,  51.4640274 ,
 -23.10816383,  -3.59480333,  52.30579758, -55.18940735,  -5.5338974 ,
  14.36355495, -56.52801514,   7.9984479 ,   4.83885384, -56.74055481,
   5.24056196,  -5.98770618, -56.38643265,   8.42057133,  -5.69830275,
 -56.70147324,   8.18735123,   0.84669745, -67.96513367,   9.05914497,
 -86.93943024],
[ -3.40009928,  -6.55012226,  35.68513489,  12.14904881, -28.01518631,
 -48.48047638, -41.95137787,  -1.55076635,  38.9933815 , -32.67606354,
   1.23637748,  47.04840469, -25.18352509,   0.2242118 ,  51.4640274 ,
 -23.10816383,  -3.59480333,  52.30579758, -55.18940735,  -5.5338974 ,
  14.36355495, -56.52801514,   7.9984479 ,   4.83885384, -56.74055481,
   5.24056196,  -5.98770618, -56.38643265,   8.42057133,  -5.69830275,
 -56.70147324,   8.18735123,   0.84669745, -73.31733704,   8.06820202,
 -87.91613007],
[ -3.40009928,  -6.55012226,  35.68513489,  12.14904881, -28.01518631,
 -48.48047638, -41.95137787,  -1.55076635,  38.9933815 , -32.67606354,
   1.23637748,  47.04840469, -25.18352509,   0.2242118 ,  51.4640274 ,
 -23.10816383,  -3.59480333,  52.30579758, -55.18940735,  -5.5338974 ,
  14.36355495, -56.52801514,   7.9984479 ,   4.83885384, -56.74055481,
   5.24056196,  -5.98770618, -56.38643265,   8.42057133,  -5.69830275,
 -56.70147324,   8.18735123,   0.84669745, -67.96513367,   9.05914497,
 -86.93943024],
[ -3.40009928,  -6.55012226,  35.68513489,  12.14904881, -28.01518631,
 -48.48047638, -41.95137787,  -1.55076635,  38.9933815 , -32.67606354,
   1.23637748,  47.04840469, -25.18352509,   0.2242118 ,  51.4640274 ,
 -23.10816383,  -3.59480333,  52.30579758, -55.18940735,  -5.5338974 ,
  14.36355495, -56.52801514,   7.9984479 ,   4.83885384, -56.74055481,
   5.24056196,  -5.98770618, -56.38643265,   8.42057133,  -5.69830275,
 -56.70147324,   8.18735123,   0.84669745, -73.31733704,   8.06820202,
 -87.91613007],
[  11.13351822,    2.05049849,   13.35217094,    2.21498394,  -24.22426033,
  -51.87567139,  -21.32428551,  -26.75647163,   45.95837784,  -10.52734756,
  -24.35735321,   50.78091049,    0.33677733,  -25.37738991,   51.3680954 ,
    3.82769322,  -27.90906525,   49.89227676,  -55.00580597,  -11.4224844 ,
   11.25586605,  -56.48488235,    1.27291405,    9.5207243 ,  -57.1211319 ,
    2.06875372,    3.96270204,  -57.07525253,   -3.00353432,   -4.02500343,
  -56.85503006,    3.23348951,   -6.31318426,  135.44172668,   -3.07179832,
  -93.57770538],
[  10.79854012,    3.17180371,   11.5014925 ,    0.91674733,  -25.44960403,
  -51.32527161,  -19.39752388,  -26.78821373,   46.78604507,   -8.99120808,
  -24.1594944 ,   51.16916656,    2.68885398,  -24.96222878,   51.50207138,
    5.87817335,  -27.09340286,   50.14180756,  -54.17147827,  -12.27756691,
   14.05413723,  -56.13472748,    1.09144938,   11.42399406,  -56.99934006,
    1.69363189,    5.56896257,  -56.85458374,   -5.53732252,   -4.43853235,
  -56.93667221,    3.53685784,   -5.33967829,  135.44172668,   -3.07179832,
  -93.57770538],
[  10.79854012,    3.17180371,   11.5014925 ,    0.91674733,  -25.44960403,
  -51.32527161,  -19.39752388,  -26.78821373,   46.78604507,   -8.99120808,
  -24.1594944 ,   51.16916656,    2.68885398,  -24.96222878,   51.50207138,
    5.87817335,  -27.09340286,   50.14180756,  -54.17147827,  -12.27756691,
   14.05413723,  -56.13472748,    1.09144938,   11.42399406,  -56.99934006,
    1.69363189,    5.56896257,  -56.85458374,   -5.53732252,   -4.43853235,
  -56.93667221,    3.53685784,   -5.33967829,  161.43449402,   -1.08910966,
  -94.79228973],

[   9.91508293,    2.69816041,   12.09284306,    1.30246508,  -25.56075096,
  -51.26166153,  -20.08365822,  -25.93653297,   46.97605133,  -10.46916771,
  -21.43569946,   52.09331894,    2.20396543,  -22.46942329,   52.65998459,
    4.66704369,  -25.31996918,   51.18519592,  -53.58738327,  -16.73210335,
   11.45580769,  -56.32823181,   -0.49637428,   10.47331238,  -57.16456985,
    0.62922353,    3.8239255 ,  -57.20531845,   -1.75748122,   -2.69614816,
  -56.69228363,    3.29112101,   -7.61316729,  141.02018738,   -2.97323251,
  -94.12215424],
[  10.79854012,    3.17180371,   11.5014925 ,    0.91674733,  -25.44960403,
  -51.32527161,  -19.39752388,  -26.78821373,   46.78604507,   -8.99120808,
  -24.1594944 ,   51.16916656,    2.68885398,  -24.96222878,   51.50207138,
    5.87817335,  -27.09340286,   50.14180756,  -54.17147827,  -12.27756691,
   14.05413723,  -56.13472748,    1.09144938,   11.42399406,  -56.99934006,
    1.69363189,    5.56896257,  -56.85458374,   -5.53732252,   -4.43853235,
  -56.93667221,    3.53685784,   -5.33967829,  161.43449402,   -1.08910966,
  -94.79228973],

[   9.91508293,    2.69816041,   12.09284306,    1.30246508,  -25.56075096,
  -51.26166153,  -20.08365822,  -25.93653297,   46.97605133,  -10.46916771,
  -21.43569946,   52.09331894,    2.20396543,  -22.46942329,   52.65998459,
    4.66704369,  -25.31996918,   51.18519592,  -53.58738327,  -16.73210335,
   11.45580769,  -56.32823181,   -0.49637428,   10.47331238,  -57.16456985,
    0.62922353,    3.8239255 ,  -57.20531845,   -1.75748122,   -2.69614816,
  -56.69228363,    3.29112101,   -7.61316729,  141.02018738,   -2.97323251,
  -94.12215424],
[   9.91508293,    2.69816041,   12.09284306,    1.30246508,  -25.56075096,
  -51.26166153,  -20.08365822,  -25.93653297,   46.97605133,  -10.46916771,
  -21.43569946,   52.09331894,    2.20396543,  -22.46942329,   52.65998459,
    4.66704369,  -25.31996918,   51.18519592,  -53.58738327,  -16.73210335,
   11.45580769,  -56.32823181,   -0.49637428,   10.47331238,  -57.16456985,
    0.62922353,    3.8239255 ,  -57.20531845,   -1.75748122,   -2.69614816,
  -56.69228363,    3.29112101,   -7.61316729, -179.27191162,    0.77811378,
  -95.14180756],
[   9.52229309,    2.36507702,   11.35648251,    1.20649529,  -25.79584885,
  -51.14611435,  -19.55257034,  -25.59247398,   47.38700867,   -9.37314606,
  -22.79030037,   51.72574234,    3.4156332 ,  -23.56493759,   52.11366272,
    5.87198305,  -26.05325317,   50.69077301,  -54.39416504,  -12.75995159,
   12.69901276,  -56.35247803,    2.00166368,   10.15865421,  -56.99663162,
    3.34065914,    4.79900408,  -56.99004364,   -4.23112011,   -4.12781096,
  -56.7882843 ,    4.08481503,   -6.41963387, -179.27191162,    0.77811378,
  -95.14180756],
[   9.52229309,    2.36507702,   11.35648251,    1.20649529,  -25.79584885,
  -51.14611435,  -19.55257034,  -25.59247398,   47.38700867,   -9.37314606,
  -22.79030037,   51.72574234,    3.4156332 ,  -23.56493759,   52.11366272,
    5.87198305,  -26.05325317,   50.69077301,  -54.39416504,  -12.75995159,
   12.69901276,  -56.35247803,    2.00166368,   10.15865421,  -56.99663162,
    3.34065914,    4.79900408,  -56.99004364,   -4.23112011,   -4.12781096,
  -56.7882843 ,    4.08481503,   -6.41963387,  163.75622559,   -1.08028066,
  -95.89825439],

[   9.65222454,    2.77736592,   10.72482204,    1.35951209,  -25.31497574,
  -51.38199997,  -18.87229919,  -25.79583549,   47.55226135,   -9.07814503,
  -23.31196022,   51.54557419,    2.79640889,  -21.18379784,   53.16233063,
    5.85432529,  -23.93094254,   51.72855377,  -54.02349472,  -14.16495228,
   12.79149628,  -56.70760345,    0.3350004 ,    8.18181992,  -57.15546036,
    1.0197742 ,    3.87552238,  -57.23857498,    0.53822833,   -2.50245953,
  -56.71369934,    2.68457222,   -7.6912899 , -165.69767761,    1.75850654,
  -94.09126282],
[   9.65222454,    2.77736592,   10.72482204,    1.35951209,  -25.31497574,
  -51.38199997,  -18.87229919,  -25.79583549,   47.55226135,   -9.07814503,
  -23.31196022,   51.54557419,    2.79640889,  -21.18379784,   53.16233063,
    5.85432529,  -23.93094254,   51.72855377,  -54.02349472,  -14.16495228,
   12.79149628,  -56.70760345,    0.3350004 ,    8.18181992,  -57.15546036,
    1.0197742 ,    3.87552238,  -57.23857498,    0.53822833,   -2.50245953,
  -56.71369934,    2.68457222,   -7.6912899 , -173.06492615,    1.23685992,
  -95.81272125],
[   9.27929688,    2.11518693,   11.30221748,    1.06595564,  -25.189188  ,
  -51.45070648,  -19.58808708,  -25.33999634,   47.50787354,   -9.82361507,
  -23.00917816,   51.54493713,    2.06807733,  -22.10235596,   52.82059479,
    5.08960485,  -24.1632843 ,   51.70143127,  -52.93117523,  -17.67228127,
   12.99182606,  -56.24493408,   -0.24754441,   10.9202795 ,  -57.05033112,
   -2.91010022,    4.42691565,  -57.19115067,   -2.69562888,   -2.17071772,
  -56.92456818,    1.71641028,   -6.28122663, -173.06492615,    1.23685992,
  -95.81272125],
[   9.27929688,    2.11518693,   11.30221748,    1.06595564,  -25.189188  ,
  -51.45070648,  -19.58808708,  -25.33999634,   47.50787354,   -9.82361507,
  -23.00917816,   51.54493713,    2.06807733,  -22.10235596,   52.82059479,
    5.08960485,  -24.1632843 ,   51.70143127,  -52.93117523,  -17.67228127,
   12.99182606,  -56.24493408,   -0.24754441,   10.9202795 ,  -57.05033112,
   -2.91010022,    4.42691565,  -57.19115067,   -2.69562888,   -2.17071772,
  -56.92456818,    1.71641028,   -6.28122663, -172.22494507,    2.02697349,
  -97.1798172 ],
[   9.31568241,    2.65228796,   11.83831406,    1.7375834 ,  -25.37482834,
  -51.34106827,  -19.89537048,  -25.43044662,   47.3315239 ,  -10.28220177,
  -22.8125248 ,   51.54291153,    1.81500947,  -22.56578255,   52.6336174 ,
    4.75675774,  -24.42959023,   51.6078949 ,  -53.55532837,  -14.73503494,
   14.05388451,  -56.41878891,    2.22891831,    9.73441124,  -57.16725159,
    1.77729154,    3.39898539,  -57.14687347,   -0.37327662,   -4.11115932,
  -56.44758606,    6.18550253,   -7.62993622, -172.22494507,    2.02697349,
  -97.1798172 ],
[   9.31568241,    2.65228796,   11.83831406,    1.7375834 ,  -25.37482834,
  -51.34106827,  -19.89537048,  -25.43044662,   47.3315239 ,  -10.28220177,
  -22.8125248 ,   51.54291153,    1.81500947,  -22.56578255,   52.6336174 ,
    4.75675774,  -24.42959023,   51.6078949 ,  -53.55532837,  -14.73503494,
   14.05388451,  -56.41878891,    2.22891831,    9.73441124,  -57.16725159,
    1.77729154,    3.39898539,  -57.14687347,   -0.37327662,   -4.11115932,
  -56.44758606,    6.18550253,   -7.62993622, -169.36024475,    2.03413463,
  -96.59854889],
[   9.96057606,    2.78990102,   10.44558811,    1.68329763,  -25.33814621,
  -51.36099243,  -18.61660767,  -26.06023979,   47.50886536,   -9.06941319,
  -23.01577568,   51.68003464,    3.85173535,  -25.46451378,   51.18133545,
    7.54324579,  -26.61281776,   50.17633057,  -54.09038544,  -12.62931538,
   14.05478573,  -56.40557098,    2.57455659,    9.72572803,  -56.97024536,
    2.96143103,    5.33173704,  -57.26240158,   -1.89359272,   -0.48811132,
  -56.86735535,    3.095999  ,   -6.27096033, -169.36024475,    2.03413463,
  -96.59854889],

[   9.86237049,    2.78649688,   10.53754616,    1.09657764,  -25.59714317,
  -51.24832153,  -18.70137596,  -25.97101974,   47.52442551,   -9.26172543,
  -22.59936523,   51.82948303,    3.53408194,  -23.69677734,   52.04593658,
    6.55416775,  -25.62874603,   50.82338715,  -54.72175598,  -13.16121292,
   10.72933388,  -56.7134819 ,    0.76572216,    8.11178112,  -57.16343689,
    2.1715107 ,    3.22994137,  -57.15576553,   -0.58658129,   -3.95993066,
  -56.6078949 ,    4.36168671,   -7.70247936,  168.35609436,   -0.51628256,
  -94.75992584],
[   9.47939014,    2.58118844,   10.66924953,    1.21178448,  -25.57915878,
  -51.25470352,  -18.88882828,  -25.60935974,   47.64640045,   -9.50541687,
  -22.04243279,   52.02484512,    2.94174647,  -22.20230103,   52.73718262,
    5.96295881,  -24.6055851 ,   51.39858627,  -54.5708847 ,  -14.27336788,
   10.05464172,  -56.71389771,   -0.22241299,    8.14192581,  -57.18909836,
    0.80409861,    3.40097618,  -56.62239456,   -3.90894771,   -7.83778811,
  -56.36088181,    5.9346838 ,   -8.42834473,  168.35609436,   -0.51628256,
  -94.75992584],
[   9.47939014,    2.58118844,   10.66924953,    1.21178448,  -25.57915878,
  -51.25470352,  -18.88882828,  -25.60935974,   47.64640045,   -9.50541687,
  -22.04243279,   52.02484512,    2.94174647,  -22.20230103,   52.73718262,
    5.96295881,  -24.6055851 ,   51.39858627,  -54.5708847 ,  -14.27336788,
   10.05464172,  -56.71389771,   -0.22241299,    8.14192581,  -57.18909836,
    0.80409861,    3.40097618,  -56.62239456,   -3.90894771,   -7.83778811,
  -56.36088181,    5.9346838 ,   -8.42834473,  160.92816162,   -0.83916873,
  -94.45419312],
[   9.87236023,    2.17828274,    9.80861282,    1.22692704,  -25.45757294,
  -51.31484222,  -18.24137497,  -25.91176796,   47.73509216,   -8.79773235,
  -22.33663368,   52.02384949,    3.45063066,  -23.16387939,   52.29086304,
    8.28381824,  -26.57266617,   50.08071518,  -54.63160706,  -16.30556297,
    5.68530846,  -56.90653992,   -1.87671483,    6.3976469 ,  -57.26057434,
   -0.73258138,    1.86987054,  -56.96707153,   -1.77390349,   -5.86623859,
  -56.23056793,    1.30097091,  -10.91957378,  160.92816162,   -0.83916873,
  -94.45419312],
[   9.87236023,    2.17828274,    9.80861282,    1.22692704,  -25.45757294,
  -51.31484222,  -18.24137497,  -25.91176796,   47.73509216,   -8.79773235,
  -22.33663368,   52.02384949,    3.45063066,  -23.16387939,   52.29086304,
    8.28381824,  -26.57266617,   50.08071518,  -54.63160706,  -16.30556297,
    5.68530846,  -56.90653992,   -1.87671483,    6.3976469 ,  -57.26057434,
   -0.73258138,    1.86987054,  -56.96707153,   -1.77390349,   -5.86623859,
  -56.23056793,    1.30097091,  -10.91957378,  151.2011261 ,   -1.13990676,
  -92.70146942],
[  10.10909081,    3.35594201,    9.09592533,    0.6024332 ,  -26.61331749,
  -50.73632431,  -17.251297  ,  -26.34005356,   47.86857986,   -6.69627285,
  -26.90293121,   50.14178467,    5.29759455,  -25.43069077,   51.06879425,
    9.85734367,  -27.84993744,   49.09195709,  -52.85366821,  -21.72595596,
    4.15680647,  -57.00169754,   -3.31886554,    4.75376797,  -57.23590088,
   -2.4565239 ,   -0.90748799,  -56.67943192,   -3.11160445,   -7.78245497,
  -55.502491  ,   -1.53382838,  -14.1395731 ,  151.2011261 ,   -1.13990676,
  -92.70146942],
[  10.10909081,    3.35594201,    9.09592533,    0.6024332 ,  -26.61331749,
  -50.73632431,  -17.251297  ,  -26.34005356,   47.86857986,   -6.69627285,
  -26.90293121,   50.14178467,    5.29759455,  -25.43069077,   51.06879425,
    9.85734367,  -27.84993744,   49.09195709,  -52.85366821,  -21.72595596,
    4.15680647,  -57.00169754,   -3.31886554,    4.75376797,  -57.23590088,
   -2.4565239 ,   -0.90748799,  -56.67943192,   -3.11160445,   -7.78245497,
  -55.502491  ,   -1.53382838,  -14.1395731 , -124.52056885,    2.28330255,
  -91.38443756],
[  10.08338833,    3.84305811,    9.36760044,    1.00816417,  -26.6017189 ,
  -50.73596954,  -17.3453331 ,  -26.38210678,   47.81140518,   -6.58697891,
  -28.11959076,   49.48440933,    5.59906101,  -25.60060692,   50.95160294,
    9.03452778,  -27.26655579,   49.57538605,  -53.90164566,  -17.71041679,
    7.98500443,  -56.77723312,   -4.15364885,    6.47298622,  -57.19452667,
   -3.16761756,    1.24847937,  -56.8856163 ,   -4.38627148,   -5.25296831,
  -56.16537857,    1.35799193,  -11.24332047, -124.52056885,    2.28330255,
  -91.38443756],
[  10.08338833,    3.84305811,    9.36760044,    1.00816417,  -26.6017189 ,
  -50.73596954,  -17.3453331 ,  -26.38210678,   47.81140518,   -6.58697891,
  -28.11959076,   49.48440933,    5.59906101,  -25.60060692,   50.95160294,
    9.03452778,  -27.26655579,   49.57538605,  -53.90164566,  -17.71041679,
    7.98500443,  -56.77723312,   -4.15364885,    6.47298622,  -57.19452667,
   -3.16761756,    1.24847937,  -56.8856163 ,   -4.38627148,   -5.25296831,
  -56.16537857,    1.35799193,  -11.24332047,  172.29281616,    0.28897205,
  -93.75566864],


], "float32")
print np.shape(well)
#a = np.ones((50,1), dtype=np.int)*3

#target_data = np.array([[0], [1], [2]], "float32")

#print np.reshape(np.append(training_data10,two),(53,18))
