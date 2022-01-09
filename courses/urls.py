from django.urls import path, include
from django.views.generic.base import View
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls))
]
