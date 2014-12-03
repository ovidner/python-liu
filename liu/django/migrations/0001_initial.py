# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LiUID',
            fields=[
                ('liu_id', models.CharField(max_length=10, serialize=False, verbose_name='LiU ID', primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=256, verbose_name='last name', blank=True)),
                ('id_number', models.CharField(max_length=11, verbose_name='national identification number', blank=True)),
                ('barcode_number', models.CharField(max_length=32, verbose_name='magnet/barcode card number', blank=True)),
                ('rfid_number', models.CharField(max_length=32, verbose_name='RFID card number', blank=True)),
                ('blocked', models.NullBooleanField(verbose_name='blocked')),
            ],
            options={
                'verbose_name': 'LiU ID',
                'verbose_name_plural': 'LiU IDs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentUnion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='liuid',
            name='student_union',
            field=models.ForeignKey(related_name='members', verbose_name='student union', blank=True, to='liu.StudentUnion', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='liuid',
            name='user',
            field=models.OneToOneField(related_name='liu_id', null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=True,
        ),
    ]
