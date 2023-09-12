from django.shortcuts import render, redirect
from contact.forms import ContactForms
from django.core.mail import EmailMessage
from django.urls import reverse


# Create your views here.

def ContactViews(request):
    contact_forms = ContactForms()
    if request.method == 'POST':
        contact_forms = ContactForms(data=request.POST)
        if contact_forms.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            telepone = request.POST.get("telepone")
            contend = request.POST.get("mesage")

            email = EmailMessage(
                'Vieron tu pagina: Nuevo mensaje de contancto',
                f'De {name} <{email}> Escribio: {contend} contactar al {telepone}',
                'no-contenstar@gmail.com',
                ['garciaruizhernan9@gmail.com'],
                reply_to=[email]
            )

            try:
                # en caso de que todo ido bien
                email.send()
                return redirect(reverse('contact')+'?ok')

            except Exception as a:
                print("Error encontrado: ", {a})
                return redirect(reverse('contact') + '?fail')
    return render(request, 'contact/contact.html', {"forms": contact_forms})
