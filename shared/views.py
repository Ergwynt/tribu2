from django.contrib.auth import login
from django.shortcuts import redirect, render

from shared.forms import SignupForm


def user_signup(request):
    form = SignupForm(request.POST or None)

    if (form := SignupForm(request.POST)).is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('echos:echos')

    return render(request, './registration/signup.html', dict(form=form))


def users(request):
    pass


def profile(request):
    pass


def profile_echos(request):
    pass
