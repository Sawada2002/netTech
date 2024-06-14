# ネットワーク関連の研究用基本技術
□概要  
研究内容の基礎学習  

□ Basemapの活用  
・衛星データを取得→表示まで行う  
・実験データの可視化で利用(論文では使用しない)  
・Basemapを利用した地理的データの表示方法  
  


□手順

1. **Basemapのインストール**
   
   Basemapをインストールするためには，以下のコマンドを実行する． 

   ```bash
   pip install basemap basemap-data-hires

2. **ライブラリのインポート**
   ```python
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt

3. **実行テスト** 
以下のコードで実際に動くかテストを行う．  
   ```python
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    
    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines() #海岸線
    m.drawcountries() #国境
    plt.show()


□参考になりそうなサイト  
1. https://yyousuke.github.io/matplotlib/basemap.html  
2. https://matplotlib.org/2.0.2/users/pyplot_tutorial.html  
