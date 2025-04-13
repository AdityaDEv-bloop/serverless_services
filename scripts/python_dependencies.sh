#!/usr/bin/env bash

sudo chown -R ubuntu:ubuntu ~/serverless_services
python3 -m venv /home/ubuntu/serverless_services/env
source /home/ubuntu/serverless_services/env/bin/activate
pip install -r /home/ubuntu/serverless_services/requirements.txt