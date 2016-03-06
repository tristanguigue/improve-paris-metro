# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_speed', models.FloatField()),
                ('yearly_traffic', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RollingStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('acceleration', models.FloatField()),
                ('deceleration', models.FloatField()),
                ('max_speed', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trafficAB', models.FloatField()),
                ('trafficBA', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('name', models.CharField(max_length=150)),
                ('yearly_entries', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StationLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_order', models.PositiveIntegerField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metroapp.Line')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metroapp.Station')),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='lines',
            field=models.ManyToManyField(related_name='stations', through='metroapp.StationLine', to='metroapp.Line'),
        ),
        migrations.AddField(
            model_name='segment',
            name='stationA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_stations', to='metroapp.StationLine'),
        ),
        migrations.AddField(
            model_name='segment',
            name='stationB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_stations', to='metroapp.StationLine'),
        ),
        migrations.AddField(
            model_name='line',
            name='rolling_stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metroapp.RollingStock'),
        ),
    ]
