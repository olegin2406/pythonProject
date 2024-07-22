from unittest.mock import patch, mock_open
from src.utils import get_transactions_json


@patch("os.path.exists")
def test_get_transactions_file_not_exists(mock_os_path_exists):
    """
    Мок метод os.path.exists
    Проверяет, что если файл не существует, возвращается пустой список.
    """
    mock_os_path_exists.return_value = False  # задаём фальшивому .exists что он возвращает False
    assert get_transactions_json("operations.json") == []  # в таком случае функция должна вернуть пустой список


# @patch('os.path.exists')
# def test_get_transactions_valid_json(mock_os_path_exists):
#     """
#     Мок метод os.path.exists и функцию open()
#     Проверяет, что если файл существует и содержит валидный JSON, возвращается список словарей с данными об операциях.
#     """
#     mock_os_path_exists.return_value = True  # задаём фальшивому .exists что он возвращает True
#
#     # тут вызываем встроенную в unittest функцию mock_open - она вернёт то же, что и обычная open(), но
#     # с фиксированным содержимым, которое мы задаём в read_data=
#     m = mock_open(read_data='[{"amount": "100", "currency": "RUB"}, {"amount": "200", "currency": "USD"}]')
#     # мокаем встроенную функцию open() и передаём прошлый объект, таким образом добиваемся того, что вся функция
#     # работает со значениями в read_data
#     with patch('builtins.open', m) as mocked_open:
#         # в контексте мок объекта open вызываем тестируемую функцию. json.dump уже мокать не нужно, так как
#         # она уже будет работать с read_data
#         assert get_transactions('operations.json') == [
#             {"amount": "100", "currency": "RUB"}, {"amount": "200", "currency": "USD"}
#         ]
#         # проверяем что мок функция open() была вызвана с нужными параметрами и не была вызвана реальная
#         mocked_open.assert_called_with('operations.json', 'r', encoding='utf-8')


@patch("os.path.exists")
@patch("json.load")
def test_get_transactions_valid_json(mocked_load, mock_os_path_exists):
    """
    Мок метод os.path.exists и функцию open()
    Проверяет, что если файл существует и содержит валидный JSON, возвращается список словарей с данными об операциях.
    """
    mock_os_path_exists.return_value = True  # задаём фальшивому .exists что он возвращает True

    # тут вызываем встроенную в unittest функцию mock_open - она вернёт то же, что и обычная open(), но
    # с фиксированным содержимым, которое мы задаём в read_data=
    m = mock_open()
    # мокаем встроенную функцию open() и передаём прошлый объект, таким образом добиваемся того, что вся функция
    # работает со значениями в read_data
    with patch("builtins.open", m) as mocked_open:
        # в контексте мок объекта open вызываем тестируемую функцию. json.dump уже мокать не нужно, так как
        # она уже будет работать с read_data
        mocked_load.return_value = [{"amount": "100", "currency": "RUB"}, {"amount": "200", "currency": "USD"}]
        assert get_transactions_json("operations.json") == [
            {"amount": "100", "currency": "RUB"},
            {"amount": "200", "currency": "USD"},
        ]
        # проверяем что мок функция open() была вызвана с нужными параметрами и не была вызвана реальная
        mocked_open.assert_called_with("operations.json", "r", encoding="utf-8")


@patch("os.path.exists")
def test_get_transactions_invalid_json(mock_os_path_exists):
    """
    Логика та же, что и в прошлом тесте, только меняются мок-данные на невалидные
    """
    mock_os_path_exists.return_value = True
    m = mock_open(read_data='{"amount": "200", "currency": "USD"}')
    with patch("builtins.open", m) as mocked_open:
        assert (
            get_transactions_json("operations.json") == []
        )  # если в файле не список, функция должна вернуть пустой список
        mocked_open.assert_called_with("operations.json", "r", encoding="utf-8")


def test_get_transactions_file_not_json():
    # тут вызываем встроенную в unittest функцию mock_open - она вернёт то же, что и обычная open(), но
    # с фиксированным содержимым, которое мы задаём в read_data=
    m = mock_open(read_data="not_json_data")
    assert get_transactions_json("operations.json") == []  # если ошибка, функция должна вернуть пустой список
