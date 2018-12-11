# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-11 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bourbon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BourbonID', models.CharField(max_length=200)),
                ('Bourbon', models.CharField(max_length=200)),
                ('Aged', models.IntegerField()),
                ('Proof', models.IntegerField()),
                ('Corn', models.IntegerField()),
                ('Rye', models.IntegerField()),
                ('Barley', models.IntegerField()),
                ('Wheat', models.IntegerField()),
                ('Type', models.CharField(max_length=200)),
                ('Style', models.CharField(max_length=200)),
                ('Price_Range', models.IntegerField()),
                ('Distillery', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=200)),
                ('Website', models.URLField()),
                ('Description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RatingID', models.IntegerField(blank=True, null=True)),
                ('Pub_Date', models.DateTimeField(verbose_name='date published')),
                ('User_Name', models.CharField(max_length=100)),
                ('Comment', models.CharField(max_length=200)),
                ('Rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('Bourbon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bourbonsite.Bourbon')),
            ],
        ),
        migrations.CreateModel(
            name='SimilarBourbons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BourbonID', models.CharField(max_length=200)),
                ('Bourbon', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SimilarReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BourbonID', models.CharField(max_length=200)),
                ('Bourbon', models.CharField(max_length=200)),
                ('AvgRating', models.DecimalField(blank=True, decimal_places=2, max_digits=200, null=True)),
                ('PredRating', models.DecimalField(blank=True, decimal_places=2, max_digits=200, null=True)),
            ],
        ),
    ]
