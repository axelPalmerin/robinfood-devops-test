FROM python:3.8-slim-buster
LABEL maintainer "eric.gnome@gmail.com"

RUN mkdir /app
ADD . /app
WORKDIR /app

# Install pip-tools for manage third-party package dependencies.
RUN pip install -U pip pip-tools && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt

# For rebuild the container for installing new libraries with pip-tool run:
# docker run -rm <CONTAINER> pip-compile requirements.in

ENTRYPOINT ['python', '-u', 'main.py']
