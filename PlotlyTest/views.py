from django.shortcuts import render
from urllib.request import urlopen
import datetime as dt
import certifi
import json
from plotly.offline import plot
from plotly.graph_objs import Scatter
from PlotlyTest.models import Stock

# Create your views here.


class ApiData:
    url = "https://financialmodelingprep.com"
    endpoints = "/api/v3/historical-chart/1hour/"
    key = "ae9c5bf2fdac0c2231d11c104462cb31"

def Get_Json(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def Get_Data(ticker):
    api = ApiData()
    httpRequest = api.url + api.endpoints + ticker + "?apikey=" + api.key
    return Get_Json(httpRequest)

def index(request):
    all_prices = {}
    xAxis = []
    yAxis = []
    if 'Ticker' in request.GET:
        name = request.GET['Ticker']
        serializedData = Get_Data(name)
    
        for it in serializedData:
            stock_data = Stock(
                date = it['date'],
                openPrice = it['open'],
                low = it['low'],
                high = it['high'],
                closePrice = it['close'],
                volume = it['volume']
            )
            stock_data.save()
            all_prices = Stock.objects.all()

    for price in all_prices:
        xAxis.append(price.date)
        yAxis.append(price.closePrice)

    plot_div = plot([Scatter(x=xAxis, y=yAxis,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    return render(
        request,
        "PlotlyTest/index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Plotly Test",
            'plot_div': plot_div 
        }
    )
