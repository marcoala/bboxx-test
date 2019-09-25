FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /workingdir
WORKDIR /workingdir
COPY requirements.txt /workingdir/
RUN pip install -r requirements.txt
