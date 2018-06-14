#!/usr/bin/env python3
import time

# Timestamp:
time.time() # type: float
# OUT: 1444327310.2887266


# Datum und Uhrzeit:
time.localtime()
# OUT: time.struct_time(tm_year=2015, tm_mon=10, tm_mday=8, tm_hour=20,
# tm_min=2, tm_sec=11, tm_wday=3, tm_yday=281, tm_isdst=1)

# Zugriff über Index
time.localtime()[0] # type: int
# OUT: 2015

list(time.localtime())
# OUT: [2015, 10, 8, 20, 3, 1, 3, 281, 1]

# Zugriff über Schlüssel
time.localtime().tm_year
# OUT: 2015


# Pause:
time.sleep(1)
# Wartet eine Sekunde


# Ladebalken:

while True:
    print(".", end="", flush=True)
    time.sleep(1)
# OUT: ...........................................
