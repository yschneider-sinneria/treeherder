# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 16:50
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("model", "0001_squashed_0022_modify_bugscache_and_bugjobmap"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="bugjobmap",
            managers=[
                ("failures", django.db.models.manager.Manager()),
            ],
        ),
    ]
