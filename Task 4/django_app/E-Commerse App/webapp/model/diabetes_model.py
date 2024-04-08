import pandas as pd
import numpy as np

import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# load the dataset
from imblearn.combine import SMOTEENN
from imblearn.pipeline import Pipeline as imblearnPipeline

def make_prediction():

    print("Reading data ....")

    df = pd.read_csv("model//data/diabetes_dataset.csv")

    print("Finished reading data ....")

    last_ix = len(df.columns)-1

    print("Splitting data ......")
    X, y = df.drop(df.columns[last_ix], axis=1), df[df.columns[last_ix]]

    sk_model = SMOTEENN()

    model = DecisionTreeClassifier()
    pipeline = imblearnPipeline(
        steps = [
            ('scaler', StandardScaler()),
            ('s', sk_model), 
            ('m', model)
        ])
    
    print("Start training data .....")

    pipeline.fit(X, y)

    print("Trained data completely, saving data......")

    joblib.dump(pipeline, "model/diabetes_model.pkl")

    print("Done!")

    # mymodel = joblib.load("mymodel.pkl")

if __name__ == "__main__":

    make_prediction()