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

raw_lap_times = hamilton['LapTime'].dt.total_seconds()
raw_lap_times_verstappen = verstappen['LapTime'].dt.total_seconds()

clean_lap_times = raw_lap_times.dropna()
clean_lap_times_verstappen = raw_lap_times_verstappen.dropna()

print("Hamilton's Clean Lap Times (seconds):")
print(clean_lap_times)
print("\nVerstappen's Clean Lap Times (seconds):")
print(clean_lap_times_verstappen)

import numpy as np

lap_times = clean_lap_times.values
n_laps = len(lap_times)

x_est = np.zeros(n_laps)
P_est = np.zeros(n_laps)

x_est[0] = lap_times[0]
P_est[0] = 1.0

Q = 0.05
R = 4.0

for i in range(1, n_laps):
    x_pred = x_est[i-1]
    P_pred = P_est[i-1] + Q

    measurement = lap_times[i]

    K = P_pred / (P_pred + R)

    x_est[i] = x_pred + K * (measurement - x_pred)

    P_est[i] = (1 - K) * P_pred

print("Raw Lap", round(lap_times[9], 2), "seconds")
print("Filtered Lap", round(x_est[9], 2), "seconds")

import matplotlib.pyplot as plt

print("FIGURES:")

plt.figure(figsize=(12, 6))

plt.plot(lap_times, label='Raw Lap Times', linestyle='--', marker='o', alpha=0.5)

plt.plot(x_est, label='Kalman Filtered True Pace', linewidth=2.5)

plt.title('Hamilton Pace Estimates - Monaco 2023 Qualifying')
plt.xlabel('Valid Lap Index')
plt.ylabel('Lap Time (seconds)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.savefig('hamilton_pace_estimate.png', dpi=300)

plt.show()