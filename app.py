# app.py - Streamlit app to use trained model for predictions and show dataset/analysis
import streamlit as st
import pandas as pd
import numpy as np
import os
from astropredict.data_gen import generate_synthetic_dataset
from astropredict.model import load_model, predict_power

st.set_page_config(page_title="AstroPredict — Satellite Solar Power Predictor", layout="centered")
st.title("AstroPredict ⚡🛰️")
st.write("Predict expected average usable solar power per orbit for a small satellite (synthetic/demo model).")

# ensure model exists; if not, offer to generate and train
model_path = "model/astropredict_rf.joblib"
if not os.path.exists("data/sample_dataset.csv"):
    st.info("No dataset found — generating a small sample dataset (demo).")
    df_demo = generate_synthetic_dataset(n_samples=200)
    os.makedirs("data", exist_ok=True)
    df_demo.to_csv("data/sample_dataset.csv", index=False)
else:
    df_demo = pd.read_csv("data/sample_dataset.csv")

st.sidebar.header("Input Satellite Parameters")
altitude_km = st.sidebar.slider("Altitude (km)", 160, 1200, 500)
inclination_deg = st.sidebar.slider("Inclination (deg)", 0, 180, 51)
panel_area_m2 = st.sidebar.slider("Panel area (m²)", 0.01, 2.0, 0.1, step=0.01)
panel_efficiency = st.sidebar.slider("Panel efficiency", 0.05, 0.40, 0.25)
payload_power_w = st.sidebar.slider("Payload power (W)", 0.1, 50.0, 5.0)

st.sidebar.markdown("---")
if st.sidebar.button("Train model (takes ~30s locally)"):
    st.info("Training model on synthetic data...")
    import subprocess, sys
    subprocess.run([sys.executable, "train.py"])
    st.success("Training finished. Reload the page to load the trained model.")

st.header("Dataset (sample)")
st.dataframe(df_demo.head(200))

st.header("Model & Prediction")
if os.path.exists(model_path):
    model = load_model(model_path)
    st.success("Loaded trained model.")
    X = {
        "altitude_km": altitude_km,
        "inclination_deg": inclination_deg,
        "panel_area_m2": panel_area_m2,
        "panel_efficiency": panel_efficiency,
        "payload_power_w": payload_power_w,
        "eclipse_fraction": 0.3  # placeholder; model trained with eclipse_fraction feature
    }
    pred = predict_power(model, X)[0]
    st.metric("Predicted average usable power (W)", f"{pred:.2f}")
    st.write("Note: This model was trained on synthetic data for demonstration and explanation purposes.")
else:
    st.warning("No trained model found. Click 'Train model' on the sidebar to create one (will save to model/).")
