from django.urls import path
from investdata.views import StockPriceApiViewset


urlpatterns = [
    path('actions/', StockPriceApiViewset.as_view(), name='actions'),
]
