from src.utils import load_transactions_from_json
from src.read_financial_transactions import read_financial_transactions_csv
from src.read_financial_transactions import read_financial_transactions_excel
from src.processing import filter_by_state, sort_by_date


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    """Отвечает за основную логику проекта с пользователем,
        связывает функциональности между собой."""

    print(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    choice = input("Введите номер пункта: ")

    if choice == '1':
        file_path = '../data/operations.json'
        print("Для обработки выбран JSON-файл.")
        transactions_file = load_transactions_from_json(file_path)
    elif choice == '2':
        file_path = '../data/transactions.csv'
        print("Для обработки выбран CSV-файл.")
        transactions_file = read_financial_transactions_csv(file_path)
    elif choice == '3':
        file_path = '../data/transactions_excel.xlsx'
        print("Для обработки выбран XLSX-файл.")
        transactions_file = read_financial_transactions_excel(file_path)
    else:
        print("Неверный выбор.")
        return

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")
        status = input("Введите статус для фильтрации: ").upper()

        if status != "EXECUTED" and status != "CANCELED" and status != "PENDING":
            print(f"Статус операции {status} недоступен.")
            continue
        else:
            break

    print(f"Операции отфильтрованы по статусу {status}")
    filtered_transactions = filter_by_state(transactions_file, status)

    print("Отсортировать операции по дате? Да/Нет")
    sort_choice = input("Введите да или нет: ").lower()

    if sort_choice == 'да':
        print("Отсортировать по возрастанию или по убыванию?")
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if sort_order == "в порядке убывания":
            reverse = True
            filtered_transactions = sort_by_date(transactions_file, reverse)
        elif sort_order == "в порядке возрастания":
            reverse = False
            filtered_transactions = sort_by_date(transactions_file, reverse)
        else:
            print("Введен некорректный ответ.")
            return
    else:
        print("Введен некорректный ответ.")
        return

    print("Выводить только рублевые транзакции? Да/Нет")
    currency_filter = input("Введите да или нет: ").lower()
    if currency_filter == "да":
        rub_trans = []
        for trans in filtered_transactions:
            if currency_filter == "1" or currency_filter == "2":
                if trans["operationAmount"]["currency"]["code"] == "RUB":
                    rub_trans.append(trans)
            else:
                if trans["currency_code"] == "RUB":
                    rub_trans.append(trans)
    elif currency_filter == "нет":
        rub_trans = []
        for trans in filtered_transactions:
            rub_trans.append(trans)
        else:
            print("Введен некорректный ответ.")
            return

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_by_word = input("Введите да или нет: ").lower()
    if filter_by_word == "да":
        filter_by_word_yes = input("Введите слово для фильтрации: ")
        trans_word = []
        for trans in filtered_transactions:
            if filter_by_word_yes in trans["description"]:
                trans_word.append(trans)
    elif filter_by_word == "нет":
        trans_word = []
        for trans in filtered_transactions:
            trans_word.append(trans)
    else:
        print("Введен некорректный ответ.")
        return
    if (len(trans_word)) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(trans_word)}\n")

    for transaction in filtered_transactions:
        print(f"{transaction['date']} {transaction['description']}")
        print(f"Счет: {transaction['account']}")
        print(f"Сумма: {transaction['amount']} {transaction['currency']}")
        print()


if __name__ == "__main__":
    main()
