from unittest.mock import patch
from exchanges.infrastructure.exchange_api import ExternalExchange
from decimal import Decimal

@patch("requests.post")
def test_buy_currency(mock_post):
    mock_post.return_value.status_code = 200 

    exchange = ExternalExchange()
    success = exchange.buy_currency("ABAN", Decimal("5.0"))

    assert success is True
    mock_post.assert_called_once_with("https://api.example.com/buy", json={"currency": "ABAN", "amount": "5.0"})