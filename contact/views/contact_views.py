from django.shortcuts import render, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    return render(
        request,
        'contact/index.html',
        context,
    )

def search(request):

    search_value = request.GET.get('q', '').strip()

    if len(search_value) == 0:
        return redirect('contact:index')
    
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value) 
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': contacts,
        'site_title': 'Search - ',
        'search_value': search_value
    }
    return render(
        request,
        'contact/index.html',
        context,
    )

def contact(request, contact_id):
    try:
        single_contact = Contact.objects.filter(pk=contact_id, show=True).first()
    except:
        raise Http404()
    
    site_tile = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': site_tile
    }
    return render(
        request,
        'contact/contact.html',
        context,
    )