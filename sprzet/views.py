# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import SetForm, LatawiecForm, DeskaForm, TrapezForm
# Create your views here.

def index(request):
    set_list = Set.objects.all()
    sprzet_latawiec = Latawiec.objects.all()
    sprzet_deska = Deska.objects.all()
    sprzet_trapez = Trapez.objects.all()

    context = {}
    if sprzet_latawiec or sprzet_deska or sprzet_trapez or set_list:
       context = {
           'latawiec': sprzet_latawiec,
           'deska': sprzet_deska,
           'trapez': sprzet_trapez,
           'lista': set_list
       }
    return render(request, 'sprzet/index.html', context)


def dodaj_trapez(request):
    trapez = TrapezForm(request.POST or None)
    if trapez.is_valid():
        instance = trapez.save(commit=False)
        instance.save()
        return redirect('sprzet_list')
    return render(request, 'sprzet/dodaj_trapez.html', {'trapez': trapez})

def dodaj_deske(request):
    deska = DeskaForm(request.POST or None)
    if deska.is_valid():
        instance = deska.save(commit=False)
        instance.save()
        trapezz = TrapezForm(None)
        return render(request, 'sprzet/dodaj_trapez.html', {'trapez': trapezz})
    return render(request, 'sprzet/dodaj_deske.html', {'deska': deska})

def dodaj_latawiec(request):
    kite = LatawiecForm(request.POST or None)
    if request.method == 'POST':
        if kite.is_valid():
            instance = kite.save(commit=False)
            instance.save()
            deskaa = DeskaForm(None)
            return render(request, 'sprzet/dodaj_deske.html', {'deska': deskaa})
    return render(request, 'sprzet/dodaj_latawiec.html', {'latawiec': kite})

def dodaj_set(request):
    form = SetForm(request.POST or None)
    if request.method == 'POST':
        print (request, form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('set_list')
    context = {
    "form": form,
    }
    return render(request, 'sprzet/dodaj_set.html', context)


def usun_objekt(request, ident, numer):
    if ident == 'Latawiec':
        kite = get_object_or_404(Latawiec, pk=numer)
        kite.delete()
        return redirect('sprzet_list')

    elif ident == 'Deska':
        deska = get_object_or_404(Deska, pk=numer)
        deska.delete()
        return redirect('sprzet_list')

    elif ident == 'Trapez':
        trapez = get_object_or_404(Trapez, pk=numer)
        trapez.delete()
        return redirect('sprzet_list')
    elif ident == 'Set':
        set = get_object_or_404(Set, pk=numer)
        set.delete()
        return redirect('set_list')


def are_you_sure(request, ident, numer):
    if ident == 'Latawiec':
        kite = get_object_or_404(Latawiec, pk=numer)
        return render(request, 'sprzet/are_you_sure.html', {'objekt': kite})

    elif ident == 'Deska':
        deska = get_object_or_404(Deska, pk=numer)
        return render(request, 'sprzet/are_you_sure.html', {'objekt': deska})

    elif ident == 'Trapez':
        trapez = get_object_or_404(Trapez, pk=numer)
        return render(request, 'sprzet/are_you_sure.html', {'objekt': trapez})
    elif ident == 'Set':
        set = get_object_or_404(Set, pk=numer)
        return render(request, 'sprzet/are_you_sure.html', {'objekt': set})



def set_list(request):
    lista_set = Set.objects.all()
    return render(request, 'sprzet/set_list.html', {'lista': lista_set})




def sprzet_list(request):
    latawce = Latawiec.objects.all()
    deski = Deska.objects.all()
    trapezy = Trapez.objects.all()
    context = {
        'latawiec': latawce,
        'deska': deski,
        'trapez': trapezy,
    }
    return render(request, 'sprzet/sprzet_list.html', context)




def sprzet_detail(request, ident, numer):
    if ident == 'Latawiec':
        kite = get_object_or_404(Latawiec, pk=numer)
        context = {
            'objekt': kite,
        }

    elif ident == 'Deska':
        deska = get_object_or_404(Deska, pk=numer)
        context = {
            'objekt': deska
        }

    elif ident == 'Trapez':
        trapez = get_object_or_404(Trapez, pk=numer)
        context = {
            'objekt': trapez
        }
    return render(request, 'sprzet/sprzet_detail.html', context)



def sprzet_detail_edit(request, ident, numer):
    if ident == 'Latawiec':
        kite = get_object_or_404(Latawiec, pk=numer)
        form = LatawiecForm(request.POST or None, instance=kite)
        if request.method == 'POST':
            instance = form.save(commit=False)
            instance.save()
            return redirect('sprzet_detail', ident=ident, numer=numer)
        context = {
            'objekt': kite,
            'form': form
        }

    elif ident == 'Deska':
        deska = get_object_or_404(Deska, pk=numer)
        form = DeskaForm(request.POST or None, instance=deska)
        if request.method == 'POST':
            instance = form.save(commit=False)
            instance.save()
            return redirect('sprzet_detail', indent=ident, numer=numer)
        context = {
            'objekt': deska,
            'form': form
        }

    elif ident == 'Trapez':
        trapez = get_object_or_404(Trapez, pk=numer)
        form = TrapezForm(request.POST or None, instance=trapez)
        if request.method == 'POST':
            instance = form.save(commit=False)
            instance.save()
            return redirect('sprzet_detail', ident=ident, numer=numer)
        context = {
            'objekt': trapez,
            'form': form
        }
    return render(request, 'sprzet/sprzet_detail.html', context)




def detail(request, pk):
    pk = get_object_or_404(Set, pk=pk)

    return render(request, 'sprzet/set_detail.html', {'set': pk})


def set_detail_edit(request, pk):
    set = get_object_or_404(Set, pk=pk)
    form = SetForm(request.POST or None, instance=set)
    if request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()
        return redirect('detail', pk=pk)
    context = {
        'set': set,
        'form': form,
    }
    return render(request, 'sprzet/set_detail.html', context)

def about(request):
    return render(request, 'sprzet/about.html')
























