# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ticket


# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    filter = (
        'title',
        'description',
        'status'
    )
    list_display = (
        'id',
        'title',
        'description',
        'status',
        'created_at'
    )