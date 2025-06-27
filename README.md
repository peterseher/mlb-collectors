# ⚾ MLB Collectors – by Peter Seher

This repository contains custom Python scripts that collect and analyze real-time MLB team and player stats using the `pybaseball` library and `pandas`. These tools are built to support deeper analysis for fantasy baseball, sports betting, scouting, and predictive modeling.

---

## 📂 Contents

| File                  | Description |
|-----------------------|-------------|
| `batting.py`          | Collects team-level batting stats for the current MLB season and selects key metrics like AVG, OBP, SLG, HardHit%, CSW%, and CStr%. |
| `pitching.py`         | Collects team-level pitching stats, including ERA, FIP, WHIP, K%, BB%, GB%, CSW%, and HardHit%. |
| `top_50_batters.py`   | Ranks the top 50 individual batters based on a custom scoring model that weights AVG, RBI, and OBP. |
| `top_50_pitchers.py`  | Ranks the top 50 individual pitchers using a weighted formula based on ERA, GB%, HardHit%, IP, and CStr%. |

---

## 🛠️ Tech Stack

- **Python 3**
- `pandas` for data manipulation
- `pybaseball` for real-time MLB data
- `sklearn.preprocessing.MinMaxScaler` for stat normalization and scoring

---

## 🚀 How to Use

1. Install required packages:

```bash
pip install pybaseball pandas scikit-learn
```

2. Run any script to collect and view stats:

```bash
python batting.py
python top_50_batters.py
```

3. (Optional) Export results to CSV using `.to_csv()` in any script.

---

## 📈 Sample Use Cases

- Build custom MLB scouting reports
- Identify fantasy breakout players
- Create prop bet models based on real stat trends
- Track team-level performance daily

---

## 🚧 Work in Progress

Coming soon:
- A fully automated stat engine that stores daily data snapshots in SQLite
- A Streamlit-powered dashboard
- Team-vs-pitcher matchup predictors

---

## 🧠 Author

**Peter Seher**  
MLB enthusiast and data explorer  
Currently building custom tools for fantasy sports and sports betting analytics

---

## 📫 Contact

Want to collaborate, hire, or follow the project?  
Find me on GitHub: [@peterseher](https://github.com/peterseher)

