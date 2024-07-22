import json
import logging
import os
from typing import Dict, List


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")


def get_transactions_json(path: str) -> List[Dict]:
    """Возвращает список словарей, содержащих данные об транзакциях"""
    if not os.path.exists(path):
        logger.error("Файл пустой")
        return []

    try:
        logger.info("Получаем данные о транзакциях в формате JSON")
        with open(path, "r", encoding="utf-8") as file:
            transaction = json.load(file)

    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка в файле формата JSON: {ex}")
        return []

    if not isinstance(transaction, list):
        logger.error("Некорректный тип данных в файле формата JSON")
        return []

    return transaction


if __name__ == "__main__":
    file_path = "../data/operations.json"
    print(get_transactions_json(file_path))
