echo I will sleep one min
sleep 1m
echo I start to create an conf
APP_PORT=${PORT:-6321}
cd /app/
cd /app/network/
chmod +x manage.py
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic --noinput --clear
/opt/proj_env/bin/gunicorn --worker-tmp-dir /dev/shm config.wsgi:application --certfile=cert.pem --keyfile=key.pem --bind "0.0.0.0:${APP_PORT}"
