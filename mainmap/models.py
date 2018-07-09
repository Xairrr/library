# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

SOURCE_CHOICES=((u'Архив',u'Архив'),
                (u'Личный архив',u'Личный архив'),
                (u'Интернет источник',u'Интернет источник'),
                (u'Неизвестно',u'Неизвестно'))

class Photo(models.Model):
    name = models.CharField(max_length=254)
    year = models.DateField()
    description = models.TextField()
    source = models.CharField(max_length=32, choices=SOURCE_CHOICES, default=u'Неизвестно')
    image = models.ImageField(upload_to = 'photos')
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
