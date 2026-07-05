# AI Model

## Purpose

Detect infrastructure anomalies using machine learning.

---

## Features

- Isolation Forest
- Automatic feature engineering
- Historical baseline learning
- CloudWatch metric ingestion
- Prometheus metric ingestion

---

## Training

```bash
python train.py
```

---

## Inference

```python
from predictor import classify

metrics = {
    "cpu":42,
    "memory":61,
    "disk":50,
    "network_in":150,
    "network_out":145,
    "latency":38,
    "request_rate":620,
    "error_rate":0.02,
    "cpu_memory_ratio":0.68,
    "latency_error":0.76,
    "traffic_delta":5
}

print(classify(metrics))
```
