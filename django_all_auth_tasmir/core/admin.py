from django.contrib import admin
from core.models import User, Doctor, Lab, Pharmacy
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Lab)
admin.site.register(Pharmacy)