import numpy as np

signlang = np.array([
[ -2.93862414,  64.49217987,  62.49704361,  57.17833328,   1.00632477,
   3.52588034,  49.71056747, -28.00886345,   5.21241474, -32.23141861,
   0.27384704,  47.36947632, -31.4809227 ,   8.27622128,  47.15148163,
 -27.05584717,  14.46690941,  48.38900757, -56.04682922, -11.89624214,
  -0.19713618, -39.27893829, -40.96996307,   7.83793831,  45.3716774 ,
   4.55272532,  34.69135666,  42.24119568,  11.0286026 ,  37.10603333,
  36.44638062,  18.22741508,  40.27690506, -17.1383152 , -48.66363907,
 -69.8936615 ],
[ -2.93862414,  64.49217987,  62.49704361,  57.10643005,   2.09462762,
   4.1562829 ,  49.68590927, -28.02544785,   5.35638094, -32.97792435,
  -0.21370429,  46.85314941, -32.23096466,   8.13552189,  46.66674042,
 -28.96068573,  14.27262878,  47.33262253, -56.45715714,  -9.75236988,
  -0.53607982, -42.44704056, -37.73379135,   7.56413507,  46.12880325,
   2.75500774,  33.87255478,  43.13618851,   9.96361256,  36.37034607,
  38.70198822,  17.03708839,  38.66135406, -10.19281864, -52.48163605,
 -69.28676605],
[ -1.43293583,  66.37462616,  62.05223465,  57.10643005,   2.09462762,
   4.1562829 ,  49.68590927, -28.02544785,   5.35638094, -32.97792435,
  -0.21370429,  46.85314941, -32.23096466,   8.13552189,  46.66674042,
 -28.96068573,  14.27262878,  47.33262253, -56.45715714,  -9.75236988,
  -0.53607982, -42.44704056, -37.73379135,   7.56413507,  46.12880325,
   2.75500774,  33.87255478,  43.13618851,   9.96361256,  36.37034607,
  38.70198822,  17.03708839,  38.66135406, -10.19281864, -52.48163605,
 -69.28676605],
[ -1.43293583,  66.37462616,  62.05223465,  57.11338043,   2.1397469 ,
   4.03604603,  49.87015533, -27.56475067,   5.99653864, -32.53258133,
   0.6491915 ,  47.15947723, -32.32978058,   8.77837372,  46.48152161,
 -28.24134445,  14.72416019,  47.62805939, -56.44289017,  -9.70834732,
   1.65963125, -43.70132828, -36.32339859,   7.32196379,  45.68397141,
   1.81311345,  34.53250885,  42.65446091,   9.37347889,  37.08829117,
  38.40472794,  15.83436108,  39.46081924,  -6.53241587, -55.90306091,
 -67.89597321],
[ -2.55299735,  66.97737122,  62.34273529,  57.11338043,   2.1397469 ,
   4.03604603,  49.87015533, -27.56475067,   5.99653864, -32.53258133,
   0.6491915 ,  47.15947723, -32.32978058,   8.77837372,  46.48152161,
 -28.24134445,  14.72416019,  47.62805939, -56.44289017,  -9.70834732,
   1.65963125, -43.70132828, -36.32339859,   7.32196379,  45.68397141,
   1.81311345,  34.53250885,  42.65446091,   9.37347889,  37.08829117,
  38.40472794,  15.83436108,  39.46081924,  -6.53241587, -55.90306091,
 -67.89597321],
[ -2.55299735,  66.97737122,  62.34273529,  57.19342041,   0.95239335,
   3.28820062,  49.11225128, -27.95262146,   9.45750237, -32.7950058 ,
   2.80001354,  46.89833832, -31.6141243 ,  10.21940804,  46.67887497,
 -26.08963203,  16.24398804,  48.3556633 , -56.03961945, -11.91794395,
  -0.57466751, -44.11081314, -35.6253891 ,   8.23857307,  45.2227478 ,
   3.04807448,  35.04880524,  42.13987732,  10.93889618,  37.24751663,
  36.56324387,  18.11720848,  40.22067261, -15.37992477, -44.78890991,
 -70.63861847],
[ -9.61811924,  61.60451508,  66.68051147,  57.19342041,   0.95239335,
   3.28820062,  49.11225128, -27.95262146,   9.45750237, -32.7950058 ,
   2.80001354,  46.89833832, -31.6141243 ,  10.21940804,  46.67887497,
 -26.08963203,  16.24398804,  48.3556633 , -56.03961945, -11.91794395,
  -0.57466751, -44.11081314, -35.6253891 ,   8.23857307,  45.2227478 ,
   3.04807448,  35.04880524,  42.13987732,  10.93889618,  37.24751663,
  36.56324387,  18.11720848,  40.22067261, -15.37992477, -44.78890991,
 -70.63861847],
[ -9.61811924,  61.60451508,  66.68051147,  57.06649017,   3.24918699,
   3.95786619,  51.17603683, -22.0084362 ,  13.39584064, -34.70503616,
   4.38457108,  45.3777771 , -33.66188431,  11.57326317,  44.89703369,
 -28.64080811,  17.69906616,  46.36004257, -56.84327698,  -6.63238192,
  -2.76760507, -44.74750137, -34.50122833,   9.49382496,  44.48859406,
   0.20054625,  36.10445023,  41.52280426,   8.74834633,  38.49843597,
  36.96869278,  16.80930328,  40.41743851,  -4.12528706, -51.22480392,
 -72.33110046],
[-12.50422001,  62.07073212,  71.4677124 ,  57.06649017,   3.24918699,
   3.95786619,  51.17603683, -22.0084362 ,  13.39584064, -34.70503616,
   4.38457108,  45.3777771 , -33.66188431,  11.57326317,  44.89703369,
 -28.64080811,  17.69906616,  46.36004257, -56.84327698,  -6.63238192,
  -2.76760507, -44.74750137, -34.50122833,   9.49382496,  44.48859406,
   0.20054625,  36.10445023,  41.52280426,   8.74834633,  38.49843597,
  36.96869278,  16.80930328,  40.41743851,  -4.12528706, -51.22480392,
 -72.33110046],
[-12.50422001,  62.07073212,  71.4677124 ,  57.15305328,   2.90109801,
   2.81397748,  52.89707565, -18.144701  ,  12.46898556, -35.11030579,
   4.05372477,  45.09590149, -33.51857376,  11.25859261,  45.08387375,
 -29.0605526 ,  17.28958321,  46.25322723, -55.63386536, -13.47737122,
   2.45765662, -37.18349075, -41.15135574,  14.37916374,  46.66423035,
   8.2694912 ,  32.20049286,  42.85387039,  16.19580078,  34.40999985,
  36.54717636,  24.7811451 ,  36.51034164, -34.32720566, -43.33023453,
 -76.54472351],
[-13.09484386,  59.66543961,  71.50045776,  57.15305328,   2.90109801,
   2.81397748,  52.89707565, -18.144701  ,  12.46898556, -35.11030579,
   4.05372477,  45.09590149, -33.51857376,  11.25859261,  45.08387375,
 -29.0605526 ,  17.28958321,  46.25322723, -55.63386536, -13.47737122,
   2.45765662, -37.18349075, -41.15135574,  14.37916374,  46.66423035,
   8.2694912 ,  32.20049286,  42.85387039,  16.19580078,  34.40999985,
  36.54717636,  24.7811451 ,  36.51034164, -34.32720566, -43.33023453,
 -76.54472351],
[-13.09484386,  59.66543961,  71.50045776,  57.11074448,   2.77567911,
   3.66944909,  52.72997284, -16.77307701,  14.86674881, -36.6732254 ,
   6.17903137,  43.58555603, -35.08903122,  13.70193577,  43.17201614,
 -29.88581467,  19.64176178,  44.76433563, -56.22882462, -10.76072979,
   2.30919385, -36.10314178, -41.52678299,  15.96546173,  47.07688141,
   9.11233616,  31.3614254 ,  42.93917847,  16.95782661,  33.93325424,
  36.33680344,  26.15917969,  35.75108719, -36.75110245, -46.8388176 ,
 -77.70560455],
[-18.33658218,  64.35906982,  73.51717377,  57.11074448,   2.77567911,
   3.66944909,  52.72997284, -16.77307701,  14.86674881, -36.6732254 ,
   6.17903137,  43.58555603, -35.08903122,  13.70193577,  43.17201614,
 -29.88581467,  19.64176178,  44.76433563, -56.22882462, -10.76072979,
   2.30919385, -36.10314178, -41.52678299,  15.96546173,  47.07688141,
   9.11233616,  31.3614254 ,  42.93917847,  16.95782661,  33.93325424,
  36.33680344,  26.15917969,  35.75108719, -36.75110245, -46.8388176 ,
 -77.70560455],
[-18.33658218,  64.35906982,  73.51717377,  57.0967865 ,   3.63616228,
   3.08894849,  53.20292282, -15.9987793 ,  14.01050949, -36.24571228,
   5.74481058,  44.00058746, -34.45523453,  13.26424503,  43.81441879,
 -29.84175873,  19.26329803,  44.9577713 , -56.52284622,  -9.30092621,
   1.21132255, -36.26161194, -41.7829361 ,  14.90262413,  48.48501968,
   8.74200821,  29.25040817,  44.4175415 ,  16.71382904,  32.10197067,
  37.79045868,  26.07014847,  34.27878189, -34.3056488 , -47.35151291,
 -76.96399689],
[-17.03439331,  64.1443634 ,  72.66017914,  57.0967865 ,   3.63616228,
   3.08894849,  53.20292282, -15.9987793 ,  14.01050949, -36.24571228,
   5.74481058,  44.00058746, -34.45523453,  13.26424503,  43.81441879,
 -29.84175873,  19.26329803,  44.9577713 , -56.52284622,  -9.30092621,
   1.21132255, -36.26161194, -41.7829361 ,  14.90262413,  48.48501968,
   8.74200821,  29.25040817,  44.4175415 ,  16.71382904,  32.10197067,
  37.79045868,  26.07014847,  34.27878189, -34.3056488 , -47.35151291,
 -76.96399689],
[-17.03439331,  64.1443634 ,  72.66017914,  57.18060684,   1.60567582,
   3.25675821,  52.58185577, -16.90628815,  15.23588657, -36.38206482,
   7.29173422,  43.65755844, -33.89525223,  14.66405773,  43.80506516,
 -27.8252964 ,  20.34019279,  45.76937866, -56.55487823,  -9.13311958,
   0.96869063, -36.35766983, -42.00117493,  14.02952671,  47.70024109,
   9.40724659,  30.31496429,  44.7793045 ,  17.55943298,  31.13337135,
  38.51778412,  25.7297039 ,  33.72193909, -35.61501694, -47.0437851 ,
 -76.04614258],
[-29.84828186,  55.15904999,  75.00429535,  57.18060684,   1.60567582,
   3.25675821,  52.58185577, -16.90628815,  15.23588657, -36.38206482,
   7.29173422,  43.65755844, -33.89525223,  14.66405773,  43.80506516,
 -27.8252964 ,  20.34019279,  45.76937866, -56.55487823,  -9.13311958,
   0.96869063, -36.35766983, -42.00117493,  14.02952671,  47.70024109,
   9.40724659,  30.31496429,  44.7793045 ,  17.55943298,  31.13337135,
  38.51778412,  25.7297039 ,  33.72193909, -35.61501694, -47.0437851 ,
 -76.04614258],
[-29.84828186,  55.15904999,  75.00429535,  57.00170898,   4.14237785,
   4.05614233,  53.61839676, -12.17934036,  16.11017609, -35.8350029 ,
   6.13757133,  44.28306198, -34.27269363,  14.04860973,  43.71298981,
 -28.54380798,  19.91613388,  45.5126915 , -56.79075623,  -7.30117273,
   2.07593656, -40.29341507, -39.57995224,   9.62676907,  44.76153564,
   6.31542444,  35.20407104,  40.80361557,  14.49719238,  37.51936722,
  34.87252426,  22.55617142,  39.47065735, -19.08293343, -55.50973511,
 -69.29104614],
[-26.56320953,  57.6612854 ,  76.12818909,  57.00170898,   4.14237785,
   4.05614233,  53.61839676, -12.17934036,  16.11017609, -35.8350029 ,
   6.13757133,  44.28306198, -34.27269363,  14.04860973,  43.71298981,
 -28.54380798,  19.91613388,  45.5126915 , -56.79075623,  -7.30117273,
   2.07593656, -40.29341507, -39.57995224,   9.62676907,  44.76153564,
   6.31542444,  35.20407104,  40.80361557,  14.49719238,  37.51936722,
  34.87252426,  22.55617142,  39.47065735, -19.08293343, -55.50973511,
 -69.29104614],
[-26.56320953,  57.6612854 ,  76.12818909,  56.91549301,   5.69244814,
   3.3210268 ,  54.7039032 ,  -9.17604351,  14.35581779, -35.40714264,
   3.39340782,  44.91798401, -33.54688263,  11.66221905,  44.96004486,
 -27.86050034,  17.71469498,  46.82722092, -56.88976288,  -6.80774021,
   0.12590006, -39.96514893, -39.97317505,   9.36689281,  44.5820694 ,
   6.30714464,  35.43254471,  39.74772263,  14.61470413,  38.59190369,
  33.73692703,  22.95879745,  40.21840286, -17.77527809, -59.38457489,
 -68.09931183],
[-17.04104996,  57.2242775 ,  74.89250946,  56.91549301,   5.69244814,
   3.3210268 ,  54.7039032 ,  -9.17604351,  14.35581779, -35.40714264,
   3.39340782,  44.91798401, -33.54688263,  11.66221905,  44.96004486,
 -27.86050034,  17.71469498,  46.82722092, -56.88976288,  -6.80774021,
   0.12590006, -39.96514893, -39.97317505,   9.36689281,  44.5820694 ,
   6.30714464,  35.43254471,  39.74772263,  14.61470413,  38.59190369,
  33.73692703,  22.95879745,  40.21840286, -17.77527809, -59.38457489,
 -68.09931183],
[-17.04104996,  57.2242775 ,  74.89250946,  56.59051895,   7.53665447,
   4.84957075,  54.8877182 ,  -6.99412394,  14.87370396, -35.62358856,
   4.5811038 ,  44.64056396, -33.39259338,  12.92841148,  44.72803879,
 -30.02345657,  19.36765671,  44.79165649, -56.37060547,  -9.74593163,
  -3.1902957 , -46.19548798, -33.89357376,   0.09288914,  37.71112061,
  -2.05269504,  43.08670807,  31.35713959,   4.61853743,  47.73055267,
  25.0964241 ,  15.54096889,  49.10655975,  -7.66595936, -43.57148361,
 -64.00108337],
[ -9.40667152,  73.99275208,  74.17700958,  56.59051895,   7.53665447,
   4.84957075,  54.8877182 ,  -6.99412394,  14.87370396, -35.62358856,
   4.5811038 ,  44.64056396, -33.39259338,  12.92841148,  44.72803879,
 -30.02345657,  19.36765671,  44.79165649, -56.37060547,  -9.74593163,
  -3.1902957 , -46.19548798, -33.89357376,   0.09288914,  37.71112061,
  -2.05269504,  43.08670807,  31.35713959,   4.61853743,  47.73055267,
  25.0964241 ,  15.54096889,  49.10655975,  -7.66595936, -43.57148361,
 -64.00108337],
[ -9.40667152,  73.99275208,  74.17700958,  56.89966202,   5.13045406,
   4.3489213 ,  55.59883118,  -7.23671436,  11.79858208, -33.4996109 ,
   2.00455904,  46.4388237 , -30.74877167,   9.66760063,  47.36936569,
 -27.59901047,  16.10317612,  47.55826569, -55.8497467 , -11.80125999,
  -4.93380356, -42.70340347, -37.96146774,   4.26059771,  36.62099838,
  -0.11146567,  44.06468582,  30.56665802,   5.60241318,  48.13624954,
  21.18108368,  19.45512772,  49.55467987, -19.52271271, -35.22974396,
 -68.78264618],
[ -6.18862724,  63.47019577,  70.84700775,  56.89966202,   5.13045406,
   4.3489213 ,  55.59883118,  -7.23671436,  11.79858208, -33.4996109 ,
   2.00455904,  46.4388237 , -30.74877167,   9.66760063,  47.36936569,
 -27.59901047,  16.10317612,  47.55826569, -55.8497467 , -11.80125999,
  -4.93380356, -42.70340347, -37.96146774,   4.26059771,  36.62099838,
  -0.11146567,  44.06468582,  30.56665802,   5.60241318,  48.13624954,
  21.18108368,  19.45512772,  49.55467987, -19.52271271, -35.22974396,
 -68.78264618],
[ -6.18862724,  63.47019577,  70.84700775,  56.90949249,   5.44656277,
   3.80146217,  56.21776199,  -5.79262733,   9.42419052, -32.2832222 ,
   2.4534812 ,  47.27135086, -30.29595947,   9.99277973,  47.59312439,
 -27.48823357,  16.39381599,  47.52311325, -56.33267212,  -9.41855049,
  -4.55272865, -46.03950882, -32.86087036,   9.12870884,  33.20428085,
   1.78163147,  46.65948868,  25.78570557,   6.96588039,  50.68905258,
  15.7859745 ,  22.04484749,  50.47409439, -27.87850571, -36.03321838,
 -73.25673676],
[ -3.97075963,  69.22386932,  68.15590668,  56.90949249,   5.44656277,
   3.80146217,  56.21776199,  -5.79262733,   9.42419052, -32.2832222 ,
   2.4534812 ,  47.27135086, -30.29595947,   9.99277973,  47.59312439,
 -27.48823357,  16.39381599,  47.52311325, -56.33267212,  -9.41855049,
  -4.55272865, -46.03950882, -32.86087036,   9.12870884,  33.20428085,
   1.78163147,  46.65948868,  25.78570557,   6.96588039,  50.68905258,
  15.7859745 ,  22.04484749,  50.47409439, -27.87850571, -36.03321838,
 -73.25673676],
[ -3.97075963,  69.22386932,  68.15590668,  57.06801605,   4.16338396,
   2.9519608 ,  56.95180893,  -5.56098795,   2.89368463, -29.22950554,
  -4.78254509,  49.04660797, -24.81157303,   2.30375767,  51.59346008,
 -20.81188393,   9.47706699,  52.53434372, -56.23204041,  -8.25315952,
  -7.25598907, -49.82485199, -26.30469513,  10.40930939,  28.47319984,
  -0.28791451,  49.71921539,  19.28042984,   3.79111099,  53.82099152,
   9.16929913,  16.63774681,  54.05474472, -36.42630768, -27.36085701,
 -76.29181671],
[  7.87022829,  64.11457825,  60.46688843,  57.06801605,   4.16338396,
   2.9519608 ,  56.95180893,  -5.56098795,   2.89368463, -29.22950554,
  -4.78254509,  49.04660797, -24.81157303,   2.30375767,  51.59346008,
 -20.81188393,   9.47706699,  52.53434372, -56.23204041,  -8.25315952,
  -7.25598907, -49.82485199, -26.30469513,  10.40930939,  28.47319984,
  -0.28791451,  49.71921539,  19.28042984,   3.79111099,  53.82099152,
   9.16929913,  16.63774681,  54.05474472, -36.42630768, -27.36085701,
 -76.29181671],
[  7.71752071,  70.00174713,  53.56019592,  56.69488907,   5.55422878,
   6.13569403,  56.51097488,  -5.23755455,   7.86666107, -37.7385788 ,
   0.92597282,  43.10160828, -37.17662811,   9.02429581,  42.65286255,
 -32.80830383,  15.8564043 ,  44.21533585, -55.74433136, -11.68675137,
  -6.22863436, -44.21450424, -29.21576309,  21.77896309,  24.18546104,
   4.89181948,  51.71015549,  14.03562641,   6.14347458,  55.20928574,
   4.25460482,  14.60398769,  55.23973465, -95.04923248,  23.14488029,
 -91.47768402],
[  1.21741557,  74.35856628,  63.6496315 ,  56.69488907,   5.55422878,
   6.13569403,  56.51097488,  -5.23755455,   7.86666107, -37.7385788 ,
   0.92597282,  43.10160828, -37.17662811,   9.02429581,  42.65286255,
 -32.80830383,  15.8564043 ,  44.21533585, -55.74433136, -11.68675137,
  -6.22863436, -44.21450424, -29.21576309,  21.77896309,  24.18546104,
   4.89181948,  51.71015549,  14.03562641,   6.14347458,  55.20928574,
   4.25460482,  14.60398769,  55.23973465, -95.04923248,  23.14488029,
 -91.47768402],
[   1.21741557,   74.35856628,   63.6496315 ,   56.72502518,    7.22759771,
    3.58324742,   57.08799362,   -2.76954007,    4.01215792,  -33.95359421,
   -1.74190176,   46.11860657,  -33.36158371,    6.34518576,   46.14704514,
  -30.45388794,   12.53151989,   46.88633347,  -55.64793777,  -13.0207119 ,
   -4.07115173,  -41.69152832,  -30.37889862,   24.93481827,   23.20655441,
    9.00971699,   51.60511017,   10.7572031 ,    8.03171825,   55.70081329,
    2.63871479,   14.5418644 ,   55.35682297, -105.56783295,   52.29378128,
  -95.94441986],
[   6.51321125,   74.51617432,   60.42230606,   56.72502518,    7.22759771,
    3.58324742,   57.08799362,   -2.76954007,    4.01215792,  -33.95359421,
   -1.74190176,   46.11860657,  -33.36158371,    6.34518576,   46.14704514,
  -30.45388794,   12.53151989,   46.88633347,  -55.64793777,  -13.0207119 ,
   -4.07115173,  -41.69152832,  -30.37889862,   24.93481827,   23.20655441,
    9.00971699,   51.60511017,   10.7572031 ,    8.03171825,   55.70081329,
    2.63871479,   14.5418644 ,   55.35682297, -105.56783295,   52.29378128,
  -95.94441986],
[   6.51321125,   74.51617432,   60.42230606,   56.77909851,    7.08003521,
    2.96875882,   57.23461151,   -2.38281226,   -1.15225899,  -32.63624954,
   -6.14839458,   46.68917084,  -30.18016052,    1.71020484,   48.67277908,
  -26.14888382,    8.28321266,   50.30338669,  -56.22379684,  -10.13823032,
   -4.34827471,  -44.17988968,  -27.0560894 ,   24.47267532,   15.361866  ,
    9.97433949,   54.28933716,   -8.04795361,    4.48753357,   56.54996872,
  -13.49435043,    8.29389954,   55.06287384, -102.79690552,   63.26121902,
  -94.313797  ],
[  11.51586151,   71.85492706,   54.3112793 ,   56.77909851,    7.08003521,
    2.96875882,   57.23461151,   -2.38281226,   -1.15225899,  -32.63624954,
   -6.14839458,   46.68917084,  -30.18016052,    1.71020484,   48.67277908,
  -26.14888382,    8.28321266,   50.30338669,  -56.22379684,  -10.13823032,
   -4.34827471,  -44.17988968,  -27.0560894 ,   24.47267532,   15.361866  ,
    9.97433949,   54.28933716,   -8.04795361,    4.48753357,   56.54996872,
  -13.49435043,    8.29389954,   55.06287384, -102.79690552,   63.26121902,
  -94.313797  ],
[ 11.51586151,  71.85492706,  54.3112793 ,  56.49089432,   8.01752949,
   5.2253809 ,  57.12838745,  -2.3067975 ,   3.71919465, -36.33998489,
  -3.18809962,  44.18198776, -34.07424927,   4.6081295 ,  45.83139801,
 -29.18214035,  11.10369873,  48.04078674, -56.66907501,  -3.62561464,
  -7.63395071, -51.98469162, -22.52882385,   8.53522968,  19.54766846,
   3.8266592 ,  53.72198486, -25.59042549,  -1.53314841,  51.24047089,
 -29.86022758,   5.14939737,  48.62773895, -37.12871552, -45.29190826,
 -77.24358368],
[  9.33755398,  75.80529022,  58.05408096,  56.49089432,   8.01752949,
   5.2253809 ,  57.12838745,  -2.3067975 ,   3.71919465, -36.33998489,
  -3.18809962,  44.18198776, -34.07424927,   4.6081295 ,  45.83139801,
 -29.18214035,  11.10369873,  48.04078674, -56.66907501,  -3.62561464,
  -7.63395071, -51.98469162, -22.52882385,   8.53522968,  19.54766846,
   3.8266592 ,  53.72198486, -25.59042549,  -1.53314841,  51.24047089,
 -29.86022758,   5.14939737,  48.62773895, -37.12871552, -45.29190826,
 -77.24358368],
[  9.33755398,  75.80529022,  58.05408096,  56.95611954,   5.11209726,
   3.55996156,  57.26541138,  -1.83800352,   0.31710491, -34.97684097,
  -4.56872892,  45.15034485, -32.25656509,   3.13948321,  47.24895859,
 -27.25688934,   9.20904255,  49.54858017, -56.51551437,  -2.9621017 ,
  -8.94591141, -52.75414658, -21.99882889,   3.98221922,  23.38211823,
  -2.68939042,  52.23839569, -16.51698685,  -5.6377883 ,  54.5729866 ,
 -23.4624691 ,   1.79205787,  52.24085999, -18.12483597, -40.46123505,
 -72.23583221],
[  8.67141914,  71.10681152,  55.15262985,  56.95611954,   5.11209726,
   3.55996156,  57.26541138,  -1.83800352,   0.31710491, -34.97684097,
  -4.56872892,  45.15034485, -32.25656509,   3.13948321,  47.24895859,
 -27.25688934,   9.20904255,  49.54858017, -56.51551437,  -2.9621017 ,
  -8.94591141, -52.75414658, -21.99882889,   3.98221922,  23.38211823,
  -2.68939042,  52.23839569, -16.51698685,  -5.6377883 ,  54.5729866 ,
 -23.4624691 ,   1.79205787,  52.24085999, -18.12483597, -40.46123505,
 -72.23583221],
[  8.67141914,  71.10681152,  55.15262985,  56.42242813,   6.12141514,
   7.86412525,  56.82842636,  -2.07777381,   7.00138998, -39.22508621,
   1.52995169,  41.73557281, -37.77027893,   9.34140968,  42.05889511,
 -33.4822197 ,  15.74363708,  43.7479744 , -56.48622513,  -2.97498608,
  -9.12482357, -54.35145187, -18.11412239,   0.77741998,  21.47027779,
  -6.20948792,  52.75675964, -13.38995552,  -6.2299633 ,  55.35976028,
 -18.79685402,   1.68205523,  54.09857178,  -4.34930658, -45.84112167,
 -68.43708801],
[  1.93190789,  81.66763306,  61.790905  ,  56.42242813,   6.12141514,
   7.86412525,  56.82842636,  -2.07777381,   7.00138998, -39.22508621,
   1.52995169,  41.73557281, -37.77027893,   9.34140968,  42.05889511,
 -33.4822197 ,  15.74363708,  43.7479744 , -56.48622513,  -2.97498608,
  -9.12482357, -54.35145187, -18.11412239,   0.77741998,  21.47027779,
  -6.20948792,  52.75675964, -13.38995552,  -6.2299633 ,  55.35976028,
 -18.79685402,   1.68205523,  54.09857178,  -4.34930658, -45.84112167,
 -68.43708801],
[ 11.359025  ,  61.41482162,  55.66083145,  56.98797607,   3.93762112,
   4.43530226,  57.21165466,  -2.10125899,   2.28420258, -34.19844055,
  -2.48043513,  45.90338135, -32.69245148,   5.41854858,  46.74023056,
 -27.87031937,  11.865798  ,  48.63388443, -56.19346619,   0.6588456 ,
 -11.16543102, -56.70380783,  -6.77571726,  -4.64482689,  22.04213905,
  -9.87522602,  51.95604324, -13.79144001,  -5.01162195,  55.38489151,
 -16.54785347,   3.4764545 ,  54.74385071,  13.95756054, -58.92999268,
 -62.14139557],
[  4.60664701,  71.99985504,  56.60969925,  56.98797607,   3.93762112,
   4.43530226,  57.21165466,  -2.10125899,   2.28420258, -34.19844055,
  -2.48043513,  45.90338135, -32.69245148,   5.41854858,  46.74023056,
 -27.87031937,  11.865798  ,  48.63388443, -56.19346619,   0.6588456 ,
 -11.16543102, -56.70380783,  -6.77571726,  -4.64482689,  22.04213905,
  -9.87522602,  51.95604324, -13.79144001,  -5.01162195,  55.38489151,
 -16.54785347,   3.4764545 ,  54.74385071,  13.95756054, -58.92999268,
 -62.14139557],
[  4.60664701,  71.99985504,  56.60969925,  57.09376526,   4.76016235,
   0.67009872,  57.07309723,   3.88208437,  -3.22450709, -34.99107361,
  -9.53318405,  44.35707092, -34.22662354,  -1.84231269,  45.91242218,
 -26.76935959,   4.04485178,  50.49600983, -55.97636795,  -6.53333998,
 -10.3328619 , -54.95068741, -16.21852684,  -0.43344843,  25.1185894 ,
  -8.99631786,  50.70433044,  -5.68501425,  -8.56106567,  56.3666153 ,
 -10.3478384 ,  -0.54541242,  56.35096359,  -0.53859746, -41.86067581,
 -68.05025482],
[ 13.5493269 ,  65.78334808,  52.57062149,  57.09376526,   4.76016235,
   0.67009872,  57.07309723,   3.88208437,  -3.22450709, -34.99107361,
  -9.53318405,  44.35707092, -34.22662354,  -1.84231269,  45.91242218,
 -26.76935959,   4.04485178,  50.49600983, -55.97636795,  -6.53333998,
 -10.3328619 , -54.95068741, -16.21852684,  -0.43344843,  25.1185894 ,
  -8.99631786,  50.70433044,  -5.68501425,  -8.56106567,  56.3666153 ,
 -10.3478384 ,  -0.54541242,  56.35096359,  -0.53859746, -41.86067581,
 -68.05025482],
[ 11.55505562,  67.96868896,  55.38385391,  57.20177078,   3.20296741,
   0.7106815 ,  57.14281845,  -1.48551464,  -3.91125846, -36.44905472,
  -8.72418022,  43.33776093, -34.43338394,  -0.99888474,  45.78373718,
 -28.62326241,   5.14132118,  49.36680984, -56.00192642,  -6.09063387,
 -10.46398067, -55.78372574, -13.06241226,   0.59631777,  22.59031487,
 -10.34046745,  51.62904739,  -5.41860771,  -9.40357113,  56.25849152,
 -10.26574802,  -1.19534242,  56.35593796,  -1.29439938, -39.01594162,
 -69.37619781],
[ 12.53124619,  67.41104126,  52.19369125,  57.20177078,   3.20296741,
   0.7106815 ,  57.14281845,  -1.48551464,  -3.91125846, -36.44905472,
  -8.72418022,  43.33776093, -34.43338394,  -0.99888474,  45.78373718,
 -28.62326241,   5.14132118,  49.36680984, -56.00192642,  -6.09063387,
 -10.46398067, -55.78372574, -13.06241226,   0.59631777,  22.59031487,
 -10.34046745,  51.62904739,  -5.41860771,  -9.40357113,  56.25849152,
 -10.26574802,  -1.19534242,  56.35593796,  -1.29439938, -39.01594162,
 -69.37619781],
[ 12.53124619,  67.41104126,  52.19369125,  57.15709305,   3.78248787,
  -1.25131285,  56.71644592,   2.74945164,  -7.64797401, -34.08861923,
 -14.48974991,  43.71292496, -33.12814331,  -6.77089787,  46.25459671,
 -22.87995148,  -0.83801162,  52.52248764, -55.93215942,  -8.37613487,
  -9.17825603, -51.54465866, -24.92538643,   2.16328859,  23.86116982,
  -7.63038015,  51.52890778,   3.05157256,  -6.28826475,  56.86784744,
  -1.50089538,   2.08450127,  57.23817444, -12.24489021, -35.37704086,
 -70.93442535],
[ 19.06328011,  64.17747498,  49.2097435 ,  57.15709305,   3.78248787,
  -1.25131285,  56.71644592,   2.74945164,  -7.64797401, -34.08861923,
 -14.48974991,  43.71292496, -33.12814331,  -6.77089787,  46.25459671,
 -22.87995148,  -0.83801162,  52.52248764, -55.93215942,  -8.37613487,
  -9.17825603, -51.54465866, -24.92538643,   2.16328859,  23.86116982,
  -7.63038015,  51.52890778,   3.05157256,  -6.28826475,  56.86784744,
  -1.50089538,   2.08450127,  57.23817444, -12.24489021, -35.37704086,
 -70.93442535],
[ 19.06328011,  64.17747498,  49.2097435 ,  57.15709305,   3.78248787,
  -1.25131285,  56.71644592,   2.74945164,  -7.64797401, -34.08861923,
 -14.48974991,  43.71292496, -33.12814331,  -6.77089787,  46.25459671,
 -22.87995148,  -0.83801162,  52.52248764, -55.93215942,  -8.37613487,
  -9.17825603, -51.54465866, -24.92538643,   2.16328859,  23.86116982,
  -7.63038015,  51.52890778,   3.05157256,  -6.28826475,  56.86784744,
  -1.50089538,   2.08450127,  57.23817444, -12.24489021, -35.37704086,
 -70.93442535]
], "float32")
print np.shape(signlang)
