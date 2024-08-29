info_state = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
def filter_by_state(list_dictionary, state_id='EXECUTED') -> str:
    """Функция возвращает новый список словарей содержащий только те словари, у которых ключ
state"""
    filter_state = []
    for key in list_dictionary:
        if key.get('state') == state_id:
            filter_state.append(key)
    return filter_state

print(filter_by_state(info_state))

def sort_by_date(list_dictionary: list[str], reverse=True) -> str:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list_dictionary = sorted(list_dictionary, key=lambda info_state: info_state['date'])
    return sorted_list_dictionary

print(sort_by_date(info_state))