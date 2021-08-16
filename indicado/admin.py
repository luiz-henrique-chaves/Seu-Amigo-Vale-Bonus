from django.contrib import admin
from .models import Indicado


@admin.register(Indicado)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'bonus', 'status')
    search_fields = ('nome', 'telefone', 'email',)
