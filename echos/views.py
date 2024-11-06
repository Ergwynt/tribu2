# from echos.models import Echo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Echo


@login_required
def echo(request):
    echos = Echo.objects.all()
    return render(request, 'echo_list.html', {'echos': echos})


def echo_details(request, pk):
    echo = Echo.objects.get(pk=pk)
    waves = echo.waves.all().order_by('-created_at').filter(echo=pk)
    return render(request, 'echo_detail.html', dict(echo=echo, waves=waves))


def echo_add():
    pass


def echo_wave(request):
    echos = Echo.objects.all()
    waves = echos.waves.all().order_by('created_at')
    return render(request, 'waves_list.html', dict(waves=waves))


def echo_add_wave(request):
    pass
