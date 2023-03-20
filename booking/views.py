from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Table, Booking


class Table_list(ListView):
    model = Table


class Booking_list(ListView):
    model = Booking


def main_func(request):
    return render(request, "booking/main.html")


def experience(request):
    return render(request, "booking/experience.html")


def contact(request):
    return render(request, "booking/contact.html")


def book(request):
    submit_booking = Booking.objects.all()
    context = {
        'submit_booking': submit_booking
    }
    print(submit_booking)
    return render(request, "booking/book.html", context)




    # def book(request):
    # submit_booking = Booking.objects.all()
    # context = {
    #     'submit_booking': submit_booking
    # }
    # print(submit_booking)
    # return render(request, "booking/book.html", context)
