# Generated by Django 4.2 on 2023-08-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin1", "0004_remove_attendance_absent_remove_attendance_present"),
    ]

    operations = [
        migrations.CreateModel(
            name="Month",
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
                ("month", models.CharField(db_column="month", max_length=20)),
                ("total", models.IntegerField(db_column="total")),
            ],
            options={
                "db_table": "month",
            },
        ),
    ]
