from sgp4.api import Satrec
from sgp4.api import jday

def read_tle(file_path):
    with open(file_path, 'r') as file:
        tle_lines = file.readlines()
    return tle_lines[0].strip(), tle_lines[1].strip()

def calculate_position_velocity(tle_line1, tle_line2, year, month, day, hour, minute, second):
    satellite = Satrec.twoline2rv(tle_line1, tle_line2)
    jd, fr = jday(year, month, day, hour, minute, second)
    e, r, v = satellite.sgp4(jd, fr)
    
    if e == 0:
        return r, v
    else:
        return None, None
