# from echos.models import Echo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Echo
from .forms import AddEchoForm

@login_required
def echo(request):
    echos = Echo.objects.all()
    return render(request, 'echo_list.html', {'echos': echos})


def echo_details(request, pk):
    echo = Echo.objects.get(pk=pk)
    waves = echo.waves.all().order_by('-created_at').filter(echo=pk)
    return render(request, 'echo_detail.html', dict(echo=echo, waves=waves))



def echo_add(request):
    # Filtra los Echo del usuario
    echos = Echo.objects.filter(user=request.user)

    if request.method == 'POST':
        form = AddEchoForm(request.POST)
        if form.is_valid():
            new_echo = form.save(commit=False)
            new_echo.user = request.user  
            new_echo.save()
            # Redirige a la lista de Echo
            return redirect('echos:echos')

    else:
        form = AddEchoForm()

    return render(request, 'echo_list.html', {'form': form, 'echos':echos})


def echo_wave(request):
    echos = Echo.objects.all()
    waves = echos.waves.all().order_by('created_at')
    return render(request, 'waves_list.html', dict(waves=waves))


def echo_add_wave(request):
    pass
