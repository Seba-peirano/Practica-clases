from django.shortcuts import render

def lista_estudiantes(request):
    contexto={
        "estudiantes":[
            {"nombre":"Emanuel1","apellido":"chorongo1"},
            {"nombre":"Emanuel2","apellido":"chorongo2"},
            {"nombre":"Emanuel3","apellido":"chorongo3"},
            {"nombre":"Emanuel4","apellido":"chorongo4"}
        ]
    }
    http_responde=render(
    request= request,
    template_name='contol_estudios/lista_estudiantes.html',
    context= contexto,
    )
    return http_responde
