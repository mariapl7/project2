import re
from collections import Counter
from typing import Any


def filter_transactions(transactions: list[dict], search_string: list[str]) -> list[str, int]:
    """ Фильтрует список словарей (банковских операций) по строке поиска """
    pattern = re.compile(search_string, re.IGNORECASE)  # Регулярное выражение с игнорированием регистра
    filtered_transactions = []
    for transaction in transactions:
        description: Any = transaction.get('description', '')
        if pattern.search(description):  # Ищем совпадения
            filtered_transactions.append(transaction)
    return dict(filtered_transactions)


def count_operations_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """Подсчитывает количество операций по категориям из списка транзакций."""
    result = []
    for transaction in transactions:
        description = transaction.get('description', '')
        if description in categories:
            result.append(description)
    category_count = Counter(categories)
    return dict(category_count)


if __name__ == '__main__':
    from src.utils import load_transactions_from_json
    transactions = load_transactions_from_json('./data/operations.json')
    categories = count_operations_by_category(transactions, ["Перевод организации", "Открытие вклада"])
    print(categories)
