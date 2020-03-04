FROM python:3-alpine
MAINTAINER Gajender Pal Singh "gajenderpalsingh@gmail.com"

RUN mkdir -p /usr/src/finnair
WORKDIR /usr/src/finnair

COPY . /usr/src/finnair
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
RUN  flask create-db

CMD [ "python", "./app.py" ]
