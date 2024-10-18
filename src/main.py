from src.utils import load_transactions_from_json
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.transaction import filter_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Загрузка данных из файла...")

    # Загрузка данных с использованием функций
    file_path = 'transactions.json'
    transactions = load_transactions_from_json(file_path)

    # Фильтрация по статусу
    status = 'EXECUTED'  # Замените на нужный статус
    filtered_transactions = filter_by_state(transactions, status)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации по статусу.")
        return

    # Сортировка по дате
    sorted_transactions = sort_by_date(filtered_transactions)

    # Фильтрация по валюте
    sorted_currency_transactions = filter_by_currency(sorted_transactions, 'руб.')

    # Фильтрация по слову в описании
    keyword = 'покупка'  # Замените на нужное слово
    final_transactions = filter_transactions(sorted_currency_transactions, keyword)

    if not final_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации по описанию.")
        return

    # Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(final_transactions)}\n")

    for transaction in final_transactions:
        print(f"{transaction['date']} {transaction['description']}")
        print(f"Счет: {transaction['account']}")
        print(f"Сумма: {transaction['amount']} {transaction['currency']}")
        print()
