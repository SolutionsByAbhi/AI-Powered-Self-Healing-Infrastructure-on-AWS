PLAYBOOKS = {

    "cpu_high": "scale_asg",

    "memory_high": "restart_pod",

    "disk_full": "cleanup_disk",

    "http_5xx": "restart_ecs",

    "latency": "scale_out",

    "cache_error": "flush_cache",

    "database_down": "database_failover"
}


def choose(metric):

    return PLAYBOOKS.get(
        metric,
        "manual_review"
    )
