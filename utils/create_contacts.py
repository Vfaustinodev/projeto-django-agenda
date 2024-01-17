import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

# Caminho
DJANGO_BASE_DIR = Path(__file__).parent.parent #Volta na pasta raiz, esse .parent seria algo igual ao comando 'cd ..'
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR)) # Adcionando caminho para utilizar modulos que estão antes ou acima da pasta 'utils'
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings' # Sempre que for utilizar o Django sem o manage.py fazer essa configuração
settings.USE_TZ = False # Corrigir erro de TImeZone

django.setup() #  COnfigurou e iniciou o Django

if __name__ == '__main__':
    import faker #lib de dados fakes para dar carga na nossa aplicação

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR') # Configurando o Faker para trazer dados fakes BR
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories] # List Compreenssion

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)