from django.db import models

from mailchimp3 import MailChimp

from django.conf import settings


class Subscriber(models.Model):
    email = models.EmailField()

    def save(self, *_, **__):
        client = MailChimp(settings.MAILCHIMP_API_KEY, settings.MAILCHIMP_USERNAME)
        payload = {'email_address': self.email, 'status': 'subscribed'}
        client.lists.members.create(settings.MAILCHIMP_NEWSLETTER_LIST_ID, payload)
