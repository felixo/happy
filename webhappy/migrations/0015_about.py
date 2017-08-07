# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-07 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('webhappy', '0014_mainpage_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='\u041e\u0431 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438', max_length=200)),
                ('about_fond', tinymce.models.HTMLField(default='\u0411\u043b\u0430\u0433\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0444\u043e\u043d\u0434 - \u044d\u0442\u043e \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f, \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u0430\u044f \u0438 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0430\u044f \u0441 \u0446\u0435\u043b\u044c\u044e \u0444\u0438\u043d\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0432\u0438\u0434\u043e\u0432 \u0431\u043b\u0430\u0433\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0437\u0430 \u0441\u0447\u0435\u0442 \u0434\u0435\u043d\u0435\u0436\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0439 \u0438 \u0444\u0438\u0440\u043c, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043e\u0431\u044b\u0447\u043d\u044b\u0445 \u0433\u0440\u0430\u0436\u0434\u0430\u043d \u0441\u0442\u0440\u0430\u043d\u044b. ', max_length=5000)),
            ],
        ),
    ]