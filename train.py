# train.py - generate data, train model and save artifact
from astropredict.data_gen import generate_synthetic_dataset
from astropredict.model import train_model
import os
import pandas as pd

def main():
    os.makedirs("model", exist_ok=True)
    df = generate_synthetic_dataset(n_samples=1200)
    df.to_csv("data/sample_dataset.csv", index=False)
    model, metrics = train_model(df, save_path="model/astropredict_rf.joblib")
    print("Training done. Metrics:", metrics)
    print("Saved model to model/astropredict_rf.joblib and dataset to data/sample_dataset.csv")

if __name__ == "__main__":
    main()
