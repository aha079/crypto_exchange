from django.http import JsonResponse
from django.views import View
from orders.application.order_service import OrderService
from decimal import Decimal
import json

class OrderCreateView(View):

    def post(self, request):
        data = json.loads(request.body)
        currency = data.get("currency")
        amount = Decimal(data.get("amount"))

        order_service = OrderService()
        order = order_service.create_order(currency, amount)

        return JsonResponse({"order_id": str(order.id), "currency": order.currency, "amount": str(order.amount)}, status=201)

class OrderListView(View):

    def get(self, request):
        order_service = OrderService()
        orders = order_service.list_orders()

        return JsonResponse({"orders": [{"id": str(o.id), "currency": o.currency, "amount": str(o.amount)} for o in orders]}, safe=False)