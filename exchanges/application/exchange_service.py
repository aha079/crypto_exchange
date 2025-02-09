from decimal import Decimal
import uuid
from datetime import datetime
from exchanges.domain.models import ExchangeTransaction
from exchanges.infrastructure.exchange_api import ExternalExchange

class ExchangeService:

    def __init__(self, exchange_api: ExternalExchange):
        self.exchange_api = exchange_api
        self.pending_orders = []  
        self.MIN_PURCHASE_AMOUNT = Decimal("10.0")  

    def add_order(self, currency: str, amount: Decimal) -> ExchangeTransaction:
        transaction = ExchangeTransaction(
            id=uuid.uuid4(),
            currency=currency,
            amount=amount,
            exchange_name="External Exchange",
            status="PENDING",
            created_at=datetime.now()
        )

        self.pending_orders.append(transaction)
        self.process_orders()  

        return transaction

    def process_orders(self):
        total_amount = sum(order.amount for order in self.pending_orders)

        if total_amount >= self.MIN_PURCHASE_AMOUNT:
            self.execute_aggregated_purchase()

    def execute_aggregated_purchase(self):
        total_amount = sum(order.amount for order in self.pending_orders)
        currency = self.pending_orders[0].currency if self.pending_orders else "UNKNOWN"

        success = self.exchange_api.buy_currency(currency, total_amount)

        for order in self.pending_orders:
            if success:
                order.mark_completed()
            else:
                order.mark_failed()

        self.pending_orders = [] 