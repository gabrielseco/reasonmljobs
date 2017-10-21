# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from company.api import CompanyViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    url(r'1.0/', include(router.urls)),
    url(r'1.0/login', obtain_jwt_token),
]