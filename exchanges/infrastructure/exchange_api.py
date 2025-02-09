from exchanges.domain.exchange_interface import ExchangeInterface
from decimal import Decimal
import requests

class ExternalExchange(ExchangeInterface):
    def buy_currency(self, currency: str, amount: Decimal) -> bool:
        response = requests.post("https://api.example.com/buy", json={"currency": currency, "amount": str(amount)})
        return response.status_code == 200