import json
import os

def load_transactions_from_json(file_path):
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        return []  # Файл не найден, возвращаем пустой список

    # Читаем данные из файла
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)  # Загружаем данные из JSON-файла
        except json.JSONDecodeError:
            return []  # Если не удалось декодировать JSON, возвращаем пустой список

    # Проверяем, является ли загруженные данные списком
    if isinstance(data, list):
        return data  # Возвращаем список словарей
    else:
        return []  # Если данные не являются списком, возвращаем пустой список


transactions = load_transactions_from_json('transactions.json')
print(transactions)