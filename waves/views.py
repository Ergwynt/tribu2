# from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def edit_wave(request):
    pass


def delete_wave(request):
    pass
