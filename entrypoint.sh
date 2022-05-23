if [ ! -d ".env" ]; then
  python gen_env.py
fi

python manage.py migrate

gunicorn nighthawk2.wsgi -b 0.0.0.0:8000
