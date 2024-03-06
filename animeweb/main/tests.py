from django.test import TestCase

# Create your tests here.

class TestMain(TestCase):
    def test_index(self):  # Проверка доступности главной страницы
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)