import requests


def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction (dict): Словарь с полями 'amount' и 'currency'.

    Returns:
        float: Сумма транзакции в рублях. Если валюта не USD или EUR,
                возвращает сумму без изменений в рублях, если это уже рубли,
                или None в других случаях.
    """
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency == 'RUB':
        return float(amount)  # Если уже в рублях, просто возвращаем сумму

    # Получение курса валют
    api_key = 'API_КЛЮЧ'  # Замените на ваш API ключ
    url = f'https://api.apilayer.com/exchangerates_data/latest?base=RUB&symbols=USD,EUR'
    headers = {
        'apikey': api_key,
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        rates = response.json().get('rates', {})

        # Конвертация суммы в рубли
        if currency == 'USD':
            return float(amount) * rates.get('USD', 1)  # Если курс существующий, конвертируем
        elif currency == 'EUR':
            return float(amount) * rates.get('EUR', 1)  # Если курс существующий, конвертируем

    return None  # Если валюта не поддерживается или не удалось получить курс


transaction_usd = {'amount': 100, 'currency': 'USD'}
transaction_eur = {'amount': 150, 'currency': 'EUR'}
transaction_rub = {'amount': 1000, 'currency': 'RUB'}

print(convert_to_rub(transaction_usd))
print(convert_to_rub(transaction_eur))
print(convert_to_rub(transaction_rub))
