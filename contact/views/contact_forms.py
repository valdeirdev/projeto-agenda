from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact 

# Create your views here.
def create(request):

    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)  

        context = {
            'form': form,
            'form_action': form_action,
            'action_type': 'Create Contact'
        }

        if form.is_valid():
            contact = form.save()

            return redirect('contact:update', contact_id=contact.id)


        return render(
            request,
            'contact/create.html',
            context,
        )
    
    context = {
        'form': ContactForm(),
        'form_action': form_action,
        'action_type': 'Create Contact'
    }
    return render(
        request,
        'contact/create.html',
        context,
    )

def update(request, contact_id):

    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        print(request.POST.get('first_name'))

        form = ContactForm(request.POST, request.FILES, instance=contact)  

        context = {
            'form': form,
            'form_action': form_action,
            'action_type': 'Update Contact'
        }

        if form.is_valid():
            contact = form.save()

            return redirect('contact:update', contact_id=contact.id)


        return render(
            request,
            'contact/create.html',
            context,
        )
    
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        'action_type': 'Update Contact'
    }

    return render(
        request,
        'contact/create.html',
        context,
    )

def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, 
        pk=contact_id, 
        show=True
    )

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        print('Valor de confirmtion ', confirmation)
        contact.delete()
        return redirect('contact:index')
    else:
        print('Sem valor confirmation')
    
    context = {
        'contact': contact,
        'confirmation': confirmation
    }
    
    return render(
        request,
        'contact/contact.html',
        context
    )