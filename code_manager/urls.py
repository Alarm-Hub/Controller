from django.urls import include, path
from rest_framework import routers
from code_manager import views

router = routers.DefaultRouter()
router.register(r'codes', views.CodeView)


urlpatterns = [
    path('', include(router.urls)),
]
