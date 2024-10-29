# from echos.models import Echo
from django.shortcuts import render


def echo(request):
    return render(request, 'wave_detail.html')


def echo_details(request):
    pass


def echo_add():
    pass


def echo_wave(request):
    pass


def echo_add_wave(request):
    pass
