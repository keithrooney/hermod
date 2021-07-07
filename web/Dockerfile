FROM python:3.8-slim-buster

WORKDIR /home/hermod

COPY main.py .
COPY requirements.txt .

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install curl -y

RUN python -m pip install -r requirements.txt

ENV FLASK_APP main.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]
