import unittest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    @patch('requests.get')
    def test_usd_to_rub(self, mock_get):
        # Настройка мока для успешного ответа с курсом USD
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'rates': {'USD': 75.0, 'EUR': 90.0}}
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        expected_result = 100 * 75.0
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_eur_to_rub(self, mock_get):
        # Настройка мока для успешного ответа с курсом EUR
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'rates': {'USD': 75.0, 'EUR': 90.0}}
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'EUR'}
        result = convert_to_rub(transaction)
        expected_result = 100 * 90.0
        self.assertEqual(result, expected_result)

    def test_rub(self):
        # Тестирование транзакции уже в RUB
        transaction = {'amount': 1000, 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 1000.0)

    def test_unsupported_currency(self):
        # Тестирование неподдерживаемой валюты
        transaction = {'amount': 100, 'currency': 'JPY'}
        result = convert_to_rub(transaction)
        self.assertIsNone(result)

    @patch('requests.get')
    def test_api_error(self, mock_get):
        # Настройка мока для неуспешного ответа API
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertIsNone(result)
