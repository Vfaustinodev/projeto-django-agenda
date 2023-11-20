from django.urls import path
from contact import views

# Criar name espace para evitar que arquivos com mesmo nome crie problemas
# Exemplo de name espace abaixo com app_name
app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
