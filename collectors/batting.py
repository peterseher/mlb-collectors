from pybaseball import team_batting
import pandas as pd
def run():
    df = team_batting(2025)
    batting_stats_sorted = df[['Team', 'H', 'xwOBA','AB', 'HardHit%', 'G']]
    return batting_stats_sorted
if __name__ == "__main__":
    run()