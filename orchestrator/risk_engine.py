RISK_MATRIX = {

    "restart_pod": "LOW",

    "restart_ecs": "LOW",

    "scale_out": "LOW",

    "flush_cache": "LOW",

    "restart_ec2": "MEDIUM",

    "rollback": "HIGH",

    "traffic_shift": "HIGH",

    "database_failover": "CRITICAL"
}


def calculate(action):

    return RISK_MATRIX.get(
        action,
        "MEDIUM"
    )
