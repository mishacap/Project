
FROM python:3.11-alpine

WORKDIR tests

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt


COPY . .


CMD ["pytest"]