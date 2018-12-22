import numpy as np


static28 = np.array([[  1, -69,  -5,  -2,  -4, -57,  -9, -14, -54, -24, -19, -47, -26, -29, -40,
 -25,   1,  51],
[  1, -69,  -5,  -2,  -4, -57,  -8, -14, -54, -24, -19, -47, -26, -30, -40,
 -25,   1,  51],
[  1, -70,  -5,  -2,  -4, -57,  -9, -15, -54, -24, -19, -47, -26, -30, -40,
 -25,   1,  51],
[  1, -70,  -5,  -2,  -4, -57, -10, -15, -54, -24, -19, -48, -27, -29, -40,
 -25,   2,  51],
[  1, -71,  -5,  -2,  -4, -57, -11, -15, -54, -24, -18, -48, -27, -28, -41,
 -26,   2,  50],
[  0, -71,  -5,  -2,  -5, -57, -12, -15, -53, -24, -18, -48, -27, -29, -40,
 -26,   2,  50],
[  1, -71,  -4,  -1,  -4, -57, -11, -14, -54, -24, -18, -48, -27, -28, -41,
 -26,   2,  50],
[  1, -70,  -5,  -2,  -4, -57, -10, -15, -54, -24, -19, -47, -27, -28, -41,
 -26,   1,  50],
[  1, -70,  -5,  -2,  -4, -57, -10, -15, -54, -24, -19, -47, -27, -27, -42,
 -26,   1,  50],
[  1, -69,  -5,  -2,  -4, -57, -10, -15, -54, -24, -19, -48, -27, -27, -42,
 -25,   1,  51],
[  1, -69,  -6,  -3,  -3, -57, -10, -14, -54, -24, -19, -48, -27, -26, -42,
 -26,   0,  50],
[  2, -69,  -5,  -2,  -2, -57,  -9, -13, -54, -25, -19, -47, -28, -24, -43,
 -28,   0,  49],
[  3, -70,  -5,  -2,  -2, -57,  -9, -13, -54, -25, -19, -47, -28, -23, -43,
 -29,   0,  49],
[  4, -71,  -4,  -1,  -1, -57,  -8, -12, -55, -25, -19, -47, -28, -24, -43,
 -29,   0,  49],
[  3, -70,  -5,  -2,  -2, -57, -10, -13, -54, -25, -19, -47, -28, -26, -42,
 -27,   0,  50],
[  3, -71,  -4,  -1,  -2, -57, -10, -13, -54, -25, -19, -47, -28, -26, -42,
 -27,   0,  50],
[  3, -71,  -4,  -1,  -2, -57, -10, -13, -54, -25, -19, -47, -28, -26, -42,
 -28,   0,  49],
[  3, -71,  -3,   0,  -1, -57, -10, -12, -54, -26, -19, -47, -28, -25, -42,
 -29,   0,  49],
[  4, -72,  -3,   0,  -1, -57, -10, -12, -54, -26, -19, -46, -29, -23, -43,
 -30,   0,  48],
[  4, -72,  -3,   0,  -1, -57, -10, -12, -55, -26, -19, -46, -29, -22, -43,
 -30,   0,  48],
[  4, -73,  -3,   0,  -1, -57, -10, -11, -54, -26, -19, -46, -29, -22, -43,
 -30,   0,  48],
[  4, -73,  -3,   0,   0, -57, -11, -11, -54, -26, -19, -46, -30, -21, -43,
 -29,   0,  48],
[  5, -73,  -4,  -1,   0, -57, -11, -11, -54, -27, -18, -46, -30, -21, -43,
 -29,   0,  49],
[  5, -72,  -4,  -1,   0, -57, -11, -11, -54, -27, -18, -46, -30, -21, -43,
 -29,   0,  49],
[  6, -72,  -4,  -1,   0, -57, -11, -10, -55, -28, -18, -45, -30, -20, -44,
 -29,  -1,  49],
[  6, -72,  -4,  -1,   0, -57, -11, -10, -55, -29, -18, -45, -30, -20, -44,
 -29,  -1,  49],
[  6, -72,  -4,  -1,   0, -57, -11, -10, -55, -29, -18, -45, -30, -20, -44,
 -29,  -1,  49],
[  6, -72,  -4,  -1,   1, -57, -11,  -9, -55, -29, -19, -45, -30, -19, -44,
 -28,  -2,  49],
[  7, -72,  -5,  -2,   1, -57, -12,  -9, -55, -29, -19, -44, -30, -19, -44,
 -28,  -2,  49],
[  7, -72,  -5,  -2,   1, -57, -12,  -9, -55, -30, -19, -44, -30, -18, -44,
 -28,  -2,  49],
[  7, -72,  -5,  -2,   1, -57, -12,  -9, -55, -30, -19, -44, -31, -18, -44,
 -28,  -2,  49],
[  7, -72,  -5,  -2,   1, -57, -12,  -9, -55, -30, -20, -44, -31, -18, -44,
 -28,  -2,  49],
[  8, -72,  -5,  -2,   2, -57, -12,  -8, -55, -30, -20, -43, -31, -17, -44,
 -27,  -2,  49],
[  8, -72,  -6,  -3,   2, -57, -13,  -8, -55, -31, -20, -43, -31, -16, -44,
 -27,  -3,  50],
[  8, -71,  -6,  -3,   2, -57, -13,  -8, -55, -30, -20, -43, -31, -16, -44,
 -27,  -3,  50],
[  8, -71,  -6,  -3,   2, -57, -13,  -8, -55, -30, -20, -44, -31, -16, -44,
 -27,  -3,  50],
[  8, -71,  -6,  -3,   2, -57, -13,  -8, -55, -30, -20, -43, -31, -17, -44,
 -28,  -3,  49],
[  8, -71,  -6,  -3,   2, -57, -13,  -8, -55, -30, -20, -43, -31, -17, -44,
 -28,  -3,  49],
[  8, -71,  -6,  -3,   2, -57, -13,  -8, -55, -30, -20, -44, -30, -18, -44,
 -28,  -3,  49],
[  8, -71,  -6,  -3,   2, -57, -13,  -8, -55, -29, -20, -44, -30, -18, -44,
 -28,  -3,  49],
[  8, -71,  -6,  -3,   2, -57, -13,  -8, -55, -28, -20, -44, -30, -18, -44,
 -28,  -3,  49],
[  8, -71,  -6,  -3,   2, -57, -12,  -8, -55, -28, -20, -44, -30, -17, -44,
 -28,  -3,  49],
[  8, -71,  -6,  -3,   2, -57, -12,  -8, -55, -28, -20, -45, -30, -17, -44,
 -28,  -3,  49],
[  8, -71,  -5,  -2,   2, -57, -12,  -8, -55, -28, -20, -45, -31, -17, -44,
 -28,  -3,  49],
[  8, -72,  -5,  -2,   2, -57, -12,  -8, -55, -28, -20, -45, -31, -15, -44,
 -28,  -3,  49],
[  8, -72,  -5,  -2,   2, -57, -12,  -8, -55, -28, -20, -45, -32, -15, -44,
 -28,  -3,  49],
[  8, -73,  -5,  -2,   2, -57, -12,  -8, -55, -27, -20, -45, -32, -14, -44,
 -28,  -3,  49],
[  8, -73,  -5,  -2,   2, -57, -13,  -7, -55, -27, -20, -45, -32, -14, -44,
 -28,  -3,  49],
[  9, -73,  -5,  -3,   3, -57, -13,  -7, -55, -27, -20, -45, -32, -13, -44,
 -28,  -3,  49],
[  9, -73,  -6,  -3,   3, -57, -13,  -7, -55, -28, -20, -45, -33, -13, -44,
 -28,  -3,  49],
[ 27, -79,  13,   6,  21, -52,   0,  11, -56, -24,  10, -50,  -9,   2, -56,
 -48, -12,  27],
[ 27, -80,  14,   6,  21, -52,   0,  11, -56, -24,  10, -50,  -9,   3, -56,
 -49, -11,  27],
[ 27, -79,  14,   6,  21, -52,   0,  11, -56, -24,  10, -50,  -9,   5, -56,
 -48, -12,  27],
[ 27, -79,  14,  -9,   5, -56,   6,  21, -52,   0,  11, -56, -24,  10, -50,
 -49, -11,  26],
[ 27, -80,  13, -10,   6, -55,   6,  21, -52,   0,  12, -55, -24,  11, -50,
 -49, -11,  25],
[ 28, -79,  10, -12,   9, -55,   3,  22, -52,   0,  12, -55, -26,  11, -49,
 -48, -13,  28],
[ 27, -78,  12, -10,   9, -55,   4,  21, -52,   0,  11, -56, -24,  10, -50,
 -49, -12,  26],
[ 27, -78,  13,   5,  21, -52,   0,  11, -56, -24,  10, -50,  -9,   9, -55,
 -50, -12,  23],
[ 27, -78,  13,  -9,   9, -55,   6,  21, -52,   0,  11, -56, -24,  10, -50,
 -50, -12,  23],
[ 26, -78,  13,  -9,  10, -55,   6,  20, -53,   0,  11, -56, -24,  11, -50,
 -50, -11,  24],
[ 26, -79,  13,  -9,   9, -55,   5,  20, -53,   0,  11, -56, -24,  11, -50,
 -50, -11,  24],
[ 26, -80,  13,   6,  20, -52,   0,  11, -56, -23,  11, -50,  -9,  10, -55,
 -50, -10,  24],
[ 26, -79,  13,   6,  21, -52,   0,  11, -56, -24,  11, -50,  -9,  10, -55,
 -50, -10,  24],
[ 27, -79,  14,   6,  21, -52,   1,  11, -56, -24,  11, -50,  -9,  10, -55,
 -50, -11,  23],
[ 27, -79,  13,   6,  21, -52,   0,  11, -56, -24,  11, -50,  -9,  10, -55,
 -51, -11,  23],
[ 27, -79,  13,   6,  21, -52,   0,  11, -56, -24,  11, -50,  -9,  10, -55,
 -51, -10,  23],
[ 27, -80,  13,   6,  21, -52,   0,  11, -56, -23,  12, -50,  -9,  11, -55,
 -51, -10,  22],
[ 27, -79,  13,  -9,  11, -55,   6,  21, -52,   0,  12, -56, -24,  12, -50,
 -50, -11,  24],
[ 27, -78,  13,  -9,  12, -55,   6,  21, -52,   0,  12, -55, -24,  11, -50,
 -49, -12,  25],
[ 27, -78,  13,  -9,  12, -55,   6,  21, -52,   0,  12, -55, -25,  11, -50,
 -49, -13,  26],
[ 27, -78,  13,  -9,  12, -55,   6,  21, -52,   0,  11, -56, -25,  11, -50,
 -49, -13,  26],
[ 27, -77,  13,   6,  21, -52,   0,  11, -56, -25,  10, -50,  -8,  12, -55,
 -49, -13,  25],
[ 27, -76,  13,   6,  21, -52,   0,  11, -56, -25,  10, -50,  -8,  12, -55,
 -50, -14,  24],
[ 27, -76,  13,  -8,  12, -55,   6,  21, -52,   0,  11, -56, -26,  10, -49,
 -49, -14,  24],
[ 27, -76,  13,   6,  21, -52,   0,  11, -56, -26,  10, -49,  -8,  12, -55,
 -49, -14,  24],
[ 28, -76,  13,  -8,  12, -55,   6,  22, -52,   0,  11, -56, -26,  10, -49,
 -50, -13,  22],
[ 28, -76,  13,   5,  23, -52,   0,  11, -56, -27,  10, -49,  -8,  12, -55,
 -49, -14,  24],
[ 28, -75,  11,   4,  24, -51,   0,  12, -55, -29,  10, -48, -10,  12, -54,
 -45, -16,  29],
[ 29, -74,  11,   4,  26, -50,   0,  12, -55, -31,  10, -46, -10,  11, -55,
 -40, -19,  35],
[ 29, -74,  11,   4,  25, -50,   0,  11, -56, -32,   9, -46,  -9,   9, -55,
 -37, -19,  38],
[ 28, -73,  12,   5,  25, -50,   0,  10, -56, -31,   8, -46,  -9,   7, -55,
 -37, -19,  39],
[ 28, -73,  12,   5,  25, -50,   0,  10, -56, -32,   8, -46,  -8,   4, -56,
 -35, -19,  40],
[ 28, -73,  12,   6,  25, -51,   0,  10, -56, -31,   7, -47,  -7,   1, -56,
 -35, -19,  40],
[ 26, -72,  13,   5,  24, -51,   1,   8, -56, -31,   6, -47,  -6,   0, -56,
 -35, -18,  40],
[ 24, -72,  13,   6,  24, -51,   1,   6, -56, -30,   4, -48,  -5,  -5, -56,
 -34, -16,  42],
[ 23, -72,  13,   6,  24, -51,   2,   5, -56, -30,   3, -48,  -4,  -6, -56,
 -34, -15,  43],
[ 22, -71,  14,   6,  24, -51,   2,   4, -57, -29,   1, -49,  -4,  -7, -56,
 -34, -14,  42],
[ 21, -70,  14,   6,  24, -51,   3,   3, -57, -29,   0, -49,  -3,  -7, -56,
 -36, -14,  41],
[ 21, -70,  15,   7,  24, -51,   3,   3, -57, -29,   0, -49,  -3,  -7, -56,
 -38, -14,  39],
[ 21, -70,  15,   7,  24, -51,   3,   3, -57, -29,   0, -49,  -2,  -7, -56,
 -39, -14,  38],
[ 21, -70,  15,   7,  24, -51,   3,   3, -57, -29,   0, -49,  -2,  -7, -56,
 -39, -14,  38],
[ 21, -70,  15,   7,  24, -51,   3,   3, -57, -29,   0, -49,  -2,  -7, -56,
 -40, -13,  38],
[ 20, -70,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -1, -11, -56,
 -40, -14,  38],
[ 20, -70,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -1, -15, -55,
 -39, -14,  38],
[ 20, -69,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -1, -15, -55,
 -39, -14,  38],
[ 20, -69,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -1, -10, -56,
 -39, -14,  38],
[ 20, -69,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -2,  -8, -56,
 -40, -14,  38],
[ 20, -69,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -2,  -8, -56,
 -40, -14,  38],
[ 20, -69,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -1, -12, -55,
 -39, -14,  38],
[ 20, -70,  15,   7,  23, -51,   3,   3, -57, -29,   0, -49,  -1, -17, -54,
 -39, -13,  39]
],"float32")

print np.shape(static28)