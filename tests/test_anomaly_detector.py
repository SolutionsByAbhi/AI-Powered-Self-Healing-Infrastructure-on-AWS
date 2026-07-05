from lambda.anomaly_detector import detector


def test_detector():

    result = detector.detect({

        "cpu":90,

        "memory":80,

        "disk":70,

        "network_in":200,

        "network_out":180,

        "latency":650,

        "request_rate":1800,

        "error_rate":0.40,

        "cpu_memory_ratio":1.12,

        "latency_error":260,

        "traffic_delta":20

    })

    assert "anomaly" in result

    assert "confidence" in result
