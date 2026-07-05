from unittest.mock import MagicMock
from lambda.dynamodb import IncidentRepository


def test_save():

    repo = IncidentRepository.__new__(IncidentRepository)

    repo.table = MagicMock()

    repo.save(

        {

            "incident_id": "123"

        }

    )

    repo.table.put_item.assert_called_once()
