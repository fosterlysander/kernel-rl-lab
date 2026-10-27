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

# 矩阵乘法的三种理解方式
# 点积 对应行*对应列 一次算一个元素
C = np.zeros((3,3),dtype=int)
for i in range(3):
    for j in range(3):
        C[i,j] = A[i,:] @ B[:,j]
print(C[0,1],C[2,1]) # 30 106

# 列组合 一次算一整列
print(A @ B[:,0]) # [27 61 95]

# 外积之和
L0 = np.outer(A[:,0],B[0,:])
L1 = np.outer(A[:,1],B[1,:])
print(L0)
print(L1)
print(L0+L1)
