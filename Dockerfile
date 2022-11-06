FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "app.main:app", "--bind", "0.0.0.0" ]
