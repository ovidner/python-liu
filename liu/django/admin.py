# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import LiUID


@admin.register(LiUID)
class LiUIDAdmin(admin.ModelAdmin):
    pass
