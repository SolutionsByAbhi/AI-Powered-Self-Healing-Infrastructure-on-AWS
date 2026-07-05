RUNBOOKS = {

    "restart_ecs": "RestartECS",

    "restart_pod": "RestartEKSPod",

    "restart_ec2": "RestartEC2",

    "flush_cache": "FlushCache",

    "scale_out": "ScaleASG",

    "database_failover": "FailoverRDS"

}


def select(action):

    return RUNBOOKS.get(

        action,

        "ManualApproval"

    )
