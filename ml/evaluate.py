import joblib

from preprocessing import (

    load_dataset,

    prepare

)


model = joblib.load(
    "model.joblib"
)


df = prepare(

    load_dataset(

        "sample_dataset.csv"

    )

)


score = model.score_samples(

    df.drop(

        columns=["timestamp"]

    )

)


print(score)
