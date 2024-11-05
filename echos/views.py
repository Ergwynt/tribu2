# from echos.models import Echo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Echo


@login_required
def echo(request):
    echos = Echo.objects.all()
    return render(request, 'wave_detail.html', {'echos': echos})


def echo_details(request):
    pass


def echo_add():
    pass


def echo_wave(request):
    pass


def echo_add_wave(request):
    pass
