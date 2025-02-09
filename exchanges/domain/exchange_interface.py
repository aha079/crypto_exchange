from abc import ABC, abstractmethod
from decimal import Decimal

class ExchangeInterface(ABC):
	@abstractmethod
	def buy_currency(self, currency: str, amount: Decimal) -> bool:
		pass