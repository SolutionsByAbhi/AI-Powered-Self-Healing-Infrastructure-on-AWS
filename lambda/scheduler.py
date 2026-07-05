import boto3

events = boto3.client("events")


def schedule(rule):

    events.enable_rule(

        Name=rule

    )


def disable(rule):

    events.disable_rule(

        Name=rule

    )
