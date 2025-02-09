from exchanges.application.exchange_service import ExchangeService
from exchanges.infrastructure.exchange_api import ExternalExchange
from exchanges.infrastructure.repository_impl import DjangoExchangeTransactionRepository
from unittest.mock import MagicMock
from decimal import Decimal
import pytest

@pytest.mark.django_db
def test_aggregated_purchase():
    mock_api = MagicMock()
    repo = DjangoExchangeTransactionRepository()
    mock_api.buy_currency.return_value = True 

    service = ExchangeService(mock_api, repo)

    service.add_order("ABAN", Decimal("4.0"))
    service.add_order("ABAN", Decimal("3.0"))
    service.add_order("ABAN", Decimal("2.5"))

    assert len(service.pending_orders) == 3

    service.add_order("ABAN", Decimal("1.5"))

    assert len(service.pending_orders) == 0