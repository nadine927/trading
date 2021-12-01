from django.contrib import admin
from .models import *  #importing all models
# Register your models here.

class IdafarmuserAdmin (admin.ModelAdmin):
    list_display =['phoneNumber', 'names']
    search_fields =['phoneNumber']

class IteganyagiheAdmin (admin.ModelAdmin):
    list_display = ['phonNumber', 'category']
    search_fields = ['phonNumber', 'category']


admin.site.register(Idafarmuser, IdafarmuserAdmin)
admin.site.register(Iteganyagihe, IteganyagiheAdmin)