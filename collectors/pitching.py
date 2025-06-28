from pybaseball import team_pitching
import pandas as pd
def run():
    df = team_pitching(2025)
    wanted_columns = ['Team', 'ERA', 'WHIP', 'FIP', 'K%', 'BB%', 'HardHit%']
    pitching_stats = df[wanted_columns]
    pitching_stats = pitching_stats.sort_values(by='ERA', ascending=True)
    return pitching_stats
