from django.urls import path
from hotelapp import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]