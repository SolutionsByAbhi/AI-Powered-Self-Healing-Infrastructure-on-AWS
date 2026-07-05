#!/bin/bash

set -e

rm -rf build

mkdir build

pip install \
-r lambda/requirements.txt \
-t build/

cp lambda/*.py build/

cd build

zip -r anomaly_handler.zip .

cd ..
