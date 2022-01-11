FROM python:3.9-alpine

ENV APP_ROOT /usr/src/app

COPY . ${APP_ROOT}
WORKDIR ${APP_ROOT}

RUN pip install -r requirements.txt

ENV FLASK_APP app

CMD ["flask", "run"]
