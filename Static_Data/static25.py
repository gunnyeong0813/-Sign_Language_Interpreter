import numpy as np

static25 = np.array([[ 66, -19, -12,  -4,  43, -36,   6,  31, -47,   8,  26, -49,   0, -56,  10,
  -9, -55,  12],
[ 65, -19,  -8,  -3,  43, -37,   9,  30, -47,  11,  25, -50,  -2, -56,  11,
 -11, -54,  12],
[ 64, -17,  -6,  -2,  43, -37,  10,  29, -47,  12,  24, -50,  -2, -55,  12,
 -12, -54,  13],
[ 64, -17,  -3,  -1,  42, -38,  11,  28, -48,  13,  23, -50,  -3, -55,  15,
 -12, -53,  15],
[ 63, -17,  -2,   0,  42, -38,  11,  26, -49,  13,  23, -50,  -3, -54,  16,
 -12, -53,  17],
[ 62, -19,   0,   0,  41, -39,  12,  25, -49,  13,  23, -50,  -3, -53,  19,
 -13, -52,  19],
[ 62, -21,   0,   0,  41, -39,  12,  25, -49,  13,  22, -50,  -2, -52,  21,
 -12, -51,  22],
[ 68, -23,  -9,  -3,  44, -35,  10,  30, -47,  11,  28, -48,   1, -54,  18,
  -8, -53,  19],
[ 72, -29, -16,  -5,  47, -32,   7,  33, -45,   8,  32, -46,   3, -55,  13,
  -7, -54,  14],
[ 75, -32, -30,  -8,  48, -29,   3,  36, -43,   5,  35, -44,   6, -56,   9,
  -4, -55,  11],
[ 75, -35, -38, -11,  48, -28,   0,  36, -44,   1,  35, -44,   9, -55,   9,
  -1, -55,  12],
[ 71, -29, -38, -14,  45, -31,  -3,  33, -46,   0,  32, -47,  11, -54,  12,
   1, -55,  15],
[ 69, -28, -32, -13,  44, -33,  -2,  30, -48,   0,  29, -49,   9, -55,  12,
   0, -54,  16],
[ 66, -25, -25, -11,  42, -36,  -1,  27, -50,   2,  26, -50,   6, -55,  14,
  -3, -54,  17],
[ 63, -23, -18,  -9,  41, -38,   2,  25, -51,   4,  23, -51,   4, -54,  16,
  -5, -53,  19],
[ 62, -22, -16,  -8,  41, -39,   4,  26, -50,   5,  23, -51,   3, -54,  17,
  -7, -53,  18],
[ 64, -21, -18,  -7,  42, -37,   5,  28, -49,   6,  25, -50,   4, -54,  16,
  -6, -54,  17],
[ 66, -21, -16,  -6,  43, -36,   5,  29, -48,   8,  27, -49,   5, -53,  18,
  -5, -53,  19],
[ 66, -21, -16,  -6,  43, -36,   5,  30, -48,   8,  27, -49,   5, -53,  19,
  -5, -53,  20],
[ 66, -21, -17,  -6,  43, -36,   5,  30, -48,   8,  27, -49,   6, -53,  18,
  -5, -53,  20],
[ 66, -21, -17,  -7,  43, -36,   5,  29, -48,   8,  27, -49,   6, -54,  18,
  -5, -53,  19],
[ 66, -21, -17,  -7,  43, -36,   4,  28, -49,   8,  26, -49,   5, -54,  16,
  -5, -53,  18],
[ 65, -21, -20,  -8,  42, -37,   3,  27, -50,   6,  26, -50,   7, -53,  19,
  -3, -52,  21],
[ 64, -19, -22,  -9,  42, -37,   3,  27, -50,   5,  27, -50,  10, -52,  21,
  -2, -52,  22],
[ 63, -18, -21,  -9,  41, -38,   4,  26, -50,   5,  26, -50,   9, -51,  22,
  -2, -51,  24],
[ 62, -18, -20,  -9,  40, -38,   4,  25, -51,   4,  26, -50,   9, -52,  21,
  -2, -52,  23],
[ 62, -16, -20,  -9,  40, -39,   4,  25, -51,   1,  27, -50,   9, -52,  21,
  -2, -52,  23],
[ 62, -17, -20,  -9,  40, -39,   4,  25, -51,   0,  27, -50,   9, -52,  21,
  -2, -52,  23],
[ 61, -18, -23, -11,  39, -39,   2,  24, -51,  -2,  27, -50,  11, -51,  21,
   0, -51,  24],
[ 60, -17, -24, -12,  38, -40,   2,  23, -52,   0,  24, -51,  12, -50,  23,
   0, -51,  25],
[ 59, -17, -23, -12,  37, -41,   2,  22, -52,   2,  22, -52,  12, -49,  25,
   0, -50,  27],
[ 59, -17, -23, -12,  37, -41,   2,  22, -52,   2,  22, -52,  12, -50,  24,
   0, -50,  26],
[ 59, -17, -22, -11,  38, -41,   2,  22, -52,   2,  21, -52,  11, -50,  23,
   0, -51,  25],
[ 59, -18, -22, -11,  38, -40,   2,  21, -53,   3,  21, -52,  12, -50,  23,
   0, -50,  26],
[ 59, -18, -22, -11,  38, -41,   1,  20, -53,   2,  21, -53,  12, -50,  24,
   0, -50,  26],
[ 59, -18, -24, -12,  38, -40,   1,  22, -52,   1,  22, -52,  12, -50,  23,
   0, -50,  26],
[ 64, -22, -27, -12,  41, -37,   2,  28, -49,   1,  26, -50,  12, -52,  20,
   0, -52,  22],
[ 65, -24, -27, -12,  42, -36,   2,  28, -49,   0,  27, -50,  10, -53,  15,
  -1, -54,  18],
[ 65, -24, -26, -12,  42, -37,   2,  28, -49,   0,  27, -50,  10, -53,  16,
  -2, -53,  19],
[ 64, -23, -25, -12,  41, -37,   2,  27, -50,   0,  26, -50,  10, -53,  17,
  -1, -53,  20],
[ 63, -22, -25, -12,  40, -38,   2,  27, -50,   1,  25, -51,  12, -52,  20,
   0, -52,  22],
[ 62, -21, -25, -12,  40, -38,   1,  26, -51,   1,  25, -51,  12, -51,  21,
   0, -52,  23],
[ 62, -21, -25, -12,  40, -38,   0,  23, -52,   1,  24, -51,  12, -51,  21,
   0, -52,  24],
[ 62, -21, -25, -12,  40, -38,   0,  23, -52,   1,  24, -51,  12, -52,  20,
   0, -52,  23],
[ 58,  10, -21, -10,  45, -32,   6,  24, -51,  23,  26, -45,   8, -53,  17,
   2, -54,  18],
[ 58,   9, -20, -10,  45, -33,   6,  23, -51,  24,  25, -45,   8, -53,  18,
   2, -53,  19],
[ 57,  10, -20, -10,  45, -33,   6,  23, -51,  25,  24, -45,   8, -53,  19,
   2, -53,  19],
[ 57,   9, -20, -10,  45, -33,   6,  23, -51,  25,  24, -45,   8, -53,  19,
   2, -53,  19],
[ 57,   9, -20, -10,  45, -33,   6,  23, -51,  23,  25, -45,   8, -53,  19,
   2, -53,  19],
[ 57,   9, -20, -10,  44, -33,   6,  23, -52,  24,  24, -45,   8, -52,  19,
   3, -53,  20],
[ 61, -23, -21, -12,  41, -36,  -8,  20, -52,  -1,  21, -53,  -1, -56,  -6,
 -13, -55,  -4],
[ 62, -25, -23, -13,  42, -36,  -8,  20, -52,  -2,  22, -52,  -2, -56,  -8,
 -13, -55,  -5],
[ 61, -25, -23, -13,  41, -36,  -9,  20, -52,  -3,  21, -52,  -2, -56,  -7,
 -13, -55,  -5],
[ 61, -25, -24, -13,  41, -36,  -9,  19, -52,  -3,  21, -53,  -2, -56,  -7,
 -13, -55,  -4],
[ 61, -25, -24, -13,  41, -36,  -9,  19, -52,  -3,  21, -52,  -2, -56,  -8,
 -13, -55,  -4],
[ 62, -25, -24, -13,  41, -36,  -9,  19, -52,  -3,  21, -52,  -2, -56,  -8,
 -13, -55,  -4],
[ 62, -26, -24, -14,  41, -36,  -9,  19, -52,  -2,  21, -52,  -2, -56,  -8,
 -13, -55,  -4],
[ 62, -26, -24, -14,  41, -36,  -9,  19, -52,  -2,  21, -52,  -2, -56,  -7,
 -12, -55,  -3],
[ 62, -27, -25, -14,  41, -36,  -9,  20, -52,  -1,  21, -52,  -2, -56,  -7,
 -13, -55,  -4],
[ 62, -28, -25, -14,  41, -36,  -8,  21, -52,  -1,  21, -53,  -2, -56,  -7,
 -14, -54,  -6],
[ 62, -29, -25, -14,  42, -36,  -8,  21, -52,  -1,  21, -53,  -3, -56,  -8,
 -16, -54,  -6],
[ 62, -31, -24, -14,  42, -35,  -8,  22, -52,  -1,  21, -53,  -5, -56,  -8,
 -17, -54,  -7],
[ 62, -32, -23, -14,  42, -35,  -9,  22, -52,  -1,  21, -53,  -6, -56,  -9,
 -18, -53,  -8],
[ 62, -32, -23, -14,  42, -35,  -9,  21, -52,  -2,  20, -53,  -6, -55, -10,
 -18, -53,  -8],
[ 62, -32, -23, -14,  42, -35,  -9,  21, -52,  -2,  20, -53,  -6, -55, -10,
 -18, -53,  -8],
[ 62, -32, -23, -14,  42, -35,  -9,  21, -52,  -3,  20, -53,  -7, -55, -10,
 -18, -53,  -9],
[ 62, -31, -23, -14,  42, -36,  -8,  21, -52,  -3,  20, -53,  -6, -55, -10,
 -18, -53,  -8],
[ 63, -33, -24, -14,  42, -35,  -9,  21, -52,  -3,  21, -53,  -7, -55, -11,
 -19, -52,  -9],
[ 63, -34, -24, -14,  43, -35,  -9,  21, -52,  -2,  21, -53,  -8, -55, -11,
 -19, -52,  -9],
[ 64, -35, -24, -14,  43, -34,  -9,  21, -52,  -1,  21, -53,  -8, -55, -12,
 -19, -52,  -9],
[ 64, -35, -24, -14,  43, -34,  -9,  20, -52,  -1,  21, -53,  -8, -55, -12,
 -19, -52,  -9],
[ 64, -35, -24, -14,  43, -34, -10,  20, -52,  -1,  21, -53,  -8, -55, -12,
 -19, -52,  -9],
[ 64, -36, -24, -14,  43, -34, -10,  19, -52,   0,  21, -53,  -8, -55, -12,
 -19, -52,  -9],
[ 65, -36, -23, -13,  44, -33, -10,  20, -52,   1,  21, -53,  -9, -54, -13,
 -20, -52,  -9],
[ 65, -36, -23, -13,  44, -33, -10,  20, -52,   3,  20, -53,  -9, -54, -13,
 -20, -52,  -9],
[ 65, -36, -23, -13,  44, -33, -10,  19, -52,   4,  20, -53,  -9, -54, -13,
 -19, -53,  -8],
[ 65, -36, -23, -13,  44, -33, -10,  19, -52,   4,  20, -53,  -9, -54, -13,
 -19, -53,  -8],
[ 65, -36, -23, -13,  44, -33, -11,  19, -52,   5,  20, -53,  -9, -54, -13,
 -19, -53,  -7],
[ 65, -36, -22, -13,  44, -33, -11,  19, -52,   5,  20, -53,  -9, -54, -13,
 -19, -53,  -7],
[ 65, -36, -22, -12,  44, -33, -11,  19, -52,   6,  20, -53,  -9, -54, -14,
 -19, -53,  -7],
[ 66, -37, -22, -12,  44, -33, -11,  19, -52,   7,  20, -52,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -37, -22, -12,  44, -33, -11,  19, -52,   7,  20, -52,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -37, -22, -12,  44, -33, -11,  19, -52,   7,  20, -52,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -37, -23, -12,  44, -33, -11,  19, -52,   6,  20, -52,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -37, -23, -13,  44, -33, -11,  19, -52,   6,  20, -52,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -37, -24, -13,  44, -33, -11,  19, -52,   6,  20, -52,  -9, -54, -14,
 -19, -53,  -9],
[ 66, -37, -24, -13,  44, -32, -11,  19, -52,   5,  21, -52,  -9, -54, -14,
 -19, -52,  -9],
[ 66, -37, -23, -13,  44, -33, -11,  19, -52,   6,  20, -52,  -9, -54, -14,
 -20, -52,  -9],
[ 66, -37, -23, -13,  44, -33, -11,  19, -52,   7,  20, -53,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -37, -23, -13,  44, -33, -11,  19, -52,   7,  20, -53,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -36, -23, -13,  44, -33, -11,  19, -52,   7,  20, -53,  -9, -54, -14,
 -19, -53,  -8],
[ 66, -36, -24, -13,  44, -33, -11,  18, -52,   7,  20, -53,  -8, -54, -14,
 -18, -53,  -8],
[ 66, -36, -24, -13,  44, -33, -11,  18, -53,   6,  20, -53,  -8, -54, -14,
 -18, -53,  -8],
[ 66, -36, -24, -13,  44, -33, -11,  18, -53,   6,  20, -53,  -8, -54, -14,
 -19, -53,  -9],
[ 66, -36, -24, -13,  44, -33, -11,  17, -53,   6,  20, -53,  -9, -54, -14,
 -19, -53,  -9],
[ 66, -36, -24, -13,  44, -33, -11,  17, -53,   6,  20, -53,  -9, -54, -14,
 -19, -53,  -9],
[ 66, -37, -24, -13,  44, -33, -11,  17, -53,   6,  20, -53,  -9, -54, -14,
 -19, -53,  -9],
[ 66, -37, -24, -13,  44, -33, -11,  17, -53,   6,  20, -53,  -9, -54, -14,
 -19, -53,  -9],
[ 66, -37, -24, -13,  44, -33, -11,  17, -53,   6,  20, -53,  -9, -54, -14,
 -19, -53,  -9],
[ 66, -37, -24, -13,  44, -32, -12,  16, -53,   7,  20, -53,  -9, -54, -14,
 -19, -53,  -9]
], "float32")
print np.shape(static25)
#a = np.ones((50,1), dtype=np.int)*3

#target_data = np.array([[0], [1], [2]], "float32")

#print np.reshape(np.append(training_data10,two),(53,18))
