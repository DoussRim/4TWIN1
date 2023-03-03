from django.contrib import admin
from .models import Person
# Register your models here.
@admin.register(Person)
class Recherche(admin.ModelAdmin):
    search_fields=['username']
# admin.site.register(Person,Recherche)
