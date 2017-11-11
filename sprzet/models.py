# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.urls import reverse



class Trapez(models.Model):

    rozmiary = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    rodzaje = (
        ('biodrowy', 'biodrowy'),
        ('ledzwiowy', 'ledzwiowy'),
    )
    producenci = (
        ('ION', 'ION'),
        ('Mystic', 'Mystic'),
        ('Manera', 'Manera'),
        ('DaKine', 'Dakine'),
        ('Liquid Force', 'Liquid Force'),
        ('Neilpryde', 'Neilpryde'),
        ('Severne', 'Severne'),
    )

    rozmiar = models.CharField(max_length=4, choices=rozmiary)
    rodzaj = models.CharField(max_length=30, choices=rodzaje)
    producent = models.CharField(max_length=30, choices=producenci)

    def __str__(self):
        return self.producent + ' ' + self.rodzaj

    def identyfikuj(self):
        return self.__class__.__name__



class Deska(models.Model):
    typ_deski = (
        ('TwinTip', 'Twintip'),
        ('Wave', 'Wave'),
        ('Skimboard', 'Skim'),
    )
    styl_deski = (
        ('Freeride', 'Freeride'),
        ('Freestyle', 'Freestyle'),
    )
    rozmiary = (
        ('mala', 'mala'),
        ('srednia', 'srednia'),
        ('duza', 'duza'),
    )

    typ = models.CharField(max_length=50, choices=typ_deski)
    styl = models.CharField(max_length=50, choices=styl_deski)
    rozmiar = models.CharField(max_length=100, choices=rozmiary)

    def __str__(self):
        return self.typ + ' ' + self.styl

    def identyfikuj(self):
        return self.__class__.__name__



class Latawiec(models.Model):

    roz1='5m'
    roz2='6m'
    roz3='7m'
    roz4='7m'
    roz5='8m'
    roz6='9m'
    roz7='10m'
    roz8='10m'
    roz9='11m'
    roz10='12m'
    roz11='13m'
    roz12='14m'
    roz13='15m'
    roz14='16m'
    roz15='17m'
    roz16='18m'
    roz17='21m'

    typy = (
        ('C-Shape', 'C-Shape'),
        ('Delta', 'Delta'),
        ('Bow', 'Bow'),
    )
    rozmiary = (
        (roz1, '5m'),
        (roz2, '6m'),
        (roz3, '7m'),
        (roz4, '7.5m'),
        (roz5, '8m'),
        (roz6, '9m'),
        (roz7, '10m'),
        (roz8, '10.5m'),
        (roz9, '11m'),
        (roz10, '12m'),
        (roz11, '13m'),
        (roz12, '14m'),
        (roz13, '15m'),
        (roz14, '16m'),
        (roz15, '17m'),
        (roz16, '18m'),
        (roz17, '21m')
    )
    producenci = (
        ('Nobile Kiteboarding', 'Nobile Kiteboarding'),
        ('Gin Kiteboarding', 'Gin Kiteboarding'),
        ('Ozone', 'Ozone'),
        ('Slingshot', 'Slingshot'),
        ('Weinmann', 'Weinmann'),
        ('Naish', 'Naish'),
        ('Airush', 'Airush'),
    )

    typ = models.CharField(max_length=50, choices=typy)
    rozmiar = models.CharField(max_length=39, choices=rozmiary)
    producent = models.CharField(max_length=80, choices=producenci)


    def __str__(self):
        return self.producent + ' ' + str(self.rozmiar)+ ' ' + self.typ

    def identyfikuj(self):
        return self.__class__.__name__



class Set(models.Model):

    nazwa = models.CharField(max_length=50)
    latawiec = models.ForeignKey(Latawiec, default='---', related_name='Latawiec', blank=True, null=True, on_delete=models.SET_NULL)
    deska = models.ForeignKey(Deska, default='---', related_name='Deska', blank=True, null=True, on_delete=models.SET_NULL)
    trapez = models.ForeignKey(Trapez, default='---', related_name='Trapez', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nazwa

    def identyfikuj(self):
        return self.__class__.__name__















