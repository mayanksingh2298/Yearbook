# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 12:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180405_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='AnswersAboutMyself',
            field=jsonfield.fields.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='CommensIGet',
            field=jsonfield.fields.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='CommentsIWrite',
            field=jsonfield.fields.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='VotesIHaveGiven',
            field=jsonfield.fields.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='oneliner',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
