import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [("7000792289606361", "7000 79** **** 6361"),
                                                   (" ", None),
                                                   ("700079228968", None),
                                                   ],)
def test_get_mask_card_number(card_number: str, expected):
    """Функция тестирования для функции get_mask_card_number"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("bank_account, expected", [("73654108430135874305", "**4305"),
                                                    ("73654", None),
                                                    ("", None)
                                                    ])


def test_get_mask_account(bank_account: str, expected) -> str:
    """Функция тестирования для функции get_mask_account"""
    assert get_mask_account(bank_account) == expected
