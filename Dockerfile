FROM python:3

EXPOSE 8000

COPY . /nighthawk

WORKDIR /nighthawk

RUN pip install -r requirements.txt

RUN python manage.py collectstatic

RUN pip install gunicorn

RUN chmod +x entrypoint.sh

CMD ./entrypoint.sh
