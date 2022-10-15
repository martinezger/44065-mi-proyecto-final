from django.shortcuts import render
from django.views import View
from ejemplo.models import Familiar
from ejemplo.form import Buscar
from django.http import HttpResponse

def index(request):
    suma = 1 + 1
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre": "German",
        "apellido": suma,
    })

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre":nombre,
        "apellido": apellido,
    })

def index_tres(request):

    return render(request,  "ejemplo/saludar.html", 
    {"notas": [1,2,3,4,5,6,7,8]}
    )

def imc(request, peso, altura):
    altura_en_metros = altura / 100 
    peso_en_kilos = peso / 100
    imc = peso_en_kilos / altura_en_metros * altura_en_metros


    return render(request, "ejemplo/imc.html", {"imc": imc})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", 
                {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":"German"}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})
