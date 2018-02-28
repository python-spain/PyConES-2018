from unittest.mock import call, patch

from django import test


class SubscribersAPIViewTestCase(test.TestCase):

    @patch('newsletter.views.SubscribeMail')
    def test_post_returns_201_if_send_subscribe_mail_ok(self, mock_subscribe_mail):
        expected_email = 'test@example.com'

        response = self.client.post('/newsletter/subscribers/', data={'email': expected_email})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(mock_subscribe_mail.create.call_count, 1)
        self.assertEqual(mock_subscribe_mail.create.call_args, call(expected_email))

    @patch('newsletter.views.SubscribeMail')
    def test_post_returns_500_if_send_subscribe_mail_failed(self, mock_subscribe_mail):
        expected_email = 'test@example.com'
        mock_subscribe_mail.create.side_effect = Exception()

        response = self.client.post('/newsletter/subscribers/', data={'email': expected_email})

        self.assertEqual(response.status_code, 500)

    def test_post_returns_400_if_email_is_empty(self):
        response = self.client.post('/newsletter/subscribers/', data={'email': ''})

        self.assertEqual(response.status_code, 400)

    def test_post_returns_400_if_email_is_invalid(self):
        invalid_email = 'invalid-test-email'

        response = self.client.post('/newsletter/subscribers/', data={'email': invalid_email})

        self.assertEqual(response.status_code, 400)
