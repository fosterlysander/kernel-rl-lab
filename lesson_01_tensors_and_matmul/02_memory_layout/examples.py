import numpy as np
# 内存布局
A = np.arange(6).reshape(2,3)
# [[0 1 2]
# [3 4 5]]
print(A)
print(A.ravel()) # 内存里的真实顺序 [0 1 2 3 4 5]
print(A.strides) # (24,8)

print(A.itemsize) # 8 每个元素占8字节
print(A.shape) # (2,3)

# 使用numpy验证
i, j = 1,2
offset_base = (A.strides[0] * i + A.strides[1] * j)
print(offset_base) # 40
print(A[i, j]) # 5

# 转置不搬数据只改strides
B = A.T
print(B.shape,B.strides) # (3,2) (8,24)
