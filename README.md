# ⚾ MLB Collectors – by Peter Seher

This repository contains custom Python scripts that collect and analyze real-time **MLB team and player stats** using the `pybaseball` library and `pandas`. These tools are built to support deeper analysis for fantasy baseball, sports betting, scouting, and predictive modeling.

---

## 📂 Contents

| File                  | Description |
|-----------------------|-------------|
| `batting.py`          | Collects **team-level batting stats** for the current MLB season and selects key metrics like AVG, OBP, SLG, HardHit%, CSW%, and CStr%. |
| `pitching.py`         | Collects **team-level pitching stats**, including ERA, FIP, WHIP, K%, BB%, GB%, CSW%, and HardHit%. |
| `top_50_batters.py`   | Ranks the **top 50 individual batters** based on a custom scoring model that weights AVG, RBI, and OBP. |
| `top_50_pitchers.py`  | Ranks the **top 50 individual pitchers** using a weighted formula based on ERA, GB%, HardHit%, IP, and CStr%. |

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

python batting.py
python top_50_batters.py
