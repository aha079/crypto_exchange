from django.db import models
import uuid

class ExchangeTransactionORM(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    currency = models.CharField(max_length=16)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    exchange_name = models.CharField(max_length=64)
    status = models.CharField(max_length=20, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "exchanges"