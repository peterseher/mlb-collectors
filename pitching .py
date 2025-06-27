from pybaseball import team_pitching
import pandas as pd
df = team_pitching(2025)
print(df.columns.tolist())
wanted_cols = ['Team', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%', 'GB%', 'CSW%', 'HardHit%', 'HR/9']
pitching_stats = df[wanted_cols]
pitching_stats_sorted = pitching_stats.sort_values(by='ERA')
print(pitching_stats_sorted)