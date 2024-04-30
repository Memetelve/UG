FROM python:3.12

COPY ./req.txt .
RUN pip install -r req.txt

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]
