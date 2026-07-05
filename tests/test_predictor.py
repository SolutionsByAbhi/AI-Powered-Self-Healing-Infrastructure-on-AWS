from ml.predictor import classify


def test_prediction():

    metrics = {

        "cpu": 40,

        "memory": 60,

        "disk": 55,

        "network_in": 150,

        "network_out": 140,

        "latency": 45,

        "request_rate": 500,

        "error_rate": 0.02,

        "cpu_memory_ratio": 0.66,

        "latency_error": 0.9,

        "traffic_delta": 10

    }

    result = classify(metrics)

    assert "anomaly" in result

    assert "confidence" in result
