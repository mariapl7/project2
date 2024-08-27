def mask_account_card(card_number: str) -> list[str]:
    """Функция для маскировки карт и счетов"""
    if card_number == 16:
        mask_number = card_number.split()[-1]
        name_card = " ".join(card_number)
        mask_name_number = name_card + mask_number
        return mask_name_number
    elif card_number == 20:
        mask_number = mask_account_card(card_number.split()[-1])
        name_card = " ".join(card_number)
        mask_name_number = name_card + mask_number
        return mask_name_number

print(mask_account_card('Счет 73654108430135874305'))
print(mask_account_card('Maestro 7000792289606361'))
print(mask_account_card('Visa Platinum 7000792289606361'))


def get_date(data: str) -> str:
    """Функция преобразования даты формата "2018-07-11T02:26:18.671407" в формат "11.07.2018"""
    return f'{data[8:10]}.{data[5:7]}.{data[0:4]}'

print(get_date("2024-03-11T02:26:18.671407"))