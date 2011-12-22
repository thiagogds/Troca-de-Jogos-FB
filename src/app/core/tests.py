from lib.testtools import TestCase


class TestHome(TestCase):
    def test_correct_reponse(self):
        response = self.client.get('core:home')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
