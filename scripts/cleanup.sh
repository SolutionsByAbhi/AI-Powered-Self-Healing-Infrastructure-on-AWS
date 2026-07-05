#!/bin/bash

rm -rf build

rm -rf .pytest_cache

find . \
-name "__pycache__" \
-type d \
-exec rm -rf {} +

find . \
-name "*.pyc" \
-delete
