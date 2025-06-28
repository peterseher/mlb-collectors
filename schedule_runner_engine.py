import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from collectors import batting, pitching, top_50_batters as bat50, top_50_pitchers as pit50
from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d')
save_dir = os.path.join('storage', today)
os.makedirs(save_dir, exist_ok=True)
batting_data = batting.run()
batting_data.to_csv(os.path.join(save_dir, 'team_batting.csv'), index=False)
pitching_data = pitching.run()
pitching_data.to_csv(os.path.join(save_dir, 'team_pitching.csv'), index=False)
bat50_data = bat50.run()
pit50_data = pit50.run()
bat50_data.to_csv(os.path.join(save_dir, 'top_50_batters.csv'), index=False)
pit50_data.to_csv(os.path.join(save_dir, 'top_50_pitchers.csv'), index=False)
print(f"✅ Data collected and saved to {save_dir}")