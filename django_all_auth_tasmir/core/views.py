from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from core.serializers import (
    DoctorCustomRegistrationSerializer, LabCustomRegistrationSerializer, PharmacyCustomRegistrationSerializer,
    DoctorCustomProfileSerializer
)


class DoctorRegistrationView(RegisterView):
    serializer_class = DoctorCustomRegistrationSerializer


class LabRegistrationView(RegisterView):
    serializer_class = LabCustomRegistrationSerializer


class PharmacyRegistrationView(RegisterView):
    serializer_class = PharmacyCustomRegistrationSerializer


class DoctorProfileView(RegisterView):
    serializer_class = DoctorCustomProfileSerializer
