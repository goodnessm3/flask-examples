FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-dev  build-essential python3-pip gunicorn
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8000", "--access-logfile", "alog.txt"]