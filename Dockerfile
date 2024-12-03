FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y

# update pip
RUN pip install pip -U
# install pip requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

COPY ./src /opt/REQ-117214/
WORKDIR /opt/REQ-117214/

ENV LOG_LEVEL="INFO"
ENV MQTT_TOPIC_ID="b996957a-921d-46a3-b384-48ad106f75f7"
ENV MQTT_HOSTNAME="test.mosquitto.org"
ENV MQTT_PORT=1883

ENTRYPOINT ["python", "main.py"]
