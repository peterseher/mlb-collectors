from pybaseball import pitching_stats
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
pitchers = pitching_stats(2025)
wanted = ['Name', 'Team', 'ERA', 'GB%', 'HardHit%', 'IP', 'CStr%']
pitchers = pitchers[wanted].dropna()
for col in ['ERA', 'GB%', 'HardHit%', 'IP', 'CStr%']:
    pitchers[col] = pd.to_numeric(pitchers[col], errors='coerce')

pitchers = pitchers.dropna()
pitchers['ERA_inv'] = pitchers['ERA'].max()- pitchers['ERA']
pitchers['HardHit_inv'] = pitchers['HardHit%'].max() - pitchers ['HardHit%']
scaler = MinMaxScaler()
pitchers[['ERA_scaled', 'GB_scaled', 'HardHit_scaled', 'IP_scaled', 'CStr_scaled']] = scaler.fit_transform(pitchers[['ERA_inv', 'GB%', 'HardHit_inv', 'IP', 'CStr%']])
pitchers['score'] = (
    pitchers['ERA_scaled'] * 0.35 +
    pitchers['GB_scaled'] * 0.35 +
    pitchers['GB_scaled'] * 0.35 +
    pitchers['IP_scaled'] * 0.075 +
    pitchers['CStr_scaled']* 0.075
)
top_pitchers = pitchers.sort_values(by='score', ascending=False).head(50)
print(top_pitchers[['Name', 'Team', 'ERA', 'GB%', 'HardHit%', 'IP', 'CStr%', 'score']]) 
