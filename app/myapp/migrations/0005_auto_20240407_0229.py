# Generated by Django 3.2 on 2024-04-07 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20240406_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='Coordinates',
            new_name='coordinates',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='Address_range_high',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='Address_range_low',
        ),
    ]