# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0002_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='myuser',
            field=models.ForeignKey(null=True, default=None, to='aplikacja.MyUser'),
        ),
        migrations.AddField(
            model_name='nurse',
            name='myuser',
            field=models.ForeignKey(null=True, default=None, to='aplikacja.MyUser'),
        ),
    ]
