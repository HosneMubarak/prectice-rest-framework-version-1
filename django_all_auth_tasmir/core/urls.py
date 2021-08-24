from django.urls import path
from core.views import DoctorRegistrationView, LabRegistrationView, PharmacyRegistrationView, DoctorProfileView
app_name = 'core'

urlpatterns = [
    # Registration Urls
    path('registration/doctor/', DoctorRegistrationView.as_view(), name='register-doctor'),
    path('registration/lab/', LabRegistrationView.as_view(), name='register-lab'),
    path('registration/pharmacy/', PharmacyRegistrationView.as_view(), name='register-pharmacy'),
    # profile urls
    path('profile/doctor/', DoctorProfileView.as_view(), name='profile-doctor'),

]