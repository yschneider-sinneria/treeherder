# Generated by Django 2.2.6 on 2019-11-11 16:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("model", "0015_add_repository_tc_root_url"),
        ("perf", "0020_add_application_field"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="performancesignature",
            unique_together={
                ("repository", "framework", "signature_hash"),
                (
                    "repository",
                    "suite",
                    "test",
                    "framework",
                    "platform",
                    "option_collection",
                    "extra_options",
                    "last_updated",
                ),
            },
        ),
    ]
