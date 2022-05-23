if [ ! -d ".env" ]; then
  python gen_env.py
fi

python manage.py migrate

python gunicorn /nighthawk/nighthawk2/wsgi.py