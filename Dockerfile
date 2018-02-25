FROM python:3

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs

RUN npm install less -g

ENV PYTHONUNBUFFERED 1

COPY . ./

RUN make install

RUN make migrate