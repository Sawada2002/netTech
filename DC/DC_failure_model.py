'''
必要であれば
pip install numpy pandas scikit-learn
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# テキストファイルから各国のデータセンター情報を読み取る
file_path = 'DC.txt'

countries = []
data_centers = []

with open(file_path, 'r') as file:
    for line in file:
        country, centers = line.strip().split()
        countries.append(country)
        data_centers.append(int(centers))

# 各データセンターの障害確率（仮定）
failure_prob_per_center = 0.02

# データの生成
np.random.seed(42)
data = []

for country, centers in zip(countries, data_centers):
    for _ in range(100):  # 各国ごとに100サンプル生成
        failures = np.random.binomial(centers, failure_prob_per_center)
        data.append([country, centers, failures])

df = pd.DataFrame(data, columns=['Country', 'DataCenters', 'Failures'])
print("データフレームの内容を確認:")
print(df.head())  # データフレームの内容を確認

# カテゴリカルデータの数値化
le = LabelEncoder()
df['Country'] = le.fit_transform(df['Country'])

# 特徴量とターゲットの分割
X = df[['Country', 'DataCenters']]
y = df['Failures']

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# モデルの作成と訓練
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# 予測と評価
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"平均二乗誤差 (Mean Squared Error): {mse}")
print(f"R2スコア: {r2}")

# エンコードされた値を元の国名に戻す
df['Country'] = le.inverse_transform(df['Country'])

# 各国のデータを表示
for country in countries:
    country_data = df[df['Country'] == country].head(5)  # 各国ごとに上位5行を表示
    print(f"\n{country}のデータ:")
    print(country_data)

# データフレームの全体内容を表示
print("\nデータフレームの全体内容を表示:")
print(df)
