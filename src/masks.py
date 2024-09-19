def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера банковской карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return None


def get_mask_account(bank_account: str) -> str | None:
    """Функция маскировки номера банковского счета"""
    if bank_account.isdigit() and len(bank_account) == 20:
        return "**" + bank_account[-4:]
    else:
        return None


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("606361"))
