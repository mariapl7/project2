from typing import Any
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> Any:
    """Функция для маскировки карт и счетов"""
    card_number_mask = card_number.split()
    if len(card_number_mask) > 1 and len(card_number_mask[-1]) == 16:
        mask_number = get_mask_card_number(card_number_mask[-1])
        if mask_number is not None:
            card_number_mask[-1] = mask_number
            return " ".join(card_number_mask)
    elif len(card_number_mask) > 1 and len(card_number_mask[-1]) == 20:
        mask_number = get_mask_account(card_number_mask[-1])
        if mask_number is not None:
            card_number_mask[-1] = mask_number
            return " ".join(card_number_mask)
    else:
        return "Ошибка ввода данных"


def get_date(user_data: str) -> str:
    """Функция преобразования даты формата в формат "ДД.ММ.ГГГГ"""
    date_for_format = user_data[0:10].split("-")
    if len(user_data) >= 10 and len(date_for_format) == 3:
        return ".".join(date_for_format[::-1])
    else:
        return "Неверно задана дата"
