from exchanges.domain.models import ExchangeTransaction
from exchanges.domain.repository import ExchangeTransactionRepository
from .models import ExchangeTransactionORM

class DjangoExchangeTransactionRepository(ExchangeTransactionRepository):
    def save(self, exchangeTransaction: ExchangeTransaction) -> None:
        ExchangeTransactionORM.objects.create(
            id=exchangeTransaction.id,
            currency=exchangeTransaction.currency,
            amount=exchangeTransaction.amount,
            exchange_name=exchangeTransaction.exchange_name,
            created_at=exchangeTransaction.created_at,
            status=exchangeTransaction.status
        )

    def find_by_id(self, id) -> ExchangeTransaction:
        exchange_transaction_orm = ExchangeTransactionORM.objects.get(id=id)
        return Order(
            id=exchange_transaction_orm.id,
            currency=exchange_transaction_orm.currency,
            amount=exchange_transaction_orm.amount,
            exchange_name=exchangeTransaction.exchange_name,
            created_at=exchange_transaction_orm.created_at,
            status=exchange_transaction_orm.status
        )