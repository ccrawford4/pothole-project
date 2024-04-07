# Generated by Django 3.2 on 2024-04-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_unit_severity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='flow_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='radius_m',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='severity',
            field=models.FloatField(default=0.0),
        ),
    ]