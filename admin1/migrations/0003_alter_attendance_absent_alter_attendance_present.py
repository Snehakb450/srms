# Generated by Django 4.2 on 2023-08-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin1", "0002_attendance_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="absent",
            field=models.IntegerField(db_column="absent", null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="present",
            field=models.IntegerField(db_column="present", null=True),
        ),
    ]