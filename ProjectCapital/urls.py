from django.conf.urls import include, url
import Graph.views

# Django processes URL patterns in the order they appear in the array

urlpatterns = [
    url(r'^$', Graph.views.index, name='index'),
    url(r'^home$', Graph.views.index, name='home'),
]
