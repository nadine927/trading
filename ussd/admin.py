from django.contrib import admin
from .models import *
# Register your models here.

class IdafarmuserAdmin (admin.ModelAdmin):
    list_display =['phoneNumber', 'names']
    search_fields =['phoneNumber']

admin.site.register(Idafarmuser, IdafarmuserAdmin)