from django.urls import path
from hotelapp import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('room_list/', views.RoomsListView.as_view(), name='room_list'),
    path('hotel_update/<int:pk>/', views.HotelUpdate.as_view(), name='hotel_update'),
    path('hotel_create/', views.HotelCreate.as_view(), name='hotel_create'),
    path('room_create/', views.RoomCreate.as_view(), name='room_create'),
    path('room_update/<int:pk>/', views.RoomUpdate.as_view(), name='room_update'),
    path('room_detail/<int:pk>/', views.RoomDetail.as_view(), name='room_detail'),
    path('reservations_create/<int:pk>/', views.ReservationCreate.as_view(), name='reservations_create'),
    path('reservations_update/<int:pk>/', views.ReservationUpdate.as_view(), name='reservations_update'),
]