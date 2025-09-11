from django.contrib import admin
from .models import Alimentacao

class Alimentacao_admin(admin.ModelAdmin):
    search_fields = ['cafe_da_manha', 'almoco', 'lanche', 'janta']

admin.site.register()

