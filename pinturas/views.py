from django.shortcuts import render
from pinturas.models import Usuario, Estilo, Pintura, Historial
from datetime import datetime

#--------------------------------------------------------------------------------------------------------





def mostrarIndex(request):
    return render(request, 'index.html')

#--------------------------------------------------------------------------------------------------------





def iniciarSesion(request):
    if request.method == 'POST':
        nom = request.POST["txtusu"]
        pas = request.POST["txtpas"]
        comprobarLogin = Usuario.objects.filter(nombre_usuario=nom, password_usuario=pas).values()

        if comprobarLogin:
            request.session['estadoSesion'] = True
            request.session['idUsuario'] = comprobarLogin[0]['id']
            request.session['nomUsuario'] = nom.upper()
            datos = {'nomUsuario':nom.upper()}
            if nom.upper() == "ADMIN":
                return render(request,'menu_admin.html.',datos)
            else:
                return render(request, 'menu_usuario.html', datos)
            
        else:
            datos = {'r2':'Usuario o contraseña incorrectos'}
            return render(request,'index.html',datos)

    else:
        datos = {'r2':'No se puede procesar la solicitud'}
        return render(request,'index.html',datos)   
    




#--------------------------------------------------------------------------------------------------------





def cerrarSesion(request):
    try:
        del request.session['estadoSesion']
        del request.session['idUsuario']
        del request.session['nomUsuario']
        return render(request, 'index.html')
    except:
        return render(request, 'index.html')




#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------





def mostrarMenuAdmin(request):
    return render(request, 'menu_admin.html')





#--------------------------------------------------------------------------------------------------------





def mostrarFormRegistrarEstilo(request):
    pass





#--------------------------------------------------------------------------------------------------------





def registrarEstilo(request):
    pass





#--------------------------------------------------------------------------------------------------------





def mostrarFormActualizarEstilo(request, id):
    pass





#--------------------------------------------------------------------------------------------------------





def actualizarEstilo(request, id):
    pass





#--------------------------------------------------------------------------------------------------------





def eliminarEstilo(request, id):
    pass





#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------





def mostrarListarHistorial(request):
    pass





#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------





def mostrarMenuUsuario(request):
    return render(request, 'menu_usuario.html')





#--------------------------------------------------------------------------------------------------------





def mostrarListarPinturas(request):
    pass





#--------------------------------------------------------------------------------------------------------





def eliminarPintura(request, id):
    pass





#--------------------------------------------------------------------------------------------------------





def mostrarFormRegistrarPinturas(request):
    pass





#--------------------------------------------------------------------------------------------------------





def registrarPintura(request):
    pass





#--------------------------------------------------------------------------------------------------------





def mostrarFormActualizarPintura(request, id):
    pass





#--------------------------------------------------------------------------------------------------------





def actualizarPintura(request, id):
    pass





#--------------------------------------------------------------------------------------------------------
