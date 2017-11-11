from django import forms
from .models import Latawiec, Set, Deska, Trapez
from django.forms.widgets import DateInput



class SetForm(forms.ModelForm):
    class Meta:
        model = Set
       # exclude = ['key_field']
        fields = ['nazwa', 'latawiec', 'deska', 'trapez']



class TrapezForm(forms.ModelForm):
    class Meta:
        model = Trapez
        fields = ['rozmiar', 'rodzaj', 'producent']


class DeskaForm(forms.ModelForm):
    class Meta:
        model = Deska
        fields = ['typ', 'styl', 'rozmiar']


class LatawiecForm(forms.ModelForm):
    class Meta:
        model = Latawiec
        fields = ('producent', 'rozmiar', 'typ')
