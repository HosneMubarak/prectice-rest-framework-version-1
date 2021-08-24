
from django.contrib import admin
from django.urls import path, include
from cbvApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('student/', views.StudentList.as_view()),
#     path('student/<int:pk>', views.StudentDetails.as_view())
# ]
