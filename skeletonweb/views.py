from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


from django.contrib import messages

from contacto.forms import ContactoForm
# Create your views here.



def index(request):
    form = ContactoForm()
    if request.method == 'POST':
        form = ContactoForm(request.POST or NONE)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            to_mail = ['paul@skeleton.cl']
            subject = "Web Mail x"
            from_email = settings.DEFAULT_FROM_EMAIL
            context = {
                'nombre': instance.nombre,
                'email': instance.email,
                'asunto': instance.asunto,
                'mensaje': instance.mensaje
            }
            with open(settings.BASE_DIR + "/skeletonweb/templates/mail/contacto.txt") as f:
                signup_message = f.read()
            html_template = get_template("mail/contacto.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()
            messages.success(request, "Tu mensaje ha sido recibido")
            return redirect("/")

    context = {'form':form}
    return render(request,'index.html',context)  