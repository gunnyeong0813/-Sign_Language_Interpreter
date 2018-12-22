import numpy as np

meet = np.array([
[ 38.31441116,  45.93120575,  39.08728027,  28.6114769 ,  40.50328064,
 -28.6997242 ,  31.97288704,   1.10019386, -47.53241348, -20.89189339,
 -39.5535965 ,  35.80290985, -18.43739891, -33.93087006,  42.32687759,
 -12.39740849, -29.99010468,  47.21974564, -25.80410004,  38.94197083,
 -33.17344666, -33.0529747 ,   1.32827282, -46.78186417, -15.31287098,
 -50.54306412,  22.219841  , -19.94548988, -46.02366257,  27.69126892,
 -31.45641327, -34.91590881,  32.77468109,  39.5521698 , -40.70112228,
 -30.89148521],

[ 43.28318405,  44.94166565,  36.79487228,  29.67293739,  39.18727112,
 -29.4394474 ,  32.84378052,  -0.8985939 , -46.93915939, -21.70720291,
 -38.12071228,  36.85668182, -19.40048027, -32.49053192,  43.02084351,
 -13.89683914, -27.691185  ,  48.19629288, -25.80953407,  38.97019958,
 -33.13605118, -33.49251938,   2.11114693, -46.43921661, -16.52362442,
 -50.74819183,  20.84219551, -21.53076363, -46.29253387,  26.00449944,
 -33.00485611, -35.10632324,  31.00051498,  39.80875397, -40.71644974,
 -30.17238235],
[ 41.64208984,  44.73304367,  37.26852036,  29.67293739,  39.18727112,
 -29.4394474 ,  32.84378052,  -0.8985939 , -46.93915939, -21.70720291,
 -38.12071228,  36.85668182, -19.40048027, -32.49053192,  43.02084351,
 -13.89683914, -27.691185  ,  48.19629288, -25.80953407,  38.97019958,
 -33.13605118, -33.49251938,   2.11114693, -46.43921661, -16.52362442,
 -50.74819183,  20.84219551, -21.53076363, -46.29253387,  26.00449944,
 -33.00485611, -35.10632324,  31.00051498,  39.80875397, -40.71644974,
 -30.17238235],
[ 41.64208984,  44.73304367,  37.26852036,  27.54160881,  41.38005066,
 -28.49487305,  32.72922134,  -2.16048312, -46.97804642, -21.9511261 ,
 -37.53489685,  37.31066895, -19.37017059, -31.91985893,  43.45946884,
 -14.79959774, -26.66244888,  48.50662231, -26.23701859,  38.70328903,
 -33.11315155, -33.32972717,   1.59273636, -46.57680893, -16.5888958 ,
 -50.5968895 ,  21.15583801, -21.19840813, -46.22996902,  26.38605309,
 -33.06100845, -34.90862274,  31.16350937,  39.73545456, -40.79909897,
 -30.52410126],
[ 40.53418732,  43.81711197,  38.02722549,  27.54160881,  41.38005066,
 -28.49487305,  32.72922134,  -2.16048312, -46.97804642, -21.9511261 ,
 -37.53489685,  37.31066895, -19.37017059, -31.91985893,  43.45946884,
 -14.79959774, -26.66244888,  48.50662231, -26.23701859,  38.70328903,
 -33.11315155, -33.32972717,   1.59273636, -46.57680893, -16.5888958 ,
 -50.5968895 ,  21.15583801, -21.19840813, -46.22996902,  26.38605309,
 -33.06100845, -34.90862274,  31.16350937,  39.73545456, -40.79909897,
 -30.52410126],
[ 40.53418732,  43.81711197,  38.02722549,  28.03437042,  41.01353836,
 -28.54417992,  32.35161209,  -1.70894039, -47.25737381, -21.87558746,
 -37.36468506,  37.52526474, -18.96118164, -31.79833603,  43.72809219,
 -14.17888165, -26.48078918,  48.79071426, -25.66950607,  39.19528198,
 -32.97896957, -32.928936  ,   1.275576  , -46.87072372, -16.53442574,
 -50.35068512,  21.77676773, -20.98906898, -46.01895142,  26.9169426 ,
 -32.6686821 , -34.68016434,  31.82530403,  39.22230148, -40.73865509,
 -30.43319511],
[ 40.0208931 ,  42.17029953,  37.89771652,  28.03437042,  41.01353836,
 -28.54417992,  32.35161209,  -1.70894039, -47.25737381, -21.87558746,
 -37.36468506,  37.52526474, -18.96118164, -31.79833603,  43.72809219,
 -14.17888165, -26.48078918,  48.79071426, -25.66950607,  39.19528198,
 -32.97896957, -32.928936  ,   1.275576  , -46.87072372, -16.53442574,
 -50.35068512,  21.77676773, -20.98906898, -46.01895142,  26.9169426 ,
 -32.6686821 , -34.68016434,  31.82530403,  39.22230148, -40.73865509,
 -30.43319511],
[ 40.0208931 ,  42.17029953,  37.89771652,  29.19034767,  40.30332184,
 -28.39669418,  32.31214523,  -1.79426706, -47.28120422, -21.89485931,
 -37.6278801 ,  37.25002289, -19.3862896 , -31.85726929,  43.49819183,
 -13.58376884, -26.78967476,  48.79140091, -24.7849884 ,  40.34567261,
 -32.26046753, -34.08533096,   1.01791286, -46.04302597, -16.6182785 ,
 -50.08188629,  22.32585335, -20.94148254, -45.67418671,  27.53414917,
 -32.5133667 , -34.25120163,  32.44290924,  38.76556778, -40.84695816,
 -30.38556862],
[ 41.27193069,  43.64188004,  37.73552704,  29.19034767,  40.30332184,
 -28.39669418,  32.31214523,  -1.79426706, -47.28120422, -21.89485931,
 -37.6278801 ,  37.25002289, -19.3862896 , -31.85726929,  43.49819183,
 -13.58376884, -26.78967476,  48.79140091, -24.7849884 ,  40.34567261,
 -32.26046753, -34.08533096,   1.01791286, -46.04302597, -16.6182785 ,
 -50.08188629,  22.32585335, -20.94148254, -45.67418671,  27.53414917,
 -32.5133667 , -34.25120163,  32.44290924,  38.76556778, -40.84695816,
 -30.38556862],
[ 41.27193069,  43.64188004,  37.73552704,  30.76437759,  38.62210846,
 -29.0635891 ,  32.14307022,  -1.1944406 , -47.41521454, -22.01437378,
 -37.84277344,  36.96076584, -19.27981567, -31.32381821,  43.93078232,
 -13.04719257, -26.91087532,  48.87107468, -25.2230587 ,  39.85989761,
 -32.52371597, -35.00615692,   1.72029805, -45.32566452, -17.1426487 ,
 -50.05653   ,  21.98362732, -21.48062134, -45.71354294,  27.04924393,
 -32.98707581, -34.17325211,  32.04447174,  38.87322235, -41.01560211,
 -30.36340523],
[ 41.92656708,  44.02071381,  37.74026489,  30.76437759,  38.62210846,
 -29.0635891 ,  32.14307022,  -1.1944406 , -47.41521454, -22.01437378,
 -37.84277344,  36.96076584, -19.27981567, -31.32381821,  43.93078232,
 -13.04719257, -26.91087532,  48.87107468, -25.2230587 ,  39.85989761,
 -32.52371597, -35.00615692,   1.72029805, -45.32566452, -17.1426487 ,
 -50.05653   ,  21.98362732, -21.48062134, -45.71354294,  27.04924393,
 -32.98707581, -34.17325211,  32.04447174,  38.87322235, -41.01560211,
 -30.36340523],
[ 41.92656708,  44.02071381,  37.74026489,  29.2019577 ,  39.75627136,
 -29.14602852,  32.40680313,  -2.24919653, -47.19689178, -21.23907089,
 -38.18501663,  37.06228256, -17.65828896, -31.85350227,  44.23059464,
 -13.45310402, -25.76079559,  49.37815475, -25.32879829,  39.70630264,
 -32.62924957, -35.03252029,   1.43395567, -45.31525803, -17.36029816,
 -50.02463913,  21.88519669, -21.61504364, -45.61216354,  27.11322212,
 -32.95813751, -34.12042618,  32.13042068,  38.91916656, -41.09980011,
 -30.61908531],
[ 40.360466  ,  42.38858032,  38.0571785 ,  29.2019577 ,  39.75627136,
 -29.14602852,  32.40680313,  -2.24919653, -47.19689178, -21.23907089,
 -38.18501663,  37.06228256, -17.65828896, -31.85350227,  44.23059464,
 -13.45310402, -25.76079559,  49.37815475, -25.32879829,  39.70630264,
 -32.62924957, -35.03252029,   1.43395567, -45.31525803, -17.36029816,
 -50.02463913,  21.88519669, -21.61504364, -45.61216354,  27.11322212,
 -32.95813751, -34.12042618,  32.13042068,  38.91916656, -41.09980011,
 -30.61908531],

[ 40.07836533,  41.62830353,  37.80465317,  27.98908615,  40.93146896,
 -28.70596123,  31.89310455,  -2.33022308, -47.54162979, -22.16413307,
 -36.7939949 ,  37.9178009 , -18.41008949, -31.73207283,  44.01080322,
 -13.04462051, -25.59517479,  49.57349396, -25.73984146,  39.23646164,
 -32.87501907, -34.42500687,  -0.11025321, -45.80079651, -16.21260834,
 -50.1166687 ,  22.5450058 , -20.6495285 , -45.7082634 ,  27.69761658,
 -32.37262726, -34.32256317,  32.50817108,  37.92062378, -40.06770706,
 -30.91357613],
[ 39.37432861,  41.82482529,  37.83671951,  27.98908615,  40.93146896,
 -28.70596123,  31.89310455,  -2.33022308, -47.54162979, -22.16413307,
 -36.7939949 ,  37.9178009 , -18.41008949, -31.73207283,  44.01080322,
 -13.04462051, -25.59517479,  49.57349396, -25.73984146,  39.23646164,
 -32.87501907, -34.42500687,  -0.11025321, -45.80079651, -16.21260834,
 -50.1166687 ,  22.5450058 , -20.6495285 , -45.7082634 ,  27.69761658,
 -32.37262726, -34.32256317,  32.50817108,  37.92062378, -40.06770706,
 -30.91357613],
[ 39.37432861,  41.82482529,  37.83671951,  28.50047684,  40.60775757,
 -28.6625061 ,  31.19407463,  -0.70684415, -48.05451584, -20.65185928,
 -37.77555084,  37.80628204, -17.78132629, -32.5259819 ,  43.68857193,
 -12.18029785, -26.88669395,  49.10756302, -24.78568459,  40.10686493,
 -32.55634689, -33.58106995,   0.19077981, -46.42285538, -16.05346298,
 -50.0235939 ,  22.86335182, -20.33911896, -45.57188416,  28.14836121,
 -32.18959808, -34.1846199 ,  32.83364105,  37.35858536, -39.67405319,
 -30.98982239],

[ 39.62877655,  42.13288116,  37.23859024,  31.2822361 ,  38.49193192,
 -28.68099594,  32.36918259,  -0.56467956, -47.27286148, -18.5758152 ,
 -39.13130569,  37.50315094, -15.45148087, -34.48862839,  43.06498337,
 -10.75144672, -27.68804932,  48.99576187, -24.72513771,  40.1724472 ,
 -32.52150726, -33.92111588,   0.13089414, -46.17517853, -15.25768185,
 -50.02071381,  23.40807343, -19.23690033, -45.54553223,  28.954319  ,
 -31.2191143 , -34.17065811,  33.77187347,  36.86582184, -39.08105469,
 -31.30502129],
[ 39.62877655,  42.13288116,  37.23859024,  31.49861336,  38.31742477,
 -28.67784309,  31.79532623,   0.79506779, -47.65743637, -19.12108803,
 -40.13611221,  36.14253616, -16.48176765, -35.71166992,  41.66334534,
 -10.93770218, -29.22405052,  48.05338669, -25.83579445,  39.27253342,
 -32.75646591, -34.50431061,  -0.16876626, -45.74090576, -15.44711018,
 -49.94351578,  23.4486351 , -19.45391083, -45.38870621,  29.05541611,
 -31.30119705, -33.93054199,  33.93758774,  37.17097092, -39.59851456,
 -31.00306511],
[ 42.25559235,  43.30524063,  37.18886948,  31.49861336,  38.31742477,
 -28.67784309,  31.79532623,   0.79506779, -47.65743637, -19.12108803,
 -40.13611221,  36.14253616, -16.48176765, -35.71166992,  41.66334534,
 -10.93770218, -29.22405052,  48.05338669, -25.83579445,  39.27253342,
 -32.75646591, -34.50431061,  -0.16876626, -45.74090576, -15.44711018,
 -49.94351578,  23.4486351 , -19.45391083, -45.38870621,  29.05541611,
 -31.30119705, -33.93054199,  33.93758774,  37.17097092, -39.59851456,
 -31.00306511],
[ 42.25559235,  43.30524063,  37.18886948,  31.82286263,  37.84926987,
 -28.94036865,  32.14591217,   0.41321433, -47.42653275, -19.61325073,
 -39.95940018,  36.07455063, -17.73509789, -35.23419189,  41.5550766 ,
 -11.74037838, -28.67995071,  48.1916008 , -25.89286232,  39.12015152,
 -32.89345932, -34.20656204,  -0.77587837, -45.95775986, -15.47272682,
 -49.93498611,  23.44991302, -19.61027908, -45.37263489,  28.97528839,
 -31.38763237, -33.92663956,  33.86156845,  37.21005249, -39.65197754,
 -31.11027908],
[ 42.14758301,  42.85755539,  37.74077606,  31.82286263,  37.84926987,
 -28.94036865,  32.14591217,   0.41321433, -47.42653275, -19.61325073,
 -39.95940018,  36.07455063, -17.73509789, -35.23419189,  41.5550766 ,
 -11.74037838, -28.67995071,  48.1916008 , -25.89286232,  39.12015152,
 -32.89345932, -34.20656204,  -0.77587837, -45.95775986, -15.47272682,
 -49.93498611,  23.44991302, -19.61027908, -45.37263489,  28.97528839,
 -31.38763237, -33.92663956,  33.86156845,  37.21005249, -39.65197754,
 -31.11027908],
[ 42.14758301,  42.85755539,  37.74077606,  32.663517  ,  36.94430161,
 -29.17224121,  31.78252411,   1.25413096, -47.65610886, -20.04950333,
 -40.33327866,  35.41257477, -18.21284485, -35.35928345,  41.24100113,
 -11.33353424, -30.25113678,  47.32046127, -25.34808731,  39.63210297,
 -32.70439529, -32.66560364,  -0.1869527 , -47.07154083, -15.11407661,
 -50.12849808,  23.27025604, -19.3272686 , -45.48725891,  28.9857254 ,
 -31.2733326 , -34.27840805,  33.61213684,  37.00046539, -39.11955643,
 -31.05152512],
[ 44.64237976,  45.14681625,  37.17446899,  32.663517  ,  36.94430161,
 -29.17224121,  31.78252411,   1.25413096, -47.65610886, -20.04950333,
 -40.33327866,  35.41257477, -18.21284485, -35.35928345,  41.24100113,
 -11.33353424, -30.25113678,  47.32046127, -25.34808731,  39.63210297,
 -32.70439529, -32.66560364,  -0.1869527 , -47.07154083, -15.11407661,
 -50.12849808,  23.27025604, -19.3272686 , -45.48725891,  28.9857254 ,
 -31.2733326 , -34.27840805,  33.61213684,  37.00046539, -39.11955643,
 -31.05152512],
[ 55.1072998 ,  57.78538895,  18.00707054,  34.96198654,  38.40846634,
 -24.19205475,  26.31458282,  15.01323032, -48.63077164,  -4.43642712,
 -49.11656189,  29.16655159,  -2.44303608, -43.8323555 ,  36.81796646,
   3.14916396, -42.54977417,  38.24141693, -37.72856903,  32.6897049 ,
 -28.12018204, -33.79117966,   2.47157598, -46.20447922,   6.32237768,
 -43.62247086,  36.60483551,   4.16760683, -37.51527786,  43.10500336,
  -6.70737648, -26.18811989,  50.51732254,  39.1858902 , -45.24905396,
 -31.27718544],
[ 54.3176651 ,  56.1396637 ,  19.56708717,  36.13881302,  37.0668869 ,
 -24.55277252,  27.23770714,  13.26539803, -48.63067627,  -6.54565096,
 -48.46913147,  29.84467316,  -3.43709612, -43.41214371,  37.23410416,
   2.05134463, -42.18444824,  38.71783447, -38.54458237,  31.96122551,
 -27.84962654, -33.14220047,   3.37532616, -46.61553574,   5.63636971,
 -43.91044617,  36.3718338 ,   3.22079301, -37.88750839,  42.85988617,
  -7.96101332, -26.53482628,  50.1530838 ,  39.1858902 , -45.24905396,
 -31.27718544],
[ 54.3176651 ,  56.1396637 ,  19.56708717,  36.13881302,  37.0668869 ,
 -24.55277252,  27.23770714,  13.26539803, -48.63067627,  -6.54565096,
 -48.46913147,  29.84467316,  -3.43709612, -43.41214371,  37.23410416,
   2.05134463, -42.18444824,  38.71783447, -38.54458237,  31.96122551,
 -27.84962654, -33.14220047,   3.37532616, -46.61553574,   5.63636971,
 -43.91044617,  36.3718338 ,   3.22079301, -37.88750839,  42.85988617,
  -7.96101332, -26.53482628,  50.1530838 ,  40.07588196, -46.61249924,
 -29.54807472],
[ 52.01216507,  52.09909821,  22.91131973,  35.79345322,  37.50900269,
 -24.38667297,  28.95405006,  11.4975481 , -48.08613205,  -9.85007858,
 -46.88489532,  31.42593384,  -6.05285454, -41.94603729,  38.55774307,
  -0.48758006, -40.86047363,  40.16205215, -38.57513428,  32.38066483,
 -27.31772423, -31.66887856,   2.70179462, -47.67167664,   6.64995623,
 -43.89042282,  36.22451401,   3.60757327, -37.57416916,  43.10422134,
  -7.56799841, -27.40279579,  49.74554062,  40.07588196, -46.61249924,
 -29.54807472],
[ 52.01216507,  52.09909821,  22.91131973,  35.79345322,  37.50900269,
 -24.38667297,  28.95405006,  11.4975481 , -48.08613205,  -9.85007858,
 -46.88489532,  31.42593384,  -6.05285454, -41.94603729,  38.55774307,
  -0.48758006, -40.86047363,  40.16205215, -38.57513428,  32.38066483,
 -27.31772423, -31.66887856,   2.70179462, -47.67167664,   6.64995623,
 -43.89042282,  36.22451401,   3.60757327, -37.57416916,  43.10422134,
  -7.56799841, -27.40279579,  49.74554062,  40.13454437, -46.15176392,
 -28.83924866],
[ 52.16370392,  52.31021881,  22.95574188,  36.48092651,  36.88562393,
 -24.3187027 ,  28.32754898,  11.60110378, -48.43315887, -10.85394955,
 -46.40384674,  31.80693436,  -6.31498718, -41.90946579,  38.55546951,
  -0.56740421, -40.75296021,  40.27009964, -39.32142258,  31.90613937,
 -26.8072834 , -32.96820831,   0.22778046, -46.85991669,   8.10511303,
 -42.03330994,  38.08299255,   5.59532547, -35.02507782,  44.99714279,
  -4.91274881, -24.63531876,  51.49536514,  40.13454437, -46.15176392,
 -28.83924866],
[ 52.16370392,  52.31021881,  22.95574188,  36.48092651,  36.88562393,
 -24.3187027 ,  28.32754898,  11.60110378, -48.43315887, -10.85394955,
 -46.40384674,  31.80693436,  -6.31498718, -41.90946579,  38.55546951,
  -0.56740421, -40.75296021,  40.27009964, -39.32142258,  31.90613937,
 -26.8072834 , -32.96820831,   0.22778046, -46.85991669,   8.10511303,
 -42.03330994,  38.08299255,   5.59532547, -35.02507782,  44.99714279,
  -4.91274881, -24.63531876,  51.49536514,  38.13117218, -46.75026321,
 -29.07692146],
[ 50.33269501,  48.42934799,  24.80537224,  33.39259338,  40.53885651,
 -22.89851761,  28.26119232,  10.52879047, -48.7160759 , -13.07314491,
 -44.90284729,  33.10035324,  -8.51163006, -40.68796158,  39.43156815,
  -2.23751879, -39.86859512,  41.08886719, -39.55951309,  31.80632973,
 -26.57458687, -33.63496399,  -0.11291418, -46.38408279,   8.52305126,
 -41.54576111,  38.52419662,   6.05919313, -34.30834198,  45.48659515,
  -4.46632242, -23.4286232 ,  52.09566498,  38.13117218, -46.75026321,
 -29.07692146],
[ 50.33269501,  48.42934799,  24.80537224,  33.39259338,  40.53885651,
 -22.89851761,  28.26119232,  10.52879047, -48.7160759 , -13.07314491,
 -44.90284729,  33.10035324,  -8.51163006, -40.68796158,  39.43156815,
  -2.23751879, -39.86859512,  41.08886719, -39.55951309,  31.80632973,
 -26.57458687, -33.63496399,  -0.11291418, -46.38408279,   8.52305126,
 -41.54576111,  38.52419662,   6.05919313, -34.30834198,  45.48659515,
  -4.46632242, -23.4286232 ,  52.09566498,  37.61194992, -46.98610306,
 -29.15704918],
[ 48.75985718,  49.25251007,  25.73770714,  35.71054459,  37.88261795,
 -23.92636108,  29.50111008,   5.52225924, -48.80569077, -12.87804317,
 -44.31132507,  33.96275711,  -9.77431583, -39.3640213 ,  40.46903992,
  -4.15516138, -38.28639221,  42.42279053, -40.16818237,  30.91417503,
 -26.71399117, -33.90458298,   0.11442117, -46.18736267,   7.94215441,
 -41.64306259,  38.54327393,   5.4278698 , -34.18032455,  45.6623497 ,
  -4.92739248, -22.95082664,  52.26649857,  37.61194992, -46.98610306,
 -29.15704918],
[ 48.75985718,  49.25251007,  25.73770714,  35.71054459,  37.88261795,
 -23.92636108,  29.50111008,   5.52225924, -48.80569077, -12.87804317,
 -44.31132507,  33.96275711,  -9.77431583, -39.3640213 ,  40.46903992,
  -4.15516138, -38.28639221,  42.42279053, -40.16818237,  30.91417503,
 -26.71399117, -33.90458298,   0.11442117, -46.18736267,   7.94215441,
 -41.64306259,  38.54327393,   5.4278698 , -34.18032455,  45.6623497 ,
  -4.92739248, -22.95082664,  52.26649857,  37.84289551, -48.02286148,
 -28.37735558],
[ 50.70274734,  50.67316818,  24.206707  ,  35.03264236,  38.62698746,
 -23.73765755,  29.06399536,   9.44386578, -48.46549225, -11.56112385,
 -45.45293045,  32.9116745 ,  -8.5488224 , -40.80046844,  39.30707169,
  -2.58302379, -39.88097   ,  41.0565834 , -40.08502579,  31.0945015 ,
 -26.62948036, -33.59205246,   1.40687394, -46.3939743 ,   8.02638912,
 -42.04371643,  38.08818054,   5.140172  , -34.66604614,  45.3282547 ,
  -5.44713831, -24.35364723,  51.57552719,  37.84289551, -48.02286148,
 -28.37735558],
[ 50.70274734,  50.67316818,  24.206707  ,  35.03264236,  38.62698746,
 -23.73765755,  29.06399536,   9.44386578, -48.46549225, -11.56112385,
 -45.45293045,  32.9116745 ,  -8.5488224 , -40.80046844,  39.30707169,
  -2.58302379, -39.88097   ,  41.0565834 , -40.08502579,  31.0945015 ,
 -26.62948036, -33.59205246,   1.40687394, -46.3939743 ,   8.02638912,
 -42.04371643,  38.08818054,   5.140172  , -34.66604614,  45.3282547 ,
  -5.44713831, -24.35364723,  51.57552719,  38.12093353, -46.88653183,
 -27.96432877],
[ 48.81098175,  48.79443359,  25.99241066,  36.09785461,  37.58430862,
 -23.81535149,  30.58265114,   6.76915312, -47.97589493, -14.36790371,
 -43.26789474,  34.70243835, -10.29065895, -39.38930511,  40.31614304,
  -4.52650118, -38.41905975,  42.2645607 , -40.79182434,  30.06879234,
 -26.73390007, -33.88504791,  -0.29173505, -46.2009201 ,   8.18623543,
 -41.20871735,  38.95681763,   5.50529957, -33.81824112,  45.92193985,
  -4.9128027 , -22.99766922,  52.24727631,  38.12093353, -46.88653183,
 -27.96432877],
[ 48.81098175,  48.79443359,  25.99241066,  36.09785461,  37.58430862,
 -23.81535149,  30.58265114,   6.76915312, -47.97589493, -14.36790371,
 -43.26789474,  34.70243835, -10.29065895, -39.38930511,  40.31614304,
  -4.52650118, -38.41905975,  42.2645607 , -40.79182434,  30.06879234,
 -26.73390007, -33.88504791,  -0.29173505, -46.2009201 ,   8.18623543,
 -41.20871735,  38.95681763,   5.50529957, -33.81824112,  45.92193985,
  -4.9128027 , -22.99766922,  52.24727631,  37.4493866 , -47.77497101,
 -27.8087616 ],
[ 46.81765747,  45.05561829,  28.90057373,  34.93020248,  39.38019562,
 -22.62493134,  34.09738541,   7.58280611, -45.41669083, -16.86047363,
 -41.88411331,  35.2739563 , -12.75554657, -38.00933838,  40.93156052,
  -6.7319622 , -37.25188065,  43.00912476, -40.88217163,  30.23228836,
 -26.40952492, -34.86682129,  -2.34099603, -45.4051857 ,   9.43421173,
 -39.70611572,  40.2147522 ,   7.49075747, -32.1150322 ,  46.8542366 ,
  -3.92469931, -19.75745773,  53.63809967,  37.4493866 , -47.77497101,
 -27.8087616 ],
[ 46.81765747,  45.05561829,  28.90057373,  34.93020248,  39.38019562,
 -22.62493134,  34.09738541,   7.58280611, -45.41669083, -16.86047363,
 -41.88411331,  35.2739563 , -12.75554657, -38.00933838,  40.93156052,
  -6.7319622 , -37.25188065,  43.00912476, -40.88217163,  30.23228836,
 -26.40952492, -34.86682129,  -2.34099603, -45.4051857 ,   9.43421173,
 -39.70611572,  40.2147522 ,   7.49075747, -32.1150322 ,  46.8542366 ,
  -3.92469931, -19.75745773,  53.63809967,  35.73396301, -47.43099594,
 -28.86034012],
[ 46.68980408,  43.40410995,  29.558321  ,  34.23307419,  40.06817627,
 -22.48209381,  33.76526642,   7.57250452, -45.66585541, -17.39497566,
 -41.87852859,  35.02013779, -13.30175304, -37.99304962,  40.77251434,
  -6.91237354, -37.4491806 ,  42.80869675, -40.72710419,  30.7091465 ,
 -26.09708405, -35.03887558,  -2.50742555, -45.26363373,   9.367589  ,
 -39.2123909 ,  40.71170807,   7.56031704, -31.63097572,  47.17127609,
  -4.08995008, -18.45888519,  54.08649063,  35.73396301, -47.43099594,
 -28.86034012],
[ 46.68980408,  43.40410995,  29.558321  ,  34.23307419,  40.06817627,
 -22.48209381,  33.76526642,   7.57250452, -45.66585541, -17.39497566,
 -41.87852859,  35.02013779, -13.30175304, -37.99304962,  40.77251434,
  -6.91237354, -37.4491806 ,  42.80869675, -40.72710419,  30.7091465 ,
 -26.09708405, -35.03887558,  -2.50742555, -45.26363373,   9.367589  ,
 -39.2123909 ,  40.71170807,   7.56031704, -31.63097572,  47.17127609,
  -4.08995008, -18.45888519,  54.08649063,  35.11972809, -47.44313049,
 -28.63916016],
[ 47.47984314,  44.47809982,  28.96495056,  34.26316071,  39.4565239 ,
 -23.49521255,  31.16162491,   6.97146559, -47.57266617, -15.80435276,
 -43.2059288 ,  34.15078735, -12.72911167, -38.5549202 ,  40.42640305,
  -6.12303877, -37.90348816,  42.52811432, -40.99541855,  30.49716759,
 -25.92498779, -35.04949951,  -1.35527861, -45.30455017,   8.84644985,
 -39.96305084,  40.09365463,   6.91224909, -32.73377609,  46.5137291 ,
  -4.61017561, -19.52045822,  53.67033005,  35.11972809, -47.44313049,
 -28.63916016],
[ 47.47984314,  44.47809982,  28.96495056,  34.26316071,  39.4565239 ,
 -23.49521255,  31.16162491,   6.97146559, -47.57266617, -15.80435276,
 -43.2059288 ,  34.15078735, -12.72911167, -38.5549202 ,  40.42640305,
  -6.12303877, -37.90348816,  42.52811432, -40.99541855,  30.49716759,
 -25.92498779, -35.04949951,  -1.35527861, -45.30455017,   8.84644985,
 -39.96305084,  40.09365463,   6.91224909, -32.73377609,  46.5137291 ,
  -4.61017561, -19.52045822,  53.67033005,  36.04393768, -47.66516495,
 -28.3567028 ],
[ 48.12970734,  46.20107651,  28.2105484 ,  34.99065781,  38.32752991,
 -24.27881622,  30.11053848,   6.17376757, -48.35335159, -14.37409401,
 -44.01496506,  33.74721527, -12.07993603, -38.96337891,  40.23353195,
  -5.74924374, -38.08620071,  42.41690445, -40.23176193,  31.51799393,
 -25.90034485, -34.14131927,   2.94912696, -45.91818237,   7.47046757,
 -42.23410416,  37.99051285,   5.23390484, -35.73001099,  44.4834671 ,
  -6.51375532, -23.29656029,  51.93888474,  36.04393768, -47.66516495,
 -28.3567028 ],
[ 48.12970734,  46.20107651,  28.2105484 ,  34.99065781,  38.32752991,
 -24.27881622,  30.11053848,   6.17376757, -48.35335159, -14.37409401,
 -44.01496506,  33.74721527, -12.07993603, -38.96337891,  40.23353195,
  -5.74924374, -38.08620071,  42.41690445, -40.23176193,  31.51799393,
 -25.90034485, -34.14131927,   2.94912696, -45.91818237,   7.47046757,
 -42.23410416,  37.99051285,   5.23390484, -35.73001099,  44.4834671 ,
  -6.51375532, -23.29656029,  51.93888474,  39.1728363 , -48.16682816,
 -27.41314697],
[ 49.79121399,  47.67347717,  26.95967102,  34.7408905 ,  38.59767914,
 -24.20942497,  30.38615227,   9.27470589, -47.68089676, -13.10625267,
 -45.10362244,  32.81304169, -10.58674335, -40.34269333,  39.28351212,
  -4.13476753, -39.42356873,  41.37018585, -40.56557083,  30.70456314,
 -26.35281181, -34.34156799,   3.37633491, -45.73908234,   7.57322502,
 -42.70253754,  37.44256973,   5.15244246, -36.41886902,  43.9309082 ,
  -6.02596712, -25.2000885 ,  51.10234451,  39.1728363 , -48.16682816,
 -27.41314697],
[ 49.79121399,  47.67347717,  26.95967102,  34.7408905 ,  38.59767914,
 -24.20942497,  30.38615227,   9.27470589, -47.68089676, -13.10625267,
 -45.10362244,  32.81304169, -10.58674335, -40.34269333,  39.28351212,
  -4.13476753, -39.42356873,  41.37018585, -40.56557083,  30.70456314,
 -26.35281181, -34.34156799,   3.37633491, -45.73908234,   7.57322502,
 -42.70253754,  37.44256973,   5.15244246, -36.41886902,  43.9309082 ,
  -6.02596712, -25.2000885 ,  51.10234451,  39.9858017 , -48.4691391 ,
 -27.52124405],
[ 49.99222565,  50.13355255,  25.87376976,  34.27756119,  39.13669968,
 -24.00362206,  31.06220055,   9.15854454, -47.26591873, -12.87439632,
 -44.72238159,  33.42102432,  -9.59700203, -40.51729584,  39.35800934,
  -3.44053721, -39.08659744,  41.75173187, -40.12895203,  31.11354828,
 -26.54092598, -33.71889877,  -1.92231834, -46.28333282,   9.78034496,
 -40.4826889 ,  39.34848022,   7.61639452, -33.99534607,  45.48751068,
  -3.31375289, -23.39221954,  52.19798279,  39.9858017 , -48.4691391 ,
 -27.52124405],
[ 49.99222565,  50.13355255,  25.87376976,  34.27756119,  39.13669968,
 -24.00362206,  31.06220055,   9.15854454, -47.26591873, -12.87439632,
 -44.72238159,  33.42102432,  -9.59700203, -40.51729584,  39.35800934,
  -3.44053721, -39.08659744,  41.75173187, -40.12895203,  31.11354828,
 -26.54092598, -33.71889877,  -1.92231834, -46.28333282,   9.78034496,
 -40.4826889 ,  39.34848022,   7.61639452, -33.99534607,  45.48751068,
  -3.31375289, -23.39221954,  52.19798279,  36.6852417 , -46.12727737,
 -29.37786293]
], "float32")
print np.shape(meet)
#a = np.ones((50,1), dtype=np.int)*3

#target_data = np.array([[0], [1], [2]], "float32")

#print np.reshape(np.append(training_data10,two),(53,18))
