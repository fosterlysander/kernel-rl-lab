"""
    张量就是一个多维数组
    一堆同类型的数字，按规则排成几个方向。
    “有几个方向”叫维度数ndim“每个方向有多长”合起来叫形状shape
"""

import numpy as np

s = np.array(3.0)
v = np.array([1.0, 2.0, 3.0])
M = np.array([[1, 2, 3],
              [4, 5, 6]])
T = np.zeros((2, 3, 4))

for name, x in [("s", s), ("v", v), ("M", M), ("T", T)]:
    print(name, x.shape, x.ndim, x.dtype)
# s () 0 float64
# v (3,) 1 float64
# M (2, 3) 2 int64
# T (2, 3, 4) 3 float64

# 计算张量有多大
x = np.zeros((32,128,768),dtype=np.float32)
print(x.size) # 32*128*768
print(x.nbytes) # 32*128*768*4 元素个数*字节数 float32占据4个字节 约12M