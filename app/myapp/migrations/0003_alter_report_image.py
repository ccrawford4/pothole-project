# Generated by Django 3.2 on 2024-04-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240406_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.JSONField(null=True),
        ),
    ]
