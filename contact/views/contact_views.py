from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q

# Create your views here.

def index(request):
    # Filter show=True vai mostrar todos os contatos que estão com show
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id') #posso também fazer fatiamento Exemplo .order_by('-id')[:10] e mostrar apenas os 10 ultimos contatos
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context,
    )

def search(request):

    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')
    
    # Metodo LookUp Icontains para buscar filtrar contatos sem ter que digitar o nome do contato por inteiro
    # Obrigatorio a utilização do metodo Q que é como se fosse um 
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value)|
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )

def contact(request, contact_id):
    # Filter show=True vai mostrar todos os contatos que estão com show
    # single_contact = Contact.objects.filter(pk=contact_id).first() #Nessa situação o filter() é melhor que get()

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )