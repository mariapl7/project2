import json


def get_transactions_before_json(path_to_file: str) -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_to_file) as file:
            try:
                transactions_data = json.loads(file)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data
