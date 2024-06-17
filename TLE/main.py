from TLE import read_tle, calculate_position_velocity

# TLEファイルのパスを指定
tle_file_path = 'tle_data.txt'

# TLEデータを読み込み
tle_line1, tle_line2 = read_tle(tle_file_path)

# 日時を指定（例：2024年6月18日12:00:00 UTC）
year = 2024
month = 6
day = 18
hour = 12
minute = 0
second = 0

# 衛星の位置と速度を計算
position, velocity = calculate_position_velocity(tle_line1, tle_line2, year, month, day, hour, minute, second)

if position and velocity:
    print(f"位置 (km): {position}")
    print(f"速度 (km/s): {velocity}")
else:
    print("計算エラーが発生しました")
