FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh

COPY . /app/


RUN chmod +x entrypoint.sh
