FROM python:3.7

RUN pip3 install pipenv

ENV FLASK_APP microblog.py

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

# RUN pipenv shell
RUN set -ex && pipenv install --deploy --system

COPY . .

CMD flask run

EXPOSE 5000