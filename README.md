# AstroPredict — Satellite Solar Power Predictor (Demo)

**AstroPredict** is a small, explainable project that demonstrates how to:
- generate a physics-inspired synthetic dataset for satellite solar power,
- train a simple machine learning model (Random Forest) to predict average usable power per orbit,
- expose a Streamlit UI for interactive prediction and dataset inspection.

This project is intentionally designed for teaching / MSc-application demos. The dataset is synthetic (and documented) so you can explain exactly how data was generated to your professor.

## Quick start (local)
```bash
unzip astropredict_package.zip
cd astropredict_package
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
# generate data and train:
python train.py
# run the Streamlit app:
streamlit run app.py
```

## What to show your professor
- `train.py` shows the data-generation logic (physics-inspired) and a small RF model training.
- Explain features like `eclipse_fraction` and how altitude/inclination affect sun exposure.
- Include plots (you can extend notebook/) showing correlation between altitude and generated power.

## Files
- `astropredict/` : package with data generation & model helpers
- `train.py` : script that creates dataset and trains model (`model/astropredict_rf.joblib`)
- `app.py` : Streamlit demo to predict using the trained model
- `data/sample_dataset.csv` : generated sample dataset
- `requirements.txt`, `README.md`, `.gitignore`

## Extending for research-level quality
- Replace synthetic data with simulated or real pass/illumination computations (SGP4 + eclipse modeling).
- Add explainability: SHAP plots showing feature importance per prediction.
- Add uncertainty estimation (quantile regression / ensembles).
