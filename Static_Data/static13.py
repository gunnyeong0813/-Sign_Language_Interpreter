import numpy as np


static13 = np.array([[ 50, -20, -11, -37,  16, -40, -22, -12, -51, -17, -11, -53, -19, -14, -51,
 -15, -15, -52],
[ 50, -20, -12, -37,  16, -40, -23, -11, -51, -17,  -9, -53, -17, -10, -53,
 -14, -14, -53],
[ 49, -20, -12, -37,  16, -40, -23, -10, -51, -16,  -7, -54, -17,  -8, -53,
 -13, -11, -54],
[ 49, -20, -12, -37,  16, -40, -24,  -7, -51, -16,  -5, -54, -16,  -5, -54,
 -11,  -8, -55],
[ 49, -20, -12, -37,  16, -40, -24,  -6, -51, -15,  -3, -54, -16,  -3, -54,
 -11,  -7, -55],
[ 48, -20, -12, -36,  15, -41, -24,  -6, -51, -15,  -3, -54, -16,  -3, -54,
 -10,  -8, -55],
[ 48, -20, -12, -36,  15, -41, -24,  -5, -51, -15,  -2, -55, -16,  -3, -54,
 -10,  -8, -55],
[ 48, -20, -12, -35,  15, -41, -24,  -4, -51, -15,  -1, -55, -15,  -2, -55,
 -10,  -7, -55],
[ 48, -19, -12, -35,  16, -41, -23,  -3, -51, -14,   0, -55, -14,  -1, -55,
  -9,  -7, -56],
[ 49, -18, -12, -34,  18, -42, -23,  -1, -52, -13,   0, -55, -14,  -1, -55,
  -8,  -5, -56],
[ 48, -17, -12, -33,  17, -42, -22,  -3, -52, -13,   0, -55, -14,  -3, -55,
  -8,  -6, -56],
[ 48, -14, -13, -32,  19, -42, -20,  -1, -53, -12,   0, -56, -12,  -2, -55,
  -7,  -6, -56],
[ 47, -12, -13, -32,  19, -43, -19,   0, -53, -10,   0, -56, -11,  -3, -56,
  -6,  -6, -56],
[ 47, -13, -13, -32,  16, -44, -19,  -5, -53, -12,  -2, -55, -12,  -6, -55,
  -7,  -9, -56],
[ 48, -13, -13, -31,  18, -43, -18,  -4, -53, -11,  -3, -55, -12,  -6, -55,
  -7,  -8, -56],
[ 48, -12, -13, -31,  20, -43, -17,  -3, -54, -11,  -4, -56, -12,  -7, -55,
  -7,  -9, -55],
[ 49, -12, -12, -30,  21, -43, -17,  -5, -54, -11,  -5, -55, -12,  -9, -55,
  -8, -11, -55],
[ 49, -12, -12, -31,  21, -43, -17,  -6, -54, -11,  -5, -55, -11,  -9, -55,
  -9, -12, -55],
[ 49, -12, -12, -31,  21, -42, -17,  -6, -54, -11,  -6, -55, -11,  -9, -55,
  -8, -12, -55],
[ 47, -12, -12, -31,  19, -43, -17,  -8, -53, -11,  -7, -55, -11,  -9, -55,
  -8, -12, -55],
[ 48, -13, -12, -32,  19, -43, -18,  -7, -53, -11,  -6, -55, -11,  -8, -55,
  -7, -11, -55],
[ 47, -13, -12, -32,  19, -43, -18,  -8, -53, -12,  -7, -55, -12,  -9, -55,
  -8, -11, -55],
[ 47, -11, -13, -32,  20, -42, -17,  -7, -54, -10,  -6, -55, -10,  -9, -55,
  -6, -12, -55],
[ 47, -10, -13, -32,  19, -43, -16,  -4, -54,  -9,  -5, -56, -10,  -9, -55,
  -6, -11, -55],
[ 46, -13, -12, -32,  16, -44, -18,  -8, -53, -11,  -7, -55, -12, -10, -54,
  -7, -12, -55],
[ 47, -12, -12, -32,  18, -43, -17,  -7, -54, -11,  -6, -55, -11,  -9, -55,
  -6, -11, -55],
[ 47, -12, -12, -31,  18, -44, -17,  -7, -53, -11,  -6, -55, -11,  -9, -55,
  -6, -11, -55],
[ 47, -10, -11, -31,  19, -44, -16,  -6, -54, -10,  -6, -56, -10,  -9, -55,
  -6, -12, -55],
[ 46, -12, -11, -31,  17, -44, -18,  -9, -53, -11,  -8, -55, -11, -11, -54,
  -8, -14, -54],
[ 46, -13, -12, -32,  16, -44, -19, -11, -52, -12,  -9, -54, -14, -13, -53,
  -9, -15, -54],
[ 46, -14, -13, -33,  15, -44, -20, -12, -52, -14, -10, -54, -14, -12, -54,
 -10, -15, -54],
[ 46, -14, -13, -32,  16, -44, -19, -10, -52, -13,  -9, -55, -14, -13, -53,
  -9, -15, -54],
[ 46, -14, -11, -31,  15, -45, -19, -12, -52, -13, -11, -54, -14, -15, -53,
 -11, -17, -53],
[ 46, -13, -11, -30,  15, -46, -18, -12, -52, -13, -11, -54, -13, -16, -53,
 -10, -18, -53],
[ 46, -14, -11, -31,  15, -45, -19, -12, -52, -13, -10, -54, -12, -11, -54,
  -9, -15, -54],
[ 46, -16, -11, -32,  15, -44, -20, -12, -52, -15, -11, -53, -16, -14, -52,
 -11, -15, -53],
[ 47, -17, -11, -32,  15, -44, -20, -14, -51, -16, -14, -52, -12, -17, -53,
 -18, -16, -51],
[ 48, -18, -11, -32,  15, -44, -20, -15, -50, -17, -15, -52, -19, -16, -51,
 -13, -17, -52],
[ 49, -17, -11, -32,  15, -44, -19, -15, -51, -16, -14, -53, -18, -15, -52,
 -13, -17, -53],
[ 48, -15, -13, -33,  15, -44, -19, -14, -51, -15, -13, -53, -12, -17, -53,
 -17, -15, -52],
[ 48, -15, -14, -33,  15, -43, -19, -14, -51, -15, -13, -53, -12, -20, -52,
 -17, -19, -50],
[ 49, -15, -14, -33,  14, -44, -18, -16, -51, -15, -15, -52, -15, -22, -50,
 -18, -21, -49],
[ 50, -15, -14, -33,  15, -44, -18, -16, -51, -15, -15, -53, -15, -22, -50,
 -18, -22, -49],
[ 51, -16, -14, -33,  15, -43, -18, -16, -51, -16, -14, -53, -18, -20, -50,
 -16, -21, -50],
[ 51, -16, -14, -33,  16, -43, -18, -16, -51, -16, -14, -53, -18, -19, -50,
 -15, -20, -51],
[ 51, -15, -14, -32,  15, -44, -18, -16, -51, -15, -15, -52, -17, -20, -50,
 -15, -20, -51],
[ 51, -15, -14, -33,  15, -43, -17, -17, -51, -15, -16, -52, -17, -20, -50,
 -15, -21, -51],
[ 51, -15, -14, -33,  15, -43, -17, -16, -51, -15, -13, -53, -15, -21, -50,
 -17, -20, -50],
[ 51, -15, -14, -33,  15, -44, -18, -15, -52, -15, -11, -53, -15, -21, -50,
 -17, -20, -50],
[ 51, -15, -15, -32,  15, -44, -18, -14, -52, -15, -12, -53, -16, -20, -50,
 -14, -20, -51],
[ 64,  -1,  -2,  -7,  47, -30,   3,  -6, -56,  -5,  -8, -56,  -9, -13, -54,
 -18,  -5, -54],
[ 64,  -2,  -3,  -8,  47, -30,   2,  -5, -57,  -6,  -7, -56, -10, -12, -55,
 -18,  -4, -54],
[ 65,  -6,  -4,  -8,  -7, -56,  -9,  47, -30,   0,  -2, -57, -11, -11, -54,
 -20,  -3, -53],
[ 64,  -5,  -4,  -9,  48, -29,   1,  -5, -57,  -7,  -8, -56, -11, -11, -55,
 -19,  -2, -53],
[ 63,  -2,  -4,  -8,  48, -29,   2,  -4, -57,  -6,  -8, -56,  -9, -11, -55,
 -18,  -3, -54],
[ 64,   1,  -5,  -8,  48, -29,   3,  -4, -57,  -4,  -9, -56,  -8, -11, -55,
 -17,  -4, -54],
[ 64,   2,  -3,  -8,  48, -29,   4,  -4, -56,  -4,  -8, -56,  -9, -13, -54,
 -17,  -6, -54],
[ 63,   0,  -2,  -7,  48, -30,   3,  -3, -57,  -5,  -6, -56,  -9, -13, -54,
 -18,  -5, -54],
[ 64,  -1,  -2,  -8,  48, -29,   2,  -3, -57,  -6,  -6, -56, -10, -12, -54,
 -18,  -3, -54],
[ 64,  -1,  -2,  -8,  48, -29,   2,  -3, -57,  -5,  -6, -56, -10, -12, -55,
 -18,  -3, -54],
[ 65,   0,  -3,  -8,  48, -28,   3,  -4, -57,  -5,  -9, -56,  -9, -13, -54,
 -17,  -5, -54],
[ 64,   3,  -4,  -7,  48, -29,   4,  -3, -56,  -4,  -8, -56,  -8, -14, -54,
 -16,  -7, -54],
[ 62,   6,  -4,  -7,  47, -30,   6,  -2, -56,  -2,  -7, -56,  -7, -16, -54,
 -15,  -9, -54],
[ 61,   6,  -3,  -8,  47, -30,   6,  -1, -56,  -1,  -6, -56,  -6, -15, -54,
 -15,  -8, -54],
[ 60,   5,  -2,  -8,  47, -30,   6,  -2, -56,  -2,  -6, -56,  -7, -13, -55,
 -15,  -7, -54],
[ 60,   4,  -2,  -7,  47, -31,   6,  -5, -56,  -3,  -7, -56,  -7, -13, -55,
 -16,  -6, -54],
[ 59,   3,  -3,  -8,  47, -31,   5,  -6, -56,  -3,  -7, -56,  -8, -13, -55,
 -16,  -6, -54],
[ 59,   4,  -3,  -8,  47, -31,   6,  -3, -56,  -3,  -7, -56,  -8, -13, -55,
 -16,  -6, -54],
[ 60,   1,  -1,  -6,  46, -32,   5,  -4, -56,  -4,  -6, -56,  -9, -13, -55,
 -17,  -5, -54],
[ 61,  -1,  -2,  -8,  47, -31,   3,  -4, -57,  -6,  -7, -56, -10, -12, -54,
 -18,  -4, -53],
[ 61,  -1,  -2,  -8,  47, -31,   3,  -4, -57,  -6,  -7, -56, -10, -12, -54,
 -18,  -4, -53],
[ 61,   0,  -3,  -9,  47, -30,   3,  -5, -56,  -6,  -9, -56, -10, -13, -54,
 -18,  -5, -53],
[ 62,   0,  -5,  -8,  47, -31,   3,  -4, -56,  -5,  -8, -56,  -9, -13, -54,
 -18,  -6, -54],
[ 62,   2,  -5,  -7,  47, -31,   4,  -3, -56,  -4,  -7, -56,  -8, -14, -54,
 -17,  -7, -54],
[ 62,   3,  -5,  -6,  47, -32,   5,  -3, -56,  -3,  -6, -56,  -8, -12, -55,
 -16,  -6, -54],
[ 63,   4,  -2,   0,  46, -33,   6,  -3, -56,  -3,  -5, -56,  -7, -12, -55,
 -15,  -6, -54],
[ 63,   3,  -6,  -1,  47, -31,   4,  -3, -56,  -4,  -5, -56,  -8, -12, -55,
 -16,  -6, -54],
[ 62,   7,  -6,  -1,  48, -29,   6,   1, -56,  -2,  -3, -57,  -6,  -9, -56,
 -14,  -3, -55],
[ 59,  12,  -5,  -1,  47, -31,   9,  -3, -56,   0,  -5, -56,  -4,  -9, -56,
 -12,  -4, -55],
[ 61,  15,  -3,   0,  48, -29,  10,  -2, -56,   1,  -4, -57,  -3,  -8, -56,
 -10,  -2, -56],
[ 61,  14,  -4,   0,  48, -30,  10,  -2, -56,   0,  -3, -57,  -3,  -8, -56,
 -11,  -2, -56],
[ 60,  16,  -1,   2,  47, -31,  11,  -3, -55,   1,  -4, -57,  -2,  -9, -56,
 -10,  -3, -56],
[ 59,  16,  -2,   3,  47, -32,  12,  -4, -55,   0,  -5, -57,  -3, -10, -56,
 -10,  -4, -56],
[ 59,  19,  -1,   2,  47, -31,  13,  -4, -55,   1,  -5, -57,  -2, -11, -56,
  -9,  -5, -56],
[ 59,  20,  -1,   2,  48, -30,  13,  -4, -55,   0,  -5, -57,  -1, -11, -56,
  -9,  -6, -56],
[ 59,  21,  -1,   2,  48, -30,  14,  -5, -55,   1,  -5, -56,  -1, -12, -55,
  -8,  -6, -56],
[ 59,  21,   0,   1,  47, -31,  14,  -5, -55,   0,  -5, -56,  -1, -12, -55,
  -8,  -7, -56],
[ 60,  19,   0,   2,  48, -31,  13,  -6, -55,   0,  -5, -57,  -2, -12, -55,
  -9,  -7, -56],
[ 61,  19,   0,   2,  48, -29,  13,  -4, -55,   0,  -4, -57,  -2, -12, -55,
 -10,  -6, -55],
[ 60,  18,   0,   3,  47, -31,  12,  -5, -55,   0,  -5, -57,  -3, -11, -56,
 -10,  -6, -55],
[ 60,  13,   0,   4,  46, -32,  10,  -5, -55,  -3,  -5, -56,  -5,  -9, -56,
 -12,  -4, -55],
[ 60,  11,   0,   4,  46, -32,   9,  -5, -56,  -3,  -4, -56,  -6,  -8, -56,
 -13,  -2, -55],
[ 61,  11,   0,   3,  47, -31,   9,  -4, -56,  -4,  -4, -57,  -6,  -6, -56,
 -13,   0, -55],
[ 61,  12,   0,   2,  47, -31,   9,  -4, -56,  -4,  -3, -57,  -6,  -8, -56,
 -13,  -1, -55],
[ 61,  13,  -1,   2,  48, -30,   9,  -4, -56,  -3,  -3, -57,  -6,  -8, -56,
 -13,  -1, -55],
[ 61,  13,  -1,   1,  48, -30,   9,  -4, -56,  -3,  -3, -57,  -6, -10, -56,
 -13,  -3, -55],
[ 61,  14,  -2,   0,  48, -30,  10,  -4, -56,  -3,  -4, -57,  -5, -10, -56,
 -12,  -4, -55],
[ 60,  14,  -2,   0,  47, -31,  10,  -5, -56,  -2,  -5, -57,  -5,  -7, -56,
 -12,  -2, -55],
[ 59,  14,  -2,   1,  47, -31,  10,  -5, -55,  -2,  -5, -56,  -5,  -8, -56,
 -12,  -2, -55],
[ 59,  15,  -2,   0,  47, -31,  11,  -5, -55,  -2,  -5, -56,  -4,  -9, -56,
 -11,  -2, -55]
],"float32")

print np.shape(static13)