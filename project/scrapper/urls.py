from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("scrap/", scrapperUrlData, name="scrap"),
    path("testing/", celeryWorker, name="testing"),
]
