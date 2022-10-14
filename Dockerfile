FROM python:3.10.6-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

COPY . .
