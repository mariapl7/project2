import unittest
import json
from unittest.mock import patch
from src.utils import load_transactions_from_json


class TestLoadTransactionsFromJson(unittest.TestCase):

    @patch("builtins.open", read_data=json.dumps([
        {"amount": 100, "currency": "USD"},
        {"amount": 200, "currency": "EUR"},
    ]))
    @patch("pathlib.Path.is_file", return_value=True)
    def test_valid_json(self):
        transactions = load_transactions_from_json("valid_transactions.json")
        self.assertEqual(len(transactions), 2)  # Проверяем, что вернулся список из 2 элементов
        self.assertEqual(transactions[0]["currency"], "USD")  # Проверяем правильность данных

    @patch("builtins.open", read_data='')
    @patch("pathlib.Path.is_file", return_value=True)
    def test_empty_file(self):
        transactions = load_transactions_from_json("empty_file.json")
        self.assertEqual(transactions, [])  # Проверяем, что вернулся пустой список

    # Некорректные данные
    @patch("builtins.open", read_data='{"amount": 100, "currency": "USD"}')
    @patch("pathlib.Path.is_file", return_value=True)
    def test_invalid_json(self):
        transactions = load_transactions_from_json("invalid_file.json")
        self.assertEqual(transactions, [])  # Проверяем, что вернулся пустой список

    @patch("pathlib.Path.is_file", return_value=False)
    def test_non_existent_file(self):
        transactions = load_transactions_from_json("non_existent_file.json")
        self.assertEqual(transactions, [])  # Проверяем, что вернулся пустой список


if __name__ == '__main__':
    unittest.main()
