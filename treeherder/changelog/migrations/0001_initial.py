# Generated by Django 3.0.3 on 2020-03-13 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Changelog",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("remote_id", models.CharField(max_length=255)),
                ("date", models.DateTimeField(db_index=True)),
                ("author", models.CharField(max_length=100)),
                ("owner", models.CharField(max_length=100)),
                ("project", models.CharField(max_length=100)),
                ("project_url", models.CharField(max_length=360)),
                ("message", models.CharField(max_length=360)),
                ("description", models.CharField(max_length=360)),
                ("type", models.CharField(max_length=100)),
                ("url", models.CharField(max_length=360)),
            ],
            options={
                "db_table": "changelog_entry",
                "unique_together": {("id", "remote_id", "type")},
            },
        ),
        migrations.CreateModel(
            name="ChangelogFile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.SlugField(max_length=255)),
                (
                    "changelog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="changelog.Changelog",
                    ),
                ),
            ],
            options={
                "db_table": "changelog_file",
            },
        ),
    ]
