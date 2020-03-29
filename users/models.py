from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Contact(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    # identity = models.ManyToManyField(
    #     'Identity',  blank=True, null=True, related_name='contact_ids')

    # Field name made lowercase.
    nationality = models.ForeignKey(
        'Country', on_delete=models.CASCADE, db_column='country_id', blank=True, null=True)
    email = models.ManyToManyField('Email', blank=True, null=True)
    phone = models.ManyToManyField('Phone', blank=True, null=True)
    address = models.ManyToManyField('Address', blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'contact'


class Identity(models.Model):
    id_type_lookup = (
        ('NtnlId', 'National ID'),
        ('BrthCrt', 'Birth certificat'),
        ('PasPrt', 'Passport'),
    )

    id = models.AutoField(db_column='id', primary_key=True)
    id_number = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=250)
    birth_date = models.DateField(blank=True, null=True)

    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    id_type = models.CharField(max_length=25, choices=id_type_lookup)
    address = models.CharField(max_length=250, blank=True, null=True)

    contact = models.ForeignKey(
        'Contact', on_delete=models.CASCADE, db_column='contact_id', blank=False, null=False)
    nationality = models.ForeignKey('Country', on_delete=models.CASCADE,
                                    db_column='country_id', blank=True, null=True)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE,
                              db_column='photo_id', blank=True, null=True)
    # photo

    def __str__(self):
        return self.name

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'identity'


class Country(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=256, blank=False, null=False)
    nationality = models.CharField(max_length=256, blank=True, null=True)
    Arabicname = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Countries'
        managed = True
        db_table = 'country'


class Email(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    email = models.EmailField(max_length=254, blank=True)
    email_name = models.CharField(max_length=100, blank=True, null=True)
    email_server = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'email'


class Phone(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    number1 = models.CharField(max_length=25, blank=False, null=False)
    country_code = models.CharField(max_length=5, blank=False, null=False)
    city_code = models.CharField(max_length=3, blank=False, null=False)

    # Field name made lowercase.
    is_active = models.BooleanField(
        db_column='is_active', blank=True, null=True)
    is_fax = models.BooleanField(db_column='is_fax', blank=True, null=True)
    is_voice = models.BooleanField(db_column='is_voice', blank=True, null=True)
    is_direct = models.BooleanField(
        db_column='is_direct', blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'phone'


class Address(models.Model):
    address_type_lookup = (
        ('Building', 'Building'),
        ('Mall', 'Mall'),
        ('Flat', 'Flat'),
        ('Room', 'Room'),
        ('Factory', 'Factory'),
        ('Store', 'Store'),
        ('ShowRoom', 'ShowRoom'),
    )

    id = models.AutoField(db_column='id', primary_key=True)
    address = models.CharField(max_length=25, blank=False, null=False)
    district = models.CharField(max_length=25, blank=True, null=True)
    floor = models.CharField(max_length=25, blank=True, null=True)
    flat_no = models.CharField(max_length=25, blank=True, null=True)

    city = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=25, blank=True, null=True)
    address_type = models.CharField(
        max_length=25, choices=address_type_lookup, blank=True, null=True)

    # contacts=models.ManyToManyField('Contact',)
    def __str__(self):
        return self.address

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'address'


class Photo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'photo'


class Organization(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=250)

    start_date = models.DateField(blank=True, null=True)
    is_branch = models.BooleanField(
        db_column='is_branch', blank=True, null=True)

    parent = models.ForeignKey(
        'Organization', on_delete=models.CASCADE, db_column='parent_id', blank=True, null=True)

    # Field name made lowercase.
    nationality = models.ForeignKey(
        'Country', on_delete=models.CASCADE, db_column='country_id', blank=True, null=True)
    email = models.ManyToManyField('Email', blank=True, null=True)
    phone = models.ManyToManyField('Phone', blank=True, null=True)
    address = models.ManyToManyField('Address', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'organization'


class Department(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=250)
    organization = models.ForeignKey(
        'Organization', on_delete=models.CASCADE, db_column='organization_id', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    # parent = models.ManyToManyField(
    #     'Department', through='Department_Department', through_fields=('parent_id', 'child_id'), blank=True, null=True)

    # email = models.ManyToManyField('Email', blank=True, null=True)
    # objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'department'


class Department_Department(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)

    parent_id = models.ForeignKey(
        'Department', on_delete=models.CASCADE, db_column='parent_id', blank=True, null=True, related_name='parent_id')
    child_id = models.ForeignKey(
        'Department', on_delete=models.CASCADE, db_column='child_id', blank=True, null=True, related_name='child_id')

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.parent_id.name + "_" + self.child_id.name

    class Meta:
        # verbose_name_plural='Contacts'
        managed = True
        db_table = 'department_department'
