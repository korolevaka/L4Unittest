import unittest
from app import app

class TestHome(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_request(self):
        """Тестирование GET запроса."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Now expecting 200
        self.assertIn('Рассчет объема объекта'.encode('utf-8'), response.data)

    def test_post_request_with_valid_data(self):
        """Тестирование POST запроса с корректными данными."""
        data = {
            'length': '5',
            'width': '5',
            'depth': '5'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Объем объекта: 125'.encode('utf-8'), response.data)  # Проверяем результат с точностью 2 знака

    def test_post_request_with_precision(self):
        """Тестирование POST запроса с заданной точностью."""
        data = {
            'length': '10.5',
            'width': '5.2',
            'depth': '2.1',
            'precision': '3'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Объем объекта: 114.66'.encode('utf-8'), response.data)  # Проверяем результат с точностью 3 знака

    def test_post_request_with_zero_values(self):
        """Тестирование POST запроса с нулевыми значениями."""
        data = {
            'length': '0',
            'width': '5',
            'depth': '2'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Объем объекта:'.encode('utf-8'), response.data)  # Проверяем, что результат не отображается


    def test_404_error(self):
        """Тестирование 404 ошибки."""
        response = self.client.get('/nonexistent-route')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
