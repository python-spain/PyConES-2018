FROM python:3

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs gettext

RUN npm install sass -g

ENV PYTHONUNBUFFERED 1

COPY . ./

RUN pip install -r requirements.txt