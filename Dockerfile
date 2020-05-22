FROM python:3

RUN mkdir /application 

ADD ./app /application/app
ADD ./static /application/static
ADD ./utils /application/utils
ADD ./checkpoints /application/checkpoints


COPY ./settings.py /application/
COPY ./requirements.txt /application/
COPY ./__init__.py /application/

RUN pip install --upgrade pip 
RUN pip install -r /application/requirements.txt

WORKDIR  /application/

ENV FLASK_APP="app/ISEAR_app/ISEAR.py"

EXPOSE 5000