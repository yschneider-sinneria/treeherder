# Generated by Django 4.0.8 on 2023-05-08 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("perf", "0048_performancedatum_application_version"),
    ]

    operations = [
        migrations.CreateModel(
            name="PerformanceDatumReplicate",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("value", models.FloatField()),
                (
                    "performance_datum",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="perf.performancedatum"
                    ),
                ),
            ],
            options={
                "db_table": "performance_datum_replicate",
            },
        ),
    ]
