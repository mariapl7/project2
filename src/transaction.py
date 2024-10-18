import re
from collections import Counter


def filter_transactions(transactions, search_string):
    """ Фильтрует список словарей (банковских операций) по строке поиска """
    pattern = re.compile(search_string, re.IGNORECASE)  # Регулярное выражение с игнорированием регистра
    filtered_transactions = []
    for transaction in transactions:
        description = transaction.get('description', '')
        if pattern.search(description):  # Ищем совпадения
            filtered_transactions.append(transaction)
    return filtered_transactions


def count_operations_by_category(transactions):
    """Подсчитывает количество операций по категориям из списка транзакций."""
    categories = [transaction.get('category', '') for transaction in transactions]
    category_count = Counter(categories)
    return dict(category_count)
