from pybaseball import team_batting
import pandas as pd
df = team_batting(2025)
batting_stats_sorted = df[['Team', 'AVG', 'OBP', 'SLG', 'HardHit%', 'CStr%', 'CSW%']]
print(batting_stats_sorted)