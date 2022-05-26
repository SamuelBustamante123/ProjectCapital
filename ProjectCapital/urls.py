from django.urls import include, re_path

import PlotlyTest.views

urlpatterns = [
    re_path(r'^$', PlotlyTest.views.index, name='index')
]
