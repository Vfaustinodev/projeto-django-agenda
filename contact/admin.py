from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')
    ordering = 'id', 
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10 #Limita quantidas de contatos por página
    list_max_show_all = 200 #Limita a quantidade de contatos que podem ser mostrados no "Mostrar Tudo"
    # list_editable = 'first_name', 'last_name', #Não é muito bom a utilização e não pode ser utilizado com list_display_links
    list_display_links = 'id', 'first_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = 'id', 