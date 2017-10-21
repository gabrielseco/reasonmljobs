# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'url')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Company, CompanyAdmin)
