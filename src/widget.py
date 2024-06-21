from datetime import datetime


def mask_account_card(string: str) -> str:
    """Функция для маскировки карты и счета"""
    if "Счет" in string:
        return string[:5] + "**" + string[-4:]
    else:
        return string[:-16] + string[-16:-12] + " " + string[-12:-10] + "** **** " + string[-4:]


def get_data(date: str) -> str:
    """Функция которая возвращает дату"""
    d = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return d.strftime("%d.%m.%Y")


# if __name__ == "__main__":
#     print(mask_account_card('Maestro 1596837868705199'))
#     print(mask_account_card('Счет 64686473678894779589'))
#     print(get_data("2018-07-11T02:26:18.671407"))
