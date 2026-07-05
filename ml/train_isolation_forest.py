import joblib

import pandas as pd

from sklearn.ensemble import IsolationForest

df = pd.read_csv(

    "training_dataset.csv"

)

model = IsolationForest(

    contamination=0.03,

    n_estimators=300,

    random_state=42

)

model.fit(df)

joblib.dump(

    model,

    "iforest.joblib"

)

print("Training Completed")
