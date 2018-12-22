import numpy as np

different = np.array([
[  -6.46542358,   -7.56521225,   53.70633698,   45.23007965,   -2.45807743,
  -35.08566666,   45.23007965,   -2.45807743,  -35.08566666,   45.23007965,
   -2.45807743,  -35.08566666,   45.23007965,   -2.45807743,  -35.08566666,
   45.23007965,   -2.45807743,  -35.08566666,  -20.68062019,   52.08499146,
  -11.92778206,  -20.68062019,   52.08499146,  -11.92778206,  -20.68062019,
   52.08499146,  -11.92778206,  -20.68062019,   52.08499146,  -11.92778206,
  -20.68062019,   52.08499146,  -11.92778206,   33.94041443,  177.42245483,
  -40.93348694],
[ -10.18718719,   -8.7627449 ,   53.75944138,   44.85569382,   -1.01748776,
  -35.6333847 ,   44.85569382,   -1.01748776,  -35.6333847 ,   44.85569382,
   -1.01748776,  -35.6333847 ,   44.85569382,   -1.01748776,  -35.6333847 ,
   44.85569382,   -1.01748776,  -35.6333847 ,  -19.76634598,   52.48417282,
  -11.72646046,  -19.76634598,   52.48417282,  -11.72646046,  -19.76634598,
   52.48417282,  -11.72646046,  -19.76634598,   52.48417282,  -11.72646046,
  -19.76634598,   52.48417282,  -11.72646046,   33.94041443,  177.42245483,
  -40.93348694],
[ -10.18718719,   -8.7627449 ,   53.75944138,   44.85569382,   -1.01748776,
  -35.6333847 ,   44.85569382,   -1.01748776,  -35.6333847 ,   44.85569382,
   -1.01748776,  -35.6333847 ,   44.85569382,   -1.01748776,  -35.6333847 ,
   44.85569382,   -1.01748776,  -35.6333847 ,  -19.76634598,   52.48417282,
  -11.72646046,  -19.76634598,   52.48417282,  -11.72646046,  -19.76634598,
   52.48417282,  -11.72646046,  -19.76634598,   52.48417282,  -11.72646046,
  -19.76634598,   52.48417282,  -11.72646046,   34.06665802,  176.46640015,
  -41.03499222],
[ -11.84435558,   -9.49621391,   54.04661942,   45.16449356,   -1.37244451,
  -35.22912598,   45.16449356,   -1.37244451,  -35.22912598,   45.16449356,
   -1.37244451,  -35.22912598,   45.16449356,   -1.37244451,  -35.22912598,
   45.16449356,   -1.37244451,  -35.22912598,  -19.16797638,   52.62449646,
  -12.08542347,  -19.16797638,   52.62449646,  -12.08542347,  -19.16797638,
   52.62449646,  -12.08542347,  -19.16797638,   52.62449646,  -12.08542347,
  -19.16797638,   52.62449646,  -12.08542347,   34.06665802,  176.46640015,
  -41.03499222],
[ -11.84435558,   -9.49621391,   54.04661942,   45.16449356,   -1.37244451,
  -35.22912598,   45.16449356,   -1.37244451,  -35.22912598,   45.16449356,
   -1.37244451,  -35.22912598,   45.16449356,   -1.37244451,  -35.22912598,
   45.16449356,   -1.37244451,  -35.22912598,  -19.16797638,   52.62449646,
  -12.08542347,  -19.16797638,   52.62449646,  -12.08542347,  -19.16797638,
   52.62449646,  -12.08542347,  -19.16797638,   52.62449646,  -12.08542347,
  -19.16797638,   52.62449646,  -12.08542347,   35.6255722 ,  175.79248047,
  -41.85038757],
[ -11.35481071,   -9.20712852,   53.74279785,   45.03449249,   -2.03437781,
  -35.36328888,   45.03449249,   -2.03437781,  -35.36328888,   45.03449249,
   -2.03437781,  -35.36328888,   45.03449249,   -2.03437781,  -35.36328888,
   45.03449249,   -2.03437781,  -35.36328888,  -18.63183594,   52.79203415,
  -12.19271469,  -18.63183594,   52.79203415,  -12.19271469,  -18.63183594,
   52.79203415,  -12.19271469,  -18.63183594,   52.79203415,  -12.19271469,
  -18.63183594,   52.79203415,  -12.19271469,   35.6255722 ,  175.79248047,
  -41.85038757],
[ -11.35481071,   -9.20712852,   53.74279785,   45.03449249,   -2.03437781,
  -35.36328888,   45.03449249,   -2.03437781,  -35.36328888,   45.03449249,
   -2.03437781,  -35.36328888,   45.03449249,   -2.03437781,  -35.36328888,
   45.03449249,   -2.03437781,  -35.36328888,  -18.63183594,   52.79203415,
  -12.19271469,  -18.63183594,   52.79203415,  -12.19271469,  -18.63183594,
   52.79203415,  -12.19271469,  -18.63183594,   52.79203415,  -12.19271469,
  -18.63183594,   52.79203415,  -12.19271469,   36.87256622,  175.44241333,
  -42.28855515],
[ -11.13117313,   -8.63463593,   53.74912643,   45.16876221,   -1.84040105,
  -35.20230484,   45.16876221,   -1.84040105,  -35.20230484,   45.16876221,
   -1.84040105,  -35.20230484,   45.16876221,   -1.84040105,  -35.20230484,
   45.16876221,   -1.84040105,  -35.20230484,  -18.2961998 ,   53.02614212,
  -11.67405987,  -18.2961998 ,   53.02614212,  -11.67405987,  -18.2961998 ,
   53.02614212,  -11.67405987,  -18.2961998 ,   53.02614212,  -11.67405987,
  -18.2961998 ,   53.02614212,  -11.67405987,   36.87256622,  175.44241333,
  -42.28855515],
[ -11.13117313,   -8.63463593,   53.74912643,   45.16876221,   -1.84040105,
  -35.20230484,   45.16876221,   -1.84040105,  -35.20230484,   45.16876221,
   -1.84040105,  -35.20230484,   45.16876221,   -1.84040105,  -35.20230484,
   45.16876221,   -1.84040105,  -35.20230484,  -18.2961998 ,   53.02614212,
  -11.67405987,  -18.2961998 ,   53.02614212,  -11.67405987,  -18.2961998 ,
   53.02614212,  -11.67405987,  -18.2961998 ,   53.02614212,  -11.67405987,
  -18.2961998 ,   53.02614212,  -11.67405987,   37.27004623,  174.93803406,
  -42.50216293],
[ -12.90889549,   -9.01691437,   54.41804886,   45.67048645,   -2.12125516,
  -34.53278351,   45.67048645,   -2.12125516,  -34.53278351,   45.67048645,
   -2.12125516,  -34.53278351,   45.67048645,   -2.12125516,  -34.53278351,
   45.67048645,   -2.12125516,  -34.53278351,  -17.89473343,   53.53210831,
   -9.84370804,  -17.89473343,   53.53210831,   -9.84370804,  -17.89473343,
   53.53210831,   -9.84370804,  -17.89473343,   53.53210831,   -9.84370804,
  -17.89473343,   53.53210831,   -9.84370804,   37.27004623,  174.93803406,
  -42.50216293],
[ -12.90889549,   -9.01691437,   54.41804886,   45.67048645,   -2.12125516,
  -34.53278351,   45.67048645,   -2.12125516,  -34.53278351,   45.67048645,
   -2.12125516,  -34.53278351,   45.67048645,   -2.12125516,  -34.53278351,
   45.67048645,   -2.12125516,  -34.53278351,  -17.89473343,   53.53210831,
   -9.84370804,  -17.89473343,   53.53210831,   -9.84370804,  -17.89473343,
   53.53210831,   -9.84370804,  -17.89473343,   53.53210831,   -9.84370804,
  -17.89473343,   53.53210831,   -9.84370804,   39.151577  ,  174.96765137,
  -41.83826065],
[ -10.53392124,   -9.34790039,   54.16656113,   45.46265793,   -1.10356867,
  -34.85305023,   45.46265793,   -1.10356867,  -34.85305023,   45.46265793,
   -1.10356867,  -34.85305023,   45.46265793,   -1.10356867,  -34.85305023,
   45.46265793,   -1.10356867,  -34.85305023,  -18.44034004,   53.12768555,
  -10.96400738,  -18.44034004,   53.12768555,  -10.96400738,  -18.44034004,
   53.12768555,  -10.96400738,  -18.44034004,   53.12768555,  -10.96400738,
  -18.44034004,   53.12768555,  -10.96400738,   39.151577  ,  174.96765137,
  -41.83826065],
[ -10.53392124,   -9.34790039,   54.16656113,   45.46265793,   -1.10356867,
  -34.85305023,   45.46265793,   -1.10356867,  -34.85305023,   45.46265793,
   -1.10356867,  -34.85305023,   45.46265793,   -1.10356867,  -34.85305023,
   45.46265793,   -1.10356867,  -34.85305023,  -18.44034004,   53.12768555,
  -10.96400738,  -18.44034004,   53.12768555,  -10.96400738,  -18.44034004,
   53.12768555,  -10.96400738,  -18.44034004,   53.12768555,  -10.96400738,
  -18.44034004,   53.12768555,  -10.96400738,   37.75000381,  175.30258179,
  -41.79709625],
[  -9.17439938,   -8.37781334,   54.27719498,   45.41930389,   -1.24372387,
  -34.90481949,   45.41930389,   -1.24372387,  -34.90481949,   45.41930389,
   -1.24372387,  -34.90481949,   45.41930389,   -1.24372387,  -34.90481949,
   45.41930389,   -1.24372387,  -34.90481949,  -18.62471962,   52.80039978,
  -12.16733932,  -18.62471962,   52.80039978,  -12.16733932,  -18.62471962,
   52.80039978,  -12.16733932,  -18.62471962,   52.80039978,  -12.16733932,
  -18.62471962,   52.80039978,  -12.16733932,   37.75000381,  175.30258179,
  -41.79709625],
[  -9.17439938,   -8.37781334,   54.27719498,   45.41930389,   -1.24372387,
  -34.90481949,   45.41930389,   -1.24372387,  -34.90481949,   45.41930389,
   -1.24372387,  -34.90481949,   45.41930389,   -1.24372387,  -34.90481949,
   45.41930389,   -1.24372387,  -34.90481949,  -18.62471962,   52.80039978,
  -12.16733932,  -18.62471962,   52.80039978,  -12.16733932,  -18.62471962,
   52.80039978,  -12.16733932,  -18.62471962,   52.80039978,  -12.16733932,
  -18.62471962,   52.80039978,  -12.16733932,   35.57261276,  176.088974  ,
  -41.89726257],
[  -9.32919216,   -8.34306335,   54.17720413,   45.59575653,   -1.71672821,
  -34.65380478,   45.59575653,   -1.71672821,  -34.65380478,   45.59575653,
   -1.71672821,  -34.65380478,   45.59575653,   -1.71672821,  -34.65380478,
   45.59575653,   -1.71672821,  -34.65380478,  -18.83279228,   52.71038818,
  -12.2371254 ,  -18.83279228,   52.71038818,  -12.2371254 ,  -18.83279228,
   52.71038818,  -12.2371254 ,  -18.83279228,   52.71038818,  -12.2371254 ,
  -18.83279228,   52.71038818,  -12.2371254 ,   35.57261276,  176.088974  ,
  -41.89726257],
[  -9.32919216,   -8.34306335,   54.17720413,   45.59575653,   -1.71672821,
  -34.65380478,   45.59575653,   -1.71672821,  -34.65380478,   45.59575653,
   -1.71672821,  -34.65380478,   45.59575653,   -1.71672821,  -34.65380478,
   45.59575653,   -1.71672821,  -34.65380478,  -18.83279228,   52.71038818,
  -12.2371254 ,  -18.83279228,   52.71038818,  -12.2371254 ,  -18.83279228,
   52.71038818,  -12.2371254 ,  -18.83279228,   52.71038818,  -12.2371254 ,
  -18.83279228,   52.71038818,  -12.2371254 ,   35.63225937,  175.69075012,
  -41.72073746],
[  -8.21123981,   -7.68392467,   54.23538589,   45.6112442 ,   -0.99776256,
  -34.66158295,   45.6112442 ,   -0.99776256,  -34.66158295,   45.6112442 ,
   -0.99776256,  -34.66158295,   45.6112442 ,   -0.99776256,  -34.66158295,
   45.6112442 ,   -0.99776256,  -34.66158295,  -19.02060509,   52.62357712,
  -12.31997585,  -19.02060509,   52.62357712,  -12.31997585,  -19.02060509,
   52.62357712,  -12.31997585,  -19.02060509,   52.62357712,  -12.31997585,
  -19.02060509,   52.62357712,  -12.31997585,   35.63225937,  175.69075012,
  -41.72073746],
[  -8.21123981,   -7.68392467,   54.23538589,   45.6112442 ,   -0.99776256,
  -34.66158295,   45.6112442 ,   -0.99776256,  -34.66158295,   45.6112442 ,
   -0.99776256,  -34.66158295,   45.6112442 ,   -0.99776256,  -34.66158295,
   45.6112442 ,   -0.99776256,  -34.66158295,  -19.02060509,   52.62357712,
  -12.31997585,  -19.02060509,   52.62357712,  -12.31997585,  -19.02060509,
   52.62357712,  -12.31997585,  -19.02060509,   52.62357712,  -12.31997585,
  -19.02060509,   52.62357712,  -12.31997585,   35.18009567,  175.84112549,
  -41.61870193],
[  -9.63130665,   -8.18473911,   54.70601273,   45.66282654,   -1.04712701,
  -34.5921402 ,   45.66282654,   -1.04712701,  -34.5921402 ,   45.66282654,
   -1.04712701,  -34.5921402 ,   45.66282654,   -1.04712701,  -34.5921402 ,
   45.66282654,   -1.04712701,  -34.5921402 ,  -18.66403961,   52.94338226,
  -11.46552753,  -18.66403961,   52.94338226,  -11.46552753,  -18.66403961,
   52.94338226,  -11.46552753,  -18.66403961,   52.94338226,  -11.46552753,
  -18.66403961,   52.94338226,  -11.46552753,   35.18009567,  175.84112549,
  -41.61870193],
[  -9.63130665,   -8.18473911,   54.70601273,   45.66282654,   -1.04712701,
  -34.5921402 ,   45.66282654,   -1.04712701,  -34.5921402 ,   45.66282654,
   -1.04712701,  -34.5921402 ,   45.66282654,   -1.04712701,  -34.5921402 ,
   45.66282654,   -1.04712701,  -34.5921402 ,  -18.66403961,   52.94338226,
  -11.46552753,  -18.66403961,   52.94338226,  -11.46552753,  -18.66403961,
   52.94338226,  -11.46552753,  -18.66403961,   52.94338226,  -11.46552753,
  -18.66403961,   52.94338226,  -11.46552753,   35.05663681,  176.18309021,
  -41.32843018],
[  -6.27824354,   -6.75849915,   54.57200623,   45.53866959,   -0.63667858,
  -34.7653656 ,   45.53866959,   -0.63667858,  -34.7653656 ,   45.53866959,
   -0.63667858,  -34.7653656 ,   45.53866959,   -0.63667858,  -34.7653656 ,
   45.53866959,   -0.63667858,  -34.7653656 ,  -16.62257195,   53.70651627,
  -11.0501976 ,  -16.62257195,   53.70651627,  -11.0501976 ,  -16.62257195,
   53.70651627,  -11.0501976 ,  -16.62257195,   53.70651627,  -11.0501976 ,
  -16.62257195,   53.70651627,  -11.0501976 ,   35.05663681,  176.18309021,
  -41.32843018],
[  -6.27824354,   -6.75849915,   54.57200623,   45.53866959,   -0.63667858,
  -34.7653656 ,   45.53866959,   -0.63667858,  -34.7653656 ,   45.53866959,
   -0.63667858,  -34.7653656 ,   45.53866959,   -0.63667858,  -34.7653656 ,
   45.53866959,   -0.63667858,  -34.7653656 ,  -16.62257195,   53.70651627,
  -11.0501976 ,  -16.62257195,   53.70651627,  -11.0501976 ,  -16.62257195,
   53.70651627,  -11.0501976 ,  -16.62257195,   53.70651627,  -11.0501976 ,
  -16.62257195,   53.70651627,  -11.0501976 ,   33.59047318,  175.96562195,
  -41.56345367],
[  -7.70808983,   -7.05424166,   54.71920395,   45.73122025,   -1.90171337,
  -34.46512985,   45.73122025,   -1.90171337,  -34.46512985,   45.73122025,
   -1.90171337,  -34.46512985,   45.73122025,   -1.90171337,  -34.46512985,
   45.73122025,   -1.90171337,  -34.46512985,  -16.28057098,   53.73470306,
  -11.41626644,  -16.28057098,   53.73470306,  -11.41626644,  -16.28057098,
   53.73470306,  -11.41626644,  -16.28057098,   53.73470306,  -11.41626644,
  -16.28057098,   53.73470306,  -11.41626644,   33.59047318,  175.96562195,
  -41.56345367],
[  -7.70808983,   -7.05424166,   54.71920395,   45.73122025,   -1.90171337,
  -34.46512985,   45.73122025,   -1.90171337,  -34.46512985,   45.73122025,
   -1.90171337,  -34.46512985,   45.73122025,   -1.90171337,  -34.46512985,
   45.73122025,   -1.90171337,  -34.46512985,  -16.28057098,   53.73470306,
  -11.41626644,  -16.28057098,   53.73470306,  -11.41626644,  -16.28057098,
   53.73470306,  -11.41626644,  -16.28057098,   53.73470306,  -11.41626644,
  -16.28057098,   53.73470306,  -11.41626644,   32.23338318,  176.24327087,
  -41.84913254],
[  -0.20776646,   -5.48873377,   49.71886444,   40.2925415 ,    9.84671974,
  -39.52669907,   40.2925415 ,    9.84671974,  -39.52669907,   40.2925415 ,
    9.84671974,  -39.52669907,   40.2925415 ,    9.84671974,  -39.52669907,
   40.2925415 ,    9.84671974,  -39.52669907,  -38.67636871,   17.21618462,
  -38.60761261,  -38.67636871,   17.21618462,  -38.60761261,  -38.67636871,
   17.21618462,  -38.60761261,  -38.67636871,   17.21618462,  -38.60761261,
  -38.67636871,   17.21618462,  -38.60761261,    9.43275642, -163.41314697,
  -38.32714081],
[  -1.7871381 ,   -5.71474075,   50.02507019,   40.99653244,    7.82542276,
  -39.25370789,   40.99653244,    7.82542276,  -39.25370789,   40.99653244,
    7.82542276,  -39.25370789,   40.99653244,    7.82542276,  -39.25370789,
   40.99653244,    7.82542276,  -39.25370789,  -38.42516708,   15.40533829,
  -39.61045837,  -38.42516708,   15.40533829,  -39.61045837,  -38.42516708,
   15.40533829,  -39.61045837,  -38.42516708,   15.40533829,  -39.61045837,
  -38.42516708,   15.40533829,  -39.61045837,    9.43275642, -163.41314697,
  -38.32714081],
[  -1.7871381 ,   -5.71474075,   50.02507019,   40.99653244,    7.82542276,
  -39.25370789,   40.99653244,    7.82542276,  -39.25370789,   40.99653244,
    7.82542276,  -39.25370789,   40.99653244,    7.82542276,  -39.25370789,
   40.99653244,    7.82542276,  -39.25370789,  -38.42516708,   15.40533829,
  -39.61045837,  -38.42516708,   15.40533829,  -39.61045837,  -38.42516708,
   15.40533829,  -39.61045837,  -38.42516708,   15.40533829,  -39.61045837,
  -38.42516708,   15.40533829,  -39.61045837,    5.97408676, -163.79100037,
  -37.98093033],
[  -2.94115472,   -6.1822772 ,   50.23063278,   41.39261627,    6.20663404,
  -39.12717056,   41.39261627,    6.20663404,  -39.12717056,   41.39261627,
    6.20663404,  -39.12717056,   41.39261627,    6.20663404,  -39.12717056,
   41.39261627,    6.20663404,  -39.12717056,  -38.89753342,   17.36559296,
  -38.31742096,  -38.89753342,   17.36559296,  -38.31742096,  -38.89753342,
   17.36559296,  -38.31742096,  -38.89753342,   17.36559296,  -38.31742096,
  -38.89753342,   17.36559296,  -38.31742096,    5.97408676, -163.79100037,
  -37.98093033],
[  -2.94115472,   -6.1822772 ,   50.23063278,   41.39261627,    6.20663404,
  -39.12717056,   41.39261627,    6.20663404,  -39.12717056,   41.39261627,
    6.20663404,  -39.12717056,   41.39261627,    6.20663404,  -39.12717056,
   41.39261627,    6.20663404,  -39.12717056,  -38.89753342,   17.36559296,
  -38.31742096,  -38.89753342,   17.36559296,  -38.31742096,  -38.89753342,
   17.36559296,  -38.31742096,  -38.89753342,   17.36559296,  -38.31742096,
  -38.89753342,   17.36559296,  -38.31742096,    9.03326893, -162.09162903,
  -37.83874512],
[   1.1758523 ,   -8.11534786,   48.88478851,   39.78628922,    6.59817696,
  -40.6979332 ,   39.78628922,    6.59817696,  -40.6979332 ,   39.78628922,
    6.59817696,  -40.6979332 ,   39.78628922,    6.59817696,  -40.6979332 ,
   39.78628922,    6.59817696,  -40.6979332 ,  -39.04011536,   17.4966259 ,
  -38.1122551 ,  -39.04011536,   17.4966259 ,  -38.1122551 ,  -39.04011536,
   17.4966259 ,  -38.1122551 ,  -39.04011536,   17.4966259 ,  -38.1122551 ,
  -39.04011536,   17.4966259 ,  -38.1122551 ,    9.03326893, -162.09162903,
  -37.83874512],
[   1.1758523 ,   -8.11534786,   48.88478851,   39.78628922,    6.59817696,
  -40.6979332 ,   39.78628922,    6.59817696,  -40.6979332 ,   39.78628922,
    6.59817696,  -40.6979332 ,   39.78628922,    6.59817696,  -40.6979332 ,
   39.78628922,    6.59817696,  -40.6979332 ,  -39.04011536,   17.4966259 ,
  -38.1122551 ,  -39.04011536,   17.4966259 ,  -38.1122551 ,  -39.04011536,
   17.4966259 ,  -38.1122551 ,  -39.04011536,   17.4966259 ,  -38.1122551 ,
  -39.04011536,   17.4966259 ,  -38.1122551 ,    8.66046333, -161.07533264,
  -37.75309753],
[   3.01234055,   -4.66187859,   50.11884689,   40.14041901,    6.38484955,
  -40.38300705,   40.14041901,    6.38484955,  -40.38300705,   40.14041901,
    6.38484955,  -40.38300705,   40.14041901,    6.38484955,  -40.38300705,
   40.14041901,    6.38484955,  -40.38300705,  -39.36903763,   17.60725403,
  -37.72094727,  -39.36903763,   17.60725403,  -37.72094727,  -39.36903763,
   17.60725403,  -37.72094727,  -39.36903763,   17.60725403,  -37.72094727,
  -39.36903763,   17.60725403,  -37.72094727,    8.66046333, -161.07533264,
  -37.75309753],
[   3.01234055,   -4.66187859,   50.11884689,   40.14041901,    6.38484955,
  -40.38300705,   40.14041901,    6.38484955,  -40.38300705,   40.14041901,
    6.38484955,  -40.38300705,   40.14041901,    6.38484955,  -40.38300705,
   40.14041901,    6.38484955,  -40.38300705,  -39.36903763,   17.60725403,
  -37.72094727,  -39.36903763,   17.60725403,  -37.72094727,  -39.36903763,
   17.60725403,  -37.72094727,  -39.36903763,   17.60725403,  -37.72094727,
  -39.36903763,   17.60725403,  -37.72094727,    8.80736923, -162.362854  ,
  -37.70078278],
[   5.08209276,   -4.27525377,   49.88438797,   40.17689133,    6.19672251,
  -40.3760376 ,   40.17689133,    6.19672251,  -40.3760376 ,   40.17689133,
    6.19672251,  -40.3760376 ,   40.17689133,    6.19672251,  -40.3760376 ,
   40.17689133,    6.19672251,  -40.3760376 ,  -39.39213943,   18.28880692,
  -37.37091446,  -39.39213943,   18.28880692,  -37.37091446,  -39.39213943,
   18.28880692,  -37.37091446,  -39.39213943,   18.28880692,  -37.37091446,
  -39.39213943,   18.28880692,  -37.37091446,    8.80736923, -162.362854  ,
  -37.70078278],
[   5.08209276,   -4.27525377,   49.88438797,   40.17689133,    6.19672251,
  -40.3760376 ,   40.17689133,    6.19672251,  -40.3760376 ,   40.17689133,
    6.19672251,  -40.3760376 ,   40.17689133,    6.19672251,  -40.3760376 ,
   40.17689133,    6.19672251,  -40.3760376 ,  -39.39213943,   18.28880692,
  -37.37091446,  -39.39213943,   18.28880692,  -37.37091446,  -39.39213943,
   18.28880692,  -37.37091446,  -39.39213943,   18.28880692,  -37.37091446,
  -39.39213943,   18.28880692,  -37.37091446,    9.2817049 , -162.62242126,
  -37.68949127],
[   5.68639517,   -3.80439401,   49.92622375,   40.43524551,    5.39779902,
  -40.23258591,   40.43524551,    5.39779902,  -40.23258591,   40.43524551,
    5.39779902,  -40.23258591,   40.43524551,    5.39779902,  -40.23258591,
   40.43524551,    5.39779902,  -40.23258591,  -39.39635468,   17.95264435,
  -37.52914047,  -39.39635468,   17.95264435,  -37.52914047,  -39.39635468,
   17.95264435,  -37.52914047,  -39.39635468,   17.95264435,  -37.52914047,
  -39.39635468,   17.95264435,  -37.52914047,    9.2817049 , -162.62242126,
  -37.68949127],
[   5.68639517,   -3.80439401,   49.92622375,   40.43524551,    5.39779902,
  -40.23258591,   40.43524551,    5.39779902,  -40.23258591,   40.43524551,
    5.39779902,  -40.23258591,   40.43524551,    5.39779902,  -40.23258591,
   40.43524551,    5.39779902,  -40.23258591,  -39.39635468,   17.95264435,
  -37.52914047,  -39.39635468,   17.95264435,  -37.52914047,  -39.39635468,
   17.95264435,  -37.52914047,  -39.39635468,   17.95264435,  -37.52914047,
  -39.39635468,   17.95264435,  -37.52914047,    8.65746689, -162.03408813,
  -37.20423508],
[   3.09031701,   -4.57003403,   50.08686447,   40.69512558,    4.99374914,
  -40.02219009,   40.69512558,    4.99374914,  -40.02219009,   40.69512558,
    4.99374914,  -40.02219009,   40.69512558,    4.99374914,  -40.02219009,
   40.69512558,    4.99374914,  -40.02219009,  -39.6102562 ,   18.08242607,
  -37.24057007,  -39.6102562 ,   18.08242607,  -37.24057007,  -39.6102562 ,
   18.08242607,  -37.24057007,  -39.6102562 ,   18.08242607,  -37.24057007,
  -39.6102562 ,   18.08242607,  -37.24057007,    8.65746689, -162.03408813,
  -37.20423508],
[   3.09031701,   -4.57003403,   50.08686447,   40.69512558,    4.99374914,
  -40.02219009,   40.69512558,    4.99374914,  -40.02219009,   40.69512558,
    4.99374914,  -40.02219009,   40.69512558,    4.99374914,  -40.02219009,
   40.69512558,    4.99374914,  -40.02219009,  -39.6102562 ,   18.08242607,
  -37.24057007,  -39.6102562 ,   18.08242607,  -37.24057007,  -39.6102562 ,
   18.08242607,  -37.24057007,  -39.6102562 ,   18.08242607,  -37.24057007,
  -39.6102562 ,   18.08242607,  -37.24057007,   10.01165771, -161.26905823,
  -37.64382172],
[   6.88695002,   -2.94681263,   49.92061234,   40.57159424,    5.94040155,
  -40.01829529,   40.57159424,    5.94040155,  -40.01829529,   40.57159424,
    5.94040155,  -40.01829529,   40.57159424,    5.94040155,  -40.01829529,
   40.57159424,    5.94040155,  -40.01829529,  -39.25568008,   36.01805496,
  -21.08311844,  -39.25568008,   36.01805496,  -21.08311844,  -39.25568008,
   36.01805496,  -21.08311844,  -39.25568008,   36.01805496,  -21.08311844,
  -39.25568008,   36.01805496,  -21.08311844,   10.01165771, -161.26905823,
  -37.64382172],
[   6.88695002,   -2.94681263,   49.92061234,   40.57159424,    5.94040155,
  -40.01829529,   40.57159424,    5.94040155,  -40.01829529,   40.57159424,
    5.94040155,  -40.01829529,   40.57159424,    5.94040155,  -40.01829529,
   40.57159424,    5.94040155,  -40.01829529,  -39.25568008,   36.01805496,
  -21.08311844,  -39.25568008,   36.01805496,  -21.08311844,  -39.25568008,
   36.01805496,  -21.08311844,  -39.25568008,   36.01805496,  -21.08311844,
  -39.25568008,   36.01805496,  -21.08311844,   11.96883202, -166.25952148,
  -38.22660828],
[   7.71665239,   -3.43477845,   49.73761749,   40.34519577,    5.92558289,
  -40.24871445,   40.34519577,    5.92558289,  -40.24871445,   40.34519577,
    5.92558289,  -40.24871445,   40.34519577,    5.92558289,  -40.24871445,
   40.34519577,    5.92558289,  -40.24871445,  -34.86927414,   20.69555855,
  -40.48004532,  -34.86927414,   20.69555855,  -40.48004532,  -34.86927414,
   20.69555855,  -40.48004532,  -34.86927414,   20.69555855,  -40.48004532,
  -34.86927414,   20.69555855,  -40.48004532,   11.96883202, -166.25952148,
  -38.22660828],
[   7.71665239,   -3.43477845,   49.73761749,   40.34519577,    5.92558289,
  -40.24871445,   40.34519577,    5.92558289,  -40.24871445,   40.34519577,
    5.92558289,  -40.24871445,   40.34519577,    5.92558289,  -40.24871445,
   40.34519577,    5.92558289,  -40.24871445,  -34.86927414,   20.69555855,
  -40.48004532,  -34.86927414,   20.69555855,  -40.48004532,  -34.86927414,
   20.69555855,  -40.48004532,  -34.86927414,   20.69555855,  -40.48004532,
  -34.86927414,   20.69555855,  -40.48004532,    9.69316673, -164.55412292,
  -38.25639725],
[   7.4207592 ,   -4.60226583,   49.79399872,   40.40468979,    5.17293167,
  -40.29277802,   40.40468979,    5.17293167,  -40.29277802,   40.40468979,
    5.17293167,  -40.29277802,   40.40468979,    5.17293167,  -40.29277802,
   40.40468979,    5.17293167,  -40.29277802,  -38.50353622,   20.01486397,
  -37.41242599,  -38.50353622,   20.01486397,  -37.41242599,  -38.50353622,
   20.01486397,  -37.41242599,  -38.50353622,   20.01486397,  -37.41242599,
  -38.50353622,   20.01486397,  -37.41242599,    9.69316673, -164.55412292,
  -38.25639725],
[   7.4207592 ,   -4.60226583,   49.79399872,   40.40468979,    5.17293167,
  -40.29277802,   40.40468979,    5.17293167,  -40.29277802,   40.40468979,
    5.17293167,  -40.29277802,   40.40468979,    5.17293167,  -40.29277802,
   40.40468979,    5.17293167,  -40.29277802,  -38.50353622,   20.01486397,
  -37.41242599,  -38.50353622,   20.01486397,  -37.41242599,  -38.50353622,
   20.01486397,  -37.41242599,  -38.50353622,   20.01486397,  -37.41242599,
  -38.50353622,   20.01486397,  -37.41242599,    8.87362862, -161.7328186 ,
  -37.77788925],
[   8.11339569,   -3.80187416,   50.24057388,   40.65503311,    5.060009  ,
  -40.05459976,   40.65503311,    5.060009  ,  -40.05459976,   40.65503311,
    5.060009  ,  -40.05459976,   40.65503311,    5.060009  ,  -40.05459976,
   40.65503311,    5.060009  ,  -40.05459976,  -34.84315491,   22.33099937,
  -39.62432861,  -34.84315491,   22.33099937,  -39.62432861,  -34.84315491,
   22.33099937,  -39.62432861,  -34.84315491,   22.33099937,  -39.62432861,
  -34.84315491,   22.33099937,  -39.62432861,    8.87362862, -161.7328186 ,
  -37.77788925],
[   8.11339569,   -3.80187416,   50.24057388,   40.65503311,    5.060009  ,
  -40.05459976,   40.65503311,    5.060009  ,  -40.05459976,   40.65503311,
    5.060009  ,  -40.05459976,   40.65503311,    5.060009  ,  -40.05459976,
   40.65503311,    5.060009  ,  -40.05459976,  -34.84315491,   22.33099937,
  -39.62432861,  -34.84315491,   22.33099937,  -39.62432861,  -34.84315491,
   22.33099937,  -39.62432861,  -34.84315491,   22.33099937,  -39.62432861,
  -34.84315491,   22.33099937,  -39.62432861,    5.03802633, -163.90464783,
  -36.9006958 ],
[   6.66853428,   -3.66091871,   50.12688065,   40.80579758,    5.14458656,
  -39.8901825 ,   40.80579758,    5.14458656,  -39.8901825 ,   40.80579758,
    5.14458656,  -39.8901825 ,   40.80579758,    5.14458656,  -39.8901825 ,
   40.80579758,    5.14458656,  -39.8901825 ,  -35.57299805,   23.1336956 ,
  -38.4993515 ,  -35.57299805,   23.1336956 ,  -38.4993515 ,  -35.57299805,
   23.1336956 ,  -38.4993515 ,  -35.57299805,   23.1336956 ,  -38.4993515 ,
  -35.57299805,   23.1336956 ,  -38.4993515 ,    5.03802633, -163.90464783,
  -36.9006958 ],
[   6.66853428,   -3.66091871,   50.12688065,   40.80579758,    5.14458656,
  -39.8901825 ,   40.80579758,    5.14458656,  -39.8901825 ,   40.80579758,
    5.14458656,  -39.8901825 ,   40.80579758,    5.14458656,  -39.8901825 ,
   40.80579758,    5.14458656,  -39.8901825 ,  -35.57299805,   23.1336956 ,
  -38.4993515 ,  -35.57299805,   23.1336956 ,  -38.4993515 ,  -35.57299805,
   23.1336956 ,  -38.4993515 ,  -35.57299805,   23.1336956 ,  -38.4993515 ,
  -35.57299805,   23.1336956 ,  -38.4993515 ,    5.10653925, -161.0148468 ,
  -35.86685944]
], "float32")
print np.shape(different)
