import numpy as np
import matplotlib.pyplot as plt

# 定数
g = 9.81  # 重力加速度(m/s^2)
l = 1.0   # 振り子の長さ(m)
theta_0 = np.pi / 4  # 初期角度(rad)

# 時間の設定
dt = 0.01  # 時間刻み(s)
t = np.arange(0, 10, dt)

# 初期条件
omega = 0.0  # 初角速度(rad/s)
theta = theta_0  # 初期角度(rad)

# 角速度と角度のリスト
omega_list = []
theta_list = []

for time in t:
    alpha = - (g / l) * np.sin(theta)  # 角加速度(rad/s^2)
    omega += alpha * dt  # 角速度の更新
    theta += omega * dt  # 角度の更新
    omega_list.append(omega)
    theta_list.append(theta)

# グラフの描画
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, theta_list, label='Angle')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, omega_list, label='Angular Velocity', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.legend()

plt.tight_layout()
plt.show()
