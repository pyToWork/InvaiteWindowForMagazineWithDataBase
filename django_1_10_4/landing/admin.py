from django.contrib import admin
from .models import *
# Register your models here.

class SubcriberAdmin(admin.ModelAdmin):
    #list_display=["Username","email"]
    list_display=[field.name for field in Subcriber._meta.fields]
    list_filter=["name"] # фильтр колонка для поиска
    #exclude,fields  исключить что то при показе в бд или добавить .Точнее что не показыват и что ПОказывать!
    search_fields=["name"]#поиск по имени! через запятую в скобках можно еще добавлять поля для поиска
    
    class Meta:
        model=Subcriber

admin.site.register(Subcriber,SubcriberAdmin)

