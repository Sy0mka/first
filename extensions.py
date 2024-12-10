import requests
import json
from config import keys

# Создаем класс исключения APIException
class APIException(Exception):
    pass

# Класс Converter с методом для получения иконки погоды
class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        if amount <= 0:
            raise APIException(f'Количество должно быть больше нуля')

        # Отправка запроса к API
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        result = json.loads(response.content)

        price = result[base_ticker]

        return price * amount