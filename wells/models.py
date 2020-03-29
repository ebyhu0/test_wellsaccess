# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed =  True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
import datetime
# from django.contrib.gis.db import models

# class wells_11(models.Model):
#     objectid = models.AutoField(db_column='objectid',primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     # shape = models.Multi(db_column='program', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     def __str__(self):
#         return str(self.name)

#     class Meta:
#         verbose_name_plural='Bindata'
#         managed = False
#         db_table = 'wells_11'

class Bindata(models.Model):
    bg_id = models.AutoField(db_column='bg_id',primary_key=True)  # Field name made lowercase.
    area = models.CharField(db_column='area', max_length=50, blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(db_column='program', max_length=255, blank=True, null=True)  # Field name made lowercase.
    programold = models.CharField(db_column='programold', max_length=50, blank=True, null=True)  # Field name made lowercase.
    point = models.CharField(db_column='point', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inline = models.IntegerField(db_column='inline', blank=True, null=True)  # Field name made lowercase.
    xline = models.IntegerField(db_column='xline', blank=True, null=True)  # Field name made lowercase.
    east = models.FloatField(db_column='east', blank=True, null=True)  # Field name made lowercase.
    north = models.FloatField(db_column='north', blank=True, null=True)  # Field name made lowercase.
    psd = models.CharField(db_column='psd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='year', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    originalprojection = models.CharField(db_column='originalprojection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    displayprojection = models.CharField(db_column='displayprojection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #seismicid = models.IntegerField(db_column='seismicid', blank=True, null=True)  # Field name made lowercase.
    seismicid = models.ForeignKey('Seismicvintage', models.DO_NOTHING, db_column='seismicid', blank=True, null=True) # Field name made lowercase.
    #SeismicVentage = models.ForeignKey('Seismicvintage', models.DO_NOTHING, db_column='id', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.program)

    class Meta:
        verbose_name_plural='Bindata'
        managed = True
        db_table = 'bindata'

class Checked(models.Model):
    chk_cellar_CHOICES = (
        ('Corner1', 'Corner1'),
        ('Corner2', 'Corner2'),
        ('Corner3', 'Corner3'),
        ('Corner4', 'Corner4'),
        ('Center', 'Center'),
    )

    chk_id = models.AutoField(primary_key=True)
    chk_lat = models.FloatField(blank=True, null=True)
    chk_long = models.FloatField(blank=True, null=True)
    chk_east = models.FloatField(blank=True, null=True)
    chk_north = models.FloatField(blank=True, null=True)
    chk_elev = models.FloatField(blank=True, null=True)
    chk_cellar_pno = models.CharField(max_length=50,choices=chk_cellar_CHOICES, blank=True, null=True)
    # chk_by = models.CharField(max_length=50, blank=True, null=True)
    chk_by= models.ManyToManyField('Persons',related_name='persons_checked_by')
    chk_date = models.DateField(blank=True, null=True)
    # chk_sv = models.IntegerField(db_column='chk_sv', blank=True, null=True)  # Field name made lowercase.
    chk_sv = models.ForeignKey('Persons', models.DO_NOTHING, db_column='chk_sv', blank=True, null=True)  # Field name made lowercase.
    chk_remarks = models.TextField(db_column='chk_remarks', blank=True, null=True)  # Field name made lowercase.
    st = models.ForeignKey('Staked', models.DO_NOTHING, db_column='st_id', blank=True, null=True)  # Field name made lowercase.
    # st = models.IntegerField(db_column='st_id', blank=True, null=True)  # Field name made lowercase.
    well_info = models.ForeignKey('WellGeoinfo', on_delete=models.CASCADE, db_column='well_info_id', blank=True, null=True)  # Field name made lowercase.
    equip_tech_id = models.IntegerField(db_column='equip_tech_id', blank=True, null=True)  # Field name made lowercase.
    usedcontrolgarminid = models.CharField(db_column='usedcontrolgarminid', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tripscope = models.CharField(db_column='tripscope', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tripstartdate = models.DateField(db_column='tripstartdate', blank=True, null=True)  # Field name made lowercase.
    tripenddate = models.DateField(db_column='tripenddate', blank=True, null=True)  # Field name made lowercase.
    garminlateg07 = models.CharField(db_column='garminlateg07', max_length=20, blank=True, null=True)  # Field name made lowercase.
    garminlongeg07 = models.CharField(db_column='garminlongeg07', max_length=20, blank=True, null=True)  # Field name made lowercase.
    facilitysurveyimage = models.TextField(db_column='facilitysurveyimage', blank=True, null=True)  # Field name made lowercase.
    tgojobpath = models.TextField(db_column='tgojobpath', blank=True, null=True)  # Field name made lowercase.
    observedby = models.IntegerField(db_column='observedby', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'checked'


class Companies(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='phone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='phone2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone3 = models.CharField(db_column='phone3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone4 = models.CharField(db_column='phone4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact_person = models.CharField(db_column='contact_person', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cont_pers_phone = models.CharField(db_column='cont_pers_phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cont_pers_mobile = models.CharField(db_column='cont_pers_mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return str(self.name)
   
    class Meta:
        managed = True
        db_table = 'companies'


class Concession(models.Model):
    conctype_CHOICES = (
        (1, 'Concession'),
        (2, 'Development Lease'),
        (3, 'Released Concession'),
        (4, 'Unknown'),
    )

    tt = models.IntegerField(db_column='tt', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    concession = models.CharField(db_column='concession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    egpc_name = models.CharField(db_column='egpc_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field_name = models.CharField(db_column='field_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='area', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # arabicname = models.CharField(db_column='arabicname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    holder = models.CharField(db_column='holder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # operator = models.IntegerField(db_column='operator', blank=True, null=True)  # Field name made lowercase.
    operator = models.ForeignKey('Operator', models.DO_NOTHING, db_column='operator',to_field='comp_id', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isactive', blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='field2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='location', blank=True, null=True)  # Field name made lowercase.
    agreement_id = models.IntegerField(db_column='agreement_id', blank=True, null=True)  # Field name made lowercase.
    area_km2 = models.FloatField(db_column='area_km2', blank=True, null=True)  # Field name made lowercase.
    concessiontype = models.IntegerField(db_column='concessiontype',choices=conctype_CHOICES, blank=True, null=True)  # Field name made lowercase.
    

    def __str__(self):
        return str(self.concession)

    class Meta:
        managed = True
        db_table = 'concession'


class HcContent(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    hc_content = models.CharField(db_column='hc_content', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.hc_content

    class Meta:
        managed = True
        db_table = 'hc_content'


# class Heightreference(models.Model):
#     id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
#     heightreference = models.CharField(db_column='heightreference', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = True
#         db_table = 'heightreference'


# class MapPsdDescription(models.Model):
#     id = models.AutoField(primary_key=True)
#     map_psd = models.CharField(db_column='map_psd', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='description', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = True
#         db_table = 'map_psd_description'


class Operator(models.Model):
    comp_id = models.AutoField(db_column='comp_id',primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='company_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='phone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='phone2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone3 = models.CharField(db_column='phone3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone4 = models.CharField(db_column='phone4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact_person = models.CharField(db_column='contact_person', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cont_pers_phone = models.CharField(db_column='cont_pers_phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cont_pers_mobile = models.CharField(db_column='cont_pers_mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.company_name

    class Meta:
        managed = True
        db_table = 'operator'


class Psd_Datum(models.Model):
    Datum_id = models.AutoField(db_column='datum_id', primary_key=True,unique=True)  # Field name made lowercase.
    datum = models.CharField(db_column='datum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ellipsoid_name = models.CharField(db_column='ellipsoid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epsg_code =  models.IntegerField(db_column='epsg', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='remark', max_length=255, blank=True, null=True)  # Field name made lowercase.
    toWgs84_dx_m = models.FloatField(db_column='towgs84_dx_m', blank=True, null=True)  # Field name made lowercase.
    toWgs84_dy_m = models.FloatField(db_column='towgs84_dy_m', blank=True, null=True)  # Field name made lowercase.
    toWgs84_dz_m = models.FloatField(db_column='towgs84_dz_m', blank=True, null=True)  # Field name made lowercase.
    toWgs84_rx_sec = models.FloatField(db_column='towgs84_rx_sec', blank=True, null=True)  # Field name made lowercase.
    toWgs84_ry_sec = models.FloatField(db_column='towgs84_ry_sec', blank=True, null=True)  # Field name made lowercase.
    toWgs84_rz_sec = models.FloatField(db_column='towgs84_rz_sec', blank=True, null=True)  # Field name made lowercase.
    toWgs84_sf_ppm = models.FloatField(db_column='towgs84_sf_ppm', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.datum

    class Meta:
        managed = True
        db_table = 'psd_datum'

class Psd(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    psd_name = models.CharField(db_column='psd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='alias', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ellipsoid = models.CharField(db_column='ellipsoid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datum_fk = models.ForeignKey('Psd_Datum', models.DO_NOTHING, db_column='datum_fk',to_field='Datum_id', blank=True, null=True)  # Field name made lowercase.
    datum = models.CharField(db_column='datum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datum_txt = models.CharField(db_column='datum_txt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projection = models.CharField(db_column='projection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epsg =  models.IntegerField(db_column='epsg', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.epsg) + ": " + self.alias

    class Meta:
        managed = True
        db_table = 'psd'



class Seismictype(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    seismictype = models.CharField(db_column='seismictype', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.seismictype

    class Meta:
        managed = True
        db_table = 'seismictype'

class SeismicSurvey(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    openworksproject = models.CharField(db_column='openworksproject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seismicworksproject = models.CharField(db_column='seismicworksproject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='year', max_length=50, blank=True, null=True)  # Field name made lowercase.
           
    def __str__(self):
        return'{0} {1}'.format(self.openworksproject,self.seismicworksproject)

    class Meta:
        managed = True
        db_table = 'seismicsurvey'


class Seismicvintage(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    concession_id = models.IntegerField(db_column='concession_id', blank=True, null=True)  # Field name made lowercase.
    seismicvintage = models.CharField(db_column='seismicvintage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    openworksproject = models.CharField(db_column='openworksproject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seismicworksproject = models.CharField(db_column='seismicworksproject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='year', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area_km = models.FloatField(db_column='area_km', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='path', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oldpath = models.CharField(db_column='oldpath', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):

        return'{0} {1} {2}'.format(self.id,self.seismicvintage,self.seismicworksproject)


    class Meta:
        managed = True
        db_table = 'seismicvintage'


# class ProvApp(models.Model):
#     app_id = models.AutoField(db_column='app_id', primary_key=True)  # Field name made lowercase.
#     prov_id = models.IntegerField(db_column='prov_id')  # Field name made lowercase.
#     prov_name = models.CharField(db_column='prov_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_from = models.CharField(db_column='prov_from', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_interpreter_name = models.CharField(db_column='prov_interpreter_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_interpreter_dept = models.IntegerField(db_column='prov_interpreter_dept', blank=True, null=True)  # Field name made lowercase.
#     prov_dept = models.IntegerField(db_column='prov_dept', blank=True, null=True)  # Field name made lowercase.
#     prov_seismic_vintage = models.IntegerField(db_column='prov_seismic_vintage', blank=True, null=True)  # Field name made lowercase.
#     prov_inline = models.CharField(db_column='prov_inline', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_xline = models.CharField(db_column='prov_xline', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_lat = models.FloatField(db_column='prov_lat', blank=True, null=True)  # Field name made lowercase.
#     prov_long = models.FloatField(db_column='prov_long', blank=True, null=True)  # Field name made lowercase.
#     prov_east = models.FloatField(db_column='prov_east', blank=True, null=True)  # Field name made lowercase.
#     prov_north = models.FloatField(db_column='prov_north', blank=True, null=True)  # Field name made lowercase.
#     prov_date = models.DateField(db_column='prov_date', blank=True, null=True)  # Field name made lowercase.
#     prov_well_type = models.IntegerField(db_column='prov_well_type', blank=True, null=True)  # Field name made lowercase.
#     prov_type = models.CharField(db_column='prov_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_seis_type = models.CharField(db_column='prov_seis_type', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     prov_remarks = models.TextField(db_column='prov_remarks', blank=True, null=True)  # Field name made lowercase.
#     prov_concession = models.CharField(db_column='prov_concession', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_checked_by = models.CharField(db_column='prov_checked_by', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prov_checked_date = models.DateField(db_column='prov_checked_date', blank=True, null=True)  # Field name made lowercase.
#     prov_rigname = models.CharField(db_column='prov_rigname', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     prov_spuddate = models.DateField(db_column='prov_spuddate', blank=True, null=True)  # Field name made lowercase.
#     prov_spuddate_old = models.DateField(db_column='prov_spuddate_old', blank=True, null=True)  # Field name made lowercase.
#     app_name = models.CharField(db_column='app_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     app_inline = models.CharField(db_column='app_inline', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     app_xline = models.CharField(db_column='app_xline', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     app_lat = models.FloatField(db_column='app_lat', blank=True, null=True)  # Field name made lowercase.
#     app_long = models.FloatField(db_column='app_long', blank=True, null=True)  # Field name made lowercase.
#     app_east = models.FloatField(db_column='app_east', blank=True, null=True)  # Field name made lowercase.
#     app_north = models.FloatField(db_column='app_north', blank=True, null=True)  # Field name made lowercase.
#     app_elev = models.FloatField(db_column='app_elev', blank=True, null=True)  # Field name made lowercase.
#     app_date = models.DateField(db_column='app_date', blank=True, null=True)  # Field name made lowercase.
#     app_remarks = models.TextField(db_column='app_remarks', blank=True, null=True)  # Field name made lowercase.
#     app_type = models.CharField(db_column='app_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     # prop = models.ForeignKey('Provisional', models.DO_NOTHING, db_column='prop_id', blank=True, null=True)  # Field name made lowercase.
#     appr_east_keyin = models.FloatField(db_column='appr_east_keyin', blank=True, null=True)  # Field name made lowercase.
#     appr_north_keyin = models.FloatField(db_column='appr_north_keyin', blank=True, null=True)  # Field name made lowercase.
#     calc_basedon = models.CharField(db_column='calc_basedon', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projection = models.ForeignKey(Psd, models.DO_NOTHING, db_column='projection', blank=True, null=True)  # Field name made lowercase.
#     well_info = models.ForeignKey('WellGeoinfo', models.DO_NOTHING, db_column='well_info_id', blank=True, null=True)  # Field name made lowercase.

#     def __str__(self):
#         return str(self.app_name)
 
#     class Meta:
#         managed = True
#         db_table = 'provapp'


# class Approved(models.Model):
#     app_id = models.AutoField(db_column='app_id', primary_key=True)  # Field name made lowercase.
#     well_info = models.ForeignKey('WellGeoinfo', models.DO_NOTHING, db_column='well_info_id', blank=True, null=True)  # Field name made lowercase.
#     app_name = models.CharField(db_column='app_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     app_inline = models.CharField(db_column='app_inline', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     app_xline = models.CharField(db_column='app_xline', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     app_lat = models.FloatField(db_column='app_lat', blank=True, null=True)  # Field name made lowercase.
#     app_long = models.FloatField(db_column='app_long', blank=True, null=True)  # Field name made lowercase.
#     app_east = models.FloatField(db_column='app_east', blank=True, null=True)  # Field name made lowercase.
#     app_north = models.FloatField(db_column='app_north', blank=True, null=True)  # Field name made lowercase.
#     app_elev = models.FloatField(db_column='app_elev', blank=True, null=True)  # Field name made lowercase.
#     app_date = models.DateField(db_column='app_date', blank=True, null=True)  # Field name made lowercase.
#     app_remarks = models.TextField(db_column='app_remarks', blank=True, null=True)  # Field name made lowercase.
#     app_type = models.CharField(db_column='app_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prop = models.OneToOneField('Provisional', on_delete=models.CASCADE, db_column='prop_id', blank=True, null=True)  # Field name made lowercase.
#     appr_east_keyin = models.FloatField(db_column='appr_east_keyin', blank=True, null=True)  # Field name made lowercase.
#     appr_north_keyin = models.FloatField(db_column='appr_north_keyin', blank=True, null=True)  # Field name made lowercase.
#     calc_basedon = models.CharField(db_column='calc_basedon', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     def __str__(self):
#         return str(self.app_name)
 
#     class Meta:
#         managed = True
#         db_table = 'approved'


class Provisional(models.Model):
    OptionFinal_CHOICES = (
        ('Option', 'Option'),
        ('Final', 'Final'),
        )

    prov_id = models.AutoField(db_column='prov_id', primary_key=True)  # Field name made lowercase.
    prov_name = models.CharField(db_column='prov_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov_from = models.CharField(db_column='prov_from', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov_interpreter_name = models.CharField(db_column='prov_interpreter_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov_interpreter_dept = models.IntegerField(db_column='prov_interpreter_dept', blank=True, null=True)  # Field name made lowercase.
    prov_dept = models.IntegerField(db_column='prov_dept', blank=True, null=True)  # Field name made lowercase.
    # prov_seismic_vintage = models.IntegerField(db_column='prov_seismic_vintage', blank=True, null=True)  # Field name made lowercase.
    # prov_seismin_survey = models.ForeignKey('SeismicSurvey', models.DO_NOTHING, db_column='seismin_survey',default=1, blank=True, null=True)  # Field name made lowercase.
    # prov_seismic_survey = models.IntegerField(db_column='prov_seismic_vintage', blank=True, null=True)  # Field name made lowercase.
    prov_seismic_survey = models.ForeignKey(Seismicvintage, models.DO_NOTHING, db_column='prov_seismic_vintage', blank=True, null=True)  # Field name made lowercase.
    prov_inline = models.CharField(db_column='prov_inline', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov_xline = models.CharField(db_column='prov_xline', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov_lat = models.FloatField(db_column='prov_lat', blank=True, null=True)  # Field name made lowercase.
    prov_long = models.FloatField(db_column='prov_long', blank=True, null=True)  # Field name made lowercase.
    prov_east = models.FloatField(db_column='prov_east', blank=True, null=True)  # Field name made lowercase.
    prov_north = models.FloatField(db_column='prov_north', blank=True, null=True)  # Field name made lowercase.
    projection = models.ForeignKey(Psd, models.DO_NOTHING, db_column='projection',default='2', blank=True, null=True)  # Field name made lowercase.
    prov_date = models.DateField(db_column='prov_date', default=datetime.date.today, blank=True, null=True)  # Field name made lowercase.
    # prov_well_type = models.IntegerField(db_column='prov_well_type',choices=OptionFinal_CHOICES,default='Option', blank=True, null=True)  # Field name made lowercase.
    prov_well_type = models.ForeignKey("WellType", models.DO_NOTHING, db_column='prov_well_type', blank=True, null=True) # Field name made lowercase.
    prov_type = models.CharField(db_column='prov_type', max_length=50,choices=OptionFinal_CHOICES,default='Option', blank=True, null=True)  # Field name made lowercase.
    prov_seis_type = models.CharField(db_column='prov_seis_type', max_length=2, blank=True, null=True)  # Field name made lowercase.
    prov_remarks = models.TextField(db_column='prov_remarks', blank=True, null=True)  # Field name made lowercase.
    prov_concession = models.CharField(db_column='prov_concession', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov_checked_by = models.CharField(db_column='prov_checked_by', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov_checked_date = models.DateField(db_column='prov_checked_date', blank=True, null=True)  # Field name made lowercase.
    well_info = models.ForeignKey('WellGeoinfo', on_delete=models.CASCADE, db_column='well_info_id', blank=True, null=True)  # Field name made lowercase.
    prov_rigname = models.CharField(db_column='prov_rigname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prov_spuddate = models.DateField(db_column='prov_spuddate', blank=True, null=True)  # Field name made lowercase.
    prov_spuddate_old = models.DateField(db_column='prov_spuddate_old', blank=True, null=True)  # Field name made lowercase.
    prov_militarypermit= models.CharField(db_column='prov_military_permit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.prov_name


    class Meta:
        managed = True
        db_table = 'provisional'


class Approved(Provisional):
    
    OptionFinal_CHOICES = (
        ('Option', 'Option'),
        ('Final', 'Final'),
    )
    app_id = models.AutoField(db_column='app_id', primary_key=True)  # Field name made lowercase.
    app_well_info = models.IntegerField('WellGeoinfo',  db_column='well_info_id', blank=True, null=True)  # Field name made lowercase.
    app_name = models.CharField(db_column='app_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    app_inline = models.CharField(db_column='app_inline', max_length=50, blank=True, null=True)  # Field name made lowercase.
    app_xline = models.CharField(db_column='app_xline', max_length=50, blank=True, null=True)  # Field name made lowercase.
    app_lat = models.FloatField(db_column='app_lat', blank=True, null=True)  # Field name made lowercase.
    app_long = models.FloatField(db_column='app_long', blank=True, null=True)  # Field name made lowercase.
    app_east = models.FloatField(db_column='app_east', blank=True, null=True)  # Field name made lowercase.
    app_north = models.FloatField(db_column='app_north', blank=True, null=True)  # Field name made lowercase.
    app_elev = models.FloatField(db_column='app_elev', blank=True, null=True)  # Field name made lowercase.
    app_date = models.DateField(db_column='app_date', default=datetime.date.today, blank=True, null=True) # Field name made lowercase.
    app_remarks = models.TextField(db_column='app_remarks', blank=True, null=True)  # Field name made lowercase.
    app_type = models.CharField(db_column='app_type', max_length=50,choices=OptionFinal_CHOICES,default='Option', blank=True, null=True)  # Field name made lowercase.
    prop = models.OneToOneField('Provisional', on_delete=models.CASCADE, db_column='prop_id',parent_link=True, blank=True, null=True)  # Field name made lowercase.
    appr_east_keyin = models.FloatField(db_column='appr_east_keyin', blank=True, null=True)  # Field name made lowercase.
    appr_north_keyin = models.FloatField(db_column='appr_north_keyin', blank=True, null=True)  # Field name made lowercase.
    calc_basedon = models.CharField(db_column='calc_basedon', max_length=100, blank=True, null=True)  # Field name made lowercase.
    meridian_conv_dbl = models.FloatField(db_column='meridian_conv_dbl', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.app_id) + ":"+ str(self.app_name) + "--" + str(self.prov_name)  
 
    class Meta:
        managed = True
        db_table = 'approved'

class Rig(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)  # Field name made lowercase.
    rig = models.CharField(db_column='rig', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rigfloorheight = models.FloatField(db_column='rigfloorheight', blank=True, null=True)  # Field name made lowercase.
    mastheight = models.CharField(db_column='mastheight', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isactive', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.rig

    class Meta:
        managed = True
        db_table = 'rig'


class Staked(models.Model):
    OptionFinal_CHOICES = (
        ('Option', 'Option'),
        ('Final', 'Final'),
    )

    st_id = models.AutoField(db_column='st_id', primary_key=True)  # Field name made lowercase.
    st_lat = models.FloatField(db_column='st_lat', blank=True, null=True)  # Field name made lowercase.
    st_long = models.FloatField(db_column='st_long', blank=True, null=True)  # Field name made lowercase.
    st_east = models.FloatField(db_column='st_east', blank=True, null=True)  # Field name made lowercase.
    st_north = models.FloatField(db_column='st_north', blank=True, null=True)  # Field name made lowercase.
    st_elev = models.FloatField(db_column='st_elev', blank=True, null=True)  # Field name made lowercase.
    st_date = models.DateField(db_column='st_date', blank=True, null=True)  # Field name made lowercase.
    # tags = ArrayField(models.CharField(max_length=200), blank=True)
    # pieces = ArrayField(ArrayField(models.IntegerField()))
    # st_by_array= ArrayField(models.IntegerField(),default=(1,2))
    # st_by = models.CharField(db_column='st_by', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_by= models.ManyToManyField('Persons',related_name='persons_stake_by')
    # st_by = models.CharField(db_column='st_by', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # st_sv = models.IntegerField(db_column='st_sv', blank=True, null=True)  # Field name made lowercase.
    st_sv = models.ForeignKey('Persons', models.DO_NOTHING, db_column='st_sv', blank=True, null=True)  # Field name made lowercase.
    st_remarks = models.TextField(db_column='st_remarks', blank=True, null=True)  # Field name made lowercase.
    st_type = models.CharField(db_column='st_type', max_length=50,choices=OptionFinal_CHOICES, blank=True, null=True)  # Field name made lowercase.
    app = models.ForeignKey(Approved, models.DO_NOTHING, db_column='app_id', blank=True, null=True)  # Field name made lowercase.
    well_info = models.ForeignKey('WellGeoinfo', on_delete=models.CASCADE, db_column='well_info_id', blank=True, null=True)  # Field name made lowercase.
    equip_tech_id = models.IntegerField(db_column='equip_tech_id', blank=True, null=True)  # Field name made lowercase.
    usedcontrolgarminid = models.CharField(db_column='usedcontrolgarminid', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tripscope = models.CharField(db_column='tripscope', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tripid = models.IntegerField(db_column='tripid', blank=True, null=True)  # Field name made lowercase.
    tripstartdate = models.DateField(db_column='tripstartdate', blank=True, null=True)  # Field name made lowercase.
    tripenddate = models.DateField(db_column='tripenddate', blank=True, null=True)  # Field name made lowercase.
    garmineast = models.CharField(db_column='garmineast', max_length=20, blank=True, null=True)  # Field name made lowercase.
    garminnorth = models.CharField(db_column='garminnorth', max_length=20, blank=True, null=True)  # Field name made lowercase.
    garminlateg07 = models.CharField(db_column='garminlateg07', max_length=20, blank=True, null=True)  # Field name made lowercase.
    garminlongeg07 = models.CharField(db_column='garminlongeg07', max_length=20, blank=True, null=True)  # Field name made lowercase.
    handoverrep = models.IntegerField(db_column='handoverrep', blank=True, null=True)  # Field name made lowercase.
    facilitysurveyimage = models.TextField(db_column='facilitysurveyimage', blank=True, null=True)  # Field name made lowercase.
    tgojobpath = models.TextField(db_column='tgojobpath', blank=True, null=True)  # Field name made lowercase.
    transportationtosite = models.CharField(db_column='transportationtosite', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transportationinsite = models.IntegerField(db_column='transportationinsite', blank=True, null=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='imagepath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    controlused = models.CharField(db_column='controlused', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.st_id) + ": " + str(self.st_east) + ", " + str(self.st_north)

    class Meta:
        managed = True
        db_table = 'staked'


class WellType(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    well_type = models.CharField(db_column='well_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arabicname = models.CharField(db_column='arabicname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='groupname', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.well_type


    class Meta:
        managed = True
        db_table = 'well_type'


class WellStatus(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    well_status = models.CharField(db_column='well_statu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isoperating = models.BooleanField(db_column='isoperating', blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return self.well_status


    class Meta:
        verbose_name_plural='WellStatus'
        managed = True
        db_table = 'well_status'

class Production_Field(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)  # Field name made lowercase.
    field_name = models.CharField(db_column='production_field_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    

    def __str__(self):
        return self.field_name


    class Meta:
        verbose_name_plural='Production_Fields'
        managed = True
        db_table = 'production_field'        

class WellGeoinfo(models.Model):
    Deviated_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Unknown', 'Unknown')
        )

    well_id = models.AutoField(db_column='well_id', primary_key=True)  # Field name made lowercase.
    # well_id = models.IntegerField(db_column='well_id2', blank=False, null=False)  # Field name made lowercase.
    concession = models.ForeignKey(Concession, models.DO_NOTHING, db_column='concession_id', blank=True, null=True)  # Field name made lowercase.
    production_field = models.ForeignKey(Production_Field, models.DO_NOTHING, db_column='production_field_id', blank=True, null=True)  # Field name made lowercase.

    app_id = models.ForeignKey(Approved, models.DO_NOTHING, db_column='app_id', blank=True, null=True)  # Field name made lowercase.
    # concession_txt = models.CharField(db_column='concession_txt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # arabicnameconcession = models.CharField(db_column='arabicnameconcession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='location', blank=True, null=True)  # Field name made lowercase.
 
    # operator = models.IntegerField(db_column='operator', blank=True, null=True)  # Field name made lowercase.
    operator = models.ForeignKey('Operator', models.DO_NOTHING, db_column='operator',to_field='comp_id',related_name='operator', blank=True, null=True)  # Field name made lowercase.
    owner_original = models.ForeignKey('Operator', models.DO_NOTHING, db_column='owner_original',to_field='comp_id',related_name='owner_original', blank=True, null=True)  # Field name made lowercase.
 
    alias = models.CharField(db_column='alias', max_length=25, blank=True, null=True)  # Field name made lowercase.
    # arabicnamewell = models.CharField(db_column='arabicnamewell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # proposedname = models.CharField(db_column='proposedname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    
    exploration_name = models.CharField(db_column='exploration_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    openworks_name = models.CharField(db_column='openworks_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    egpc_name = models.CharField(db_column='egpc_name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    wims_name_shell = models.CharField(db_column='wims_name_shell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uwi_operation_shell = models.CharField(db_column='uwi_operation_shell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uwi_exploration_shell = models.CharField(db_column='uwi_exploration_shell', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sap_functional_location = models.CharField(db_column='sap_functional_location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sap_name = models.CharField(db_column='sap_name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    projects_name = models.CharField(db_column='projects_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    production_name = models.CharField(db_column='production_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # lat_EG_dd = models.FloatField(db_column='lat_eg_dd', blank=True, null=True)  # Field name made lowercase.
    # long_EG_dd = models.FloatField(db_column='long_eg_dd', blank=True, null=True)  # Field name made lowercase.
    lat_red = models.FloatField(db_column='lat_red', blank=True, null=True)  # Field name made lowercase.
    long_red = models.FloatField(db_column='long_red', blank=True, null=True)  # Field name made lowercase.
    east_red = models.FloatField(db_column='east_red', blank=True, null=True)  # Field name made lowercase.
    north_red = models.FloatField(db_column='north_red', blank=True, null=True)  # Field name made lowercase.
    elevation = models.FloatField(db_column='elevation', blank=True, null=True)  # Field name made lowercase.
    # rig = models.IntegerField(db_column='rig', blank=True, null=True)  # Field name made lowercase.
    rig = models.ForeignKey(Rig, models.DO_NOTHING, db_column='rig', blank=True, null=True)  # Field name made lowercase.
    meridian_conv = models.CharField(db_column='meridian_conv', max_length=255, blank=True, null=True)  # Field name made lowercase.
    magnetic_dec = models.CharField(db_column='magnetic_dec', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # well_type = models.IntegerField(db_column='well_type', blank=True, null=True)  # Field name made lowercase.
    well_type = models.ForeignKey(WellType, models.DO_NOTHING, db_column='well_type', default=2, blank=True, null=True) # Field name made lowercase.
    # well_type_txt = models.CharField(db_column='well_type_txt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deviated = models.CharField(db_column='deviated',max_length=255,choices=Deviated_CHOICES, default='No', blank=True, null=True)  # Field name made lowercase.
    # well_status = models.IntegerField(db_column='well_status', blank=True, null=True)  # Field name made lowercase.
    well_status = models.ForeignKey(WellStatus, models.DO_NOTHING, db_column='well_status', default=5, blank=True, null=True) # Field name made lowercase.
    # well_status_txt = models.CharField(db_column='well_status_txt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    heightreference = models.IntegerField(db_column='heightreference', blank=True, null=True)  # Field name made lowercase.
    issued_by = models.ForeignKey('Persons', models.DO_NOTHING, db_column='issued_by', blank=True, null=True)  #models.IntegerField(db_column='issued_by', blank=True, null=True)  # Field name made lowercase.
    issued_date = models.DateField(db_column='issued_date', blank=True, null=True)  # Field name made lowercase.
    # spuddate_drillseq = models.DateField(db_column='spuddate_drillseq', blank=True, null=True)  # Field name made lowercase.
    # spuddate_drillseq = models.DateField(db_column='spuddate_drillseq', default=datetime.date.today, blank=True, null=True)   # Field name made lowercase.
    # spud_date = models.DateField(db_column='spud_date', blank=True, null=True)  # Field name made lowercase.
    # spud_date = models.DateField(db_column='spud_date',  default=datetime.date.today, blank=True, null=True)  # Field name made lowercase.
    spud_date = models.DateField(db_column='spud_date', blank=True, null=True)  # Field name made lowercase.
    well_remarks = models.TextField(db_column='well_remarks', blank=True, null=True)  # Field name made lowercase.
    # left_scale = models.IntegerField(db_column='left_scale', blank=True, null=True)  # Field name made lowercase.
    # right_scale = models.IntegerField(db_column='right_scale', blank=True, null=True)  # Field name made lowercase.
    chk_id = models.IntegerField(db_column='chk_id', blank=True, null=True)  # Field name made lowercase.
    # chartview = models.BooleanField(db_column='chartview', blank=True, null=True)  # Field name made lowercase.
    # prov_rigname = models.CharField(db_column='prov_rigname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # prov_spuddate = models.DateField(db_column='prov_spuddate', blank=True, null=True)  # Field name made lowercase.
    # militarypermitid = models.IntegerField(db_column='militarypermitid', blank=True, null=True)  # Field name made lowercase.
    # militarypermitdate = models.DateField(db_column='militarypermitdate', blank=True, null=True)  # Field name made lowercase.
    # militaryrenewpermitdate = models.DateField(db_column='militaryrenewpermitdate', blank=True, null=True)  # Field name made lowercase.
    # militaryapproval = models.IntegerField(db_column='militaryapproval', blank=True, null=True)  # Field name made lowercase.
    # militaryapprovaldate = models.DateField(db_column='militaryapprovaldate', blank=True, null=True)  # Field name made lowercase.
    # militaryapprovalnumber = models.CharField(db_column='militaryapprovalnumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # guardfamilyid = models.IntegerField(db_column='guardfamilyid', blank=True, null=True)  # Field name made lowercase.
    # boundary400mbuffer = models.CharField(db_column='boundary400mbuffer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # militarymap100id = models.IntegerField(db_column='militarymap100id', blank=True, null=True)  # Field name made lowercase.
    # arguppergrosstotal = models.FloatField(db_column='arguppergrosstotal', blank=True, null=True)  # Field name made lowercase.
    # arguppernettotal = models.FloatField(db_column='arguppernettotal', blank=True, null=True)  # Field name made lowercase.
    # argupperporosity = models.FloatField(db_column='argupperporosity', blank=True, null=True)  # Field name made lowercase.
    # formationobjectives = models.CharField(db_column='formationobjectives', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # t_depth = models.IntegerField(db_column='t_depth', blank=True, null=True)  # Field name made lowercase.
    # meridian_conv_dbl = models.FloatField(db_column='meridian_conv_dbl', blank=True, null=True)  # Field name made lowercase.

    # def get_queryset(self):
    # return Approved.objects.filter(pub_date__lte=timezone.now(), choice__count__gt=0)

    def get_absolute_url(self):
        return reverse("update-well-view", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.exploration_name
    
    # @property
    # def formatedlat(self):
    #     # "Returns the person's full name."
    #     # return '%s, %s %s' % (self.lastname, self.firstname, self.middlename)
    #     latstr=str(self.lat_red)
    #     return (latstr[:2] + "°" + latstr[2:4] + "'" + latstr[4:] + "N")
    # # formatedlat = property(getformatedlat)

    class Meta:
        ordering = ('exploration_name',)
        verbose_name_plural='WellGeoinfo'
        managed = True
        db_table = 'well_geoinfo'





class Persons(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    room = models.CharField(db_column='room', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mrgrelation = models.CharField(db_column='mrgrelation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='un', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pw = models.CharField(db_column='pw', max_length=50, blank=True, null=True)  # Field name made lowercase.
    do_pdf_creation = models.BooleanField(db_column='do_pdf_creation', blank=True, null=True)  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='departmentid', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='companyid', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        db_table = 'persons'

class ConcessionCorners(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)  # Field name made lowercase.
    objectid_1 = models.FloatField(db_column='objectid_1', blank=True, null=True)  # Field name made lowercase.
    concessionid = models.CharField(db_column='concessionid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lnm = models.CharField(db_column='lnm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pno = models.IntegerField(db_column='pno', blank=True, null=True)  # Field name made lowercase.
    pointtype = models.CharField(db_column='pointtype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude_egy07 = models.CharField(db_column='latitude_egy07', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude_egy07 = models.CharField(db_column='longitude_egy07', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude_wgs84 = models.CharField(db_column='latitude_wgs84', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude_wgs84 = models.CharField(db_column='longitude_wgs84', max_length=255, blank=True, null=True)  # Field name made lowercase.
    northingred = models.FloatField(db_column='northingred', blank=True, null=True)  # Field name made lowercase.
    eastingred = models.FloatField(db_column='eastingred', blank=True, null=True)  # Field name made lowercase.
    northingpurple = models.FloatField(db_column='northingpurple', blank=True, null=True)  # Field name made lowercase.
    eastingpurple = models.FloatField(db_column='eastingpurple', blank=True, null=True)  # Field name made lowercase.
    partnership = models.CharField(db_column='partnership', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    effictive_date = models.DateTimeField(db_column='effictive_date', blank=True, null=True)  # Field name made lowercase.
    law_no = models.CharField(db_column='law_no', max_length=255, blank=True, null=True)  # Field name made lowercase.
    relinquisheddate_on = models.CharField(db_column='relinquisheddate_on', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='isactive', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'concession_corners'