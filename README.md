# 🛰️ AstroPredict  
### _“Exploring the bridge between AI and Space Science.”_

**by Salma Hoque Koli, BSc in CSE (2026)**  

---

## 🚀 Overview
**AstroPredict** is a small but research-inspired project that predicts how much **solar power a satellite can generate per orbit** using **Machine Learning**.  

I built this to explore how data-driven models can connect with real orbital behavior — without using any external datasets.  
All the data in this project is **synthetic**, generated through physics-inspired logic.

---

## 🎯 Objective
- Estimate satellite solar power output based on orbit parameters.  
- Analyze how altitude, inclination, and eclipse fraction affect energy.  
- Create a simple, interactive prediction app for demonstration.

---

## ⚙️ How It Works
1. **Synthetic Dataset**  
   Generated using `data_gen.py`, which simulates:
   - Altitude (km)  
   - Inclination (°)  
   - Eclipse fraction (0–1)  
   - Panel efficiency (%)  
   - Temperature (°C)  
   - → Output: Average Power (Watts)

2. **Model Training**  
   The model (`RandomForestRegressor`) is trained in `train.py` and saved for reuse.

3. **Interactive App**  
   Built with **Streamlit**, allowing users to test different orbit values and see instant predictions.

---

## 📊 Insights
- Higher **altitude** → less eclipse time → more solar power.  
- Greater **inclination** → slightly lower average output due to thermal stress.  
- **Panel efficiency** has the strongest positive correlation with power.

These results make physical sense — which means even synth
