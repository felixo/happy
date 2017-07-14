#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class MainPage(models.Model):
    name_of_page = models.CharField(max_length=50, default='Главная страница и общая информация')
    phone_country = models.CharField(max_length=3, default='+7')
    phone_code = models.CharField(max_length=5, default='925')
    phone_number = models.CharField(max_length=10, default='346-07-27')
    email = models.CharField(max_length=30, default='fond-schastie@hotmail.com')
    youtube = models.CharField(max_length=100, default='https://www.youtube.com/channel/UC20_z5bq_QyONSbVNtb3EVg')
    fb = models.CharField(max_length=100, default='https://www.facebook.com/fond.schastie/')
    insta = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    words = HTMLField(max_length=1000, default=' ')
    title = models.CharField(max_length=100, default=' ')
    name = models.CharField(max_length=100, default='Диана Менинбаева')
    photo = models.FileField(upload_to='media/CEO', default="")
    ps = HTMLField(max_length=1000, default=' ')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name_of_page) or u''

class Slider(models.Model):
    number = models.IntegerField(default=0)
    img = models.FileField(upload_to='media/slider')
    link = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    name = models.CharField(max_length=50, default='Слайдер №')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Partner(models.Model):
    name = models.CharField(max_length=50, default='Партнер №')
    link = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    img = models.FileField(upload_to='media/parner')
    number = models.IntegerField(default=0)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Wwd(models.Model):
    name = models.CharField(max_length=50, default='Что мы делаем?')
    img = models.FileField(upload_to='media/wwd_ico')
    text = HTMLField(max_length=1000, default='Задачей программ явлеяется целевые проекты и социальная поддержка населения')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Video(models.Model):
    name = models.CharField(max_length=50, default='Счастье is - ')
    img = models.FileField(upload_to='media/videos_cover', blank=True)
    link = models.CharField(max_length=150, default='https://www.youtube.com/channel/UC20_z5bq_QyONSbVNtb3EVg')
    cover = models.CharField(max_length=150, default='https://img.youtube.com/vi/wi9Oz75dvI0/0.jpg')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class How_to_help(models.Model):
    name = models.CharField(max_length=200, default='Благотворительная акция Банан')
    img = models.FileField(upload_to='media/how_to_help', blank=True)
    text = HTMLField(max_length=2000,
                     default='Задачей программ явлеяется целевые проекты и социальная поддержка населения')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''