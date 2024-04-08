import pandas as pd
import numpy as np

import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# load the dataset
from imblearn.combine import SMOTEENN
from imblearn.pipeline import Pipeline as imblearnPipeline

def make_prediction():

    df = pd.read_csv("data/diabetes_dataset.csv")

    last_ix = len(df.columns)-1
    X, y = df.drop(df.columns[last_ix], axis=1), df[df.columns[last_ix]]

    sk_model = SMOTEENN()

    model = DecisionTreeClassifier()
    pipeline = imblearnPipeline(
        steps = [
            ('scaler', StandardScaler()),
            ('s', sk_model), 
            ('m', model)
        ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, "diabetes_model.pkl")

    # mymodel = joblib.load("mymodel.pkl")