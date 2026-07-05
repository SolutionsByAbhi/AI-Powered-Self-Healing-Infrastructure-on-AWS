import pytest


@pytest.fixture
def sample_metrics():

    return {

        "cpu": 90,

        "memory": 88,

        "disk": 74,

        "network_in": 450,

        "network_out": 310,

        "latency": 750,

        "request_rate": 1400,

        "error_rate": 0.31

    }
