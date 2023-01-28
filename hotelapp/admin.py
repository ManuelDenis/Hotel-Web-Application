from django.contrib import admin
from hotelapp.models import Room, Hotel, Reservations


class RoomTabularInline(admin.TabularInline):
    model = Room


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [RoomTabularInline]
    list_display = ('user', 'name')


@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('room', 'start', 'end')
