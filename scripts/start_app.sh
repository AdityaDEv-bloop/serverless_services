#!/usr/bin/bash
echo Virtual Env Activating
source /home/ubuntu/serverless_services/env/bin/activate
echo Virtual Env Activated----Done
sed -i 's/\[]/\["52.221.199.60"]/' /home/ubuntu/serverless_services/serverless_services/settings.py

cp .env /home/ubuntu/serverless_services/
python3 /home/ubuntu/serverless_services/manage.py makemigrations
python3 /home/ubuntu/serverless_services/manage.py migrate
python3 /home/ubuntu/serverless_services/manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
#sudo tail -f /var/log/nginx/error.log
#sudo systemctl reload nginx
#sudo tail -f /var/log/nginx/error.log
#sudo nginx -t
#sudo systemctl restart gunicorn
#sudo systemctl status gunicorn
#sudo systemctl status nginx
# Check the status
#systemctl status gunicorn
# Restart:
#systemctl restart gunicorn
#sudo systemctl status nginx
