import re
from unittest.mock import patch, MagicMock
from collections import Counter
from src.transaction import filter_transactions, categorize_transactions
from src.transaction import count_operations_by_category, count_description_occurrences


@patch('re.compile')
def test_filter_transactions(self, mock_compile):
    mock_pattern = MagicMock()
    mock_compile.return_value = mock_pattern
    mock_pattern.search.side_effect = [True, False, True, False]  # Эмуляция результатов поиска

    result = filter_transactions(self.transactions, 'Buy')
    expected = [
        {'description': 'Buy groceries', 'category': 'Food'},
        {'description': 'Buy a new phone', 'category': 'Electronics'}
    ]
    self.assertEqual(result, expected)
    mock_compile.assert_called_once_with('Buy', re.IGNORECASE)
    self.assertEqual(mock_pattern.search.call_count, 4)  # Проверяем, что search вызван 4 раза


def test_count_operations_by_category(self):
    result = count_operations_by_category(self.transactions, ['Food', 'Books'])
    expected = {'Food': 3, 'Books': 1}
    self.assertEqual(result, expected)


@patch('collections.Counter')
def test_categorize_transactions(self, mock_counter):
    mock_counter.return_value = Counter({'a new phone': 1, 'groceries': 1})
    result = categorize_transactions(self.transactions, 'buy')
    expected = {'buy groceries': 1, 'buy a new phone': 1}
    self.assertEqual(result, expected)
    mock_counter.assert_called_once()  # Проверяем, что Counter был вызван


@patch('re.compile')
def test_count_description_occurrences(self, mock_compile):
    mock_pattern = MagicMock()
    mock_compile.return_value = mock_pattern
    mock_pattern.search.side_effect = [True, False, True, False]  # Эмуляция результатов поиска

    result = count_description_occurrences(self.transactions, 'out')
    expected = {'dinner out': 1}
    self.assertEqual(result, expected)
    mock_compile.assert_called_once_with('out', re.IGNORECASE)
