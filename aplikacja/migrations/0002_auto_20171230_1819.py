# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karta',
            old_name='name',
            new_name='personalities',
        ),
        migrations.RemoveField(
            model_name='karta',
            name='surname',
        ),
    ]
