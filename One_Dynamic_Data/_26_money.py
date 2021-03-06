import numpy as np

money = np.array([
[ 45, -39, -33, -16,  48, -25,   0,  46, -33,  12,  34, -43, -42,   6, -38,
 -18, -53,  -8],
[ 45, -37, -35, -18,  48, -24,  -1,  46, -33,  11,  35, -43, -42,   5, -38,
 -16, -54,  -8],
[ 46, -36, -37, -19,  48, -24,  -2,  47, -32,  11,  36, -42, -41,   6, -38,
 -15, -53, -11],
[ 46, -36, -37, -18,  47, -25,  -2,  46, -33,  11,  35, -43, -41,   6, -38,
 -12, -55,  -8],
[ 45, -35, -37, -19,  46, -26,  -3,  45, -35,  10,  34, -44, -41,   6, -38,
  -8, -56,  -6],
[ 45, -35, -37, -20,  45, -27,  -4,  44, -35,   8,  33, -45, -42,   6, -38,
  -7, -56,  -4],
[ 44, -35, -37, -20,  45, -27,  -4,  44, -35,   8,  33, -45, -42,   6, -38,
  -7, -56,  -4],
[ 44, -35, -37, -20,  45, -27,  -4,  44, -36,   8,  32, -46, -42,   4, -38,
  -7, -56,  -3],
[ 43, -35, -37, -21,  45, -28,  -5,  43, -36,   7,  32, -46, -42,   4, -38,
  -8, -56,  -3],
[ 43, -34, -37, -21,  44, -28,  -5,  43, -36,   7,  32, -46, -41,   4, -39,
  -7, -56,  -3],
[ 43, -34, -36, -21,  44, -28,  -6,  43, -37,   7,  31, -47, -41,   4, -39,
  -7, -56,  -4],
[ 42, -34, -36, -22,  44, -28,  -6,  42, -37,   6,  31, -47, -41,   3, -39,
  -5, -57,  -2],
[ 42, -34, -37, -22,  43, -28,  -7,  42, -38,   6,  30, -47, -41,   3, -39,
  -7, -56,  -3],
[ 42, -33, -37, -23,  43, -28,  -8,  42, -37,   5,  30, -47, -41,   2, -39,
  -6, -56,  -3],
[ 41, -33, -38, -23,  43, -28,  -8,  42, -37,   4,  31, -47, -41,   2, -38,
  -6, -56,  -3],
[ 41, -32, -38, -23,  43, -28,  -8,  42, -37,   4,  31, -47, -42,   2, -38,
  -7, -56,  -3],
[ 41, -32, -38, -23,  43, -29,  -8,  42, -37,   4,  30, -48, -41,   2, -38,
  -7, -56,  -3],
[ 41, -32, -38, -23,  43, -28,  -8,  42, -37,   4,  30, -47, -41,   2, -39,
  -7, -56,  -4],
[ 40, -32, -38, -23,  43, -28,  -9,  41, -38,   4,  30, -47, -41,   2, -39,
  -8, -56,  -4],
[ 41, -32, -38, -24,  43, -29,  -9,  41, -38,   4,  31, -47, -41,   3, -39,
  -8, -56,  -4],
[ 41, -32, -38, -24,  43, -28,  -8,  42, -37,   4,  31, -47, -42,   3, -38,
  -9, -56,  -6],
[ 42, -32, -38, -24,  43, -28,  -7,  42, -37,   5,  32, -47, -42,   3, -38,
  -8, -56,  -5],
[ 42, -32, -38, -24,  43, -28,  -7,  42, -37,   5,  31, -47, -42,   3, -38,
 -10, -55,  -6],
[ 42, -32, -38, -24,  43, -28,  -7,  42, -37,   6,  31, -47, -42,   3, -38,
 -10, -55,  -6],
[ 42, -32, -38, -23,  43, -28,  -7,  42, -37,   6,  31, -47, -42,   3, -38,
 -11, -55,  -7],
[ 42, -32, -38, -23,  43, -28,  -7,  42, -37,   6,  31, -47, -42,   3, -38,
 -10, -55,  -7],
[ 42, -32, -38, -23,  43, -28,  -7,  42, -37,   6,  31, -47, -42,   3, -38,
 -10, -55,  -6],
[ 42, -32, -38, -23,  43, -28,  -7,  42, -37,   6,  31, -47, -42,   3, -38,
 -13, -55,  -8],
[ 42, -32, -38, -23,  44, -27,  -7,  43, -37,   6,  31, -47, -42,   3, -38,
 -14, -54,  -9],
[ 41, -31, -38, -23,  44, -27,  -7,  43, -37,   6,  31, -47, -42,   3, -38,
 -14, -54,  -9],
[ 41, -31, -38, -24,  44, -27,  -7,  42, -37,   5,  31, -47, -42,   3, -38,
 -13, -55,  -8],
[ 41, -31, -37, -24,  44, -27,  -7,  42, -37,   5,  31, -47, -42,   3, -38,
 -12, -55,  -8],
[ 41, -31, -37, -24,  44, -27,  -8,  43, -36,   5,  31, -47, -42,   3, -38,
  -9, -56,  -6],
[ 41, -31, -37, -24,  44, -27,  -8,  42, -37,   4,  31, -47, -42,   2, -38,
  -8, -56,  -5],
[ 40, -31, -38, -24,  44, -27,  -8,  42, -37,   5,  31, -47, -42,   2, -38,
  -5, -56,  -3],
[ 40, -31, -38, -24,  44, -27,  -8,  42, -37,   5,  31, -47, -42,   1, -38,
  -3, -57,  -2],
[ 41, -31, -38, -24,  43, -27,  -8,  42, -37,   5,  30, -47, -42,   1, -38,
  -3, -57,  -1],
[ 41, -31, -38, -24,  43, -27,  -8,  42, -37,   5,  31, -47, -42,   1, -38,
  -2, -57,  -1],
[ 41, -31, -38, -24,  43, -27,  -8,  42, -37,   6,  31, -47, -42,   1, -38,
   0, -57,   0],
[ 41, -31, -38, -24,  43, -27,  -8,  42, -37,   6,  31, -47, -42,   1, -38,
   0, -57,   0],
[ 41, -32, -38, -24,  43, -27,  -8,  42, -37,   5,  31, -47, -42,   1, -38,
  -6, -56,  -3],
[ 41, -32, -39, -25,  43, -27,  -8,  42, -37,   5,  30, -47, -42,   1, -38,
  -8, -56,  -4],
[ 41, -32, -39, -25,  43, -27,  -9,  42, -37,   4,  30, -48, -42,   1, -37,
  -6, -56,  -3],
[ 41, -32, -38, -25,  43, -27,  -9,  42, -37,   3,  30, -48, -42,   1, -37,
  -7, -56,  -3],
[ 41, -32, -38, -25,  43, -27,  -9,  42, -37,   3,  30, -48, -42,   2, -37,
  -4, -57,  -1],
[ 41, -32, -38, -25,  43, -27,  -9,  42, -37,   4,  30, -48, -42,   1, -38,
  -7, -56,  -3],
[ 41, -32, -39, -25,  43, -27,  -9,  42, -37,   4,  30, -48, -42,   1, -38,
  -7, -56,  -3],
[ 41, -32, -39, -25,  43, -27,  -9,  42, -37,   4,  30, -48, -42,   1, -38,
  -5, -56,  -2],
[ 41, -31, -39, -25,  43, -27,  -9,  42, -37,   4,  30, -48, -42,   1, -38,
  -3, -57,   0],
[ 41, -31, -39, -25,  43, -27,  -9,  42, -37,   4,  30, -48, -42,   2, -37,
  -3, -57,  -1],



], "float32")
print np.shape(money)
