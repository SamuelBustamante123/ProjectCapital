from django.shortcuts import render
from urllib.request import urlopen 
import matplotlib.pyplot as plt
import certifi
import json
import io
import urllib, base64

class ApiData:
    url = "https://financialmodelingprep.com"
    endpoints = "/api/v3/historical-price-full/AAPL"
    key = "ae9c5bf2fdac0c2231d11c104462cb31"


def Get_Json(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)


def Get_Data():
    api = ApiData()
    httpRequest = api.url + api.endpoints + "?apikey=" + api.key
    return Get_Json(httpRequest)


def index(request):
    serializedData = Get_Data()
    historicalData = serializedData["historical"]
    historicalData.reverse()
    xValue = []
    yValue = []

    for day in historicalData:
        xValue.append(day["date"])
        yValue.append(day["open"])

    plt.plot(xValue, yValue, label = serializedData["symbol"])
    plt.title('test plot')

    plt.legend() 
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    
    return render(
        request,
        "Graph/index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Hello Django",
            'body' : uri
        }
    )

