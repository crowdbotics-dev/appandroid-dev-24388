# Generated by Django 2.2.26 on 2022-05-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0001_load_initial_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Datauser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
            ],
        ),
    ]
