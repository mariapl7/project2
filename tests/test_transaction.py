import pytest

from unittest.mock import patch
from src.transaction import filter_transactions, categorize_transactions


@patch('transaction_filter.filter_transactions')
def test_filter_transactions(mock_filter_transactions):
    # Предположим, что mock возвращает список транзакций
    mock_filter_transactions.return_value = [
        {'id': 1, 'description': 'Оплата за газ', 'amount': -300},
        {'id': 3, 'description': 'Оплата интернета', 'amount': -500}
    ]

    transactions = [
        {'id': 1, 'description': 'Оплата за газ', 'amount': -300},
        {'id': 2, 'description': 'Перевод зарплаты', 'amount': 1000},
        {'id': 3, 'description': 'Оплата интернета', 'amount': -500},
        {'id': 4, 'description': 'Купон на скидку', 'amount': 50},
    ]

    result = filter_transactions(transactions, 'оплата')

    assert len(result) == 2  # Проверяем, что нашли 2 совпадения
    assert result[0]['id'] in [1, 3]
    assert result[1]['id'] in [1, 3]
    assert result[0]['id'] != result[1]['id']  # Убедитесь, что они разные


@patch('transaction_filter.categorize_transactions')
def test_categorize_transactions(mock_categorize_transactions):
    # Установка возврата замокированной функции
    mock_categorize_transactions.side_effect = [
        {'оплата за газ': 1, 'оплата интернета': 1},  # ожидание для 'оплата'
        {'перевод зарплаты': 1},                      # ожидание для 'перевод'
        {}                                             # ожидание для 'неизвестная категория'
    ]

    transactions = [
        {'id': 1, 'description': 'Оплата за газ', 'amount': -300},
        {'id': 2, 'description': 'Перевод зарплаты', 'amount': 1000},
        {'id': 3, 'description': 'Оплата интернета', 'amount': -500},
        {'id': 4, 'description': 'Купон на скидку', 'amount': 50},
    ]

    result1 = categorize_transactions(transactions, 'оплата')
    assert result1 == {'оплата за газ': 1, 'оплата интернета': 1}

    result2 = categorize_transactions(transactions, 'перевод')
    assert result2 == {'перевод зарплаты': 1}

    result3 = categorize_transactions(transactions, 'неизвестная категория')
    assert result3 == {}
