from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from .models import TodoItem

def home(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = f"Neue Nachricht von {name}"
        body = f"""
        Name: {name}
        E-Mail: {email}
        Telefonnummer: {phone}

        Nachricht:
        {message}
        """
        try:
            # Liste mit Empfängeradressen
            recipient_list = ['m.okon@deinlandschaftsbauer.de', 'n.carlucci@deinlandschaftsbauer.de']
            
            send_mail(
                subject,
                body,
                'no-reply@deinlandschaftsbauer.de',  # Absenderadresse
                recipient_list,
                fail_silently=False,
            )
            success = True
        except Exception as e:
            return HttpResponse(f"<h2>Es gab ein Problem beim Senden der Nachricht: {e}</h2>")

    return render(request, "index.html", {"success": success})


# Model Beispiel
def todos(request):
    items = TodoItem.objects.all
    return render(request, "todos.html", {"todos": items})

def impressum(request):
    return render(request, 'impressum.html')

def datenschutz(request):
    return render(request, 'datenschutz.html')