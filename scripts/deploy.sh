#!/bin/bash

set -e

terraform -chdir=terraform init

terraform -chdir=terraform apply \
-auto-approve

bash scripts/package_lambda.sh

aws lambda update-function-code \
--function-name anomaly-handler \
--zip-file fileb://build/anomaly_handler.zip
