from decimal import Decimal
import uuid
from datetime import datetime
from orders.domain.models import Order
from orders.infrastructure.repository_impl import DjangoOrderRepository
from exchanges.application.exchange_service import ExchangeService

class OrderService:

    def __init__(self, order_repository: DjangoOrderRepository, exchange_service: ExchangeService):
        self.order_repository = order_repository
        self.exchange_service = exchange_service

    def create_order(self, user_id: uuid.UUID, currency: str, amount: Decimal) -> Order:
        order = Order(
            id=uuid.uuid4(),
            user_id=user_id,
            currency=currency,
            amount=amount,
            created_at=datetime.now()
        )

        try:
            self.order_repository.save(order)

            self.exchange_service.add_order(currency, amount)

            return order
        except Exception as e:
            self.order_repository.delete(order)
            raise e 