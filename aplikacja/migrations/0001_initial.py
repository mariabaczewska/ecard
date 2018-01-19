# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Karta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(blank=True, null=True, to='aplikacja.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=40)),
                ('pesel', models.CharField(max_length=9)),
                ('doctor', models.ForeignKey(to='aplikacja.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='measurement',
            name='nurse',
            field=models.ForeignKey(blank=True, null=True, to='aplikacja.Nurse'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='patient',
            field=models.ForeignKey(to='aplikacja.Patient'),
        ),
        migrations.AddField(
            model_name='karta',
            name='patient',
            field=models.ForeignKey(null=True, to='aplikacja.Patient'),
        ),
    ]
