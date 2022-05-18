from django.conf.urls import include, url
import StockChart.views

# Django processes URL patterns in the order they appear in the array

urlpatterns = [
    url(r'^$', StockChart.views.index, name='index')
]
