FROM python:3

RUN mkdir /app

COPY ./app/ISEAR_app /app/

COPY ./requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt

ENV FLASK_APP = 'ISEAR.py'

WORKDIR  /app/

EXPOSE 5000

CMD ["flask", 'run']