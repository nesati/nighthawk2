FROM python:3

COPY . /nighthawk

WORKDIR /nighthawk

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN chmod +x entrypoint.sh

CMD entrypoint.sh