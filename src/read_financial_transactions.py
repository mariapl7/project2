import pandas as pd


def read_financial_transactions_csv(file_path):
    """Считывает финансовые операции из CSV файла."""
    try:
        # Считываем данные из CSV
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Файл пуст: {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Ошибка парсинга файла: {file_path}")
        return None


def read_financial_transactions_xlsx(file_path):
    """Считывает финансовые операции из XLSX файла."""
    try:
        # Считываем данные из XLSX
        data = pd.read_excel(file_path, engine='openpyxl')
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return None
    except ValueError:
        print(f"Ошибка значения в файле: {file_path}")
        return None
