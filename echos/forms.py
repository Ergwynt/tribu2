from django import forms

from .models import Echo


class AddEchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu echo aquí'}),
        }


class EditEchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)