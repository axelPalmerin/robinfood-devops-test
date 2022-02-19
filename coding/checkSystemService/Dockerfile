FROM python:3.8-slim-buster
LABEL maintainer "eric.gnome@gmail.com"

ADD . /robinfood-devops-test/coding/checkSystemService
WORKDIR /checkSystemService

# Install pip-tools for manage third-party package dependencies.
RUN pip install -U pip pip-tools && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt

# For rebuild the container for installing new libraries with pip-tool.
# $ docker run -rm <CONTAINER> pip-compile requirements.in

ENTRYPOINT ['python3', '-u', 'main.py']
