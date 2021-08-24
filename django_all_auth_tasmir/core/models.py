from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models, migrations


class User(AbstractUser):
    # Boolean fields to select the type of account.
    is_doctor = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)
    is_pharmacy = models.BooleanField(default=False)

    def apply_migration(apps, schema_editor):
        Group = apps.get_model('auth', 'Group')
        Group.objects.bulk_create([
            Group(name=u'group1'),
            Group(name=u'group2'),
            Group(name=u'group3'),
        ])


class Doctor(models.Model):
    doctor = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    degree = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    office_phone = models.CharField(max_length=255)
    nid_number = models.CharField(max_length=255)
    tin_number = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    bank_account_holder = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    bank_branch_name = models.CharField(max_length=255)
    bank_swift_code = models.CharField(max_length=255)

    def __str__(self):
        return self.doctor.username


class Lab(models.Model):
    lab = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lab_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    office_phone = models.CharField(max_length=255)
    nid_number = models.CharField(max_length=255)
    tin_number = models.CharField(max_length=255)

    def __str__(self):
        return self.lab.username


class Pharmacy(models.Model):
    pharmacy = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pharmacy_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    office_phone = models.CharField(max_length=255)
    nid_number = models.CharField(max_length=255)
    tin_number = models.CharField(max_length=255)

    def __str__(self):
        return self.pharmacy.username