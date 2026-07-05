import json
import logging
import os
from datetime import datetime

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logger = logging.getLogger()

logger.setLevel(LOG_LEVEL)


def log(level, message, **kwargs):

    payload = {

        "timestamp": datetime.utcnow().isoformat(),

        "level": level,

        "message": message

    }

    payload.update(kwargs)

    getattr(logger, level.lower())(

        json.dumps(payload)

    )
