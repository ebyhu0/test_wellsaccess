# Generated by Django 2.1.7 on 2019-06-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0017_auto_20190610_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staked',
            name='st_by_mm',
        ),
        migrations.RemoveField(
            model_name='staked',
            name='st_by',
        ),
        migrations.AddField(
            model_name='staked',
            name='st_by',
            field=models.ManyToManyField(related_name='persons_stake_by', to='wells.Persons'),
        ),
    ]
