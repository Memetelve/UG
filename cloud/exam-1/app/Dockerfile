FROM python:3.12 as base

ARG BUILD_ENV="production"
ARG STATUS_MESSAGE=""

ENV APP_PORT=5000
ENV STATUS_MESSAGE=${STATUS_MESSAGE}

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE ${APP_PORT}

CMD ["python", "main.py"]
