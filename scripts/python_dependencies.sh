#!/usr/bin/env bash

sudo chown -R ubuntu:ubuntu ~/serverless_services
virtualenv /home/ubuntu/serverless_services/venv
source /home/ubuntu/serverless_services/venv/bin/activate
pip install -r /home/ubuntu/serverless_services/requirements.txt