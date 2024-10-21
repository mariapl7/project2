# info_state = [
#              {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#              ]
#

# def filter_by_state(info_list, state="EXECUTED"):
#     for i in info_list:
#         print(f'Словарь: {i}')
#         print(f'ключ: {i.get('state')}')


def filter_by_state(info_list: list[dict], state="EXECUTED") -> list[dict]:
    """Функция возвращается новый список, по значению 'state'"""
    result = []
    for i in info_list:
        if i.get("state") == state:
            result.append(i)
    return result


def sort_by_date(date_list: list[dict], sort_reverse: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(date_list, key=lambda x: x["date"], reverse=sort_reverse)
    return sorted_list
