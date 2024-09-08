import pytest
from src.widget import get_date


@pytest.mark.parametrize("data, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                            ("", "Неверно задана дата"),
                                            ("2024-03-11", "11.03.2024"),
                                            ("2024-030211554478411", "Неверно задана дата")
                                            ])
def test_get_date(data: str, expected) -> str | None:
    """Функция тестирования для функции get_date"""
    assert test_get_date(data) == expected
