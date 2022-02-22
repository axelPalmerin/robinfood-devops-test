
# Dockerfile for run pytest Service

FROM alpine:3.14 AS builder

# ensures that the python output is sent straight to terminal
ENV PYTHONUNBUFFERED=1

# install the prerequisites
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# create a folder to hold the downloaded/built requirements
RUN mkdir -p /app

# copy in the requirements
COPY requirements.txt /app/requirements.txt

# install the requirenents to that folder
RUN pip3 install -r /app/requirements.txt --target /app

# test runner
FROM alpine:3.14

# install the prerequisites only python
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

# copy the requirements from the builder stage
COPY --from=builder /app /app

# copy in the code to be tested
COPY . /app

# change to the appropriate folder
WORKDIR /app

CMD python3 -m pytest -v main.py
