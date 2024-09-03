import pytest


@pytest.fixture
def card_number():
    return ["7000792289606361", "7000 79** **** 6361", " ", "700079228968"]


@pytest.fixture
def bank_account():
    return [606361]


@pytest.fixture()
def data():
    return [("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("", "Неверно задана дата"),
            ("2024-03-11", "11.03.2024"),
            ("2024-030211554478411", "Неверно задана дата")
            ]


@pytest.fixture()
def list_info():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ]