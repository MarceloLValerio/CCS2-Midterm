FROM python:3.9-alpine3.16

COPY ./requirements.txt /requirements.txt
COPY ./src /src
WORKDIR /src
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev && \
    /py/bin/pip install -r /requirements.txt --use-pep517

ENV PATH="/py/bin:$PATH"
