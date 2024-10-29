# from echos.models import Echo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
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
