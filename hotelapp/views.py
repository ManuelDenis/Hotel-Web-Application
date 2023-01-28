from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView

from hotelapp.forms import HotelForm, RoomForm, ReservationsForm
from hotelapp.models import Room, Hotel, Reservations


class Index(TemplateView):
    template_name = 'hotelapp/index.html'


class RoomsListView(ListView):
    model = Room
    template_name = 'hotelapp/room_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(RoomsListView, self).get_queryset()
        if Hotel.objects.filter(user=self.request.user).exists():
            rooms = Room.objects.filter(hotel=Hotel.objects.get(user=self.request.user))
            return rooms

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if Hotel.objects.filter(user=self.request.user).exists():
            data['hotel'] = Hotel.objects.get(user=self.request.user)
        hotel = Hotel.objects.get(user=self.request.user)
        data['res'] = Reservations.objects.filter(room__hotel=hotel).order_by('start')
        return data


class HotelCreate(CreateView):
    model = Hotel
    template_name = 'hotelapp/hotel_update.html'
    success_url = '/room_list/'
    form_class = HotelForm

    def get(self, request, *args, **kwargs):
        context = {'form': HotelForm()}
        return render(request, 'hotelapp/hotel_update.html', context)

    def post(self, request, *args, **kwargs):
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.user = self.request.user
            hotel.save()
            return HttpResponseRedirect('/')
        return render(request, 'hotelapp/hotel_update.html', {'form': form})


class HotelUpdate(UpdateView):
    model = Hotel
    template_name = 'hotelapp/hotel_update.html'
    fields = ['name']
    success_url = '/room_list/'


class RoomCreate(CreateView):
    model = Room
    template_name = 'hotelapp/room_create.html'
    success_url = '/room_list/'
    form_class = RoomForm

    def get(self, request, *args, **kwargs):
        context = {'form': RoomForm()}
        return render(request, 'hotelapp/room_create.html', context)

    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            hotel = Hotel.objects.get(user=self.request.user)
            room.hotel = hotel
            room.save()
            return HttpResponseRedirect(redirect_to='/room_list/')
        return render(request, 'hotelapp/room_create.html', {'form': form})


class RoomUpdate(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'hotelapp/room_create.html'
    success_url = '/room_list/'


class RoomDetail(DetailView):
    model = Room
    form_class = ReservationsForm
    template_name = 'hotelapp/room_detail.html'
    success_url = '/room_list/'


class ReservationCreate(CreateView):
    model = Reservations
    template_name = 'hotelapp/reservations_create.html'
    form_class = ReservationsForm
    success_url = '/room_list/'

    def get_object(self, queryset=None):
        return Room.objects.get(pk=self.kwargs.get("pk"))

    def get(self, request, *args, **kwargs):
        context = {'form': ReservationsForm()}
        return render(request, 'hotelapp/reservations_create.html', context)

    def post(self, request, *args, **kwargs):
        form = ReservationsForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            room = self.get_object()
            reservation.room = room
            reservation.save()
            return HttpResponseRedirect(redirect_to='/room_list/')
        return render(request, 'hotelapp/reservations_create.html', {'form': form})


class ReservationUpdate(UpdateView):
    model = Reservations
    form_class = ReservationsForm
    template_name = 'hotelapp/reservations_create.html'
    success_url = '/room_list/'
