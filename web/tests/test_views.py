from django.test import TestCase


class IndexViewTestCase(TestCase):
    def test_uses_index_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'index.html')
