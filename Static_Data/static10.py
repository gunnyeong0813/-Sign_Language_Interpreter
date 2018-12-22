import numpy as np


static10 = np.array([[-70,  34, -42, -48, -29,  -8, -24, -43, -27, -10, -48, -29,   3, -53, -20,
  -5,   6,  56],
[-71,  35, -43, -49, -27,  -7, -24, -43, -27, -10, -48, -28,   2, -53, -19,
  -4,   7,  56],
[-72,  34, -46, -49, -27,  -4, -24, -44, -27, -10, -48, -28,   2, -53, -19,
  -6,   9,  56],
[-73,  33, -48, -49, -28,  -3, -24, -44, -27, -10, -48, -28,   2, -53, -20,
  -6,  10,  55],
[-71,  30, -44, -49, -27,  -6, -24, -43, -28, -10, -48, -28,   2, -53, -21,
  -7,   8,  56],
[-71,  31, -44, -49, -28,  -6, -24, -44, -26, -10, -48, -27,   2, -53, -21,
  -7,   8,  56],
[-73,  32, -46, -49, -28,  -4, -24, -44, -26, -11, -48, -28,   2, -53, -21,
  -7,  10,  55],
[-73,  32, -46, -49, -28,  -4, -24, -43, -27, -10, -48, -28,   2, -52, -21,
  -7,  10,  55],
[-70,  29, -41, -49, -27,  -7, -24, -43, -28, -10, -47, -29,   3, -52, -22,
  -7,   7,  56],
[-69,  26, -41, -49, -27,  -8, -24, -43, -28, -10, -47, -29,   3, -52, -22,
  -8,   7,  56],
[-68,  25, -40, -49, -26,  -8, -24, -42, -29, -10, -47, -30,   3, -52, -23,
  -8,   6,  56],
[-67,  20, -40, -50, -25, -10, -24, -43, -29, -10, -47, -30,   2, -52, -23,
 -10,   5,  56],
[-69,  26, -41, -49, -26,  -8, -24, -44, -27, -10, -48, -28,   3, -52, -21,
  -7,   6,  56],
[-72,  32, -48, -50, -26,  -3, -25, -44, -25, -12, -48, -27,   2, -53, -20,
  -6,   9,  56],
[-73,  34, -51, -51, -25,  -2, -26, -43, -25, -13, -48, -27,   1, -53, -21,
  -5,  10,  56],
[-71,  33, -48, -50, -26,  -3, -26, -43, -25, -12, -48, -27,   2, -53, -21,
  -4,   8,  56],
[-74,  32, -52, -51, -25,  -2, -27, -44, -24, -13, -49, -25,   0, -54, -19,
  -6,  11,  55],
[-74,  30, -52, -50, -26,  -2, -26, -44, -24, -13, -48, -26,   0, -53, -20,
  -8,  12,  55],
[-74,  25, -51, -50, -26,  -3, -26, -43, -25, -12, -48, -27,   1, -53, -20,
 -10,  13,  54],
[-73,  27, -47, -50, -26,  -5, -25, -43, -26, -12, -48, -27,   2, -53, -20,
  -9,  11,  55],
[-70,  26, -43, -50, -25,  -7, -25, -43, -26, -12, -48, -27,   2, -53, -20,
  -8,   8,  56],
[-69,  23, -40, -50, -24,  -9, -24, -43, -27, -11, -48, -27,   3, -53, -20,
  -9,   7,  55],
[-70,  23, -42, -49, -27,  -7, -24, -44, -27, -10, -48, -27,   4, -53, -20,
 -10,  15,  54],
[-70,  20, -42, -49, -27,  -7, -24, -43, -27, -10, -48, -28,   4, -52, -21,
 -10,  24,  50],
[-69,  16, -41, -49, -27,  -8, -24, -43, -27, -10, -48, -27,   4, -53, -20,
 -10,  25,  50],
[-68,  16, -41, -50, -25,  -8, -24, -44, -27, -10, -49, -27,   4, -53, -20,
  -9,  24,  50],
[-68,  17, -42, -50, -24,  -8, -24, -44, -27, -10, -49, -27,   4, -53, -20,
  -8,  24,  51],
[-69,  19, -43, -50, -24,  -8, -24, -43, -27, -10, -48, -27,   4, -53, -20,
  -8,  24,  50],
[-69,  21, -43, -51, -24,  -8, -24, -43, -27, -11, -48, -27,   4, -53, -19,
  -7,  24,  51],
[-68,  25, -41, -51, -23, -10, -24, -43, -28, -11, -48, -28,   4, -53, -19,
  -6,  23,  51],
[-71,  24, -46, -50, -25,  -6, -24, -44, -26, -11, -49, -26,   3, -53, -18,
  -7,  26,  50],
[-70,  21, -45, -50, -25,  -7, -24, -43, -27, -11, -48, -27,   3, -53, -19,
  -7,  25,  50],
[-68,  21, -43, -51, -24,  -8, -24, -43, -27, -11, -48, -27,   3, -53, -19,
  -7,  24,  51],
[-67,  20, -42, -50, -25,  -8, -25, -43, -26, -11, -49, -27,   3, -53, -20,
  -7,  23,  51],
[-66,  17, -40, -50, -25,  -9, -24, -44, -26, -11, -49, -26,   4, -53, -19,
  -8,  22,  51],
[-65,  16, -38, -50, -25, -10, -24, -44, -26, -10, -49, -27,   4, -53, -20,
  -8,  22,  52],
[-64,  10, -37, -50, -25, -11, -24, -44, -26, -10, -49, -26,   5, -53, -19,
 -10,  22,  51],
[-66,   9, -39, -49, -26,  -9, -24, -45, -25,  -9, -49, -26,   5, -53, -19,
 -11,  24,  50],
[-66,  12, -38, -50, -25, -10, -24, -45, -24,  -9, -49, -27,   5, -53, -20,
 -10,  23,  51],
[-70,  22, -43, -50, -26,  -6, -25, -45, -23, -10, -48, -28,   6, -52, -21,
  -8,  25,  50],
[-70,  24, -42, -50, -26,  -7, -26, -44, -24, -10, -48, -29,   5, -52, -22,
  -8,  25,  50],
[-70,  24, -42, -50, -26,  -8, -26, -44, -23,  -9, -48, -29,   6, -52, -22,
  -8,  25,  50],
[-70,  28, -41, -50, -26,  -8, -26, -45, -23, -10, -48, -29,   6, -52, -21,
  -7,  25,  50],
[-76,  32, -51, -50, -27,   0, -25, -46, -21, -10, -48, -28,   6, -52, -21,
  -8,  30,  47],
[-79,  41, -56, -48, -29,   4, -25, -46, -21,  -9, -49, -27,   6, -53, -20,
  -9,  30,  47],
[-74,  25, -50, -49, -29,   0, -26, -44, -25, -10, -47, -30,   5, -51, -23,
 -10,  24,  50],
[-75,  23, -52, -50, -27,   1, -25, -45, -23, -10, -48, -28,   4, -52, -21,
 -10,  24,  50],
[-73,  16, -50, -49, -28,   0, -25, -45, -24, -10, -48, -29,   5, -52, -23,
 -11,  23,  50],
[-70,  15, -46, -52, -23,  -2, -25, -45, -24, -10, -48, -29,   4, -52, -22,
 -10,  20,  52],
[-67,  17, -42, -54, -15,  -6, -24, -44, -26, -10, -48, -29,   5, -52, -23,
 -10,  17,  53],
[-83, -47,  -9, -18, -54,   1,  -4, -56,   5,   0, -56,   5,   5, -55,  13,
 -27,  -1,  50],
[-83, -47, -14, -18, -54,   1,  -4, -56,   5,   0, -57,   5,   5, -55,  12,
 -27,  -1,  50],
[-83, -48, -12, -18, -54,   1,  -4, -56,   5,   0, -57,   5,   6, -55,  10,
 -27,   0,  50],
[-83, -49, -10, -18, -54,   1,  -4, -56,   5,   0, -56,   5,   7, -55,  10,
 -28,   0,  49],
[-82, -50,  -2, -17, -54,   0,  -4, -56,   5,   0, -57,   4,   8, -55,   9,
 -29,  -2,  49],
[-82, -50,  -1, -17, -54,   0,  -3, -56,   5,   0, -57,   4,   8, -55,   8,
 -29,  -3,  48],
[-82, -38, -11, -18, -54,   1,  -4, -56,   6,   0, -56,   6,   7, -55,   9,
 -25,  -4,  50],
[-81, -33,  -8, -18, -54,   1,  -4, -56,   6,   0, -56,   6,   7, -55,  10,
 -25,  -4,  51],
[-81, -32,  -8, -17, -54,   1,  -4, -56,   7,   0, -56,   7,   6, -55,  12,
 -25,  -4,  51],
[-81, -32,  -5, -17, -54,   1,  -4, -56,   7,   0, -56,   7,   6, -55,  12,
 -25,  -4,  50],
[-80, -25,  -5, -17, -54,   0,  -4, -56,   7,   0, -56,   8,   7, -55,  13,
 -25,  -4,  51],
[-80, -21,  -4, -17, -54,   0,  -4, -56,   8,   0, -56,   9,   7, -55,  13,
 -25,  -3,  51],
[-79, -17,  -3, -17, -54,   0,  -4, -56,   8,   0, -56,   9,   7, -54,  14,
 -25,  -1,  51],
[-79, -16,  -4, -18, -54,   0,  -4, -56,   8,   0, -56,   9,   7, -54,  14,
 -25,   0,  51],
[-79, -17,  -5, -18, -54,   0,  -4, -56,   9,   0, -56,   9,   7, -54,  14,
 -25,   0,  51],
[-79, -17,  -5, -18, -54,   0,  -4, -56,   9,   0, -56,   9,   7, -54,  15,
 -25,   0,  51],
[-79, -17,  -5, -19, -54,   0,  -4, -56,   9,   0, -56,   9,   7, -54,  15,
 -25,   0,  51],
[-79, -18,  -5, -19, -54,   0,  -4, -56,   9,   0, -56,   9,   7, -54,  15,
 -25,   0,  51],
[-79, -19,  -5, -19, -54,   0,  -4, -56,   9,   0, -56,   9,   7, -54,  15,
 -25,   0,  51],
[-78, -22,  -6, -19, -53,  -1,  -5, -56,   8,  -1, -56,   8,   6, -55,  14,
 -26,  -1,  50],
[-78, -23,  -5, -20, -53,  -1,  -5, -56,   9,  -1, -56,   8,   6, -55,  14,
 -27,   0,  50],
[-77, -20,  -4, -20, -53,  -1,  -4, -56,   8,  -1, -56,   8,   7, -55,  13,
 -27,   0,  50],
[-77, -20,  -4, -20, -53,  -1,  -4, -56,   8,   0, -56,   8,   8, -55,  13,
 -27,   1,  50],
[-77, -22,  -4, -20, -53,  -1,  -4, -56,   8,   0, -56,   8,   8, -54,  13,
 -27,   1,  50],
[-78, -24,  -3, -20, -53,   0,  -4, -56,   8,   0, -56,   8,   8, -54,  13,
 -27,   1,  49],
[-78, -26,  -3, -20, -53,   0,  -4, -56,   8,   0, -56,   8,   9, -55,  12,
 -28,   1,  49],
[-78, -26,  -3, -20, -53,   0,  -4, -56,   8,   0, -56,   8,   9, -55,  12,
 -28,   0,  49],
[-78, -27,  -3, -20, -53,   0,  -4, -56,   8,   0, -56,   8,   9, -55,  12,
 -28,   0,  49],
[-77, -31,   2, -19, -53,  -1,  -4, -56,   7,   0, -56,   7,   9, -55,  11,
 -29,  -2,  48],
[-77, -33,   3, -19, -53,  -2,  -4, -56,   7,   0, -56,   7,   9, -55,  11,
 -29,  -4,  48],
[-76, -33,   6, -19, -53,  -2,  -3, -56,   8,   0, -56,   6,  10, -55,  10,
 -29,  -8,  48],
[-76, -34,   7, -18, -54,  -2,  -3, -56,   8,   0, -56,   6,  11, -55,  10,
 -28, -12,  48],
[-76, -34,   7, -18, -54,  -2,  -3, -56,   8,   0, -56,   6,  11, -55,  10,
 -27, -14,  47],
[-76, -35,   8, -18, -54,  -1,  -3, -56,   9,   0, -56,   7,  11, -55,  10,
 -27, -15,  47],
[-76, -35,   8, -19, -54,  -1,  -3, -56,   9,   0, -56,   7,  11, -55,  10,
 -26, -17,  47],
[-76, -36,   9, -19, -53,  -1,  -4, -56,   9,   0, -56,   7,  11, -55,  10,
 -26, -19,  46],
[-76, -37,   9, -19, -53,  -1,  -4, -56,  10,   0, -56,   7,  11, -55,  10,
 -26, -20,  46],
[-76, -38,   9, -20, -53,  -2,  -4, -56,  10,   0, -56,   7,  11, -54,  11,
 -26, -21,  46],
[-74, -41,   2, -22, -52,  -5,  -7, -56,   8,  -3, -56,   6,   8, -55,   9,
 -28, -23,  43],
[-73, -40,  -1, -24, -51,  -6,  -7, -56,   8,  -3, -56,   7,   7, -55,  10,
 -27, -23,  43],
[-75, -36,  -8, -27, -50,  -4,  -8, -55,  10,  -3, -56,   9,   6, -55,  14,
 -25, -22,  45],
[-77, -36,  -9, -27, -50,  -2,  -7, -55,  11,  -2, -56,  11,   7, -54,  16,
 -24, -21,  47],
[-77, -35,  -8, -27, -50,  -2,  -7, -55,  11,  -2, -55,  11,   7, -54,  17,
 -24, -21,  47],
[-77, -35,  -4, -26, -50,  -2,  -7, -55,  10,  -2, -56,  11,   8, -53,  17,
 -24, -21,  47],
[-76, -32,   3, -25, -51,  -3,  -5, -56,   9,   0, -56,  10,  10, -54,  15,
 -23, -23,  46],
[-72, -29,   4, -24, -51,  -7,  -6, -56,   6,  -1, -56,   7,  10, -55,  11,
 -24, -27,  44],
[-74, -27,   0, -24, -51,  -4,  -7, -56,   9,  -2, -56,   9,   8, -54,  14,
 -22, -25,  46],
[-75, -27,   0, -24, -51,  -3,  -7, -55,  10,  -2, -56,  10,   7, -54,  15,
 -22, -25,  46],
[-75, -26,   0, -23, -52,  -2,  -7, -55,  10,  -2, -56,  10,   8, -54,  16,
 -21, -25,  46],
[-74, -25,   4, -22, -52,  -3,  -6, -56,   8,  -1, -56,   9,   9, -54,  15,
 -21, -26,  46]
],"float32")

print np.shape(static10)