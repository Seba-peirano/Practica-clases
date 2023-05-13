from django.shortcuts import render,redirect
from django.urls import reverse
from contol_estudios.models import Estudiante, Curso
from contol_estudios.forms import CursoFormulario

def lista_estudiantes(request):
    contexto={
        "estudiantes": Estudiante.objects.all()
    }
    http_responde=render(
    request= request,
    template_name='contol_estudios/lista_estudiantes.html',
    context= contexto,
    )
    return http_responde

def lista_cursos(request):
    contexto={
        "cursos": Curso.objects.all()
    }
    http_responde=render(
    request= request,
    template_name='contol_estudios/lista_cursos.html',
    context= contexto,
    )
    return http_responde

def formulario_crear_curso(request):
    if request.method == "POST":
        formulario=CursoFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre= data["nombre"]
            comision=data["comision"]
            curso=Curso( nombre=nombre, comision=comision)
            curso.save()
            #redirecciono al usuario a la lista de cursos
            url_exitosa=reverse('lista_cursos')
            return redirect(url_exitosa)

    else: #GET
        formulario=CursoFormulario()
        http_response=render(
            request= request,
            template_name='contol_estudios/formulario_crear_curso.html',
            context= {'formulario': formulario},
            )
        return http_response
    
def buscar_cursos(request):
    if request.method == "POST":
        data=request.POST
        busqueda= data["busqueda"]
        cursos=Curso.objects.filter(comision__icontains=busqueda)
        contexto={
            "cursos": cursos,
        }
        http_response=render(
            request= request,
            template_name='contol_estudios/lista_cursos.html',
            context= contexto,
            )
        return http_response


