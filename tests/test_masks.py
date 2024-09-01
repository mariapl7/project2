import pytest
from src.masks import get_mask_card_number


@pytest.fixture
def card_number():
    return ["7000792289606361", "7000 79** **** 6361", " ", "700079228968"]


@pytest.mark.parametrize("card_number, expected", [("7000792289606361", "7000 79** **** 6361"),
                                                   ("", None),
                                                   ("700079228968", None),
                                                   ])
def test_get_mask_card_number(card_number: str, expected):
    """Функция тестирования для функции get_mask_card_number"""
    assert get_mask_card_number(card_number) == expected


import pytest
from src.masks import get_mask_account


@pytest.fixture
def bank_account():
    return [606361]


@pytest.mark.parametrize("bank_account, expected", [606361])
def test_get_mask_account(bank_account: str, expected):
    """Функция тестирования для функции get_mask_account"""
    assert get_mask_account(bank_account) == expected
