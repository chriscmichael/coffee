# Generated by Django 4.1.1 on 2022-09-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cups", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cup",
            name="description",
            field=models.CharField(max_length=200),
        ),
    ]