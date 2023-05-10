from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar(request):
    saludo="hola querido usario"
    pagina_html=HttpResponse(saludo)
    return pagina_html

def saludar_confecha(request):
    hoy=datetime.now().day
    saludo=f"hola querido usario, fecha:{hoy}"
    pagina_html=HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request):
    contexto={
       "usuario":"Pedro" 
    }
    http_responde=render(
        request=request,
        template_name='contol_estudios/base.html',
        context=contexto,
    )
    return http_responde