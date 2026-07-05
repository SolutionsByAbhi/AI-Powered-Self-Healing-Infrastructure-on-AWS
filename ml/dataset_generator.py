import random
import pandas as pd

rows = []

for _ in range(5000):

    rows.append({

        "cpu": random.randint(10,100),

        "memory": random.randint(20,100),

        "disk": random.randint(20,95),

        "network_in": random.randint(100,500),

        "network_out": random.randint(100,500),

        "latency": random.randint(20,900),

        "request_rate": random.randint(100,2500),

        "error_rate": round(random.random(),2)

    })

df = pd.DataFrame(rows)

df.to_csv(

    "training_dataset.csv",

    index=False

)
