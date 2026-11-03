# 实现流程：
# 1. 定义匿名函数 f(x) = x²
# 2. 在整数点上求值，并用列表推导打印结果
# 3. 用细密采样画出连续曲线，再把整数点画成散点
# 4. 给每个散点标注坐标 (x, f(x))
# 5. 补上坐标轴、轴标签、图例和网格，最后显示图像

import numpy as np
import matplotlib.pyplot as plt

# 匿名函数
f = lambda x: x**2

# 链式推导
print([f(x) for x in [-2, -1, 0, 1, 2, 3, 4]])

# 图像
xs = [-2, -1, 0, 1, 2, 3, 4]
ys = [f(x) for x in xs]

x = np.linspace(-2.5, 4.5, 200)
plt.plot(x, x**2, label="f(x) = x²")
plt.scatter(xs, ys, color="green", zorder=3)

# zip() 把两个可迭代对象的元素一一配对
for a, b in zip(xs, ys):
    plt.annotate(
        f"({a}, {b})",
        (a, b),
        textcoords="offset points",
        xytext=(5, 5),
    )

# 添加坐标轴 网格和图例
plt.axhline(0, color="gray", lw=0.8)
plt.axvline(0, color="gray", lw=0.8)

# 设置横轴纵轴名称
plt.xlabel("x")
plt.ylabel("f(x)")

plt.legend()
plt.grid(alpha=0.3)
plt.show()
