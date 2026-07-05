import pandas as pd


class FeatureStore:

    def __init__(

        self,

        filename

    ):

        self.filename = filename

    def append(

        self,

        row

    ):

        df = pd.DataFrame(

            [row]

        )

        df.to_csv(

            self.filename,

            mode="a",

            header=False,

            index=False

        )
