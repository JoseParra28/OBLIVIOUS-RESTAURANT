from django.http import HttpResponse
from django.shortcuts import render



def main_func(request):
    return render(request, "booking/main.html")


def experience(request):
    return render(request, "booking/experience.html")


def contact(request):
    return render(request, "booking/contact.html")


def book(request):
    return render(request, "booking/book.html")
