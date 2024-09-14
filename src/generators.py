def filter_by_currency(transactions: list[dict], currency: str) -> list:
    """Функция возвращает итератор, который поочередно выдает транзакции"""
    if len(transactions) > 0:
        filtered_transactions = filter(
            lambda x: x.get("operationAmount").get("currency").get("code") == currency, transactions)
        return filtered_transactions
    else:
        return list('Список пустой!')


usd_transactions: list = filter_by_currency([], "RUB")
for _ in range(2):
    print(next(usd_transactions))


transaction_descriptions = [x for my_list in range(5) for x in [my_list, my_list] if my_list % 2 == 0]
# возвращает описание каждоц операции поочереди


card_number_generator = [x for card_number in range(10) for x in [card_number, card_number] if card_number % 2 == 0]
# сгенерирует номера карт в заданном диапазоне
