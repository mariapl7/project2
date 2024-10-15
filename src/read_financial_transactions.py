import pandas as pd


def read_financial_transactions_csv(file_path):
    """Считывает финансовые операции из CSV файла и возвращает их в виде списка словарей."""
    try:
        # Считываем данные из CSV
        data = pd.read_csv(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = data.to_dict(orient='records')  # 'records' создает список словарей
        return transactions
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Файл пуст: {file_path}")
        return []
    except pd.errors.ParserError:
        print(f"Ошибка парсинга файла: {file_path}")
        return None


def read_financial_transactions_excel(file_path):
    """Считывает финансовые операции из Excel файла и возвращает их в виде списка словарей."""
    try:
        # Считываем данные из Excel
        data = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = data.to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Файл пуст: {file_path}")
        return []
    except ValueError:
        print(f"Ошибка чтения файла Excel: {file_path}")
        return None
