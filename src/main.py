import json
import csv
import pandas as pd
from src.utils import load_transactions_from_json
from src.read_financial_transactions import read_financial_transactions_csv
from src.read_financial_transactions import read_financial_transactions_excel
from src.processing import filter_by_state


def read_transactions_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_transactions_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def read_transactions_from_xlsx(file_path):
    return pd.read_excel(file_path).to_dict(orient='records')


def filter_transactions(transactions, status):
    return [t for t in transactions if t.get('status', '').lower() == status.lower()]


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print(f"1. Получить информацию о транзакциях из: {load_transactions_from_json}")
    print(f"2. Получить информацию о транзакциях из: {read_financial_transactions_csv}")
    print(f"3. Получить информацию о транзакциях из: {read_financial_transactions_excel}")

    choice = input("Пользователь: ")

    if choice == '1':
        file_path = 'transactions.json'
        transactions = read_transactions_from_json(file_path)
    elif choice == '2':
        file_path = 'transactions.csv'
        transactions = read_transactions_from_csv(file_path)
    elif choice == '3':
        file_path = 'transactions.xlsx'
        transactions = read_transactions_from_xlsx(file_path)
    else:
        print("Неверный выбор.")
        return

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {filter_by_state}")
        status = input("Пользователь: ")

        if status.upper() not in ['filter_by_state']:
            print(f"Статус операции \"{status}\" недоступен.")
            continue

        print(f"Операции отфильтрованы по статусу \"{status}\".")
        filtered_transactions = filter_transactions(transactions, status)

        if not filtered_transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
            return

        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()

        if sort_choice == 'да':
            sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            if sort_order.startswith('у'):
                filtered_transactions.sort(
                    key=lambda t: t['sort_by_date'])  # предполагается, что дата в формате правильного типа
            else:
                filtered_transactions.sort(key=lambda t: t['sort_by_date'], reverse=True)

        currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()

        if currency_filter == 'да':
            filtered_transactions = [t for t in filtered_transactions if t['currency'] == 'руб.']

        description_filter = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()

        if description_filter == 'да':
            keyword = input("Введите слово для фильтрации в описании: ")
            filtered_transactions = [t for t in filtered_transactions if keyword.lower() in t['description'].lower()]

        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

        for transaction in filtered_transactions:
            print(f"{transaction['date']} {transaction['description']}")
            print(f"Счет {transaction['account']}")
            print(f"Сумма: {transaction['amount']} {transaction['currency']}")
            print()


if __name__ == "__main__":
    main()
