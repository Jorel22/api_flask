FROM python:3.7-alpine3.12
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python run.py