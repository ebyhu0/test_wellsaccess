# Generated by Django 2.1.7 on 2019-08-01 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0002_auto_20190731_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wellgeoinfo',
            name='lat_EG_dd',
        ),
        migrations.RemoveField(
            model_name='wellgeoinfo',
            name='long_EG_dd',
        ),
    ]
