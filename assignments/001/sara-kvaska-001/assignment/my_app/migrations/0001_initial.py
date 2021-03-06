# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-17 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('published_date', models.DateField(max_length=150)),
                ('content', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(max_length=100)),
                ('favorite_activities', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('education', models.CharField(choices=[(b'NONE', b'None'), (b'HIGH SCHOOL', b'High School'), (b'UNDERGRADUATE', b'Undergraduate'), (b'MASTERS', b'Masters'), (b'PHD', b'PhD')], default=b'NONE', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.Author'),
        ),
    ]
