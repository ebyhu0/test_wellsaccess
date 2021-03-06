# Generated by Django 2.1.7 on 2019-08-08 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0003_auto_20190801_0811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wellgeoinfo',
            options={'managed': True, 'ordering': ('exploration_name',), 'verbose_name_plural': 'WellGeoinfo'},
        ),
        migrations.AlterField(
            model_name='provisional',
            name='well_info',
            field=models.ForeignKey(blank=True, db_column='well_info_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='wells.WellGeoinfo'),
        ),
    ]
