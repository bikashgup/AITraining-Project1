FROM python:3

RUN mkdir /app

COPY ./app/ /app/

COPY ./requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt

WORKDIR  /app/

EXPOSE 5000
