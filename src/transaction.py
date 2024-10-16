import re


def filter_transactions(transactions, search_string):
    """
    Фильтрует список словарей (банковских операций) по строке поиска.

    :param transactions: Список словарей с данными о банковских операциях
    :param search_string: Строка для поиска в описаниях операций
    :return: Список словарей, у которых в описании есть заданная строка
    """
    pattern = re.compile(search_string, re.IGNORECASE)  # Регулярное выражение с игнорированием регистра
    filtered_transactions = []
    for transaction in transactions:
        description = transaction.get('description', '')
        if pattern.search(description):  # Ищем совпадения
            filtered_transactions.append(transaction)
    return filtered_transactions


def categorize_transactions(transactions, search_term):
    category_count = {}

    for transaction in transactions:
        description = transaction.get('description', '').lower()

        if search_term.lower() in description:
            category_count[description] = category_count.get(description, 0) + 1
    return category_count
