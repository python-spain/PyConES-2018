from unittest.mock import call, patch

from django import test
from django.conf import settings

from newsletter.utils import SubscribeMail


class SubscribeMailTestCase(test.TestCase):
    @patch('newsletter.utils.MailChimp')
    def test_creates_member_to_newsletter_list(self, mock_mailchimp):
        expected_email = 'test@example.com'

        SubscribeMail.create(expected_email)

        self.assertEqual(mock_mailchimp.call_count, 1)
        self.assertEqual(mock_mailchimp.call_args, call(settings.MAILCHIMP_API_KEY, settings.MAILCHIMP_USERNAME))
        mock_mailchimp_create = mock_mailchimp.return_value.lists.members.create
        expected_payload = {'email_address': expected_email, 'status': 'subscribed'}
        self.assertEqual(mock_mailchimp_create.call_count, 1)
        self.assertEqual(mock_mailchimp_create.call_args, call(settings.MAILCHIMP_NEWSLETTER_LIST_ID, expected_payload))
