# Generated by Django 2.1.7 on 2019-10-15 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0010_remove_concession_arabicname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production_Field',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('field_name', models.CharField(blank=True, db_column='well_statu', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Production_Fields',
                'db_table': 'production_field',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='wellgeoinfo',
            name='production_field',
            field=models.ForeignKey(blank=True, db_column='production_field_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Production_Field'),
        ),
    ]
