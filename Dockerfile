# Python version can be changed, e.g.
FROM docker.io/python:3.11.3-slim-bullseye

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="An email plugin" \
      org.opencontainers.image.description="A ChRIS plugin for email"

ARG SRCDIR=/usr/local/src/mail
RUN mkdir -p ${SRCDIR}
WORKDIR ${SRCDIR}

COPY . .
RUN pip install "." \
    && cd / && rm -rf ${SRCDIR}
WORKDIR /

CMD ["mail"]
