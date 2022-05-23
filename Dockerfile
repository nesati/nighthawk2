FROM python:3

EXPOSE 8000

COPY . /nighthawk

WORKDIR /nighthawk

RUN pip install -r requirements.txt

# Secret key is not actually used, it just needs to be defined
RUN SECRET_KEY="mock-key" DEBUG="False" python manage.py collectstatic

RUN pip install gunicorn

RUN chmod +x entrypoint.sh

CMD ./entrypoint.sh
