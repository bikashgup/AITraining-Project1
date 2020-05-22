FROM python:3

RUN mkdir /application

ADD ./app /applicaion/

ADD ./static /application/

ADD ./utils /application/

ADD ./checkpoints /application/

COPY ./settings.py /application/

COPY ./requirements.txt /application/

COPY ./__init__.py /application/

RUN pip install --upgrade pip

RUN pip install -r /application/requirements.txt

ENV FLASK_APP='app/ISEAR_app/ISEAR.py'

WORKDIR  /application/

EXPOSE 5000