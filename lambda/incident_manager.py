from config import (

    INCIDENT_TABLE,

    INCIDENT_BUCKET

)

from dynamodb import IncidentRepository

from s3_archive import Archive


repository = IncidentRepository(

    INCIDENT_TABLE

)

archive = Archive(

    INCIDENT_BUCKET

)


def lambda_handler(event, context):

    repository.save(event)

    archive.store(event)

    return {

        "stored": True,

        "incident": event["incident_id"]

    }
