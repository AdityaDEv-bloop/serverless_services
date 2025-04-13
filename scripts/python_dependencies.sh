#!/usr/bin/env bash

sudo chown -R ubuntu:ubuntu ~/serverless_services
echo Virtual Env Creating
python3 -m venv /home/ubuntu/serverless_services/env
echo Virtual Env Created----Done
echo Virtual Env Activating
source /home/ubuntu/serverless_services/env/bin/activate
echo Virtual Env Activated----Done
echo Installing requirements
pip install -r /home/ubuntu/serverless_services/requirements.txt
echo Installed requirements----Done