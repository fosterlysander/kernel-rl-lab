"""第一节：张量的维度、形状、类型、索引与占用字节数。"""
import numpy as np


def main():
    s = np.array(3.0)
    v = np.array([1.0, 2.0, 3.0])
    matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
    tensor = np.zeros((2, 3, 4))
    for name, x in [("标量", s), ("向量", v), ("矩阵", matrix), ("三维张量", tensor)]:
        print(name, "shape =", x.shape, "ndim =", x.ndim, "dtype =", x.dtype)
    print("元素 / 行 / 列：", matrix[1, 2], matrix[0], matrix[:, 1])
    x = np.zeros((32, 128, 768), dtype=np.float32)
    print("元素数：", x.size, "每元素字节：", x.itemsize, "总字节：", x.nbytes)
    print("MiB：", x.nbytes / 1024**2)
    # TODO: 改为 float16，先预测 nbytes，再运行。


if __name__ == "__main__":
    main()
