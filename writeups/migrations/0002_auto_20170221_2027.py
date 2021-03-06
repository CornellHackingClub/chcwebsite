# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_CTF', models.CharField(max_length=125)),
                ('url_of_CTF', models.URLField()),
                ('date_competed', models.CharField(max_length=125)),
                ('place', models.IntegerField()),
                ('out_of', models.IntegerField()),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writeup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_challenge', models.CharField(max_length=125)),
                ('category', models.CharField(max_length=125)),
                ('text', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ctf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='writeups.CTF')),
            ],
        ),
        migrations.DeleteModel(
            name='Writeups',
        ),
    ]
