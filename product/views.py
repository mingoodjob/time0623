from item.models import Item, Category, Order, ItemOrder
from product.serializers import CategorySerializer, ItemSerializer, OrderSerializer, ItemOrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from django.db.models.query_utils import Q


class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class OrderDetailView(APIView):
    def get(self, request, id):
        # item = Q(exposure_start__lte=datetime.now()) & Q(exposure_end__gte=datetime.now()) & Q(author=request.user) & Q(active=True)
        # order_date 7weeks ago
        order = Q(id=id) & Q(order_date__lte=datetime.now() - timedelta(days=7))
        order = Order.objects.filter(order)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)