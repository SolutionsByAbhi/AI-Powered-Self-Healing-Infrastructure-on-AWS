import joblib


def save(model, filename):

    joblib.dump(

        model,

        filename

    )


def load(filename):

    return joblib.load(

        filename

    )
