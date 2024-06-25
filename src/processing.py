from typing import Any

original_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(inform_state: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция которая принимает на вход список словарей и значений для ключа
    state, и выдает новый список с заданным ключом"""

    list_state = []

    for key in inform_state:
        if key.get("state") == state_id:
            list_state.append(key)

    return list_state


def sort_by_date(inform_state: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция сортирующая по дате"""

    sorted_inform_state = sorted(inform_state, key=lambda inform_state: inform_state["date"], reverse=reverse_list)
    return sorted_inform_state


if __name__ == "__main__":
    print(filter_by_state(original_state))
    print(sort_by_date(original_state))
