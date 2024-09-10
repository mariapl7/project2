import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_number, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                  ("Счет 64686473678894779589", "Счет **9589"),
                                                  ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                  ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                                  ("", "Ошибка ввода данных"),
                                                  ])
def test_mask_account_card(card_number: str, expected) -> str:
    """Функция для маскировки карт и счетов"""
    assert mask_account_card(card_number) == expected


@pytest.mark.parametrize("data, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                            ("", "Неверно задана дата"),
                                            ("2024-03-11", "11.03.2024"),
                                            ("2024-030211554478411", "Неверно задана дата")
                                            ])
def test_get_date(data: str, expected) -> None:
    """Функция тестирования для функции get_date"""
    assert get_date(data) == expected
