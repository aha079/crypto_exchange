from rest_framework.test import APIClient
from orders.infrastructure.models import OrderORM
from decimal import Decimal

def test_create_order_api(db):
    client = APIClient()
    response = client.post("/api/orders/", {"currency": "ABAN", "amount": "2.0"}, format="json")

    assert response.status_code == 201
    assert response.data["message"] == "Order placed successfully"

    order = OrderORM.objects.get(id=response.data["order_id"])
    assert order.currency == "ABAN"
    assert order.amount == Decimal("2.0")