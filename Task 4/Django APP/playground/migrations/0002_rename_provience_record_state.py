# Generated by Django 5.0.3 on 2024-03-30 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="provience",
            new_name="state",
        ),
    ]