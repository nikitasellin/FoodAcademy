FROM python:3.9.1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY deploy/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir -p media/
COPY app/static/images media/
