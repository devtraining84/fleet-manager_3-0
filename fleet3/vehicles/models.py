from django.db import models
from django.core.exceptions import ValidationError
from vehicles.choice import *
from django.core.exceptions import ValidationError

#from vehicles.validatorss import *


# Create your models here.
def VIN_validator(value):
    if len(value) != 17:
        raise ValidationError('VIN 17 znaków !')

def VIN_unique(value):
    data = VehiclesModel.objects.all()
    vins = []
    for i in data:
        vins.append(i.VIN)
    if value in vins:
        raise ValidationError('VIN juz istnieje w bazie !')
def REJ_validator(value):
    if len(value) < 3:
        raise ValidationError('Za mało znaków !')
def REJ_unique(value):
    data = VehiclesModel.objects.all()
    nrs = []
    for i in data:
        nrs.append(i.VIN)
    if value in nrs:
        raise ValidationError('Nr juz istnieje w bazie !')

class VehiclesModel(models.Model):
    rodzaj = models.CharField(choices=RODZAJE, max_length=64)
    marka = models.CharField(choices=MARKI, max_length=16)
    model = models.CharField(max_length=32, blank=True)
    VIN = models.CharField(max_length=17,  unique=True, validators=[VIN_validator, VIN_unique])
    nr_rej = models.CharField(max_length=8, unique=True, verbose_name='nr rej.', validators=[REJ_validator, REJ_unique])
    rok_prod = models.PositiveSmallIntegerField(choices=ROCZNIK[:-1], verbose_name='rok produkcji')

    def __str__(self):
        return f"{self.marka} {self.model} nr rej. {self.nr_rej}"

