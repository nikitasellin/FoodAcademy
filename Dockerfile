FROM python:3.9.1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY deploy/requirements.txt ./
RUN pip install -r requirements.txt
