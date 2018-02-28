from django.test import TestCase

from newsletter.forms import SubscriberForm


class SubscriberFormTestCase(TestCase):
    def test_email_is_required(self):
        serializer = SubscriberForm(data={})

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {'email': ['This field is required.']})

    def test_email_is_invalid(self):
        invalid_email = 'invalid-test-email'

        serializer = SubscriberForm(data={'email': invalid_email})

        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.errors, {'email': ['Enter a valid email address.']})
