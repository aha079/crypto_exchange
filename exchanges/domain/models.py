from decimal import Decimal
import uuid
from datetime import datetime

class ExchangeTransaction:
    
    def __init__(self, id: uuid.UUID, currency: str, amount: Decimal, exchange_name: str, status: str, created_at: datetime):
        self.id = id
        self.currency = currency
        self.amount = amount
        self.exchange_name = exchange_name
        self.status = status  # "PENDING", "COMPLETED", "FAILED"
        self.created_at = created_at

    def mark_completed(self):
        self.status = "COMPLETED"

    def mark_failed(self):
        self.status = "FAILED"