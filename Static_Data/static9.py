import numpy as np


static9 = np.array([[ -96, -118,  177,    7,  -38,   41,  -17,  -50,  -19,   19,  -52,  -10,
  -16,   51,   18,  -24,   48,   19],
[ -96, -118,  176,    7,  -38,   41,  -17,  -50,  -19,   19,  -52,  -10,
  -16,   51,   17,  -24,   47,   19],
[ -95, -115, -179,    7,  -39,   40,  -17,  -50,  -20,   18,  -53,  -11,
  -16,   51,   18,  -24,   47,   20],
[ -98, -123, -165,    5,  -37,   42,  -18,  -50,  -18,   16,  -53,   -9,
  -15,   53,   15,  -23,   49,   17],
[ -98, -122, -162,    4,  -37,   42,  -18,  -50,  -19,   16,  -54,   -9,
  -14,   53,   14,  -23,   49,   17],
[ -98, -124, -161,    4,  -37,   42,  -18,  -50,  -18,   15,  -54,   -8,
  -14,   53,   14,  -22,   49,   17],
[ -98, -124, -157,    3,  -37,   43,  -18,  -50,  -19,   15,  -54,   -8,
  -14,   53,   14,  -22,   49,   17],
[ -98, -122, -156,    3,  -37,   43,  -18,  -50,  -19,   15,  -54,   -8,
  -14,   53,   13,  -22,   49,   17],
[ -97, -120, -151,    2,  -38,   42,  -19,  -50,  -19,   14,  -54,   -8,
  -13,   53,   14,  -22,   49,   17],
[ -98, -122, -156,    3,  -37,   43,  -18,  -50,  -19,   14,  -54,   -8,
  -13,   53,   13,  -22,   49,   17],
[ -98, -124, -158,    3,  -36,   43,  -18,  -50,  -18,   14,  -54,   -8,
  -13,   54,   13,  -22,   49,   16],
[ -98, -121, -154,    3,  -37,   43,  -18,  -50,  -19,   13,  -54,   -9,
  -14,   53,   15,  -23,   49,   16],
[ -98, -120, -157,    3,  -36,   43,  -18,  -50,  -18,   13,  -54,   -9,
  -15,   52,   16,  -23,   49,   16],
[ -96, -114, -150,    3,  -37,   43,  -18,  -50,  -20,   13,  -54,  -10,
  -16,   52,   17,  -24,   49,   16],
[ -96, -113, -147,    2,  -37,   43,  -18,  -50,  -20,   12,  -54,  -10,
  -15,   52,   16,  -23,   49,   16],
[ -99, -119, -143,  -20,  -50,  -17,    9,  -56,   -5,    1,  -35,   45,
  -14,   53,   13,  -22,   50,   13],
[-103, -131, -149,    1,  -31,   47,  -20,  -51,  -16,    8,  -56,   -2,
  -11,   55,    7,  -20,   52,   10],
[-103, -131, -149,    0,  -32,   47,  -19,  -51,  -16,    8,  -56,   -2,
  -11,   55,    6,  -20,   52,   10],
[-105, -142, -151,  -21,  -51,  -13,    7,  -56,    0,    0,  -31,   47,
  -10,   55,    6,  -18,   53,   10],
[-105, -145, -153,  -21,  -51,  -13,   10,  -56,   -1,   -1,  -32,   47,
  -10,   55,    6,  -18,   53,   10],
[-104, -145, -154,   -1,  -33,   46,  -20,  -51,  -14,   10,  -56,   -2,
  -10,   55,    7,  -18,   52,   12],
[-106, -145, -159,  -20,  -51,  -13,   10,  -56,   -1,    0,  -32,   47,
  -11,   55,    6,  -19,   52,   10],
[-106, -146, -163,    0,  -31,   47,  -20,  -51,  -13,   10,  -56,    0,
  -12,   55,    6,  -20,   52,   10],
[-105, -145, -165,    0,  -32,   46,  -20,  -51,  -13,   10,  -56,   -1,
  -13,   54,    8,  -21,   52,   11],
[-105, -146, -166,   -1,  -33,   46,  -20,  -51,  -13,   10,  -56,    0,
  -14,   55,    7,  -21,   51,   11],
[-106, -147, -166,   -1,  -33,   46,  -20,  -51,  -12,    9,  -56,    0,
  -13,   55,    7,  -21,   51,   11],
[-107, -147, -163,  -20,  -51,  -11,    8,  -56,    0,   -2,  -31,   47,
  -13,   55,    5,  -20,   52,    9],
[-108, -148, -157,  -22,  -51,  -11,   11,  -56,    0,   -3,  -30,   48,
  -11,   55,    6,  -18,   53,    8],
[-108, -148, -155,  -22,  -51,  -11,   11,  -56,    0,   -3,  -30,   48,
  -11,   55,    5,  -18,   53,    8],
[-107, -149, -156,  -22,  -51,  -12,   11,  -56,    0,   -2,  -31,   47,
  -10,   55,    6,  -18,   53,    9],
[-105, -148, -153,   -2,  -32,   46,  -21,  -51,  -13,   10,  -56,   -1,
  -10,   55,    7,  -17,   53,   11],
[-105, -145, -153,   -3,  -33,   46,  -21,  -51,  -14,   10,  -56,   -1,
  -10,   55,    7,  -18,   53,   11],
[-104, -143, -156,   -2,  -33,   46,  -20,  -51,  -14,    9,  -56,   -1,
  -12,   55,    8,  -19,   52,   12],
[-104, -142, -159,   -1,  -33,   46,  -20,  -51,  -14,    9,  -56,   -1,
  -13,   55,    8,  -20,   52,   11],
[-104, -142, -165,  -19,  -51,  -14,    8,  -56,   -1,    0,  -33,   46,
  -14,   54,    8,  -21,   51,   12],
[-106, -144, -166,    0,  -32,   47,  -19,  -52,  -13,    8,  -56,   -1,
  -14,   54,    7,  -21,   51,   11],
[-107, -144, -160,  -20,  -51,  -13,    5,  -57,    0,   -1,  -31,   47,
  -13,   55,    5,  -20,   52,    9],
[-106, -141, -155,   -2,  -31,   47,  -21,  -51,  -13,    7,  -56,   -1,
  -11,   55,    4,  -19,   53,    8],
[-105, -138, -153,   -2,  -32,   47,  -21,  -50,  -15,    7,  -56,   -2,
  -11,   55,    5,  -19,   52,   10],
[-106, -140, -155,   -1,  -31,   47,  -21,  -51,  -14,    7,  -56,   -1,
  -12,   55,    7,  -20,   52,    9],
[-106, -141, -154,  -21,  -51,  -14,    5,  -57,   -1,   -1,  -31,   47,
  -11,   55,    5,  -19,   52,    9],
[-106, -141, -154,  -21,  -51,  -14,    4,  -57,   -1,   -1,  -31,   47,
  -12,   55,    7,  -19,   52,    9],
[-105, -141, -152,   -2,  -32,   47,  -22,  -50,  -14,    4,  -57,   -1,
  -11,   55,    6,  -19,   53,   10],
[-105, -142, -153,  -22,  -50,  -14,    4,  -57,   -1,   -2,  -32,   47,
  -11,   55,    5,  -19,   52,   10],
[-104, -138, -154,   -2,  -32,   46,  -21,  -50,  -15,    4,  -57,   -2,
  -12,   55,    7,  -20,   52,   10],
[-104, -134, -155,   -1,  -32,   46,  -20,  -51,  -15,    4,  -57,   -3,
  -14,   55,    7,  -21,   52,   10],
[-105, -135, -152,   -1,  -31,   48,  -21,  -51,  -14,    4,  -57,   -1,
  -13,   55,    6,  -20,   52,    8],
[-106, -136, -152,   -2,  -30,   48,  -21,  -51,  -14,    5,  -57,   -1,
  -12,   55,    4,  -20,   53,    7],
[-106, -137, -152,  -21,  -51,  -14,    6,  -56,    0,   -1,  -30,   48,
  -12,   55,    5,  -19,   53,    8],
[-106, -139, -152,  -21,  -51,  -14,    7,  -56,    0,   -1,  -30,   48,
  -11,   55,    4,  -19,   53,    8],
[-54,  14,  -9, -43, -27, -25,  -6, -55,  13,   0, -55,  15,  -3,  35,  44,
 -15,  31,  45],
[-54,  13, -13, -45, -25, -24,  -6, -54,  14,  -1, -54,  16,  -1,  35,  45,
 -14,  31,  45],
[-53,  13, -15, -44, -26, -24,  -5, -55,  14,  -1, -54,  17,   0,  34,  45,
 -12,  31,  46],
[-53,  12, -17, -45, -25, -23,  -4, -55,  14,  -2, -54,  17,   0,  35,  45,
 -11,  31,  46],
[-54,  10, -20, -46, -24, -23,  -4, -54,  15,  -3, -53,  19,   1,  35,  44,
 -10,  32,  45],
[-54,  10, -20, -46, -22, -24,  -3, -54,  16,  -2, -53,  20,   1,  35,  44,
 -10,  32,  45],
[-54,  11, -20, -47, -21, -24,  -2, -54,  16,  -2, -53,  20,   1,  35,  44,
 -10,  32,  45],
[-53,   9, -19, -47, -19, -25,  -2, -55,  15,  -2, -53,  19,   0,  34,  45,
 -11,  31,  46],
[-53,   9, -19, -47, -19, -25,  -2, -54,  15,  -2, -53,  19,   1,  34,  45,
 -11,  31,  46],
[-52,   8, -19, -47, -19, -25,  -2, -54,  15,  -2, -53,  19,   1,  34,  45,
 -10,  32,  46],
[-52,   7, -19, -47, -19, -25,  -2, -55,  15,  -3, -53,  19,   1,  34,  45,
 -10,  31,  46],
[-52,   8, -20, -46, -21, -24,  -2, -55,  15,  -3, -53,  20,   1,  34,  45,
 -10,  32,  46],
[-53,   9, -20, -46, -22, -24,  -2, -54,  15,  -2, -53,  20,   1,  34,  45,
 -10,  32,  46],
[-54,  11, -19, -46, -23, -24,   0, -54,  17,   0, -52,  22,   1,  35,  44,
 -11,  32,  45],
[-53,  11, -17, -46, -22, -24,   0, -54,  17,   0, -53,  21,   0,  35,  45,
 -11,  31,  46],
[-52,  10, -15, -45, -24, -25,  -1, -54,  16,   0, -53,  20,   0,  33,  46,
 -12,  30,  46],
[-51,   8, -16, -45, -25, -24,  -2, -54,  16,  -1, -53,  20,   0,  32,  47,
 -12,  30,  47],
[-51,   7, -18, -45, -23, -24,  -4, -54,  16,  -2, -53,  20,   0,  31,  47,
 -11,  29,  47],
[-51,   7, -19, -46, -22, -24,  -4, -54,  16,  -3, -53,  20,   1,  31,  47,
 -10,  29,  47],
[-52,   8, -19, -47, -22, -24,  -4, -54,  16,  -3, -53,  20,   1,  32,  47,
 -10,  30,  47],
[-51,   9, -19, -46, -22, -24,  -3, -54,  15,  -1, -53,  19,   1,  32,  47,
 -10,  29,  47],
[-51,  10, -19, -46, -23, -24,  -3, -55,  15,  -1, -53,  19,   2,  31,  47,
  -9,  29,  48],
[-51,  10, -20, -45, -24, -23,  -3, -55,  15,  -1, -53,  19,   2,  31,  47,
  -9,  29,  48],
[-51,  10, -21, -46, -24, -23,  -4, -55,  15,  -2, -53,  19,   3,  30,  48,
  -8,  29,  48],
[-51,  10, -21, -45, -25, -23,  -3, -55,  15,  -2, -53,  19,   3,  30,  48,
  -8,  28,  48],
[-51,  10, -21, -44, -27, -24,  -3, -55,  15,  -2, -53,  19,   3,  30,  48,
  -8,  28,  48],
[-51,   9, -21, -43, -28, -24,  -3, -55,  14,  -2, -53,  19,   3,  30,  48,
  -8,  28,  49],
[-51,   9, -23, -44, -26, -24,  -3, -55,  14,  -3, -53,  19,   4,  30,  48,
  -7,  28,  49],
[-51,  10, -24, -45, -24, -24,  -3, -55,  14,  -3, -53,  19,   4,  29,  48,
  -6,  28,  49],
[-52,  10, -26, -45, -25, -23,  -4, -55,  14,  -3, -53,  20,   6,  29,  48,
  -5,  28,  49],
[-52,  11, -28, -46, -24, -22,  -4, -55,  14,  -4, -53,  19,   7,  29,  48,
  -3,  28,  49],
[-52,  10, -25, -45, -25, -24,  -3, -55,  14,  -3, -54,  18,   5,  28,  49,
  -5,  27,  49],
[-52,  11, -24, -45, -24, -25,  -2, -55,  13,  -2, -54,  18,   4,  28,  49,
  -6,  27,  50],
[-52,  10, -24, -45, -25, -24,  -2, -55,  14,  -2, -54,  18,   4,  28,  49,
  -6,  27,  50],
[-52,   9, -23, -45, -25, -23,  -2, -55,  14,  -3, -54,  18,   3,  28,  49,
  -6,  27,  50],
[-52,   9, -22, -45, -24, -23,  -2, -55,  14,  -3, -54,  18,   2,  28,  49,
  -8,  26,  50],
[-51,   8, -21, -45, -24, -23,  -2, -55,  15,  -2, -53,  19,   2,  28,  49,
  -8,  26,  50],
[-52,   8, -20, -45, -24, -24,  -3, -55,  15,  -3, -53,  19,   1,  27,  50,
  -9,  26,  49],
[-51,   6, -20, -45, -25, -23,  -3, -54,  15,  -3, -53,  19,   0,  27,  50,
 -10,  25,  50],
[-51,   7, -17, -45, -25, -23,  -3, -54,  16,  -2, -53,  20,   0,  25,  51,
 -12,  24,  50],
[-50,   6, -16, -46, -22, -24,  -3, -54,  16,  -3, -53,  20,  -1,  23,  52,
 -12,  22,  51],
[-50,   6, -15, -47, -21, -24,  -3, -54,  16,  -2, -53,  21,  -2,  22,  52,
 -13,  20,  51],
[-49,   5, -15, -46, -20, -25,  -4, -54,  15,  -3, -53,  20,  -2,  21,  53,
 -14,  19,  52],
[-49,   6, -15, -47, -20, -25,  -3, -54,  16,  -2, -53,  20,  -2,  20,  53,
 -13,  18,  52],
[-50,   6, -16, -47, -20, -24,  -4, -54,  16,  -3, -53,  20,  -1,  19,  53,
 -12,  17,  53],
[-50,   6, -17, -46, -21, -24,  -4, -54,  16,  -3, -53,  19,  -1,  17,  54,
 -11,  15,  53],
[-50,   6, -18, -46, -21, -24,  -4, -54,  16,  -3, -53,  19,  -1,  16,  54,
 -11,  14,  54],
[-49,   7, -17, -47, -20, -25,  -4, -54,  15,  -3, -53,  19,  -1,  14,  55,
 -12,  12,  54],
[-49,   7, -17, -47, -20, -25,  -4, -54,  15,  -3, -53,  19,  -1,  14,  55,
 -12,  12,  54],
[-49,   7, -16, -46, -20, -25,  -3, -55,  15,  -3, -53,  19,  -2,  14,  55,
 -12,  12,  54]
],"float32")

print np.shape(static9)