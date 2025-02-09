from dataclasses import dataclass
from decimal import Decimal
import uuid
from datetime import datetime


@dataclass
class Order:
	id: uuid.UUID
	currency: str
	amount: Decimal
	created_at: datetime
	processed: bool = False


	def mark_as_processed(self):
		self.processed = True