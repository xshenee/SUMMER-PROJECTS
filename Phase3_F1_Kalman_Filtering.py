import fastf1
import pandas as pd
import os

if not os.path.exists('f1_cache'):
    os.makedirs('f1_cache')
fastf1.Cache.enable_cache('f1_cache')

print("Loading session data...")
session = fastf1.get_session(2023, 'Monaco', 'Q')
session.load()

hamilton = session.laps.pick_driver('HAM')
verstappen = session.laps.pick_driver('VER')

raw_lap_rimes = hamilton['LapTime'].dt.total_seconds()
raw_lap_rimes_verstappen = verstappen['LapTime'].dt.total_seconds()

clean_lap_times = raw_lap_rimes.dropna()
clean_lap_times_verstappen = raw_lap_rimes_verstappen.dropna()

print("Hamilton's Clean Lap Times (seconds):")
print(clean_lap_times)
print("\nVerstappen's Clean Lap Times (seconds):")
print(clean_lap_times_verstappen)
print(clean_lap_times.head(5))