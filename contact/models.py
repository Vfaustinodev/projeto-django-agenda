from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#ID (primary key, automático)
# first_name(string), last_name(string), phone (string)
# email (email), created_date (date), description(text)
# picture(imagem), show (boolean)

#Depois
# category (foreign key), owner (foreign key)
# O que é Foreing Key?
# Foreing Key cria uma chave em Contact que aponta para outro model qualquer, posso ter varios contatos linkando numa mesma categoria

# O ID(PrimaryKey) vem autoaticamente pelo Django

class Category(models.Model):
    # Configurando a class Meta para fazer correções linguísticas no plural e singular
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, # Captura a nossa class Category que é basicamente a chamada da Foreing key
        on_delete=models.SET_NULL, #on_delete=models.CASCADE faz com que todos os contatos da categoria sejam deletados
        blank=True, # Permite que a categoria não seja obrigatoria no cadastro
        null=True  # Permite que o campo de categoria seja Nulo/Vazio
        )

    # Cria um Owner capaz de fazer alterações sem que seja o Administrador do Site
    owner = models.ForeignKey(
        User, # Captura a nossa class Category que é basicamente a chamada da Foreing key
        on_delete=models.SET_NULL, #on_delete=models.CASCADE faz com que todos os contatos da categoria sejam deletados
        blank=True, null=True # Permite que a categoria não seja obrigatoria no cadastro
        ) 

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'