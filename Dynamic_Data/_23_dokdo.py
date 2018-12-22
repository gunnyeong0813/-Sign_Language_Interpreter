import numpy as np

dokdo = np.array([
[ -8.21241474,   5.56233072,  -1.61750138, -40.13775635,   5.30094767,
  40.54216385, -40.13775635,   5.30094767,  40.54216385, -40.13775635,
   5.30094767,  40.54216385, -40.13775635,   5.30094767,  40.54216385,
 -40.13775635,   5.30094767,  40.54216385, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.77563477,  170.50866699,   29.5689373 ,  -40.13775635,    5.30094767,
   40.54216385,  -40.13775635,    5.30094767,   40.54216385,  -40.13775635,
    5.30094767,   40.54216385,  -40.13775635,    5.30094767,   40.54216385,
  -40.13775635,    5.30094767,   40.54216385,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.21954918,   5.62394857,  -1.74430215, -40.46046829,   5.40203381,
  40.20665359, -40.46046829,   5.40203381,  40.20665359, -40.46046829,
   5.40203381,  40.20665359, -40.46046829,   5.40203381,  40.20665359,
 -40.46046829,   5.40203381,  40.20665359, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.66687775,  170.92225647,   29.71348763,  -40.46046829,    5.40203381,
   40.20665359,  -40.46046829,    5.40203381,   40.20665359,  -40.46046829,
    5.40203381,   40.20665359,  -40.46046829,    5.40203381,   40.20665359,
  -40.46046829,    5.40203381,   40.20665359,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.21290493,   5.79182577,  -1.83777535, -40.57444   ,   5.68166637,
  40.05296707, -40.57444   ,   5.68166637,  40.05296707, -40.57444   ,
   5.68166637,  40.05296707, -40.57444   ,   5.68166637,  40.05296707,
 -40.57444   ,   5.68166637,  40.05296707, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.47799683,  170.66583252,   29.83049202,  -40.57444   ,    5.68166637,
   40.05296707,  -40.57444   ,    5.68166637,   40.05296707,  -40.57444   ,
    5.68166637,   40.05296707,  -40.57444   ,    5.68166637,   40.05296707,
  -40.57444   ,    5.68166637,   40.05296707,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.08533955,   5.95880842,  -1.83911109, -40.73859787,   5.73293066,
  39.87864685, -40.73859787,   5.73293066,  39.87864685, -40.73859787,
   5.73293066,  39.87864685, -40.73859787,   5.73293066,  39.87864685,
 -40.73859787,   5.73293066,  39.87864685, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.60111237,  170.5652771 ,   30.10108757,  -40.73859787,    5.73293066,
   39.87864685,  -40.73859787,    5.73293066,   39.87864685,  -40.73859787,
    5.73293066,   39.87864685,  -40.73859787,    5.73293066,   39.87864685,
  -40.73859787,    5.73293066,   39.87864685,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.02188301,   6.16535044,  -1.72587907, -40.45081711,   5.91200972,
  40.14456177, -40.45081711,   5.91200972,  40.14456177, -40.45081711,
   5.91200972,  40.14456177, -40.45081711,   5.91200972,  40.14456177,
 -40.45081711,   5.91200972,  40.14456177, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.4237442 ,  169.86175537,   29.8698349 ,  -40.45081711,    5.91200972,
   40.14456177,  -40.45081711,    5.91200972,   40.14456177,  -40.45081711,
    5.91200972,   40.14456177,  -40.45081711,    5.91200972,   40.14456177,
  -40.45081711,    5.91200972,   40.14456177,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.1186161 ,   6.13401175,  -1.73492432, -40.29868317,   5.91257906,
  40.29719543, -40.29868317,   5.91257906,  40.29719543, -40.29868317,
   5.91257906,  40.29719543, -40.29868317,   5.91257906,  40.29719543,
 -40.29868317,   5.91257906,  40.29719543, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.41488647,  169.59707642,   29.72005844,  -40.29868317,    5.91257906,
   40.29719543,  -40.29868317,    5.91257906,   40.29719543,  -40.29868317,
    5.91257906,   40.29719543,  -40.29868317,    5.91257906,   40.29719543,
  -40.29868317,    5.91257906,   40.29719543,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.08486557,   6.11906242,  -1.79566526, -40.23345947,   6.15231657,
  40.32646942, -40.23345947,   6.15231657,  40.32646942, -40.23345947,
   6.15231657,  40.32646942, -40.23345947,   6.15231657,  40.32646942,
 -40.23345947,   6.15231657,  40.32646942, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.17928314,  169.35578918,   29.7672081 ,  -40.23345947,    6.15231657,
   40.32646942,  -40.23345947,    6.15231657,   40.32646942,  -40.23345947,
    6.15231657,   40.32646942,  -40.23345947,    6.15231657,   40.32646942,
  -40.23345947,    6.15231657,   40.32646942,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.27942657,   6.20651674,  -1.77461529, -40.29305649,   6.2053194 ,
  40.25878906, -40.29305649,   6.2053194 ,  40.25878906, -40.29305649,
   6.2053194 ,  40.25878906, -40.29305649,   6.2053194 ,  40.25878906,
 -40.29305649,   6.2053194 ,  40.25878906, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.13545227,  169.39863586,   29.8760128 ,  -40.29305649,    6.2053194 ,
   40.25878906,  -40.29305649,    6.2053194 ,   40.25878906,  -40.29305649,
    6.2053194 ,   40.25878906,  -40.29305649,    6.2053194 ,   40.25878906,
  -40.29305649,    6.2053194 ,   40.25878906,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.44661713,   6.29073572,  -1.92327607, -40.12415695,   6.40857649,
  40.395401  , -40.12415695,   6.40857649,  40.395401  , -40.12415695,
   6.40857649,  40.395401  , -40.12415695,   6.40857649,  40.395401  ,
 -40.12415695,   6.40857649,  40.395401  , -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.88368988,  169.0475769 ,   29.72061539,  -40.12415695,    6.40857649,
   40.395401  ,  -40.12415695,    6.40857649,   40.395401  ,  -40.12415695,
    6.40857649,   40.395401  ,  -40.12415695,    6.40857649,   40.395401  ,
  -40.12415695,    6.40857649,   40.395401  ,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.5598774 ,   6.35374355,  -2.00252604, -40.07411957,   6.53476095,
  40.42484665, -40.07411957,   6.53476095,  40.42484665, -40.07411957,
   6.53476095,  40.42484665, -40.07411957,   6.53476095,  40.42484665,
 -40.07411957,   6.53476095,  40.42484665, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.71069717,  168.97865295,   29.65781212,  -40.07411957,    6.53476095,
   40.42484665,  -40.07411957,    6.53476095,   40.42484665,  -40.07411957,
    6.53476095,   40.42484665,  -40.07411957,    6.53476095,   40.42484665,
  -40.07411957,    6.53476095,   40.42484665,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.62683773,   6.36199713,  -2.01900482, -39.86294937,   6.74106503,
  40.59938431, -39.86294937,   6.74106503,  40.59938431, -39.86294937,
   6.74106503,  40.59938431, -39.86294937,   6.74106503,  40.59938431,
 -39.86294937,   6.74106503,  40.59938431, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.4516449 ,  168.65916443,   29.47381973,  -39.86294937,    6.74106503,
   40.59938431,  -39.86294937,    6.74106503,   40.59938431,  -39.86294937,
    6.74106503,   40.59938431,  -39.86294937,    6.74106503,   40.59938431,
  -39.86294937,    6.74106503,   40.59938431,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.66308117,   6.47318935,  -2.1027236 , -39.66648865,   6.82676125,
  40.77709198, -39.66648865,   6.82676125,  40.77709198, -39.66648865,
   6.82676125,  40.77709198, -39.66648865,   6.82676125,  40.77709198,
 -39.66648865,   6.82676125,  40.77709198, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.29178619,  168.43780518,   29.35064507,  -39.66648865,    6.82676125,
   40.77709198,  -39.66648865,    6.82676125,   40.77709198,  -39.66648865,
    6.82676125,   40.77709198,  -39.66648865,    6.82676125,   40.77709198,
  -39.66648865,    6.82676125,   40.77709198,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.73081398,   6.51398659,  -2.2171905 , -39.48862457,   6.6956706 ,
  40.97100067, -39.48862457,   6.6956706 ,  40.97100067, -39.48862457,
   6.6956706 ,  40.97100067, -39.48862457,   6.6956706 ,  40.97100067,
 -39.48862457,   6.6956706 ,  40.97100067, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.40383148,  168.28887939,   29.30124474,  -39.48862457,    6.6956706 ,
   40.97100067,  -39.48862457,    6.6956706 ,   40.97100067,  -39.48862457,
    6.6956706 ,   40.97100067,  -39.48862457,    6.6956706 ,   40.97100067,
  -39.48862457,    6.6956706 ,   40.97100067,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.89276695,   6.63668156,  -2.39470267, -39.59104156,   6.47411156,
  40.90772629, -39.59104156,   6.47411156,  40.90772629, -39.59104156,
   6.47411156,  40.90772629, -39.59104156,   6.47411156,  40.90772629,
 -39.59104156,   6.47411156,  40.90772629, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.63796234,  168.55543518,   29.42040825,  -39.59104156,    6.47411156,
   40.90772629,  -39.59104156,    6.47411156,   40.90772629,  -39.59104156,
    6.47411156,   40.90772629,  -39.59104156,    6.47411156,   40.90772629,
  -39.59104156,    6.47411156,   40.90772629,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.85375786,   6.65070295,  -2.43063402, -39.56830215,   6.35801983,
  40.94791031, -39.56830215,   6.35801983,  40.94791031, -39.56830215,
   6.35801983,  40.94791031, -39.56830215,   6.35801983,  40.94791031,
 -39.56830215,   6.35801983,  40.94791031, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.79473114,  168.50666809,   29.49834442,  -39.56830215,    6.35801983,
   40.94791031,  -39.56830215,    6.35801983,   40.94791031,  -39.56830215,
    6.35801983,   40.94791031,  -39.56830215,    6.35801983,   40.94791031,
  -39.56830215,    6.35801983,   40.94791031,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.62135029,   6.55714273,  -2.44751   , -39.62688828,   6.31690598,
  40.89758682, -39.62688828,   6.31690598,  40.89758682, -39.62688828,
   6.31690598,  40.89758682, -39.62688828,   6.31690598,  40.89758682,
 -39.62688828,   6.31690598,  40.89758682, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.82609558,  168.63427734,   29.56637383,  -39.62688828,    6.31690598,
   40.89758682,  -39.62688828,    6.31690598,   40.89758682,  -39.62688828,
    6.31690598,   40.89758682,  -39.62688828,    6.31690598,   40.89758682,
  -39.62688828,    6.31690598,   40.89758682,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.46941566,   6.36415291,  -2.44616032, -39.63651657,   6.49978971,
  40.85958481, -39.63651657,   6.49978971,  40.85958481, -39.63651657,
   6.49978971,  40.85958481, -39.63651657,   6.49978971,  40.85958481,
 -39.63651657,   6.49978971,  40.85958481, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.59811401,  168.64259338,   29.54276848,  -39.63651657,    6.49978971,
   40.85958481,  -39.63651657,    6.49978971,   40.85958481,  -39.63651657,
    6.49978971,   40.85958481,  -39.63651657,    6.49978971,   40.85958481,
  -39.63651657,    6.49978971,   40.85958481,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.44173908,   5.99361944,  -2.35482192, -39.86221695,   6.53551912,
  40.6336937 , -39.86221695,   6.53551912,  40.6336937 , -39.86221695,
   6.53551912,  40.6336937 , -39.86221695,   6.53551912,  40.6336937 ,
 -39.86221695,   6.53551912,  40.6336937 , -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.64515686,  168.89633179,   29.85610199,  -39.86221695,    6.53551912,
   40.6336937 ,  -39.86221695,    6.53551912,   40.6336937 ,  -39.86221695,
    6.53551912,   40.6336937 ,  -39.86221695,    6.53551912,   40.6336937 ,
  -39.86221695,    6.53551912,   40.6336937 ,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.5374651 ,   6.1677928 ,  -2.42107797, -39.84822083,   6.59123993,
  40.6384201 , -39.84822083,   6.59123993,  40.6384201 , -39.84822083,
   6.59123993,  40.6384201 , -39.84822083,   6.59123993,  40.6384201 ,
 -39.84822083,   6.59123993,  40.6384201 , -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.65231323,  168.77229309,   29.97503662,  -39.84822083,    6.59123993,
   40.6384201 ,  -39.84822083,    6.59123993,   40.6384201 ,  -39.84822083,
    6.59123993,   40.6384201 ,  -39.84822083,    6.59123993,   40.6384201 ,
  -39.84822083,    6.59123993,   40.6384201 ,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.93738079,   6.29606438,  -2.42882872, -39.80360794,   6.43731356,
  40.70676041, -39.80360794,   6.43731356,  40.70676041, -39.80360794,
   6.43731356,  40.70676041, -39.80360794,   6.43731356,  40.70676041,
 -39.80360794,   6.43731356,  40.70676041, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.80430984,  168.78826904,   29.9861908 ,  -39.80360794,    6.43731356,
   40.70676041,  -39.80360794,    6.43731356,   40.70676041,  -39.80360794,
    6.43731356,   40.70676041,  -39.80360794,    6.43731356,   40.70676041,
  -39.80360794,    6.43731356,   40.70676041,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -9.02005386,   6.18439245,  -2.46882772, -39.90532303,   6.17788506,
  40.64733124, -39.90532303,   6.17788506,  40.64733124, -39.90532303,
   6.17788506,  40.64733124, -39.90532303,   6.17788506,  40.64733124,
 -39.90532303,   6.17788506,  40.64733124, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  35.98209763,  169.2253418 ,   29.96837044,  -39.90532303,    6.17788506,
   40.64733124,  -39.90532303,    6.17788506,   40.64733124,  -39.90532303,
    6.17788506,   40.64733124,  -39.90532303,    6.17788506,   40.64733124,
  -39.90532303,    6.17788506,   40.64733124,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.86521626,   6.21762276,  -2.51636934, -39.8788681 ,   6.06706095,
  40.68996048, -39.8788681 ,   6.06706095,  40.68996048, -39.8788681 ,
   6.06706095,  40.68996048, -39.8788681 ,   6.06706095,  40.68996048,
 -39.8788681 ,   6.06706095,  40.68996048, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.07538223,  169.27822876,   29.94116592,  -39.8788681 ,    6.06706095,
   40.68996048,  -39.8788681 ,    6.06706095,   40.68996048,  -39.8788681 ,
    6.06706095,   40.68996048,  -39.8788681 ,    6.06706095,   40.68996048,
  -39.8788681 ,    6.06706095,   40.68996048,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.59458733,   6.1995163 ,  -2.48704791, -39.92825699,   5.86503506,
  40.67114258, -39.92825699,   5.86503506,  40.67114258, -39.92825699,
   5.86503506,  40.67114258, -39.92825699,   5.86503506,  40.67114258,
 -39.92825699,   5.86503506,  40.67114258, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.27201462,  169.48165894,   29.9623642 ,  -39.92825699,    5.86503506,
   40.67114258,  -39.92825699,    5.86503506,   40.67114258,  -39.92825699,
    5.86503506,   40.67114258,  -39.92825699,    5.86503506,   40.67114258,
  -39.92825699,    5.86503506,   40.67114258,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.67070961,   6.33079767,  -2.47215438, -39.88233185,   5.85418367,
  40.71773911, -39.88233185,   5.85418367,  40.71773911, -39.88233185,
   5.85418367,  40.71773911, -39.88233185,   5.85418367,  40.71773911,
 -39.88233185,   5.85418367,  40.71773911, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.35797501,  169.31982422,   30.14105415,  -39.88233185,    5.85418367,
   40.71773911,  -39.88233185,    5.85418367,   40.71773911,  -39.88233185,
    5.85418367,   40.71773911,  -39.88233185,    5.85418367,   40.71773911,
  -39.88233185,    5.85418367,   40.71773911,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965],
[ -8.50530243,   6.15624046,  -2.46094179, -39.9617691 ,   5.85169268,
  40.64014435, -39.9617691 ,   5.85169268,  40.64014435, -39.9617691 ,
   5.85169268,  40.64014435, -39.9617691 ,   5.85169268,  40.64014435,
 -39.9617691 ,   5.85169268,  40.64014435, -42.89574051, -35.00592041,
  14.74271107, -42.89574051, -35.00592041,  14.74271107, -42.89574051,
 -35.00592041,  14.74271107, -42.89574051, -35.00592041,  14.74271107,
 -42.89574051, -35.00592041,  14.74271107,  22.95249748, -15.94480705,
  21.66827965],
[  36.53514862,  169.30455017,   30.53538513,  -39.9617691 ,    5.85169268,
   40.64014435,  -39.9617691 ,    5.85169268,   40.64014435,  -39.9617691 ,
    5.85169268,   40.64014435,  -39.9617691 ,    5.85169268,   40.64014435,
  -39.9617691 ,    5.85169268,   40.64014435,  -42.89574051,  -35.00592041,
   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,  -42.89574051,
  -35.00592041,   14.74271107,  -42.89574051,  -35.00592041,   14.74271107,
  -42.89574051,  -35.00592041,   14.74271107,   22.95249748,  -15.94480705,
   21.66827965]
], "float32")
print np.shape(dokdo)
#a = np.ones((50,1), dtype=np.int)*3

#target_data = np.array([[0], [1], [2]], "float32")

#print np.reshape(np.append(training_data10,two),(53,18))
