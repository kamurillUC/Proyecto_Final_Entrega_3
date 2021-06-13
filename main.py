import mis_funciones, mis_clases
from getpass import getpass

#Variables globales
bandera = 0
opcion = 0


#Carga de usuarios e inventario desde txt
usuarios = mis_funciones.cargar_archivo('usuarios')
inventario = mis_funciones.cargar_archivo('inventario')


#Presentacion de portada
mis_funciones.limpiar_consola()
print(mis_funciones.get_logo())
print(mis_funciones.get_portada())
respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para continuar con el inicio de sesión...{mis_clases.consolaColor.NORMAL}")

while bandera == 0:      
    mis_funciones.limpiar_consola()    
    print("\n")
    print(mis_funciones.get_logo())

    #Login    
    print(mis_funciones.get_login()) 
    
    nombre_usuario = input(f"{mis_clases.consolaColor.VERDE}Usuario: {mis_clases.consolaColor.NORMAL}")
    password = getpass(f"{mis_clases.consolaColor.VERDE}Contraseña: {mis_clases.consolaColor.NORMAL}")    

    usuario_actual = mis_funciones.encontrar_usuario(usuarios, nombre_usuario, password)

    mis_funciones.limpiar_consola()  
    if usuario_actual == None:              
        print(f"{mis_clases.consolaColor.ROJO}¡Usuario y contraseña inválida!{mis_clases.consolaColor.NORMAL}") 
        respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para salir...{mis_clases.consolaColor.NORMAL}")  
        break     
    else:   
        #Sistema de inventario    
        print(f"{mis_clases.consolaColor.AMARILLO}Bienvenido al sistema de inventarios de tienda Simón, {usuario_actual['full_name']} es un placer atenderle{mis_clases.consolaColor.NORMAL}")        
        respuesta = input(f"{mis_clases.consolaColor.AMARILLO}¿Desea ingresar al sistema de inventarios?(Si/No) {mis_clases.consolaColor.NORMAL}\n")

        if respuesta.lower().strip() == 'si':
            while bandera == 0:
                mis_funciones.limpiar_consola()
                print(mis_funciones.get_departamento())
                
                opcion = mis_funciones.opcion_menu(4)
                
                if opcion == 1:
                    bandera = mis_funciones.menu_por_departamento(usuario_actual, inventario, 'damas') 
                elif opcion == 2:
                    bandera = mis_funciones.menu_por_departamento(usuario_actual, inventario, 'caballeros')
                elif opcion == 3:
                    bandera = mis_funciones.menu_por_departamento(usuario_actual, inventario, 'kids')                                        
                else:
                    break
                            
    break

mis_funciones.limpiar_consola()
print(mis_funciones.get_mensaje_salida())
print(mis_funciones.get_gracias())
print(mis_funciones.get_portada())




