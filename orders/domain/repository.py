from abc import ABC, abstractmethod
from .models import Order
from typing import Optional
import uuid

class OrderRepository(ABC):
	
	@abstractmethod
	def save(self, order: Order) -> None:
		pass

	@abstractmethod
	def find_by_id(self, order_id: uuid.UUID) -> Optional[Order]:
		pass