FROM python:3.11-alpine

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]