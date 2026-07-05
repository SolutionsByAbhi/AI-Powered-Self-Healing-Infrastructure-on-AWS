import random
import json
from datetime import datetime


def metric():

    return {

        "timestamp": datetime.utcnow().isoformat(),

        "cpu": random.randint(10, 100),

        "memory": random.randint(20, 100),

        "disk": random.randint(20, 95),

        "network_in": random.randint(100, 500),

        "network_out": random.randint(100, 500),

        "latency": random.randint(10, 600),

        "request_rate": random.randint(100, 1000),

        "error_rate": round(

            random.random(),

            2

        )

    }


if __name__ == "__main__":

    print(

        json.dumps(

            metric(),

            indent=2

        )

    )
