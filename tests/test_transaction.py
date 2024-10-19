import re
from unittest.mock import patch, MagicMock
from src.transaction import filter_transactions, count_operations_by_category


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
