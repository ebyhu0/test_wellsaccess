# Generated by Django 2.1.7 on 2019-07-31 12:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bindata',
            fields=[
                ('bg_id', models.AutoField(db_column='bg_id', primary_key=True, serialize=False)),
                ('area', models.CharField(blank=True, db_column='area', max_length=50, null=True)),
                ('program', models.CharField(blank=True, db_column='program', max_length=255, null=True)),
                ('programold', models.CharField(blank=True, db_column='programold', max_length=50, null=True)),
                ('point', models.CharField(blank=True, db_column='point', max_length=25, null=True)),
                ('inline', models.IntegerField(blank=True, db_column='inline', null=True)),
                ('xline', models.IntegerField(blank=True, db_column='xline', null=True)),
                ('east', models.FloatField(blank=True, db_column='east', null=True)),
                ('north', models.FloatField(blank=True, db_column='north', null=True)),
                ('psd', models.CharField(blank=True, db_column='psd', max_length=50, null=True)),
                ('year', models.CharField(blank=True, db_column='year', max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('originalprojection', models.CharField(blank=True, db_column='originalprojection', max_length=255, null=True)),
                ('displayprojection', models.CharField(blank=True, db_column='displayprojection', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Bindata',
                'db_table': 'bindata',
            },
        ),
        migrations.CreateModel(
            name='Checked',
            fields=[
                ('chk_id', models.AutoField(primary_key=True, serialize=False)),
                ('chk_lat', models.FloatField(blank=True, null=True)),
                ('chk_long', models.FloatField(blank=True, null=True)),
                ('chk_east', models.FloatField(blank=True, null=True)),
                ('chk_north', models.FloatField(blank=True, null=True)),
                ('chk_elev', models.FloatField(blank=True, null=True)),
                ('chk_cellar_pno', models.CharField(blank=True, choices=[('Corner1', 'Corner1'), ('Corner2', 'Corner2'), ('Corner3', 'Corner3'), ('Corner4', 'Corner4'), ('Center', 'Center')], max_length=50, null=True)),
                ('chk_date', models.DateField(blank=True, null=True)),
                ('chk_remarks', models.TextField(blank=True, db_column='chk_remarks', null=True)),
                ('equip_tech_id', models.IntegerField(blank=True, db_column='equip_tech_id', null=True)),
                ('usedcontrolgarminid', models.CharField(blank=True, db_column='usedcontrolgarminid', max_length=6, null=True)),
                ('tripscope', models.CharField(blank=True, db_column='tripscope', max_length=255, null=True)),
                ('tripstartdate', models.DateField(blank=True, db_column='tripstartdate', null=True)),
                ('tripenddate', models.DateField(blank=True, db_column='tripenddate', null=True)),
                ('garminlateg07', models.CharField(blank=True, db_column='garminlateg07', max_length=20, null=True)),
                ('garminlongeg07', models.CharField(blank=True, db_column='garminlongeg07', max_length=20, null=True)),
                ('facilitysurveyimage', models.TextField(blank=True, db_column='facilitysurveyimage', null=True)),
                ('tgojobpath', models.TextField(blank=True, db_column='tgojobpath', null=True)),
                ('observedby', models.IntegerField(blank=True, db_column='observedby', null=True)),
            ],
            options={
                'db_table': 'checked',
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='name', max_length=50, null=True)),
                ('location', models.CharField(blank=True, db_column='location', max_length=50, null=True)),
                ('address', models.CharField(blank=True, db_column='address', max_length=255, null=True)),
                ('phone1', models.CharField(blank=True, db_column='phone1', max_length=50, null=True)),
                ('phone2', models.CharField(blank=True, db_column='phone2', max_length=50, null=True)),
                ('phone3', models.CharField(blank=True, db_column='phone3', max_length=50, null=True)),
                ('phone4', models.CharField(blank=True, db_column='phone4', max_length=50, null=True)),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=50, null=True)),
                ('contact_person', models.CharField(blank=True, db_column='contact_person', max_length=50, null=True)),
                ('cont_pers_phone', models.CharField(blank=True, db_column='cont_pers_phone', max_length=50, null=True)),
                ('cont_pers_mobile', models.CharField(blank=True, db_column='cont_pers_mobile', max_length=50, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Concession',
            fields=[
                ('tt', models.IntegerField(blank=True, db_column='tt', null=True)),
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('concession', models.CharField(blank=True, db_column='concession', max_length=255, null=True)),
                ('area', models.CharField(blank=True, db_column='area', max_length=50, null=True)),
                ('arabicname', models.CharField(blank=True, db_column='arabicname', max_length=255, null=True)),
                ('holder', models.CharField(blank=True, db_column='holder', max_length=50, null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='isactive', null=True)),
                ('field2', models.CharField(blank=True, db_column='field2', max_length=255, null=True)),
                ('location', models.IntegerField(blank=True, db_column='location', null=True)),
                ('agreement_id', models.IntegerField(blank=True, db_column='agreement_id', null=True)),
                ('area_km2', models.FloatField(blank=True, db_column='area_km2', null=True)),
                ('concessiontype', models.IntegerField(blank=True, choices=[(1, 'Concession'), (2, 'Development Lease'), (3, 'Released Concession'), (4, 'Unknown')], db_column='concessiontype', null=True)),
            ],
            options={
                'db_table': 'concession',
            },
        ),
        migrations.CreateModel(
            name='ConcessionCorners',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('objectid_1', models.FloatField(blank=True, db_column='objectid_1', null=True)),
                ('concessionid', models.CharField(blank=True, db_column='concessionid', max_length=255, null=True)),
                ('lnm', models.CharField(blank=True, db_column='lnm', max_length=255, null=True)),
                ('pno', models.IntegerField(blank=True, db_column='pno', null=True)),
                ('pointtype', models.CharField(blank=True, db_column='pointtype', max_length=255, null=True)),
                ('latitude_egy07', models.CharField(blank=True, db_column='latitude_egy07', max_length=255, null=True)),
                ('longitude_egy07', models.CharField(blank=True, db_column='longitude_egy07', max_length=255, null=True)),
                ('latitude_wgs84', models.CharField(blank=True, db_column='latitude_wgs84', max_length=255, null=True)),
                ('longitude_wgs84', models.CharField(blank=True, db_column='longitude_wgs84', max_length=255, null=True)),
                ('northingred', models.FloatField(blank=True, db_column='northingred', null=True)),
                ('eastingred', models.FloatField(blank=True, db_column='eastingred', null=True)),
                ('northingpurple', models.FloatField(blank=True, db_column='northingpurple', null=True)),
                ('eastingpurple', models.FloatField(blank=True, db_column='eastingpurple', null=True)),
                ('partnership', models.CharField(blank=True, db_column='partnership', max_length=255, null=True)),
                ('duration', models.CharField(blank=True, db_column='duration', max_length=255, null=True)),
                ('effictive_date', models.DateTimeField(blank=True, db_column='effictive_date', null=True)),
                ('law_no', models.CharField(blank=True, db_column='law_no', max_length=255, null=True)),
                ('relinquisheddate_on', models.CharField(blank=True, db_column='relinquisheddate_on', max_length=255, null=True)),
                ('isactive', models.CharField(blank=True, db_column='isactive', max_length=255, null=True)),
            ],
            options={
                'db_table': 'concession_corners',
            },
        ),
        migrations.CreateModel(
            name='HcContent',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('hc_content', models.CharField(blank=True, db_column='hc_content', max_length=255, null=True)),
            ],
            options={
                'db_table': 'hc_content',
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('comp_id', models.AutoField(db_column='comp_id', primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, db_column='company_name', max_length=50, null=True)),
                ('location', models.CharField(blank=True, db_column='location', max_length=50, null=True)),
                ('address', models.CharField(blank=True, db_column='address', max_length=50, null=True)),
                ('phone1', models.CharField(blank=True, db_column='phone1', max_length=50, null=True)),
                ('phone2', models.CharField(blank=True, db_column='phone2', max_length=50, null=True)),
                ('phone3', models.CharField(blank=True, db_column='phone3', max_length=50, null=True)),
                ('phone4', models.CharField(blank=True, db_column='phone4', max_length=50, null=True)),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=50, null=True)),
                ('contact_person', models.CharField(blank=True, db_column='contact_person', max_length=50, null=True)),
                ('cont_pers_phone', models.CharField(blank=True, db_column='cont_pers_phone', max_length=50, null=True)),
                ('cont_pers_mobile', models.CharField(blank=True, db_column='cont_pers_mobile', max_length=50, null=True)),
            ],
            options={
                'db_table': 'operator',
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='name', max_length=50, null=True)),
                ('title', models.CharField(blank=True, db_column='title', max_length=50, null=True)),
                ('room', models.CharField(blank=True, db_column='room', max_length=50, null=True)),
                ('phone', models.CharField(blank=True, db_column='phone', max_length=50, null=True)),
                ('mrgrelation', models.CharField(blank=True, db_column='mrgrelation', max_length=50, null=True)),
                ('location', models.CharField(blank=True, db_column='location', max_length=50, null=True)),
                ('un', models.CharField(blank=True, db_column='un', max_length=50, null=True)),
                ('pw', models.CharField(blank=True, db_column='pw', max_length=50, null=True)),
                ('do_pdf_creation', models.BooleanField(blank=True, db_column='do_pdf_creation', null=True)),
                ('departmentid', models.IntegerField(blank=True, db_column='departmentid', null=True)),
                ('companyid', models.IntegerField(blank=True, db_column='companyid', null=True)),
            ],
            options={
                'db_table': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Provisional',
            fields=[
                ('prov_id', models.AutoField(db_column='prov_id', primary_key=True, serialize=False)),
                ('prov_name', models.CharField(blank=True, db_column='prov_name', max_length=50, null=True)),
                ('prov_from', models.CharField(blank=True, db_column='prov_from', max_length=50, null=True)),
                ('prov_interpreter_name', models.CharField(blank=True, db_column='prov_interpreter_name', max_length=50, null=True)),
                ('prov_interpreter_dept', models.IntegerField(blank=True, db_column='prov_interpreter_dept', null=True)),
                ('prov_dept', models.IntegerField(blank=True, db_column='prov_dept', null=True)),
                ('prov_inline', models.CharField(blank=True, db_column='prov_inline', max_length=50, null=True)),
                ('prov_xline', models.CharField(blank=True, db_column='prov_xline', max_length=50, null=True)),
                ('prov_lat', models.FloatField(blank=True, db_column='prov_lat', null=True)),
                ('prov_long', models.FloatField(blank=True, db_column='prov_long', null=True)),
                ('prov_east', models.FloatField(blank=True, db_column='prov_east', null=True)),
                ('prov_north', models.FloatField(blank=True, db_column='prov_north', null=True)),
                ('prov_date', models.DateField(blank=True, db_column='prov_date', default=datetime.date.today, null=True)),
                ('prov_type', models.CharField(blank=True, choices=[('Option', 'Option'), ('Final', 'Final')], db_column='prov_type', default='Option', max_length=50, null=True)),
                ('prov_seis_type', models.CharField(blank=True, db_column='prov_seis_type', max_length=2, null=True)),
                ('prov_remarks', models.TextField(blank=True, db_column='prov_remarks', null=True)),
                ('prov_concession', models.CharField(blank=True, db_column='prov_concession', max_length=50, null=True)),
                ('prov_checked_by', models.CharField(blank=True, db_column='prov_checked_by', max_length=50, null=True)),
                ('prov_checked_date', models.DateField(blank=True, db_column='prov_checked_date', null=True)),
                ('prov_rigname', models.CharField(blank=True, db_column='prov_rigname', max_length=255, null=True)),
                ('prov_spuddate', models.DateField(blank=True, db_column='prov_spuddate', null=True)),
                ('prov_spuddate_old', models.DateField(blank=True, db_column='prov_spuddate_old', null=True)),
                ('prov_militarypermit', models.CharField(blank=True, db_column='prov_military_permit', max_length=255, null=True)),
            ],
            options={
                'db_table': 'provisional',
            },
        ),
        migrations.CreateModel(
            name='Psd',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('psd_name', models.CharField(blank=True, db_column='psd', max_length=255, null=True)),
                ('alias', models.CharField(blank=True, db_column='alias', max_length=50, null=True)),
                ('ellipsoid', models.CharField(blank=True, db_column='ellipsoid', max_length=255, null=True)),
                ('datum', models.CharField(blank=True, db_column='datum', max_length=255, null=True)),
                ('datum_txt', models.CharField(blank=True, db_column='datum_txt', max_length=255, null=True)),
                ('projection', models.CharField(blank=True, db_column='projection', max_length=255, null=True)),
                ('epsg', models.IntegerField(blank=True, db_column='epsg', null=True)),
            ],
            options={
                'db_table': 'psd',
            },
        ),
        migrations.CreateModel(
            name='Psd_Datum',
            fields=[
                ('Datum_id', models.AutoField(db_column='datum_id', primary_key=True, serialize=False, unique=True)),
                ('datum', models.CharField(blank=True, db_column='datum', max_length=255, null=True)),
                ('ellipsoid_name', models.CharField(blank=True, db_column='ellipsoid', max_length=255, null=True)),
                ('epsg_code', models.IntegerField(blank=True, db_column='epsg', null=True)),
                ('remark', models.CharField(blank=True, db_column='remark', max_length=255, null=True)),
                ('toWgs84_dx_m', models.FloatField(blank=True, db_column='towgs84_dx_m', null=True)),
                ('toWgs84_dy_m', models.FloatField(blank=True, db_column='towgs84_dy_m', null=True)),
                ('toWgs84_dz_m', models.FloatField(blank=True, db_column='towgs84_dz_m', null=True)),
                ('toWgs84_rx_sec', models.FloatField(blank=True, db_column='towgs84_rx_sec', null=True)),
                ('toWgs84_ry_sec', models.FloatField(blank=True, db_column='towgs84_ry_sec', null=True)),
                ('toWgs84_rz_sec', models.FloatField(blank=True, db_column='towgs84_rz_sec', null=True)),
                ('toWgs84_sf_ppm', models.FloatField(blank=True, db_column='towgs84_sf_ppm', null=True)),
            ],
            options={
                'db_table': 'psd_datum',
            },
        ),
        migrations.CreateModel(
            name='Rig',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('rig', models.CharField(blank=True, db_column='rig', max_length=255, null=True)),
                ('rigfloorheight', models.FloatField(blank=True, db_column='rigfloorheight', null=True)),
                ('mastheight', models.CharField(blank=True, db_column='mastheight', max_length=255, null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='isactive', null=True)),
            ],
            options={
                'db_table': 'rig',
            },
        ),
        migrations.CreateModel(
            name='SeismicSurvey',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('openworksproject', models.CharField(blank=True, db_column='openworksproject', max_length=255, null=True)),
                ('seismicworksproject', models.CharField(blank=True, db_column='seismicworksproject', max_length=255, null=True)),
                ('year', models.CharField(blank=True, db_column='year', max_length=50, null=True)),
            ],
            options={
                'db_table': 'seismicsurvey',
            },
        ),
        migrations.CreateModel(
            name='Seismictype',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('seismictype', models.CharField(blank=True, db_column='seismictype', max_length=255, null=True)),
            ],
            options={
                'db_table': 'seismictype',
            },
        ),
        migrations.CreateModel(
            name='Seismicvintage',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('concession_id', models.IntegerField(blank=True, db_column='concession_id', null=True)),
                ('seismicvintage', models.CharField(blank=True, db_column='seismicvintage', max_length=255, null=True)),
                ('openworksproject', models.CharField(blank=True, db_column='openworksproject', max_length=255, null=True)),
                ('seismicworksproject', models.CharField(blank=True, db_column='seismicworksproject', max_length=255, null=True)),
                ('year', models.CharField(blank=True, db_column='year', max_length=50, null=True)),
                ('area_km', models.FloatField(blank=True, db_column='area_km', null=True)),
                ('path', models.CharField(blank=True, db_column='path', max_length=255, null=True)),
                ('oldpath', models.CharField(blank=True, db_column='oldpath', max_length=255, null=True)),
            ],
            options={
                'db_table': 'seismicvintage',
            },
        ),
        migrations.CreateModel(
            name='Staked',
            fields=[
                ('st_id', models.AutoField(db_column='st_id', primary_key=True, serialize=False)),
                ('st_lat', models.FloatField(blank=True, db_column='st_lat', null=True)),
                ('st_long', models.FloatField(blank=True, db_column='st_long', null=True)),
                ('st_east', models.FloatField(blank=True, db_column='st_east', null=True)),
                ('st_north', models.FloatField(blank=True, db_column='st_north', null=True)),
                ('st_elev', models.FloatField(blank=True, db_column='st_elev', null=True)),
                ('st_date', models.DateField(blank=True, db_column='st_date', null=True)),
                ('st_remarks', models.TextField(blank=True, db_column='st_remarks', null=True)),
                ('st_type', models.CharField(blank=True, choices=[('Option', 'Option'), ('Final', 'Final')], db_column='st_type', max_length=50, null=True)),
                ('equip_tech_id', models.IntegerField(blank=True, db_column='equip_tech_id', null=True)),
                ('usedcontrolgarminid', models.CharField(blank=True, db_column='usedcontrolgarminid', max_length=6, null=True)),
                ('tripscope', models.CharField(blank=True, db_column='tripscope', max_length=255, null=True)),
                ('tripid', models.IntegerField(blank=True, db_column='tripid', null=True)),
                ('tripstartdate', models.DateField(blank=True, db_column='tripstartdate', null=True)),
                ('tripenddate', models.DateField(blank=True, db_column='tripenddate', null=True)),
                ('garmineast', models.CharField(blank=True, db_column='garmineast', max_length=20, null=True)),
                ('garminnorth', models.CharField(blank=True, db_column='garminnorth', max_length=20, null=True)),
                ('garminlateg07', models.CharField(blank=True, db_column='garminlateg07', max_length=20, null=True)),
                ('garminlongeg07', models.CharField(blank=True, db_column='garminlongeg07', max_length=20, null=True)),
                ('handoverrep', models.IntegerField(blank=True, db_column='handoverrep', null=True)),
                ('facilitysurveyimage', models.TextField(blank=True, db_column='facilitysurveyimage', null=True)),
                ('tgojobpath', models.TextField(blank=True, db_column='tgojobpath', null=True)),
                ('transportationtosite', models.CharField(blank=True, db_column='transportationtosite', max_length=255, null=True)),
                ('transportationinsite', models.IntegerField(blank=True, db_column='transportationinsite', null=True)),
                ('imagepath', models.CharField(blank=True, db_column='imagepath', max_length=255, null=True)),
                ('controlused', models.CharField(blank=True, db_column='controlused', max_length=255, null=True)),
                ('st_by', models.ManyToManyField(related_name='persons_stake_by', to='wells.Persons')),
                ('st_sv', models.ForeignKey(blank=True, db_column='st_sv', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Persons')),
            ],
            options={
                'db_table': 'staked',
            },
        ),
        migrations.CreateModel(
            name='WellGeoinfo',
            fields=[
                ('well_id', models.AutoField(db_column='well_id', primary_key=True, serialize=False)),
                ('location', models.IntegerField(blank=True, db_column='location', null=True)),
                ('alias', models.CharField(blank=True, db_column='alias', max_length=25, null=True)),
                ('exploration_name', models.CharField(blank=True, db_column='exploration_name', max_length=255, null=True)),
                ('egpc_name', models.CharField(blank=True, db_column='egpc_name', max_length=255, null=True)),
                ('projects_name', models.CharField(blank=True, db_column='projects_name', max_length=50, null=True)),
                ('production_name', models.CharField(blank=True, db_column='production_name', max_length=255, null=True)),
                ('lat_EG_dd', models.FloatField(blank=True, db_column='lat_eg_dd', null=True)),
                ('long_EG_dd', models.FloatField(blank=True, db_column='long_eg_dd', null=True)),
                ('lat_red', models.FloatField(blank=True, db_column='lat_red', null=True)),
                ('long_red', models.FloatField(blank=True, db_column='long_red', null=True)),
                ('east_red', models.FloatField(blank=True, db_column='east_red', null=True)),
                ('north_red', models.FloatField(blank=True, db_column='north_red', null=True)),
                ('elevation', models.FloatField(blank=True, db_column='elevation', null=True)),
                ('meridian_conv', models.CharField(blank=True, db_column='meridian_conv', max_length=255, null=True)),
                ('magnetic_dec', models.CharField(blank=True, db_column='magnetic_dec', max_length=255, null=True)),
                ('deviated', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], db_column='deviated', default='No', max_length=255, null=True)),
                ('heightreference', models.IntegerField(blank=True, db_column='heightreference', null=True)),
                ('issued_date', models.DateField(blank=True, db_column='issued_date', null=True)),
                ('spud_date', models.DateField(blank=True, db_column='spud_date', null=True)),
                ('well_remarks', models.TextField(blank=True, db_column='well_remarks', null=True)),
                ('chk_id', models.IntegerField(blank=True, db_column='chk_id', null=True)),
                ('concession', models.ForeignKey(blank=True, db_column='concession_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Concession')),
                ('issued_by', models.ForeignKey(blank=True, db_column='issued_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Persons')),
                ('operator', models.ForeignKey(blank=True, db_column='operator', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Operator')),
                ('rig', models.ForeignKey(blank=True, db_column='rig', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Rig')),
            ],
            options={
                'verbose_name_plural': 'WellGeoinfo',
                'db_table': 'well_geoinfo',
            },
        ),
        migrations.CreateModel(
            name='WellStatus',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('well_status', models.CharField(blank=True, db_column='well_statu', max_length=255, null=True)),
                ('isoperating', models.BooleanField(blank=True, db_column='isoperating', null=True)),
            ],
            options={
                'verbose_name_plural': 'WellStatus',
                'db_table': 'well_status',
            },
        ),
        migrations.CreateModel(
            name='WellType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('well_type', models.CharField(blank=True, db_column='well_type', max_length=255, null=True)),
                ('arabicname', models.CharField(blank=True, db_column='arabicname', max_length=255, null=True)),
                ('groupname', models.CharField(blank=True, db_column='groupname', max_length=255, null=True)),
            ],
            options={
                'db_table': 'well_type',
            },
        ),
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('app_id', models.AutoField(db_column='app_id', primary_key=True, serialize=False)),
                ('app_well_info', models.IntegerField(blank=True, db_column='well_info_id', null=True, verbose_name='WellGeoinfo')),
                ('app_name', models.CharField(blank=True, db_column='app_name', max_length=50, null=True)),
                ('app_inline', models.CharField(blank=True, db_column='app_inline', max_length=50, null=True)),
                ('app_xline', models.CharField(blank=True, db_column='app_xline', max_length=50, null=True)),
                ('app_lat', models.FloatField(blank=True, db_column='app_lat', null=True)),
                ('app_long', models.FloatField(blank=True, db_column='app_long', null=True)),
                ('app_east', models.FloatField(blank=True, db_column='app_east', null=True)),
                ('app_north', models.FloatField(blank=True, db_column='app_north', null=True)),
                ('app_elev', models.FloatField(blank=True, db_column='app_elev', null=True)),
                ('app_date', models.DateField(blank=True, db_column='app_date', default=datetime.date.today, null=True)),
                ('app_remarks', models.TextField(blank=True, db_column='app_remarks', null=True)),
                ('app_type', models.CharField(blank=True, choices=[('Option', 'Option'), ('Final', 'Final')], db_column='app_type', default='Option', max_length=50, null=True)),
                ('prop', models.OneToOneField(blank=True, db_column='prop_id', null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='wells.Provisional')),
                ('appr_east_keyin', models.FloatField(blank=True, db_column='appr_east_keyin', null=True)),
                ('appr_north_keyin', models.FloatField(blank=True, db_column='appr_north_keyin', null=True)),
                ('calc_basedon', models.CharField(blank=True, db_column='calc_basedon', max_length=100, null=True)),
                ('meridian_conv_dbl', models.FloatField(blank=True, db_column='meridian_conv_dbl', null=True)),
            ],
            options={
                'db_table': 'approved',
            },
            bases=('wells.provisional',),
        ),
        migrations.AddField(
            model_name='wellgeoinfo',
            name='well_status',
            field=models.ForeignKey(blank=True, db_column='well_status', default=5, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.WellStatus'),
        ),
        migrations.AddField(
            model_name='wellgeoinfo',
            name='well_type',
            field=models.ForeignKey(blank=True, db_column='well_type', default=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.WellType'),
        ),
        migrations.AddField(
            model_name='staked',
            name='well_info',
            field=models.ForeignKey(blank=True, db_column='well_info_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.WellGeoinfo'),
        ),
        migrations.AddField(
            model_name='psd',
            name='datum_fk',
            field=models.ForeignKey(blank=True, db_column='datum_fk', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Psd_Datum'),
        ),
        migrations.AddField(
            model_name='provisional',
            name='projection',
            field=models.ForeignKey(blank=True, db_column='projection', default='2', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Psd'),
        ),
        migrations.AddField(
            model_name='provisional',
            name='prov_seismic_survey',
            field=models.ForeignKey(blank=True, db_column='prov_seismic_vintage', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Seismicvintage'),
        ),
        migrations.AddField(
            model_name='provisional',
            name='prov_well_type',
            field=models.ForeignKey(blank=True, db_column='prov_well_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.WellType'),
        ),
        migrations.AddField(
            model_name='provisional',
            name='well_info',
            field=models.ForeignKey(blank=True, db_column='well_info_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.WellGeoinfo'),
        ),
        migrations.AddField(
            model_name='concession',
            name='operator',
            field=models.ForeignKey(blank=True, db_column='operator', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Operator'),
        ),
        migrations.AddField(
            model_name='checked',
            name='chk_by',
            field=models.ManyToManyField(related_name='persons_checked_by', to='wells.Persons'),
        ),
        migrations.AddField(
            model_name='checked',
            name='chk_sv',
            field=models.ForeignKey(blank=True, db_column='chk_sv', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Persons'),
        ),
        migrations.AddField(
            model_name='checked',
            name='st',
            field=models.ForeignKey(blank=True, db_column='st_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Staked'),
        ),
        migrations.AddField(
            model_name='checked',
            name='well_info',
            field=models.ForeignKey(blank=True, db_column='well_info_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.WellGeoinfo'),
        ),
        migrations.AddField(
            model_name='bindata',
            name='seismicid',
            field=models.ForeignKey(blank=True, db_column='seismicid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Seismicvintage'),
        ),
        migrations.AddField(
            model_name='wellgeoinfo',
            name='app_id',
            field=models.ForeignKey(blank=True, db_column='app_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Approved'),
        ),
        migrations.AddField(
            model_name='staked',
            name='app',
            field=models.ForeignKey(blank=True, db_column='app_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wells.Approved'),
        ),
    ]
