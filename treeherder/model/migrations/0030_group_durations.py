# Generated by Django 4.1.9 on 2023-08-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('model', '0029_alter_failureline_index_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupstatus',
            name='duration',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
