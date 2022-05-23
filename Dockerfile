FROM python:3

COPY . /nighthawk

WORKDIR /nighthawk

RUN pip install -r requirements.txt

RUN python gen_env.py

RUN python manage.py migrate

CMD python manage.py runserver