import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    try:
        """Принимает на вход номер карты и возвращает ее маску."""
        logger.info("Маскируем номер карты")
        return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    except Exception as ex:
        logger.error(f'Произошла ошибка: {ex}')


def get_mask_account(account_number: str) -> str:
    try:
        """Принимает на вход номер счета и возвращает его маску."""
        logger.info("Маскируем номер счета")
        return "**" + account_number[-4:]
    except Exception as ex:
        logger.error(f'Произошла ошибка: {ex}')


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
