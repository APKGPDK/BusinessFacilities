FROM python:3.7.4-alpine as dependencies

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

FROM dependencies

COPY app /usr/src/app

ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1

CMD flask run --host 0.0.0.0 --port 80