# Generated by Django 4.2 on 2023-08-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin1", "0013_alter_attendance_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="month",
            field=models.IntegerField(db_column="month", null=True),
        ),
    ]