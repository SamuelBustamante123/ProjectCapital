from django.shortcuts import render
from urllib.request import urlopen 
import datetime as dt
import certifi
import json
import io
import urllib, base64

class ApiData:
    url = "https://financialmodelingprep.com"
    endpoints = "/api/v3/historical-price-full/AAPL?from=2018-03-12&to=2018-05-12"
    key = "ae9c5bf2fdac0c2231d11c104462cb31"

def Get_Json(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def Get_Data():
    api = ApiData()
    httpRequest = api.url + api.endpoints + "&apikey=" + api.key
    return Get_Json(httpRequest)

def index(request):
    serializedData = Get_Data()
    historicalData = serializedData["historical"]
    historicalData.reverse()
    xValue = []
    yValue = []

    for day in historicalData:
        date = day["date"]
        xValue.append(date.replace("&#39;", ""))
        yValue.append(day["open"])


    return render(
        request,
        "StockChart/index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Project Capital",
            'labels' : xValue,
            'data' : yValue
        }
    )