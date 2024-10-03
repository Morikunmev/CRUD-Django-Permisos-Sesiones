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
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario.upper() == "ADMIN":
            if request.method == 'POST':
                nom = request.POST["txtest"].upper()
        
                comprobarEstilo = Estilo.objects.filter(nombre_estilo=nom)
                if comprobarEstilo:
                    est= Estilo.objects.all().values().order_by('nombre_estilo')
                    datos ={
                        'nomUsuario': nomUsuario,
                        'est': est,
                        'r2': 'El Estilo (' + str(nom.upper()) + ') Ya existe!'
                    }
                    return render(request, 'form_registrar_estilos.html', datos)
                else:
                    est = Estilo(nombre_estilo=nom)
                    est.save()

                    # Se registra en la tabla historial
                    descripcion = "Insert realizado (" + str(nom.upper()) + ")"
                    tabla = "Estilo"
                    fechayhora = datetime.now()
                    usuario = request.session['idUsuario']
                    his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
                    his.save()

                    est= Estilo.objects.all().values().order_by('nombre_estilo')
                    datos = {
                        'nomUsuario': nomUsuario,
                        'est': est,
                        'r': 'Estilo (' + str(nom.upper()) + ') Registrado Correctamente!!'
                    }
                    return render(request, 'form_registrar_estilos.html', datos)
            else:
                # Se ejecuta cuando en la URL se escribe 'registrar_estilo'
                est= Estilo.objects.all().values().order_by('nombre_estilo')
                datos = {
                    'nomUsuario': nomUsuario,
                    'est': est,
                    'r2': 'Debe presionar El Boton para Registrar un Estilo!!'
                }
                return render(request, 'form_registrar_estilos.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesión para acceder!!'}
        return render(request, 'index.html', datos)

#--------------------------------------------------------------------------------------------------------

def mostrarFormActualizarEstilo(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:
            nomUsuario = request.session.get('nomUsuario')
            if nomUsuario == 'ADMIN':
                encontrado = Estilo.objects.get(id=id)
                est = Estilo.objects.all().values().order_by('nombre_estilo')
                datos = {
                    'nomUsuario': request.session["nomUsuario"],
                    'est': est,
                    'encontrado': encontrado}
                return render(request, 'form_actualizar_estilos.html', datos)   

            else:
                est = Estilo.objects.all().values().order_by('nombre_estilo')
                datos = {
                    'nomUsuario': request.session["nomUsuario"],
                    'est': est,
                    'r2': 'No tiene permisos suficientes para realizar la accion!!'}
                return render(request, 'form_registar_estilos.html', datos)
        else:
            est = Estilo.objects.all().values().order_by('nombre_estilo')
            datos = {
                    'nomUsuario': request.session["nomUsuario"],
                    'est': est,
                    'r2': 'Debe inicar sesion para acceder!!'}
            return render(request, 'index', datos)
    except:
        est = Estilo.objects.all().values().order_by("nombre_estilo")
        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'est': est,
            'r2': 'El ID (' + str(id) + ') No Existe. Imposible Actualizar!!'
        }
        return render(request, 'form_registrar_estilos.html', datos)







#--------------------------------------------------------------------------------------------------------





def actualizarEstilo(request, id):
    try:
        nom = request.POST["txtest"]

        est = Estilo.objects.get(id=id)
        est.nombre_estilo = nom
        est.save()

        # Se registra en la tabla historial
        descripcion = "Actualizado realizada (" + str(nom.upper()) + ")"
        tabla = "Estilo"
        fechayhora = datetime.now()
        usuario = request.session['idUsuario']
        his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
        his.save()

        est = Estilo.objects.all().values().order_by('nombre_estilo')
        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'est': est,
            'r': 'Estilo (' + str(nom.upper()) + ') Actualizado Correctamente!!'
        }
        return render(request, 'form_registrar_estilos.html', datos)

    except:
        est = Estilo.objects.all().values().order_by("nombre_estilo")
        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'est': est,
            'r2': 'El ID (' + str(id) + ') No Existe. Imposible Actualizar!!'
        }
        return render(request, 'form_registrar_estilos.html', datos)






#--------------------------------------------------------------------------------------------------------






def eliminarEstilo(request, id):
    # Verificamos si el usuario ha iniciado sesión
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario.upper() == "ADMIN":
            try:
                # Obtenemos el estilo por ID
                est = Estilo.objects.get(id=id)
                nom = est.nombre_estilo
                est.delete()

                # Se registra en la tabla historial
                descripcion = "Eliminado (" + str(nom.upper()) + ")"
                tabla = "Estilo"
                fechayhora = datetime.now()
                usuario = request.session['idUsuario']
                his = Historial(
                    descripcion_historial=descripcion, 
                    tabla_afectada_historial=tabla, 
                    fecha_hora_historial=fechayhora, 
                    usuario_id=usuario
                )
                his.save()

                # Recargamos la lista de estilos para mostrarla nuevamente
                est = Estilo.objects.all().values().order_by('nombre_estilo')
                datos = {
                    'nomUsuario': request.session['nomUsuario'],
                    'est': est,
                    'r': 'Estilo (' + str(nom.upper()) + ') Eliminado Correctamente!!'
                }
                return render(request, 'form_registrar_estilos.html', datos) 

            except Estilo.DoesNotExist:
                # Si el estilo no existe
                est = Estilo.objects.all().values().order_by('nombre_estilo')
                datos = {
                    'nomUsuario': request.session['nomUsuario'],
                    'est': est,
                    'r2': 'El ID (' + str(id) + ') No Existe. Imposible Eliminar!!'
                }
                return render(request, 'form_registrar_estilos.html', datos)
        else:
            # Mensaje de permisos insuficientes si no es "ADMIN"
            datos = {'r2': 'No tiene permisos suficientes para realizar esta acción!!'}
            return render(request, 'index.html', datos)
    else:
        # Si no ha iniciado sesión
        datos = {'r2': 'Debe iniciar sesión para acceder!!'}
        return render(request, 'index.html', datos)





#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------





def mostrarListarHistorial(request):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:
            nomUsuario = request.session.get('nomUsuario')
            if nomUsuario == "ADMIN":
                his = Historial.objects.select_related("usuario").all().order_by("-fecha_hora_historial")
                datos = {'nomUsuario': request.session['nomUsuario'], 'his': his}
                return render(request, 'listar_historial.html', datos)
        
            else:
                datos = {'r2':'Debe tiene permisos suficientes para sesión para acceder!!'}
                return render(request,'index.html',datos)
        else:
            datos= {'r2':'Debe iniciar sesion para acceder!!'}
            return render(request,'index.html',datos)


    except:
        datos= {'r2':'Error al cargar la lista de historial!!'}
        return render(request,'index.html',datos)





#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)






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
    estadoSesion = request.session.get('estadoSesion')
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "ADMIN":

            opcionesEstilos = Estilo.objects.all().values().order_by("nombre_estilo")
            datos = {'nomUsuario': request.session['nomUsuario'], 'opcionesEstilos': opcionesEstilos}
            return render(request,'form_registrar_pinturas.html',datos)
        else:
            datos = {'r2':'No tiene permisos suficientes para acceder!!'}
            return render(request,'index.html',datos)
    else:
        datos = {'r2':'Debe iniciar sesión para acceder!!'}
        return render(request,'index.html',datos)




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
