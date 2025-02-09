from orders.infrastructure.repository_impl import DjangoOrderRepository
from orders.domain.models import Order
from decimal import Decimal
import uuid
from datetime import datetime

def test_save_order(db):
    repo = DjangoOrderRepository()
    order = Order(id=uuid.uuid4(), user_id=uuid.uuid4(), currency="ABAN", amount=Decimal("3.5"), created_at=datetime.now())

    repo.save(order)

    saved_order = repo.find_by_id(order.id)
    assert saved_order is not None
    assert saved_order.currency == "ABAN"
    assert saved_order.amount == Decimal("3.5")

def test_find_order_by_id(db):
    repo = DjangoOrderRepository()
    order = Order(id=uuid.uuid4(), user_id=uuid.uuid4(), currency="BTC", amount=Decimal("1.2"), created_at=datetime.now())

    repo.save(order)

    retrieved_order = repo.find_by_id(order.id)

    assert retrieved_order is not None
    assert retrieved_order.id == order.id
    assert retrieved_order.currency == "BTC"
    assert retrieved_order.amount == Decimal("1.2")