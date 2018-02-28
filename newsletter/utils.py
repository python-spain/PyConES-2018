from django.conf import settings

from mailchimp3 import MailChimp


class SubscribeMail(object):

    @staticmethod
    def create(email):
        client = MailChimp(settings.MAILCHIMP_API_KEY, settings.MAILCHIMP_USERNAME)
        payload = {'email_address': email, 'status': 'subscribed'}
        client.lists.members.create(settings.MAILCHIMP_NEWSLETTER_LIST_ID, payload)
