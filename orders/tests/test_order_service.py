from orders.application.order_service import OrderService
from orders.infrastructure.repository_impl import DjangoOrderRepository
from exchanges.application.exchange_service import ExchangeService
from unittest.mock import MagicMock
from decimal import Decimal
import uuid
import pytest

def test_create_order_calls_exchange():
    mock_repo = MagicMock()
    mock_exchange = MagicMock()
    
    service = OrderService(mock_repo, mock_exchange)

    user_id = uuid.uuid4()
    currency = "ABAN"
    amount = Decimal("5.0")

    order = service.create_order(user_id, currency, amount)

    mock_repo.save.assert_called_once()  
    mock_exchange.add_order.assert_called_once_with(currency, amount)  

def test_create_order_fails_if_exchange_fails():
    mock_repo = MagicMock()
    mock_exchange = MagicMock()
    mock_exchange.add_order.side_effect = Exception("Exchange service failed") 
    
    service = OrderService(mock_repo, mock_exchange)

    user_id = uuid.uuid4()
    currency = "ABAN"
    amount = Decimal("5.0")

    with pytest.raises(Exception, match="Exchange service failed"):
        service.create_order(user_id, currency, amount)

    mock_repo.save.assert_called_once() 
    mock_repo.delete.assert_called_once() 