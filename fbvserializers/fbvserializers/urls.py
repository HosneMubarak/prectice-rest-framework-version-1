
from django.contrib import admin
from django.urls import path
from fbvApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students', views.student_list),
    path('students/<int:pk>', views.student_details),
]
