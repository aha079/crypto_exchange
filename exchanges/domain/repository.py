from abc import ABC, abstractmethod
from .models import ExchangeTransaction
from typing import Optional
import uuid

class ExchangeTransactionRepository(ABC):
	
	@abstractmethod
	def save(self, exchangeTransaction: ExchangeTransaction) -> None:
		pass

	@abstractmethod
	def find_by_id(self, exchange_transaction_id: uuid.UUID) -> Optional[ExchangeTransaction]:
		pass