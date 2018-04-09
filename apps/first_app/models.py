# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    vin = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')