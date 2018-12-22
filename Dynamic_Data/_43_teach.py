import numpy as np

teach = np.array([
[ 16.47098351,  80.8984375 ,   3.31730151,  21.90367699,  21.69822121,
 -48.29308701,  -4.35940266, -26.01178932,  50.86441422,   0.23541312,
 -18.56579399,  54.20389557,   0.18423308,  -8.95143986,  56.5919075 ,
   7.60495663,  -2.56333089,  56.73094559, -39.54180908, -31.94717598,
 -26.43160629, -22.40976334, -51.01597595, -13.34087849,  34.5413208 ,
  13.33446026,  43.72522736,  26.11906815,  12.1972456 ,  49.51593399,
  22.18221092,  10.76972675,  51.71817017, -41.8135376 ,  28.70383644,
 -38.86557388],
[ 16.56061172,  81.36062622,   3.987818  ,  22.13790512,  25.45279503,
 -46.31279373,  -5.44732141, -25.49815559,  51.01937866,  -0.32209316,
 -18.27735329,  54.3013916 ,  -0.68402857,  -8.71128464,  56.6255455 ,
   6.8404994 ,  -2.54374456,  56.82907104, -38.198246  , -32.94795609,
 -27.16859436, -20.451828  , -51.62299728, -14.12781525,  35.37113953,
   6.7426939 ,  44.56708527,  26.96786499,   5.07684326,  50.29678345,
  22.64164925,   4.08664179,  52.47343826, -41.56033707,  30.38123512,
 -37.77719498],
[ 16.56061172,  81.36062622,   3.987818  ,  22.13790512,  25.45279503,
 -46.31279373,  -5.44732141, -25.49815559,  51.01937866,  -0.32209316,
 -18.27735329,  54.3013916 ,  -0.68402857,  -8.71128464,  56.6255455 ,
   6.8404994 ,  -2.54374456,  56.82907104, -38.198246  , -32.94795609,
 -27.16859436, -20.451828  , -51.62299728, -14.12781525,  35.37113953,
   6.7426939 ,  44.56708527,  26.96786499,   5.07684326,  50.29678345,
  22.64164925,   4.08664179,  52.47343826, -41.53659439,  30.51058578,
 -37.6918335 ],
[ 19.24574089,  82.65771484,   3.81697273,  20.81922531,  27.17967224,
 -45.94161224,  -4.57729149, -27.88499451,  49.84257126,  -0.5061422 ,
 -20.27794456,  53.58502579,  -0.182843  , -10.84053326,  56.26060867,
   6.7285285 ,  -4.95264816,  56.6833725 , -38.133358  , -33.34512711,
 -26.77229691, -21.41883278, -51.44097519, -13.3366394 ,  35.23965454,
   7.07545424,  44.61962509,  26.71133804,   5.78562689,  50.35709763,
  22.34218216,   4.8309865 ,  52.53850937, -41.53659439,  30.51058578,
 -37.6918335 ],
[ 19.24574089,  82.65771484,   3.81697273,  20.81922531,  27.17967224,
 -45.94161224,  -4.57729149, -27.88499451,  49.84257126,  -0.5061422 ,
 -20.27794456,  53.58502579,  -0.182843  , -10.84053326,  56.26060867,
   6.7285285 ,  -4.95264816,  56.6833725 , -38.133358  , -33.34512711,
 -26.77229691, -21.41883278, -51.44097519, -13.3366394 ,  35.23965454,
   7.07545424,  44.61962509,  26.71133804,   5.78562689,  50.35709763,
  22.34218216,   4.8309865 ,  52.53850937, -41.59569168,  30.24115181,
 -37.82824326],
[ 18.32706642,  82.75849152,   4.42480135,  21.83753967,  27.43575668,
 -45.31233215,  -5.07048559, -26.8588829 ,  50.35570526,  -1.3334626 ,
 -19.14736748,  53.98524475,  -0.87918597,  -9.64078236,  56.4720192 ,
   6.08873844,  -4.01174021,  56.82991791, -38.41012955, -33.12322235,
 -26.65184021, -22.02203751, -51.2702179 , -13.00772572,  35.14262009,
   9.33205891,  44.27996445,  26.27283287,   8.04476357,  50.27749252,
  21.46327782,   7.01889658,  52.65803909, -41.59569168,  30.24115181,
 -37.82824326],
[ 18.32706642,  82.75849152,   4.42480135,  21.83753967,  27.43575668,
 -45.31233215,  -5.07048559, -26.8588829 ,  50.35570526,  -1.3334626 ,
 -19.14736748,  53.98524475,  -0.87918597,  -9.64078236,  56.4720192 ,
   6.08873844,  -4.01174021,  56.82991791, -38.41012955, -33.12322235,
 -26.65184021, -22.02203751, -51.2702179 , -13.00772572,  35.14262009,
   9.33205891,  44.27996445,  26.27283287,   8.04476357,  50.27749252,
  21.46327782,   7.01889658,  52.65803909, -41.62734604,  30.07707977,
 -37.90752792],
[ 18.96898651,  82.27695465,   5.16580582,  22.82365417,  25.44878387,
 -45.98094177,  -5.80505705, -26.81874657,  50.29774094,  -2.54784083,
 -19.40246582,  53.8503418 ,  -1.99832916, -10.0998106 ,  56.36317062,
   5.49243069,  -4.71100378,  56.83701324, -38.48641586, -33.05552292,
 -26.62582779, -21.65927124, -51.23033905, -13.75262642,  35.08011627,
   8.6801405 ,  44.46175003,  26.03329468,   7.33364487,  50.51031113,
  21.22741318,   7.3160162 ,  52.71317673, -41.62734604,  30.07707977,
 -37.90752792],
[ 18.96898651,  82.27695465,   5.16580582,  22.82365417,  25.44878387,
 -45.98094177,  -5.80505705, -26.81874657,  50.29774094,  -2.54784083,
 -19.40246582,  53.8503418 ,  -1.99832916, -10.0998106 ,  56.36317062,
   5.49243069,  -4.71100378,  56.83701324, -38.48641586, -33.05552292,
 -26.62582779, -21.65927124, -51.23033905, -13.75262642,  35.08011627,
   8.6801405 ,  44.46175003,  26.03329468,   7.33364487,  50.51031113,
  21.22741318,   7.3160162 ,  52.71317673, -41.48614502,  29.99663353,
 -37.61460876],
[ 16.98436737,  82.5453949 ,   4.53444099,  24.06546402,  20.06801033,
 -47.96805954,  -5.61684704, -24.69474602,  51.39481354,  -1.85733247,
 -17.51144981,  54.52252579,  -1.72448421,  -8.11198139,  56.69240189,
   6.02162695,  -2.71878886,  56.91357422, -38.59649658, -33.09923935,
 -26.41130447, -22.73287582, -50.93021774, -13.12005329,  34.8118782 ,
  10.92713356,  44.17620468,  25.83396721,   9.54273129,  50.24290085,
  21.93162727,   9.49894619,  52.07283783, -41.48614502,  29.99663353,
 -37.61460876],
[ 16.98436737,  82.5453949 ,   4.53444099,  24.06546402,  20.06801033,
 -47.96805954,  -5.61684704, -24.69474602,  51.39481354,  -1.85733247,
 -17.51144981,  54.52252579,  -1.72448421,  -8.11198139,  56.69240189,
   6.02162695,  -2.71878886,  56.91357422, -38.59649658, -33.09923935,
 -26.41130447, -22.73287582, -50.93021774, -13.12005329,  34.8118782 ,
  10.92713356,  44.17620468,  25.83396721,   9.54273129,  50.24290085,
  21.93162727,   9.49894619,  52.07283783, -41.45622253,  29.97944832,
 -37.55211258],
[ 13.70485783,  80.52088928,   4.77158403,  23.84579086,  21.80143356,
 -47.31682968,  -6.49073362, -21.75024223,  52.60802078,  -4.21434069,
 -14.83629799,  55.18088531,  -2.48512554,  -5.19366884,  57.00575638,
   6.25506735,   0.14475137,  56.95313263, -38.34757614, -33.53923798,
 -26.21811295, -22.47980309, -51.03300858, -13.15662003,  35.31180573,
   6.25005722,  44.6857872 ,  26.49102592,   5.18377399,  50.5387001 ,
  22.7131443 ,   4.27285385,  52.42768478, -41.45622253,  29.97944832,
 -37.55211258],
[ 13.70485783,  80.52088928,   4.77158403,  23.84579086,  21.80143356,
 -47.31682968,  -6.49073362, -21.75024223,  52.60802078,  -4.21434069,
 -14.83629799,  55.18088531,  -2.48512554,  -5.19366884,  57.00575638,
   6.25506735,   0.14475137,  56.95313263, -38.34757614, -33.53923798,
 -26.21811295, -22.47980309, -51.03300858, -13.15662003,  35.31180573,
   6.25005722,  44.6857872 ,  26.49102592,   5.18377399,  50.5387001 ,
  22.7131443 ,   4.27285385,  52.42768478, -41.45769882,  29.97003746,
 -37.43154907],
[ 13.0866375 ,  80.06803894,   4.51042557,  21.51144791,  25.38811111,
 -46.6423378 ,  -6.62513208, -22.06365395,  52.4605484 ,  -4.50046349,
 -14.71022987,  55.19203949,  -2.51664686,  -4.94642305,  57.02635956,
   6.62216759,   0.66390383,  56.90793228, -38.25418472, -33.60414124,
 -26.27137756, -20.44175148, -51.4972229 , -14.59374046,  35.19727325,
   5.54262781,  44.86911774,  26.30171585,   4.20534515,  50.72811127,
  22.85529518,   3.75223351,  52.40575027, -41.45769882,  29.97003746,
 -37.43154907],
[ 13.0866375 ,  80.06803894,   4.51042557,  21.51144791,  25.38811111,
 -46.6423378 ,  -6.62513208, -22.06365395,  52.4605484 ,  -4.50046349,
 -14.71022987,  55.19203949,  -2.51664686,  -4.94642305,  57.02635956,
   6.62216759,   0.66390383,  56.90793228, -38.25418472, -33.60414124,
 -26.27137756, -20.44175148, -51.4972229 , -14.59374046,  35.19727325,
   5.54262781,  44.86911774,  26.30171585,   4.20534515,  50.72811127,
  22.85529518,   3.75223351,  52.40575027, -41.47109604,  29.96538162,
 -37.31378174],
[ 11.94047165,  80.39907837,   2.54089689,  18.58094597,  26.47010422,
 -47.29575348,  -4.49403811, -20.98432541,  53.12502289,  -2.38842511,
 -13.99227715,  55.50962067,  -0.54179716,  -4.00538683,  57.15303802,
   8.48936653,   1.83332956,  56.63369751, -38.12200546, -33.66114807,
 -26.39027214, -19.07213402, -51.72764969, -15.59840679,  35.18710709,
   4.81570387,  44.96090698,  26.10341644,   3.92924619,  50.8525238 ,
  22.99504089,   3.21375322,  52.38040161, -41.47109604,  29.96538162,
 -37.31378174],
[ 11.94047165,  80.39907837,   2.54089689,  18.58094597,  26.47010422,
 -47.29575348,  -4.49403811, -20.98432541,  53.12502289,  -2.38842511,
 -13.99227715,  55.50962067,  -0.54179716,  -4.00538683,  57.15303802,
   8.48936653,   1.83332956,  56.63369751, -38.12200546, -33.66114807,
 -26.39027214, -19.07213402, -51.72764969, -15.59840679,  35.18710709,
   4.81570387,  44.96090698,  26.10341644,   3.92924619,  50.8525238 ,
  22.99504089,   3.21375322,  52.38040161, -41.47778702,  29.9630394 ,
 -37.25602722],
[ 12.74730396,  79.6403656 ,   5.42727757,  23.45650482,  19.62150383,
 -48.45199203,  -7.02316618, -21.1733799 ,  52.77470779,  -4.28968191,
 -15.17000198,  55.08426285,  -3.1465528 ,  -4.87905455,  57.0008812 ,
   5.81399536,   0.93648171,  56.9923439 , -38.04286194, -33.96194839,
 -26.11767769, -17.48175812, -52.17046738, -15.9823885 ,  34.984272  ,
   2.84349442,  45.2859993 ,  25.92340279,   1.95861506,  51.05827332,
  22.77208138,   1.24625325,  52.56125641, -41.47778702,  29.9630394 ,
 -37.25602722],
[ 12.74730396,  79.6403656 ,   5.42727757,  23.45650482,  19.62150383,
 -48.45199203,  -7.02316618, -21.1733799 ,  52.77470779,  -4.28968191,
 -15.17000198,  55.08426285,  -3.1465528 ,  -4.87905455,  57.0008812 ,
   5.81399536,   0.93648171,  56.9923439 , -38.04286194, -33.96194839,
 -26.11767769, -17.48175812, -52.17046738, -15.9823885 ,  34.984272  ,
   2.84349442,  45.2859993 ,  25.92340279,   1.95861506,  51.05827332,
  22.77208138,   1.24625325,  52.56125641, -42.1192627 ,  30.85290718,
 -36.80723572],
[ 11.48888683,  78.39975739,   4.45581532,  18.70736694,  28.64524651,
 -45.95966339,  -6.25020933, -20.21684837,  53.24491119,  -5.11409712,
 -14.02815819,  55.31602859,  -2.01589894,  -3.60419989,  57.14676285,
   7.06783438,   1.91315484,  56.82598114, -38.19101334, -33.95590973,
 -25.90847588, -16.86365128, -52.40623093, -15.87483692,  34.9203949 ,
   4.08621264,  45.24019623,  25.67237473,   3.10978436,  51.12792587,
  22.69756508,   2.54387975,  52.54669952, -42.1192627 ,  30.85290718,
 -36.80723572],
[ 11.48888683,  78.39975739,   4.45581532,  18.70736694,  28.64524651,
 -45.95966339,  -6.25020933, -20.21684837,  53.24491119,  -5.11409712,
 -14.02815819,  55.31602859,  -2.01589894,  -3.60419989,  57.14676285,
   7.06783438,   1.91315484,  56.82598114, -38.19101334, -33.95590973,
 -25.90847588, -16.86365128, -52.40623093, -15.87483692,  34.9203949 ,
   4.08621264,  45.24019623,  25.67237473,   3.10978436,  51.12792587,
  22.69756508,   2.54387975,  52.54669952, -42.24030685,  31.02456284,
 -36.71889496],
[  9.01608086,  78.57822418,   3.13937116,  18.18846703,  26.23452187,
 -47.57873535,  -5.11709261, -17.40035248,  54.34932709,  -4.49382877,
 -11.58910275,  55.93124771,  -0.47749832,  -1.33817983,  57.2781601 ,
   8.3192482 ,   4.36597204,  56.52021408, -38.39767456, -33.72519684,
 -25.90436554, -15.94300365, -52.40901184, -16.79055405,  34.82399368,
   5.49507093,  45.1652565 ,  25.51739311,   4.8846283 ,  51.06671524,
  22.67155075,   3.23012829,  52.5202179 , -42.24030685,  31.02456284,
 -36.71889496],
[  9.01608086,  78.57822418,   3.13937116,  18.18846703,  26.23452187,
 -47.57873535,  -5.11709261, -17.40035248,  54.34932709,  -4.49382877,
 -11.58910275,  55.93124771,  -0.47749832,  -1.33817983,  57.2781601 ,
   8.3192482 ,   4.36597204,  56.52021408, -38.39767456, -33.72519684,
 -25.90436554, -15.94300365, -52.40901184, -16.79055405,  34.82399368,
   5.49507093,  45.1652565 ,  25.51739311,   4.8846283 ,  51.06671524,
  22.67155075,   3.23012829,  52.5202179 , -42.28975677,  31.09492111,
 -36.68246078],
[  7.13126373,  78.89998627,   3.67268872,  20.76960564,  23.76602745,
 -47.81847   ,  -5.39002514, -14.30800152,  55.21806717,  -5.16472387,
  -9.85633373,  56.20484543,  -1.75632226,   0.08264484,  57.26879501,
   7.71726513,   6.28251123,  56.42499542, -39.02698517, -33.18529892,
 -25.66002655, -16.11882782, -52.58682251, -16.05042267,  34.25590515,
   9.58063793,  44.91715622,  24.97979546,   8.10083199,  50.92340088,
  21.79914284,   8.34637737,  52.32534409, -42.28975677,  31.09492111,
 -36.68246078],
[  7.13126373,  78.89998627,   3.67268872,  20.76960564,  23.76602745,
 -47.81847   ,  -5.39002514, -14.30800152,  55.21806717,  -5.16472387,
  -9.85633373,  56.20484543,  -1.75632226,   0.08264484,  57.26879501,
   7.71726513,   6.28251123,  56.42499542, -39.02698517, -33.18529892,
 -25.66002655, -16.11882782, -52.58682251, -16.05042267,  34.25590515,
   9.58063793,  44.91715622,  24.97979546,   8.10083199,  50.92340088,
  21.79914284,   8.34637737,  52.32534409, -43.10071564,  30.82603455,
 -37.00283432],
[  5.51303101,  78.16942596,   4.46490955,  22.58459854,  19.56131935,
 -48.88861847,  -6.08571482, -11.69294167,  55.75881577,  -5.81508207,
  -8.16237545,  56.41246796,  -2.38450456,   1.70741582,  57.22067261,
   7.11110878,   7.72285843,  56.32580185, -39.05994797, -33.14314651,
 -25.66435242, -14.96646976, -52.82541275, -16.3794632 ,  33.87506485,
  11.35411549,  44.79252625,  24.81799698,   9.67471313,  50.7274437 ,
  21.7352829 ,   9.87086105,  52.08598709, -43.10071564,  30.82603455,
 -37.00283432],
[  5.51303101,  78.16942596,   4.46490955,  22.58459854,  19.56131935,
 -48.88861847,  -6.08571482, -11.69294167,  55.75881577,  -5.81508207,
  -8.16237545,  56.41246796,  -2.38450456,   1.70741582,  57.22067261,
   7.11110878,   7.72285843,  56.32580185, -39.05994797, -33.14314651,
 -25.66435242, -14.96646976, -52.82541275, -16.3794632 ,  33.87506485,
  11.35411549,  44.79252625,  24.81799698,   9.67471313,  50.7274437 ,
  21.7352829 ,   9.87086105,  52.08598709, -43.26378632,  31.09376717,
 -36.80322647],
[  5.59519243,  78.00092316,   3.80420613,  20.8784256 ,  20.99335861,
 -49.05279541,  -5.44351625, -10.94958973,  55.97571945,  -5.25533533,
  -8.18884754,  56.46353531,  -1.21642137,   1.24077892,  57.26942444,
   7.80284739,   7.60474062,  56.25024033, -38.89948273, -33.22471619,
 -25.80223083, -16.81558037, -52.67773819, -15.00328636,  34.19120407,
  11.15216255,  44.60265732,  24.92675781,   9.93339252,  50.62401581,
  21.74409103,   9.98039722,  52.06143188, -43.25632858,  31.31542778,
 -36.60165405],
[  5.59519243,  78.00092316,   3.80420613,  20.8784256 ,  20.99335861,
 -49.05279541,  -5.44351625, -10.94958973,  55.97571945,  -5.25533533,
  -8.18884754,  56.46353531,  -1.21642137,   1.24077892,  57.26942444,
   7.80284739,   7.60474062,  56.25024033, -38.89948273, -33.22471619,
 -25.80223083, -16.81558037, -52.67773819, -15.00328636,  34.19120407,
  11.15216255,  44.60265732,  24.92675781,   9.93339252,  50.62401581,
  21.74409103,   9.98039722,  52.06143188, -43.25382614,  31.38179016,
 -36.54101562],
[  7.17219543,  77.70459747,   4.45132208,  20.1430397 ,  22.30497932,
 -48.78065491,  -6.07753706, -12.98313236,  55.47349167,  -5.98043537,
  -9.69767094,  56.15154648,  -1.9824338 ,  -0.49857655,  57.25930405,
   7.23060226,   6.0149374 ,  56.51853943, -38.97460175, -33.4213028 ,
 -25.43233109, -18.43450737, -52.47437668, -13.76281261,  34.69258499,
   9.56712818,  44.58364105,  25.27126694,   8.28054619,  50.7503891 ,
  22.20020294,   5.56234503,  52.52635193, -43.25261307,  31.41279793,
 -36.51263809],
[  7.17219543,  77.70459747,   4.45132208,  20.1430397 ,  22.30497932,
 -48.78065491,  -6.07753706, -12.98313236,  55.47349167,  -5.98043537,
  -9.69767094,  56.15154648,  -1.9824338 ,  -0.49857655,  57.25930405,
   7.23060226,   6.0149374 ,  56.51853943, -38.97460175, -33.4213028 ,
 -25.43233109, -18.43450737, -52.47437668, -13.76281261,  34.69258499,
   9.56712818,  44.58364105,  25.27126694,   8.28054619,  50.7503891 ,
  22.20020294,   5.56234503,  52.52635193, -43.25187302,  31.43144226,
 -36.49555969],
[ 10.90871429,  83.22867584,   2.49058819,  17.86584663,  30.6803875 ,
 -44.97034454,  -3.46581125, -16.71248245,  54.69449234,  -3.77843857,
 -13.40863609,  55.57641983,  -0.27616924,  -3.91090918,  57.16147995,
   7.8549757 ,   3.38615894,  56.65368271, -39.03868103, -33.35626602,
 -25.41942596, -17.81700134, -52.59293365, -14.11892986,  34.64997482,
   8.76102924,  44.7820282 ,  25.12353897,   7.3042326 ,  50.97315216,
  22.17269897,   4.94700193,  52.59947968, -43.25187302,  31.43144226,
 -36.49555969],
[ 10.90871429,  83.22867584,   2.49058819,  17.86584663,  30.6803875 ,
 -44.97034454,  -3.46581125, -16.71248245,  54.69449234,  -3.77843857,
 -13.40863609,  55.57641983,  -0.27616924,  -3.91090918,  57.16147995,
   7.8549757 ,   3.38615894,  56.65368271, -39.03868103, -33.35626602,
 -25.41942596, -17.81700134, -52.59293365, -14.11892986,  34.64997482,
   8.76102924,  44.7820282 ,  25.12353897,   7.3042326 ,  50.97315216,
  22.17269897,   4.94700193,  52.59947968, -43.25135422,  31.44435692,
 -36.4837265 ],
[  7.35474586,  78.22103882,   3.60115671,  16.94855881,  29.06173897,
 -46.37853241,  -5.10158443, -13.1388092 ,  55.53514099,  -5.27610302,
  -9.71929359,  56.21836472,  -1.51446044,  -0.61464953,  57.27246094,
   7.95379734,   5.93281317,  56.43000412, -39.00658798, -33.33868027,
 -25.49166679, -17.09755707, -52.68040085, -14.67157745,  34.57316971,
   8.88569927,  44.81681442,  25.21741867,   7.54854584,  50.89113617,
  22.12178421,   4.89428425,  52.62583923, -43.25135422,  31.44435692,
 -36.4837265 ],
[  7.35474586,  78.22103882,   3.60115671,  16.94855881,  29.06173897,
 -46.37853241,  -5.10158443, -13.1388092 ,  55.53514099,  -5.27610302,
  -9.71929359,  56.21836472,  -1.51446044,  -0.61464953,  57.27246094,
   7.95379734,   5.93281317,  56.43000412, -39.00658798, -33.33868027,
 -25.49166679, -17.09755707, -52.68040085, -14.67157745,  34.57316971,
   8.88569927,  44.81681442,  25.21741867,   7.54854584,  50.89113617,
  22.12178421,   4.89428425,  52.62583923, -43.25099182,  31.45325279,
 -36.47557068],
[  5.85508442,  77.00193787,   4.27655077,  18.52238655,  26.65369415,
 -47.21554947,  -5.84848976, -11.23703384,  55.87781906,  -5.64779186,
  -7.98458958,  56.45489502,  -1.35665011,   0.65273952,  57.27599716,
   7.56878471,   7.15577841,  56.34105682, -38.9147377 , -33.39934158,
 -25.55256653, -17.39676666, -52.65709686, -14.40100002,  34.66627502,
   8.4020071 ,  44.83817673,  25.68179512,   7.27088165,  50.69897461,
  22.19784737,   5.38422918,  52.54590225, -43.25099182,  31.45325279,
 -36.47557068],
[  5.85508442,  77.00193787,   4.27655077,  18.52238655,  26.65369415,
 -47.21554947,  -5.84848976, -11.23703384,  55.87781906,  -5.64779186,
  -7.98458958,  56.45489502,  -1.35665011,   0.65273952,  57.27599716,
   7.56878471,   7.15577841,  56.34105682, -38.9147377 , -33.39934158,
 -25.55256653, -17.39676666, -52.65709686, -14.40100002,  34.66627502,
   8.4020071 ,  44.83817673,  25.68179512,   7.27088165,  50.69897461,
  22.19784737,   5.38422918,  52.54590225, -43.25072861,  31.45974541,
 -36.46961975],
[  7.33532763,  76.99375153,   4.50067616,  13.04516411,  41.95284271,
 -36.777565  ,  -6.3781786 , -12.94534969,  55.44856262,  -5.91613102,
  -9.6094017 ,  56.17353058,  -0.60418564,  -0.86368263,  57.28608322,
   7.34725428,   5.71309471,  56.53481293, -38.85439301, -33.59951782,
 -25.38139534, -19.90902328, -52.25443649, -12.48643398,  34.57450867,
   8.85914898,  44.82103729,  25.30299187,   7.60633087,  50.84003067,
  22.12241554,   5.56180191,  52.55921936, -43.25072861,  31.45974541,
 -36.46961975],
[  7.33532763,  76.99375153,   4.50067616,  13.04516411,  41.95284271,
 -36.777565  ,  -6.3781786 , -12.94534969,  55.44856262,  -5.91613102,
  -9.6094017 ,  56.17353058,  -0.60418564,  -0.86368263,  57.28608322,
   7.34725428,   5.71309471,  56.53481293, -38.85439301, -33.59951782,
 -25.38139534, -19.90902328, -52.25443649, -12.48643398,  34.57450867,
   8.85914898,  44.82103729,  25.30299187,   7.60633087,  50.84003067,
  22.12241554,   5.56180191,  52.55921936, -43.39871597,  31.38804245,
 -36.46424866],
[  3.49408269,  75.47202301,   5.24664545,  12.50624752,  41.14922714,
 -37.85685349,  -7.41193533, -10.02051449,  55.92368698,  -6.6585803 ,
  -5.99305868,  56.5911026 ,  -2.61291838,   3.01919889,  57.1564827 ,
   6.96994638,   9.13630486,  56.13157654, -38.46590805, -33.95482635,
 -25.5       , -21.35779953, -51.93199539, -11.38941383,  34.82043076,
   5.30399036,  45.19083405,  25.4908886 ,   4.17145252,  51.14313126,
  22.45854759,   2.94043565,  52.62863922, -43.39871597,  31.38804245,
 -36.46424866],
[  3.49408269,  75.47202301,   5.24664545,  12.50624752,  41.14922714,
 -37.85685349,  -7.41193533, -10.02051449,  55.92368698,  -6.6585803 ,
  -5.99305868,  56.5911026 ,  -2.61291838,   3.01919889,  57.1564827 ,
   6.96994638,   9.13630486,  56.13157654, -38.46590805, -33.95482635,
 -25.5       , -21.35779953, -51.93199539, -11.38941383,  34.82043076,
   5.30399036,  45.19083405,  25.4908886 ,   4.17145252,  51.14313126,
  22.45854759,   2.94043565,  52.62863922, -43.31872177,  32.00469971,
 -36.02724838],
[  6.38683462,  76.68888092,   4.20976496,  13.2464695 ,  40.3107338 ,
 -38.50171661,  -6.29686832, -13.07964134,  55.4263382 ,  -5.82488918,
  -9.05961609,  56.27433395,  -1.65370691,   0.21588677,  57.27150345,
   7.70618153,   6.57383013,  56.39331436, -38.59665298, -33.86487198,
 -25.42195129, -19.39870071, -52.30594635, -13.06080437,  34.75461578,
   6.2372508 ,  45.12227631,  24.96080971,   5.54153156,  51.2743187 ,
  22.35129929,   3.94586897,  52.60851669, -43.31872177,  32.00469971,
 -36.02724838],
[  6.38683462,  76.68888092,   4.20976496,  13.2464695 ,  40.3107338 ,
 -38.50171661,  -6.29686832, -13.07964134,  55.4263382 ,  -5.82488918,
  -9.05961609,  56.27433395,  -1.65370691,   0.21588677,  57.27150345,
   7.70618153,   6.57383013,  56.39331436, -38.59665298, -33.86487198,
 -25.42195129, -19.39870071, -52.30594635, -13.06080437,  34.75461578,
   6.2372508 ,  45.12227631,  24.96080971,   5.54153156,  51.2743187 ,
  22.35129929,   3.94586897,  52.60851669, -43.39933014,  31.82850456,
 -36.13956451],
[  9.18440819,  77.46219635,   4.30053711,   9.80668449,  48.11807251,
 -29.51756477,  -6.28679514, -15.86084652,  54.69658279,  -5.95992136,
 -11.65891647,  55.77952576,  -0.99309319,  -2.57745266,  57.22916031,
   7.44376564,   3.99639797,  56.66944122, -38.73917007, -33.93797302,
 -25.10571861, -18.43846321, -52.47511292, -13.7547102 ,  34.85843658,
   6.64232588,  44.98416519,  24.98580742,   5.73782206,  51.24054337,
  22.22056389,   4.1371994 ,  52.64918518, -43.39933014,  31.82850456,
 -36.13956451],
[  9.18440819,  77.46219635,   4.30053711,   9.80668449,  48.11807251,
 -29.51756477,  -6.28679514, -15.86084652,  54.69658279,  -5.95992136,
 -11.65891647,  55.77952576,  -0.99309319,  -2.57745266,  57.22916031,
   7.44376564,   3.99639797,  56.66944122, -38.73917007, -33.93797302,
 -25.10571861, -18.43846321, -52.47511292, -13.7547102 ,  34.85843658,
   6.64232588,  44.98416519,  24.98580742,   5.73782206,  51.24054337,
  22.22056389,   4.1371994 ,  52.64918518, -43.44567108,  31.70237732,
 -36.22257233],
[  8.17498779,  76.42702484,   4.68040705,   7.54879189,  50.88773727,
 -25.22420311,  -6.6896553 , -14.8138895 ,  54.94182205,  -6.04386997,
 -10.58830643,  55.9836235 ,  -0.20042723,  -1.65048277,  57.27165222,
   7.30064011,   4.77832317,  56.62750626, -38.73469925, -33.93861389,
 -25.11175346, -19.92258453, -52.21795273, -12.61675262,  34.95215988,
   6.84472609,  44.88098145,  24.95637703,   5.75215721,  51.25327682,
  22.14237976,   3.28281689,  52.74224854, -43.44567108,  31.70237732,
 -36.22257233],
[  8.17498779,  76.42702484,   4.68040705,   7.54879189,  50.88773727,
 -25.22420311,  -6.6896553 , -14.8138895 ,  54.94182205,  -6.04386997,
 -10.58830643,  55.9836235 ,  -0.20042723,  -1.65048277,  57.27165222,
   7.30064011,   4.77832317,  56.62750626, -38.73469925, -33.93861389,
 -25.11175346, -19.92258453, -52.21795273, -12.61675262,  34.95215988,
   6.84472609,  44.88098145,  24.95637703,   5.75215721,  51.25327682,
  22.14237976,   3.28281689,  52.74224854, -43.46178818,  31.6582489 ,
 -36.25161743],
[ 10.26243877,  76.65500641,   3.94875789,   4.03845501,  53.41921616,
 -20.3195591 ,  -5.53288507, -16.82496643,  54.48957825,  -5.43454647,
 -12.79161263,  55.58459091,  -0.79497004,  -3.57514572,  57.17860413,
   7.98342991,   2.76676798,  56.66936111, -38.72494125, -33.99437714,
 -25.05129623, -20.30591011, -52.24370193, -11.87737656,  34.82111359,
   6.60601854,  45.01840591,  24.97498894,   5.09031105,  51.31418228,
  22.08049774,   2.40015769,  52.8156929 , -43.46178818,  31.6582489 ,
 -36.25161743],
[ 10.26243877,  76.65500641,   3.94875789,   4.03845501,  53.41921616,
 -20.3195591 ,  -5.53288507, -16.82496643,  54.48957825,  -5.43454647,
 -12.79161263,  55.58459091,  -0.79497004,  -3.57514572,  57.17860413,
   7.98342991,   2.76676798,  56.66936111, -38.72494125, -33.99437714,
 -25.05129623, -20.30591011, -52.24370193, -11.87737656,  34.82111359,
   6.60601854,  45.01840591,  24.97498894,   5.09031105,  51.31418228,
  22.08049774,   2.40015769,  52.8156929 , -43.47001648,  31.63567352,
 -36.26647568],
[ 10.26243877,  76.65500641,   3.94875789,   4.03845501,  53.41921616,
 -20.3195591 ,  -5.53288507, -16.82496643,  54.48957825,  -5.43454647,
 -12.79161263,  55.58459091,  -0.79497004,  -3.57514572,  57.17860413,
   7.98342991,   2.76676798,  56.66936111, -38.72494125, -33.99437714,
 -25.05129623, -20.30591011, -52.24370193, -11.87737656,  34.82111359,
   6.60601854,  45.01840591,  24.97498894,   5.09031105,  51.31418228,
  22.08049774,   2.40015769,  52.8156929 , -43.47001648,  31.63567352,
 -36.26647568]
], "float32")
print np.shape(teach)
