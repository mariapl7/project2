from unittest.mock import Mock
from unittest.mock import patch


@patch('requests.get')
def test_transaction_amount(mock_get):
    """Тестирование транзакции"""
    mock_get.return_value.json.return_value = Mock("currency")
    assert transaction_amount(transactions) == 'RUB'
    mock_get.assert_called_once_with(transactions, 'RUB')