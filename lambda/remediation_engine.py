import json

LOW_RISK_ACTIONS = [
"restart_pod",
"scale_service",
"flush_cache"
]

HIGH_RISK_ACTIONS = [
"rollback",
"db_failover",
"traffic_shift"
]

def classify_risk(action):

```
if action in LOW_RISK_ACTIONS:
    return "LOW"

return "HIGH"
```

def choose_action(service):

```
mapping = {
    "eks": "restart_pod",
    "ecs": "scale_service",
    "redis": "flush_cache",
    "database": "db_failover"
}

return mapping.get(
    service,
    "restart_pod"
)
```

def lambda_handler(event, context):

```
action = choose_action(
    event["service"]
)

risk = classify_risk(action)

return {
    "action": action,
    "risk": risk
}
```
