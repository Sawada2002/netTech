# !pip install basemap basemap-data-hires

'''
1. Basemapについて: https://yyousuke.github.io/matplotlib/basemap.html
2. Pyplotを使ったチュートリアル: https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 図の作成
fig, ax = plt.subplots(figsize=(10, 7))

# Basemapの設定
m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution='c', ax=ax)
'''
projection:地図の投影方法(mill = ミラー円筒図法)
llcrnlat:南緯
uncrnlat:北緯
llcrnlon:西経
uncrnrlon:東経
resplution:地図の解像度
    'c'（crude）: 粗い解像度
    'l'（low）: 低解像度
    'i'（intermediate）: 中程度の解像度
    'h'（high）: 高解像度
    'f'（full）: フル解像度
'''


# 海岸線，国境，経度線，緯度線を描画する
m.drawcoastlines() #海岸線
m.drawcountries() #国境
m.drawparallels(range(-90, 91, 30), labels=[1,0,0,0]) #軽度線
m.drawmeridians(range(-180, 181, 60), labels=[0,0,0,1]) #緯度線

# 都市の位置のプロット(東京,ニューヨーク,ロンドン,シドニー)
# 緯度と経度を指定してあげる
cities = {
    'Tokyo': (35.6895, 139.6917),
    'New York': (40.7128, -74.0060),
    'London': (51.5074, -0.1278),
    'Sydney': (-33.8688, 151.2093)
}

#上記で指定したcitiesを順にプロット
for city, (lat, lon) in cities.items():
    x, y = m(lon, lat)
    m.plot(x, y, 'ro')
    plt.text(x, y, city, fontsize=12) #文字サイズの指定

# 地図の表示
plt.title('World Map with Major Cities')
plt.show()
