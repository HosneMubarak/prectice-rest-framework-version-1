from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

# from core.models import Seller, Buyer
from core.models import Doctor, Pharmacy, Lab

from django.contrib.auth.models import Group


class DoctorCustomRegistrationSerializer(RegisterSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    degree = serializers.CharField(required=True)
    # address = serializers.CharField(required=True)
    # hospital = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(DoctorCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'degree': self.validated_data.get('degree', ''),
            # 'address': self.validated_data.get('address', ''),
            # 'hospital': self.validated_data.get('hospital', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(DoctorCustomRegistrationSerializer, self).save(request)
        user.is_doctor = True
        group = Group.objects.get(name='Doctor')
        user.groups.add(group)
        user.save()
        doctor = Doctor(doctor=user, degree=self.cleaned_data.get('degree'),
                        # address=self.cleaned_data.get('address'),
                        # hospital=self.cleaned_data.get('hospital')
                        )
        doctor.save()
        return user


class LabCustomRegistrationSerializer(RegisterSerializer):
    lab = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    lab_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(LabCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'lab_name': self.validated_data.get('lab_name', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(LabCustomRegistrationSerializer, self).save(request)
        user.is_lab = True
        group = Group.objects.get(name='Lab')
        user.groups.add(group)
        user.save()
        lab = Lab(lab=user, lab_name=self.cleaned_data.get('lab_name'))
        lab.save()
        return user


class PharmacyCustomRegistrationSerializer(RegisterSerializer):
    pharmacy = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    pharmacy_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(PharmacyCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'pharmacy_name': self.validated_data.get('pharmacy_name', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(PharmacyCustomRegistrationSerializer, self).save(request)
        user.is_pharmacy = True
        group = Group.objects.get(name='Pharmacy')
        user.groups.add(group)
        user.save()
        pharmacy = Pharmacy(pharmacy=user, pharmacy_name=self.cleaned_data.get('pharmacy_name'))
        pharmacy.save()
        return user


class DoctorCustomProfileSerializer(RegisterSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    degree = serializers.CharField(required=True)
    address = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)
    office_phone = serializers.CharField(max_length=255)
    nid_number = serializers.CharField(max_length=255)
    tin_number = serializers.CharField(max_length=255)
    hospital = serializers.CharField(max_length=255)
    bank_name = serializers.CharField(max_length=255)
    bank_account_holder = serializers.CharField(max_length=255)
    bank_account_number = serializers.CharField(max_length=255)
    bank_branch_name = serializers.CharField(max_length=255)
    bank_swift_code = serializers.CharField(max_length=255)

    def get_cleaned_data(self):
        data = super(DoctorCustomProfileSerializer, self).get_cleaned_data()
        extra_data = {
            'degree': self.validated_data.get('degree', ''),
            'address': self.validated_data.get('address', ''),
            'phone': self.validated_data.get('phone', ''),
            'office_phone': self.validated_data.get('office_phone', ''),
            'nid_number': self.validated_data.get('nid_number', ''),
            'tin_number': self.validated_data.get('tin_number', ''),
            'bank_name': self.validated_data.get('bank_name', ''),
            'bank_account_holder': self.validated_data.get('bank_account_holder', ''),
            'bank_account_number': self.validated_data.get('bank_account_number', ''),
            'bank_branch_name': self.validated_data.get('bank_branch_name', ''),
            'bank_swift_code': self.validated_data.get('bank_swift_code', ''),
        }
        data.update(extra_data)
        return data
