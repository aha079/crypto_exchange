from django.db import models
from django.contrib.sites.models import Site
import uuid

class OrderORM(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	currency = models.CharField(max_length=10)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	processed = models.BooleanField(default=False)

	class Meta:
		app_label = "orders"