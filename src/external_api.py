from typing import Any
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def transaction_amount(transactions: Any) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transactions["operationAmount"]["amount"]
    currency = transactions["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        url = f"https://apilayer.com/exchangerates_data-api/convers?from={currency}&amount={amount}"
        headers = {
            "apikey": "API_KEY"
        }
        responce = requests.get(url, headers=headers)
        # status_code = responce.status_code
        # print(f"Статус кода: {status_code}")
        return responce.json()
