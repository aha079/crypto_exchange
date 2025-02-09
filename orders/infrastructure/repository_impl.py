from orders.domain.models import Order
from orders.domain.repository import OrderRepository
from .models import OrderORM

class DjangoOrderRepository(OrderRepository):
    def save(self, order: Order) -> None:
        OrderORM.objects.create(
            id=order.id,
            currency=order.currency,
            amount=order.amount,
            created_at=order.created_at,
            processed=order.processed
        )

    def find_by_id(self, order_id) -> Order:
        order_orm = OrderORM.objects.get(id=order_id)
        return Order(
            id=order_orm.id,
            currency=order_orm.currency,
            amount=order_orm.amount,
            created_at=order_orm.created_at,
            processed=order_orm.processed
        )