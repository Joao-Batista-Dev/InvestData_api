from rest_framework import serializers
from investdata.models import Stocks

class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['id', 'name', 'price', 'created_at',]