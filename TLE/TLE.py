from sgp4.api import Satrec
from sgp4.api import jday

def read_tle(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    tles = []
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            name = lines[i].strip()
            tle_line1 = lines[i + 1].strip()
            tle_line2 = lines[i + 2].strip()
            tles.append((name, tle_line1, tle_line2))
    return tles

def calculate_position_velocity(tle_line1, tle_line2, year, month, day, hour, minute, second):
    satellite = Satrec.twoline2rv(tle_line1, tle_line2)
    jd, fr = jday(year, month, day, hour, minute, second)
    e, r, v = satellite.sgp4(jd, fr)
    
    if e == 0:
        return r, v
    else:
        return None, None
