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


def count_operations_by_category(transactions, categories):
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        category = transaction.get('category', '')
        if category in category_count:
            category_count[category] += 1
    return category_count


def categorize_transactions(transactions, search_term):
    category_count = {}

    for transaction in transactions:
        description = transaction.get('description', '').lower()

        if search_term.lower() in description:
            category_count[description] = category_count.get(description, 0) + 1
    return category_count


def count_description_occurrences(transactions, search_term):
    """ Подсчитывает количество упоминаний описаний, содержащих строку поиска """
    category_count = {}
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        if search_term.lower() in description:
            category_count[description] = category_count.get(description, 0) + 1
    return category_count
