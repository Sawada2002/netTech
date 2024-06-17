from TLE import read_tle, calculate_position_velocity

# TLEファイルのパスを指定
tle_file_path = 'tle_data.txt'

# TLEデータを読み込み
tles = read_tle(tle_file_path)

# 日時を指定（例：2024年6月18日12:00:00 UTC）
year = 2024
month = 6
day = 18
hour = 12
minute = 0
second = 0

# 各衛星の位置と速度を計算
for name, tle_line1, tle_line2 in tles:
    position, velocity = calculate_position_velocity(tle_line1, tle_line2, year, month, day, hour, minute, second)
    
    print(f"衛星名: {name}")
    if position and velocity:
        print(f"  位置 (km): {position}")
        print(f"  速度 (km/s): {velocity}")
    else:
        print("  計算エラーが発生しました")
    print()  # 空行を追加して見やすくする
