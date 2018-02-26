FROM python:3

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs

RUN npm install less -g

ENV PYTHONUNBUFFERED 1

ENV MAILCHIMP_API_KEY ${MAILCHIMP_API_KEY}
ENV MAILCHIMP_USERNAME ${MAILCHIMP_USERNAME}
ENV MAILCHIMP_NEWSLETTER_LIST_ID ${MAILCHIMP_NEWSLETTER_LIST_ID}

COPY . ./

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput