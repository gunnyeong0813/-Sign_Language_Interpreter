import numpy as np

forward = np.array([[ 70.28053284, -26.77522278,  25.96478081,  -3.37369919,  56.00014496,
 -11.63650513,  -3.44418192,  56.95450974,  -5.20842838,  -0.11008832,
  56.88869095,  -6.81697845,   1.72532523,  54.15718842, -18.62333298,
   9.97319221,  53.56367111, -17.72779465],
[  6.98809891e+01,  -2.44475155e+01,   2.41290302e+01,   2.14989662e+00,
   5.61686745e+01,  -1.11024437e+01,  -3.23342252e+00,   5.69828110e+01,
  -5.03098011e+00,   2.00086366e-02,   5.69598007e+01,  -6.19573593e+00,
   1.09992623e+00,   5.39732056e+01,  -1.91960831e+01,   9.40290737e+00,
   5.35466995e+01,  -1.80870876e+01],
[ 71.20858765, -24.07151985,  26.7462616 ,   1.86294162,  56.4747467 ,
  -9.48360634,  -2.30940461,  57.10729599,  -4.02859163,   0.20395042,
  57.07606506,  -5.00878286,   2.6976831 ,  55.31988525, -14.67103004,
  10.75061607,  54.2953949 , -14.80678844],
[ 71.40962982, -21.69182777,  27.49399376,   1.4095093 ,  56.59806442,
  -8.80219269,  -2.46039534,  57.10026169,  -4.03891468,   0.49557996,
  57.07908249,  -4.9537034 ,   3.02384257,  55.47945023, -13.98905563,
  11.05318069,  54.35134888, -14.37236404],
[ 71.54871368, -21.70512581,  28.6396389 ,   0.88625228,  56.50483704,
  -9.44585419,  -2.73562789,  57.06371689,  -4.36516953,   3.46706343,
  55.53705597, -13.65362358,  11.16578579,  53.90646744, -15.88158131,
  -0.31502643,  57.14706039,  -4.11350679],
[ 71.17544556, -30.25406075,  24.33538628,  -2.29457188,  55.68571854,
 -13.29066563,  -3.28447413,  57.01477814,  -4.61881542,  -1.26303959,
  57.15945816,  -3.7426188 ,   2.26824045,  55.61063766, -13.60583305,
   9.23732948,  53.98087311, -16.83875084],
[ 71.24708557, -30.61398697,  22.65896988,  -3.24169779,  55.65806198,
 -13.20901871,  -2.51516986,  57.0121994 ,  -5.10781717,   1.64997089,
  55.66699982, -13.46363354,   7.84062195,  53.95921326, -17.59927177,
  -1.98158073,  57.15136337,  -3.54985189],
[ 71.55775452, -28.06854439,  23.36486053,  -3.8950243 ,  56.13820648,
 -10.77668667,  -2.2225678 ,  57.00154114,  -5.35639   ,  -2.18450618,
  57.15446472,  -3.37665391,   1.70761752,  55.72108841, -13.2306757 ,
   7.67594576,  53.83827209, -18.03680992],
[ 71.70098877, -16.35381699,  27.95298386,   1.19740677,  56.88930511,
  -6.70668983,  -2.07097316,  57.12853241,  -3.85334563,  -1.59303379,
  57.13817978,  -3.93663979,   3.05436683,  55.60823822, -13.46109962,
   9.8136692 ,  53.67889786, -17.46636963],
[ 71.59234619, -14.19059277,  28.66056442,   2.04381514,  56.87399673,
  -6.63158989,  -2.20046949,  57.14840698,  -3.4675014 ,   3.34020972,
  55.55561829, -13.60965252,  10.05178547,  53.52075577, -17.81282234,
  -1.45657074,  57.12636185,  -4.15494776],
[ 71.65010834, -21.99753952,  27.70534325,  -1.11282802,  56.3651886 ,
 -10.22416687,  -2.09556293,  57.07527542,  -4.5637784 ,   3.14483094,
  55.6481781 , -13.2739172 ,   9.58581066,  53.51444244, -18.08655357,
  -1.26338995,  57.16761017,  -3.61592531],
[ 71.71315002, -22.67478371,  27.94329071,  -1.89309537,  56.4975853 ,
  -9.34051991,  -2.10747361,  57.08181   ,  -4.47567892,   3.22779131,
  55.66648865, -13.17686367,  10.99159908,  54.20465088, -14.96151066,
  -1.16931927,  57.1763649 ,  -3.50745893],
[ 70.99048615, -20.28941154,  26.73986435,  -3.30604076,  56.46170807,
  -9.16253281,  -2.59162283,  57.01155472,  -5.07666397,   2.43561077,
  55.04955673, -15.69779301,  12.24954128,  54.56752014, -12.45556927,
  -1.42833769,  57.11667252,  -4.29558468],
[ 70.70560455, -20.92180634,  25.01626205,  -4.51815033,  56.3436203 ,
  -9.36959171,  -2.86389208,  56.97434616,  -5.34120035,   1.27722907,
  54.49312973, -17.65428543,  12.03139687,  54.60031891, -12.5242691 ,
  -1.87260437,  57.09030914,  -4.4716897 ],
[ 70.37049866, -18.77451324,  24.17159081,  -5.15428782,  56.37348557,
  -8.84701443,  -2.48596334,  57.02869034,  -4.93506908,   0.95392001,
  54.25812531, -18.38347816,  11.65647221,  54.5288887 , -13.17321014,
  -2.20488977,  57.04469299,  -4.88344812],
[ 70.01721954, -15.19334316,  23.82463837,  -4.83921528,  56.41485596,
  -8.7608366 ,  -2.31859803,  57.06496048,  -4.58483076,   0.89476418,
  54.04358673, -19.00780487,  11.51093388,  54.46622467, -13.55489445,
  -2.47276902,  56.98532104,  -5.41894245],
[ 69.98615265, -13.05430508,  24.28418541,  -3.50768542,  56.59098816,
  -8.24395943,  -2.07346416,  57.09142685,  -4.36763477,   1.06078076,
  53.97193909, -19.20184708,  11.61658859,  54.40805054, -13.69763565,
  -2.45702815,  56.97118378,  -5.5725441 ],
[ 70.74902344, -10.34269905,  28.94932938,   0.41219518,  56.95211029,
  -6.25249577,  -1.97307479,  57.12788391,  -3.91384578,   2.59673619,
  54.11418915, -18.64719582,  12.95907402,  54.22994995, -13.19019127,
  -1.20141602,  57.06273651,  -5.02064276],
[ 70.66104126, -20.56718636,  27.90737534,  -3.89291239,  56.51564407,
  -8.58101273,  -2.19842792,  57.08966827,  -4.32933855,  -0.77136505,
  57.00464249,  -5.71681261,   2.22313452,  54.23522568, -18.34132767,
  12.96304989,  54.26364517, -13.04693985],
[ 70.88742828, -24.02384758,  26.30835915,  -5.28585243,  56.30869675,
  -9.17590046,  -2.36544418,  56.96802902,  -5.64397621,   1.47555435,
  54.36901855, -18.01773453,  12.46918201,  54.52990341, -12.4022541 ,
  -1.29192626,  56.99462128,  -5.72282743],
[ 70.39176941, -29.20518494,  23.14283943,  -6.09513283,  56.17936707,
  -9.46228409,  -2.34609008,  56.91832352,  -6.13243055,  -1.4876734 ,
  56.91475296,  -6.42683792,   0.46868694,  54.31189346, -18.24295044,
  11.63608265,  54.60414124, -12.87616825],
[ 70.53774261, -31.85113525,  22.30060577,  -6.34632587,  56.04675674,
 -10.0643692 ,  -1.42000484,  56.85747147,  -6.92951488,  -0.93743998,
  56.8861618 ,  -6.77440643,   0.099345  ,  54.39538574, -17.99829865,
  11.3728857 ,  54.69409943, -12.72868824],
[ 70.91307068, -34.34424591,  25.31507111,  -5.500597  ,  56.30054092,
  -9.09940052,  -0.72459525,  56.95413589,  -6.2054925 ,   0.82245809,
  56.95317078,  -6.20211649,   1.11871791,  54.52553177, -17.56477928,
  12.39820385,  54.56088638, -12.33695316],
[ 71.31532288, -40.56689072,  25.74827957,  -5.97009706,  55.84490967,
 -11.33624458,  -1.33016682,  57.0052681 ,  -5.60681772,   1.15730679,
  54.73215485, -16.90735054,  12.70045948,  54.60369873, -11.8296566 ,
   1.12082279,  56.99413681,  -5.76357841],
[ 71.20425415, -31.63642883,  25.98797035,  -5.76640034,  55.7947998 ,
 -11.68311691,  -2.01328087,  56.89693832,  -6.44139624,   0.53742611,
  56.95148849,  -6.24864388,   1.2207762 ,  54.55848694, -17.45530701,
  12.37918568,  54.62775803, -12.05695534],
[ 71.18458557, -30.04254913,  25.80566788,  -5.24590492,  55.84334183,
 -11.69651222,  -2.05473661,  56.8729744 ,  -6.63697052,   1.14579999,
  54.52856827, -17.55360031,  12.68617916,  54.75870132, -11.10639572,
   0.36964604,  56.9495697 ,  -6.27823544],
[ 70.86780548, -35.39324188,  22.89878464,  -5.44879007,  55.69867325,
 -12.27903938,  -2.06708741,  56.82656479,  -7.01961279,   0.20508808,
  54.53328323, -17.57513809,  12.04788685,  54.75254822, -11.82426834,
  -0.34415758,  56.72537994,  -8.05724716],
[ 71.25686646, -31.95815468,  24.11190224,  -4.89010048,  55.65779114,
 -12.69266605,  -1.85622728,  56.7444458 ,  -7.70900059,  12.24777126,
  54.84133911, -11.19045353,  -0.32952473,  56.64610291,  -8.5974884 ,
   0.47303373,  54.58469772, -17.40958023],
[  7.15286560e+01,  -3.42070580e+01,   2.29525700e+01,  -4.88830471e+00,
   5.56915054e+01,  -1.25445986e+01,  -2.07178521e+00,   5.67740059e+01,
  -7.43144751e+00,  -7.22992718e-01,   5.64042587e+01,  -1.00420685e+01,
   1.14239244e+01,   5.49986877e+01,  -1.12891369e+01,  -5.67708313e-02,
   5.46965179e+01,  -1.70614815e+01],
[ 72.61270142, -41.93417358,  22.02892876,  -5.35012197,  54.84289932,
 -15.69837189,  -2.03902531,  56.20615387, -10.93239784,  -0.22708113,
  55.52942657, -14.11514759,  10.43007755,  55.09244156, -11.78317261,
   0.92306638,  55.40417099, -14.57162476],
[ 72.91615295, -42.16038132,  24.11331749,  -4.13481283,  55.29759979,
 -14.41823196,  -0.77703077,  56.43070984,  -9.88826847,   0.69803357,
  56.08314514, -11.70470047,   9.29713726,  54.71048737, -14.25243855,
   2.10424972,  55.35189438, -14.64739895],
[ 73.71373749, -44.53469467,  25.19669533,  -1.95291328,  55.18289566,
 -15.29184628,  -1.09092295,  56.31811905, -10.4826355 ,   8.9327755 ,
  54.65675354, -14.68507576,   0.19107343,  55.87245941, -12.6900959 ,
   2.20010924,  55.22137833, -15.11836624],
[ 75.10834503, -48.62495041,  23.99743652,  -2.37502742,  55.01712799,
 -15.8202858 ,  -1.84008157,  55.93333054, -12.28343964,   8.66061592,
  54.75196075, -14.49217129,   0.11961012,  55.48490524, -14.2904644 ,
   2.06711292,  55.21210098, -15.17093945],
[ 75.61260986, -49.98017883,  23.80578232,  -3.07747293,  55.07881927,
 -15.48092461,  -1.52274656,  55.86027908, -12.65373707,   8.75069809,
  54.55295944, -15.17254448,   0.36820894,  55.19855881, -15.35546589,
   1.96642733,  54.28911209, -18.21076202],
[ 76.70840454, -47.51318741,  30.75205612,  -3.54542708,  55.77272415,
 -12.63486671,  -0.39809665,  56.09429169, -11.6652689 ,   4.07782125,
  53.79329681, -19.29919243,   1.28794396,  55.82152176, -12.84934044,
   7.94272041,  53.87289429, -17.81658745],
[ 75.13304138, -51.8119545 ,  23.59828949,  -4.33679152,  54.78507996,
 -16.20474243,  -2.1793282 ,  55.99053574, -11.96315956,  -0.56870025,
  55.54595184, -14.04031086,   3.32228184,  55.00347137, -15.69672966,
   7.75215292,  54.5885849 , -15.58194828],
[ 75.75092316, -52.33224487,  22.31822395,  -4.52764511,  54.58075714,
 -16.82997322,  -2.39980173,  55.90338135, -12.32311821,  -0.37805623,
  55.22280884, -15.26777267,   3.09313393,  54.78736877, -16.47977448,
   7.3236928 ,  54.59137344, -15.7782135 ],
[ 75.90960693, -49.58206177,  23.98727226,  -4.28199911,  55.12945175,
 -15.00714493,  -1.60157573,  55.85871506, -12.65090466,   3.21302795,
  54.76431274, -16.53338623,   0.16110688,  55.14481354, -15.55088425,
   7.03789186,  54.53411102, -16.1029644 ],
[ 75.66688538, -47.91722107,  24.14033318,  -4.64748764,  55.3624115 ,
 -14.00751495,  -1.55996192,  55.91111755, -12.42255402,   0.17477131,
  55.25424576, -15.15730667,   2.54519033,  54.86688232, -16.30807877,
   6.78776884,  54.55897522, -16.12609291],
[ 75.48960114, -47.90576553,  23.53812408,  -5.16197872,  55.33609009,
 -13.93117619,  -1.65849876,  55.96806717, -12.15036964,  -0.18294731,
  55.37072754, -14.72600269,   7.83908606,  54.45415878, -16.0031147 ,
   1.84751534,  55.07405472, -15.69208336],
[ 75.13754272, -47.14689255,  23.27915001,  -6.49077368,  55.31902695,
 -13.4343338 ,  -1.24374139,  55.98725891, -12.11141872,   8.070611  ,
  54.49404526, -15.75025749,   0.18730365,  55.55838394, -14.0013237 ,
   2.42478752,  55.33826447, -14.6493454 ],
[ 74.75793457, -44.41130447,  26.41426277,  -6.54025841,  55.78353882,
 -11.32379341,  -1.17399108,  56.23006821, -10.93652344,  10.90773773,
  55.26010895, -10.49513817,   1.21151924,  55.47692871, -14.27056408,
   3.73531485,  55.47487259, -13.83447075],
[ 74.7392807 , -43.28574753,  27.83850098,  -6.28399229,  56.07184219,
  -9.96326637,  -1.44997489,  56.30596161, -10.50440693,   1.62630451,
  55.47341919, -14.24295139,  11.5664196 ,  55.23382187,  -9.91208458,
   4.2327981 ,  55.49740219, -13.59883976],
[ 74.00681305, -41.13707733,  27.13130569,  -6.60657358,  56.11952591,
  -9.47409916,  -1.59480178,  56.35999298, -10.18893242,  11.54791164,
  55.09101486, -10.697299  ,   0.24178523,  56.00746918, -12.07938194,
   3.81368017,  55.15495682, -15.03971672],
[  7.31246567e+01,  -3.49156914e+01,   2.67757530e+01,  -6.99730253e+00,
   5.61194115e+01,  -9.19000244e+00,  -1.64478385e+00,   5.65344925e+01,
  -9.16254997e+00,   8.86046886e-01,   5.36281815e+01,  -2.01504230e+01,
   9.03114700e+00,   5.41402245e+01,  -1.64341297e+01,   1.10239722e-02,
   5.62215042e+01,  -1.10430470e+01],
[  7.31737976e+01,  -3.02018814e+01,   2.84413700e+01,  -6.74705315e+00,
   5.62123299e+01,  -8.80099964e+00,  -1.62979174e+00,   5.65659943e+01,
  -8.96874332e+00,  -4.52068336e-02,   5.63713379e+01,  -1.02506857e+01,
   9.89582241e-01,   5.23837700e+01,  -2.31898212e+01,   6.74706030e+00,
   5.31533966e+01,  -2.02977791e+01],
[ 73.35844421, -27.96910667,  30.19041252,  -6.44157696,  56.41855621,
  -7.6327672 ,  -2.11998963,  56.65246964,  -8.29516697,   1.57652342,
  52.24859619, -23.46071815,  -0.67689824,  56.71357727,  -8.11900234,
   6.58333683,  52.54191208, -21.88180923],
[ 72.5302887 , -23.16064835,  33.54601669,  -4.3940196 ,  56.82405472,
  -5.87585926,  -2.81736755,  56.77587891,  -7.16718149,   3.48450994,
  51.67424011, -24.50382805,  -1.21503055,  56.72443008,  -7.97928667,
   8.49750996,  51.7917366 , -22.98292542],
[ 72.22488403, -25.8766613 ,  33.34664536,  -5.92075491,  56.35271835,
  -8.49247551,  -3.06374168,  56.67949677,  -7.80094624,  -1.07090127,
  56.64909363,  -8.51703358,   1.59316814,  51.50767136, -25.04451561,
   8.20753765,  51.40921021, -23.92772675],
[ 72.22488403, -25.8766613 ,  33.34664536,  -5.92075491,  56.35271835,
  -8.49247551,  -3.06374168,  56.67949677,  -7.80094624,  -1.07090127,
  56.64909363,  -8.51703358,   1.59316814,  51.50767136, -25.04451561,
   8.20753765,  51.40921021, -23.92772675]
], "float32")
print np.shape(forward)
#a = np.ones((50,1), dtype=np.int)*3

#target_data = np.array([[0], [1], [2]], "float32")

#print np.reshape(np.append(training_data10,two),(53,18))