# Generated by Django 3.2.4 on 2021-09-23 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='timestamp',
            new_name='datetime',
        ),
    ]