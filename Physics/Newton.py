import numpy as np
import matplotlib.pyplot as plt

# 時間の設定
t = np.linspace(0, 10, 100)  # 0から10秒までを100等分

# 位置と速度の設定
x = t**2 
v = 2 * t  # 速度は位置の時間微分

# グラフの描画
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x, label='Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, v, label='Velocity', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()

plt.tight_layout()
plt.show()
