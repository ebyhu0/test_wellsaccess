# Generated by Django 2.1.7 on 2019-05-30 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0006_auto_20190523_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='bindata',
            name='SeismicVentage',
            field=models.ForeignKey(blank=True, db_column='id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Seismicvintage'),
        ),
    ]
