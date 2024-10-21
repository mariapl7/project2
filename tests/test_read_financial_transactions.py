import unittest
from unittest.mock import patch
import pandas as pd
from src.read_financial_transactions import read_financial_transactions_csv, read_financial_transactions_excel


class TestFinancialOperationsLoading(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_read_financial_transactions_csv_success(mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02'],
            'amount': [100, -50],
            'category': ['Groceries', 'Utilities']
        })
        transactions = read_financial_transactions_csv('dummy.csv')
        assert transactions is not None
        assert len(transactions) == 2
        assert transactions[0]['amount'] == 100
        assert transactions[1]['category'] == 'Utilities'

    @patch('pandas.read_excel')
    def test_read_financial_transactions_excel_success(mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02'],
            'amount': [100, -50],
            'category': ['Groceries', 'Utilities']
        })
        transactions = read_financial_transactions_excel('dummy.xlsx')
        assert transactions is not None
        assert len(transactions) == 2
        assert transactions[0]['amount'] == 100
        assert transactions[1]['category'] == 'Utilities'
