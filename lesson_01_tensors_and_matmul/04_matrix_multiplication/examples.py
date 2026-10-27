import numpy as np
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])          # (3, 2)
B = np.array([[7, 8, 9],
              [10, 11, 12]])    # (2, 3)

print(A @ B)                    # @ 就是 np.matmul
# [[ 27  30  33]
#  [ 61  68  75]
#  [ 95 106 117]]