import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使用微软雅黑
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 初始参数
wn = 1.0  # 自然频率
zeta = 0.2  # 阻尼比

# 定义绘图函数
def plot_response(wn, zeta):
    num = [wn**2]  # 分子
    den = [1, 2*zeta*wn, wn**2]  # 分母
    sys = ctrl.TransferFunction(num, den)

    time = np.linspace(0, 50, 1000)  # 时间范围
    t, y = ctrl.step_response(sys, T=time)

    ax.clear()
    ax.plot(t, y, label='阶跃响应', color='b')
    ax.axhline(1, color='r', linestyle='--', label='稳态值')
    ax.set_title('二阶震荡系统的阶跃响应')
    ax.set_xlabel('时间 (秒)')
    ax.set_ylabel('响应')
    ax.legend()
    ax.grid()
    plt.draw()

    # 固定坐标系的范围
    ax.set_xlim(0, 50)  # X轴范围
    ax.set_ylim(0, 2)  # Y轴范围
    plt.draw()

# 创建图形和子图
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)  # 调整底部空间以容纳滑块

# 绘制初始响应
plot_response(wn, zeta)

# 添加滑块
ax_wn = plt.axes([0.1, 0.1, 0.65, 0.03])  # 自然频率滑块位置
wn_slider = Slider(ax_wn, '自然频率', 0.1, 5.0, valinit=wn)

ax_zeta = plt.axes([0.1, 0.15, 0.65, 0.03])  # 阻尼比滑块位置
zeta_slider = Slider(ax_zeta, '阻尼比', 0.0, 1.0, valinit=zeta)

# 更新函数
def update(val):
    wn = wn_slider.val
    zeta = zeta_slider.val
    plot_response(wn, zeta)

# 绑定滑块事件
wn_slider.on_changed(update)
zeta_slider.on_changed(update)

plt.show()

