from django.shortcuts import render
from .models import Genero , Alumno

# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def crud(request):
    alumnos = Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,"alumnos/alumnos_list.html",context)

def alumnosAdd(request):
    if request.method != "POST":
        #No es un post , por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,"alumnos/alumnos_add.html",context)
    else:        
        #Es un post , por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = {"mensaje":"Ok , datos guardados....."}
        return render(request,"alumnos/alumnos_add.html",context)

def alumnos_del(request):
    return "hola"

def alumnos_findEdit(request,pk):
    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context = {'alumno':alumno,'generos':generos}

        if alumno:
            return render(request,"alumnos/alumnos_edit.html",context)
        else:
            context={"mensaje":"Error, rut no existe"}
            return render(request,"alumnos/alumnos_edit.html",context)

def alumnosUpdate(request):
    return "hola"