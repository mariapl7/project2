import unittest
from unittest.mock import patch
import pandas as pd
from src.read_financial_transactions import read_financial_transactions_csv, read_financial_transactions_xlsx


class TestFinancialOperationsLoading(unittest.TestCase):


    @patch('pandas.read_csv')
    def test_read_financial_transactions_csv_success(self, mock_read_csv):
        # Настройка mock для успешного чтения CSV
        mock_read_csv.return_value = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})
        data = read_financial_transactions_csv('transactions.csv')
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)


    @patch('pandas.read_csv')
    def test_read_financial_transactions_csv_file_not_found(self, mock_read_csv):
        # Настройка mock для ошибки FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError
        data = read_financial_transactions_csv('transactions.csv')
        self.assertIsNone(data)


    @patch('pandas.read_csv')
    def test_read_financial_transactions_csv_empty_file(self, mock_read_csv):
        # Настройка mock для ошибки EmptyDataError
        mock_read_csv.side_effect = pd.errors.EmptyDataError
        data = read_financial_transactions_csv('transactions.csv')
        self.assertIsNone(data)


    @patch('pandas.read_excel')
    def test_read_financial_transactions_xlsx_success(self, mock_read_excel):
        # Настройка mock для успешного чтения XLSX
        mock_read_excel.return_value = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})
        data = read_financial_transactions_xlsx('transactions_excel.xlsx')
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)


    @patch('pandas.read_excel')
    def test_read_financial_transactions_xlsx_file_not_found(self, mock_read_excel):
        # Настройка mock для ошибки FileNotFoundError
        mock_read_excel.side_effect = FileNotFoundError
        data = read_financial_transactions_xlsx('transactions_excel.xlsx')
        self.assertIsNone(data)


    @patch('pandas.read_excel')
    def test_read_financial_transactions_xlsx_value_error(self, mock_read_excel):
        # Настройка mock для ошибки ValueError
        mock_read_excel.side_effect = ValueError
        data = read_financial_transactions_xlsx('transactions_excel.xlsx')
        self.assertIsNone(data)
