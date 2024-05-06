ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}

COPY ./myapp ./myapp

WORKDIR /myapp

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
