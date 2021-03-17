from django.shortcuts import render, redirect
from contacto.forms import FormContact
from django.core.mail import EmailMessage

def contacto(request):
    form = FormContact()
    if request.method == 'POST':
        form = FormContact(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email = EmailMessage("Mensaje desde App Django","El usuario con nombre {} con la dirección {} te escribe lo siguiente: \n\n {}".format(nombre,email,contenido), "", ["zeitgeist.tt008@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido') #pasando URL desde GET (Cuando se hizo bien el post, y ahora se hace un get (reinicia la pagina) para decir que todos los datos se guaradon correctamente)
            except:
                return redirect('/contacto/?noSvalido') 

    else:
        form = FormContact()
    return render(request, "contacto/Contacto.html", {'form': form})

