from django.urls import path

from code_manager import views

urlpatterns = [
    path('check', views.check_code),
]
