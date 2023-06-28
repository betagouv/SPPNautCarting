FROM node:18-alpine AS node_builder

ENV http_proxy=http://proxy.shom.fr:3128
ENV https_proxy=http://proxy.shom.fr:3128

WORKDIR /app
COPY package.json /app
COPY package-lock.json /app

RUN npm ci

COPY ./static /app/static
COPY ./templates /app/templates
COPY ./tailwind.config.js /app
COPY ./.postcssrc /app
#COPY . /app

RUN npm run build

FROM python:3.10-slim-bullseye

ENV http_proxy=http://proxy.shom.fr:3128
ENV https_proxy=http://proxy.shom.fr:3128

RUN apt-get -y update
# Install depedences for psycopg2
RUN apt-get -y install libpq-dev gcc
# Install depedences for gdal
RUN apt-get -y install binutils libproj-dev gdal-bin

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /app

RUN mkdir -p /app/static/compiled
COPY --from=node_builder /app/static/compiled /app/static/compiled

RUN chown -R 1000:1000 "/app"

EXPOSE 8000

USER 1000:1000

ENTRYPOINT ["gunicorn", "--bind", ":8000", "core.wsgi:application"]
