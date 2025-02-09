from rest_framework.test import APIClient
from orders.infrastructure.models import OrderORM
from decimal import Decimal
import pytest

@pytest.mark.django_db
def test_create_order_api(db):
    client = APIClient()
    response = client.post("/api/orders/create", {"currency": "ABAN", "amount": "2.0"}, format="json")

    assert response.status_code == 301
    assert OrderORM.objects.count() == 0