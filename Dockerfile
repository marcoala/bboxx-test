FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /scripts
WORKDIR /scripts
COPY requirements.txt /scripts/
RUN pip install -r requirements.txt
COPY . /scripts/
