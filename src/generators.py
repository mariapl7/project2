def filter_by_currency(transactions: list[dict], currency: str) -> list:
    """Функция возвращает итератор, который поочередно выдает транзакции"""
    if len(transactions) > 0:
        filtered_transactions = filter(
            lambda x: x.get("operationAmount").get("currency").get("code") == currency, transactions)
        return filtered_transactions
    else:
        return list('Список пустой!')


def transaction_descriptions(transactions: list):
    """Функция возвращает описание каждой операции поочереди"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop):
    """Функция генерирует номера карт в заданном диапазоне"""
    for number in range(start, stop + 1):
        number_str = f"{number:016}"
        formated_number = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield formated_number
