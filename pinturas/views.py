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


            #se registra en la tabla historial
            descripcion = "Inicia Sesion"
            tabla = ""
            fechayhora = datetime.now()
            usuario = request.session['idUsuario']
            his = Historial(descripcion_historial=descripcion,tabla_afectada_historial=tabla,fecha_hora_historial=fechayhora,usuario_id=usuario)
            his.save()


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
        #se registra en la tabla historial
        descripcion = "Cierra Sesion"
        tabla = ""
        fechayhora = datetime.now()
        usuario = request.session['idUsuario']
        his = Historial(descripcion_historial=descripcion,tabla_afectada_historial=tabla,fecha_hora_historial=fechayhora,usuario_id=usuario)
        his.save()

        #se elimina los datos de la sesión
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
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        if nomUsuario.upper() == "ADMIN":
            datos = {'nomUsuario':nomUsuario}
            return render(request,'menu_admin.html',datos)
        else:
            datos = {'r2':'No tiene permisos suficientes para acceder !!'}
            return render(request,'index.html',datos)
    else:
        datos = {'r2':'Debe iniciar sesión para acceder!!'}
        return render(request,'index.html',datos)





#--------------------------------------------------------------------------------------------------------





def mostrarFormRegistrarEstilo(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario.upper() == "ADMIN":

            est = Estilo.objects.all().values().order_by('nombre_estilo')
            datos = {'nomUsuario':nomUsuario,'est':est}
            return render(request,'form_registrar_estilos.html',datos)
        else:
            datos = {'r2':'No tiene permisos suficientes para acceder!!'}
            return render(request,'index.html',datos)
    else:
        datos = {'r2':'Debe iniciar sesión para acceder!!'}
        return render(request,'index.html',datos)





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
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    if estadoSesion is True:
        if nomUsuario.upper() != "ADMIN":
            datos = {'nomUsuario':nomUsuario}
            return render(request,'menu_usuario.html',datos)
        else:
            datos = {'r2':'No tiene permisos suficientes para acceder !!'}
            return render(request,'index.html',datos)
    else:
        datos = {'r2':'Debe iniciar sesión para acceder!!'}
        return render(request,'index.html',datos)





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
