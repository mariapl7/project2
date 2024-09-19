import pytest


@pytest.fixture
def card_number():
    return ["7000792289606361", "7000 79** **** 6361", " ", "700079228968"]


@pytest.fixture
def bank_account():
    return [("7000792289606361", "7000 70** **** 6361"),
            (" ", None),
            ("700079228968", None),
            ]


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

@pytest.fixture
def transactions_list():
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]