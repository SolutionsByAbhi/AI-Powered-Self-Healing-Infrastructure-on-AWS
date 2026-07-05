import json


def build(incident):

    return {

        "IncidentId":

        incident["incident_id"],

        "Service":

        incident["service"],

        "Action":

        incident["action"],

        "Status":

        incident["status"],

        "Severity":

        incident.get(

            "severity",

            "LOW"

        )

    }


def lambda_handler(event, context):

    return {

        "report":

        json.dumps(

            build(event),

            indent=2

        )

    }
