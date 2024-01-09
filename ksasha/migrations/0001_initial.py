# Generated by Django 4.2.6 on 2023-10-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ksasha",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.CharField(max_length=2080)),
                ("payment", models.FloatField()),
                ("email", models.EmailField(max_length=254)),
                ("reg_no", models.CharField(max_length=50)),
            ],
        ),
    ]
