import pytest
from src.widget import get_date


@pytest.fixture()
def data():
    return ["2024-03-11T02:26:18.671407"]


@pytest.mark.parametrize("data, expected", ["2024-03-11T02:26:18.671407"])
def test_get_date(data: str, expected):
    """Функция тестирования для функции get_date"""
    assert test_get_date(data) == expected
