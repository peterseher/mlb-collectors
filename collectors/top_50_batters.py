from pybaseball import batting_stats
import pandas as pd
def run():
    batters = batting_stats(2025)
    wanted = ['Name', 'Team','AVG', 'OBP', 'SLG', 'HR', 'RBI', 'BB%', 'K%', 'HardHit%']
    batters = batters[wanted].dropna()
    batters['AVG'] = pd. to_numeric(batters['AVG'], errors='coerce')
    batters['OBP'] = pd.to_numeric(batters['OBP'], errors='coerce')
    batters['RBI'] = pd.to_numeric(batters['RBI'], errors='coerce')
    batters = batters.dropna(subset=['AVG', 'RBI', 'OBP'])
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    batters[['AVG_norm', 'RBI_norm', 'OBP_norm']] = scaler.fit_transform(batters[['AVG', 'RBI', 'OBP']])
    batters['score'] = (batters['AVG_norm'] * 0.5 +batters['RBI_norm']* 0.3 +batters ['OBP_norm'] * 0.2)
    top_batters = batters.sort_values(by='score', ascending=False).head(50)
    return top_batters