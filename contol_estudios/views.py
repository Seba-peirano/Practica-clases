from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from contol_estudios.models import Estudiante, Curso
from contol_estudios.forms import *
from django.views.generic import CreateView, ListView,DetailView,UpdateView,DeleteView

#no lo voy a usar, se va a reemplazar por clases basadas en vista
#def lista_estudiantes(request):
#    contexto={
#        "estudiantes": Estudiante.objects.all()
#    }
#    http_responde=render(
#    request= request,
#    template_name='contol_estudios/lista_estudiantes.html',
#    context= contexto,
#    )
#    return http_responde


#vista de cursos
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

def formulario_crear_estudiante(request):
    if request.method == "POST":
        formulario=EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre= data["nombre"]
            apellido=data["apellido"]
            email=data["email"]
            estudiante=Estudiante( nombre=nombre,apellido=apellido,email=email)
            estudiante.save()
            #redirecciono al usuario a la lista de estudiantes
            url_exitosa=reverse('lista_estudiantes')
            return redirect(url_exitosa)

    else: #GET
        formulario=EstudianteFormulario()
        http_response=render(
            request= request,
            template_name='contol_estudios/formulario_crear_estudiante.html',
            context= {'formulario': formulario},
            )
        return http_response
def buscar_estudiantes(request):
    if request.method == "POST":
        data=request.POST
        busqueda= data["busqueda"]
        estudiante=Estudiante.objects.filter(apellido__contains=busqueda)
        contexto={
            "Estudiante": estudiante,
        }
        http_response=render(
            request= request,
            template_name='contol_estudios/lista_estudiantes.html',
            context= contexto,
            )
        return http_response

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('lista_cursos')
    return redirect(url_exitosa)

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.save()
            url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)
    else: # GET
        inicial = {
         'nombre': curso.nombre,
         'comision': curso.comision,
            }
        formulario = CursoFormulario(initial=inicial)
        return render(
        request=request,
        template_name='contol_estudios/formulario_crear_curso.html',
        context={'formulario': formulario},
        )

#Clases de estudiantes

class EstudianteListView(ListView):
    model = Estudiante
    success_url=reverse_lazy('lista_estudiantes.html')

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields=('apellido', 'nombre', 'email', 'dni')
    success_url=reverse_lazy('lista_estudiantes.html')
class EstudianteDetailView(DetailView):
    model = Estudiante
    
    #success_url=reverse_lazy('lista_estudiantes.html')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields=('apellido', 'nombre', 'email', 'dni')
    success_url=reverse_lazy('lista_estudiantes.html')
    
class EstudianteDeleteView(DeleteView):
    model = Estudiante
    fields=('apellido', 'nombre', 'email', 'dni')
    success_url=reverse_lazy('lista_estudiantes.html')
 