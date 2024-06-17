'''
必要に応じて以下のコマンドをターミナルで実行する
pip install matplotlib
pip install numpy
pip install matplotlib basemap cartopy
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

'''
lat : 経度
lon : 緯度
alt : 高度
'''

# 衛星のサンプルデータ(ここに実験用データを入れる)
satellite_data = [
    {"name": "Satellite 1", "lat": 0, "lon": 0, "alt": 35786},
    {"name": "Satellite 2", "lat": 45, "lon": 45, "alt": 35786},
    {"name": "Satellite 3", "lat": -30, "lon": 60, "alt": 35786},
]

# 地球の描画
# 立体的な地球の描画
fig = plt.figure(figsize=(8, 8)) 
ax = fig.add_subplot(111, projection='3d')

# 地球の表面を描画
u = np.linspace(0, 2 * np.pi, 100) #地球の表面
v = np.linspace(0, np.pi, 100) #地球の表面
#地球の表面座標'x,y,z'
x = 6371 * np.outer(np.cos(u), np.sin(v))
y = 6371 * np.outer(np.sin(u), np.sin(v))
z = 6371 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b', alpha=0.5)

# 衛星の位置をプロット
# 緯度と経度をラジアンに変換し,地球の半径（6371km）を加えた衛星の高度を設定
for satellite in satellite_data:
    lat = np.deg2rad(satellite["lat"])
    lon = np.deg2rad(satellite["lon"])
    alt = satellite["alt"] + 6371  # 地球半径を追加

    # 衛星の3D座標を計算
    x = alt * np.cos(lat) * np.cos(lon)
    y = alt * np.cos(lat) * np.sin(lon)
    z = alt * np.sin(lat)
    
    ax.scatter(x, y, z, color='r', s=50)
    ax.text(x, y, z, satellite["name"], color='r')

# 軸ラベルを設定
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
