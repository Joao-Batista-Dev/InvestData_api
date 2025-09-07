from rest_framework import views, response, status
from investdata.models import Stocks
from investdata.serializers import StockSerializers
from investdata.tasks import get_stock_price_task
from datetime import datetime, timedelta

class StockPriceApiViewset(views.APIView):
    def post(self, request):
        stock_name = request.data.get('stock_name')

        get_stock_price_task.delay(stock_name)

        return response.Response(
            data={
                'message': 'Tarefa disparada com sucesso!',
                'stock_name': stock_name,
            },
            status=status.HTTP_200_OK,
        )
    
    
    def get(self, request):
        stock_name = request.query_params.get('stock_name')
        
        if stock_name:
            stocks = Stocks.objects.filter(
                name=stock_name
            )
        else:
            stocks = Stocks.objects.all()

        return response.Response(
            data=StockSerializers(
                stocks, 
                many=True
            ).data,
            status=status.HTTP_200_OK,
        )




