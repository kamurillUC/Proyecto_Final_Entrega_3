import mis_clases, os, ast, hashlib

#Salt unico para el cifrado y comparación de la contraseña
salt = b'KamurillUC'


#Cantidad opciones por rol
OPT_ADMIN = 7
OPT_GUEST = 3


#Funcion para limpiar consola segun OS
def limpiar_consola():   
    #Unix systems 
    if os.name == "posix":
        os.system("clear")
    #Windows
    elif os.name == "nt":
        os.system("cls")


#Funciones para obtener UI
def get_logo():
    logo = ""
    logo += mis_clases.consolaColor.AZUL
    logo += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"  
    logo += mis_clases.consolaColor.MAGENTA
    logo += "___________________________________________________________________________________________\n\n"    
    logo += mis_clases.consolaColor.CYAN
    logo += "████████╗██╗███████╗███╗   ██╗██████╗  █████╗     ███████╗██╗███╗   ███╗ ██████╗ ███╗   ██╗\n"
    logo += "╚══██╔══╝██║██╔════╝████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██║████╗ ████║██╔═══██╗████╗  ██║\n"
    logo += "   ██║   ██║█████╗  ██╔██╗ ██║██║  ██║███████║    ███████╗██║██╔████╔██║██║   ██║██╔██╗ ██║\n"
    logo += "   ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══██║    ╚════██║██║██║╚██╔╝██║██║   ██║██║╚██╗██║\n"
    logo += "   ██║   ██║███████╗██║ ╚████║██████╔╝██║  ██║    ███████║██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║\n"
    logo += "   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n"
    logo += mis_clases.consolaColor.MAGENTA
    logo += "___________________________________________________________________________________________\n" 
        
    logo += mis_clases.consolaColor.NORMAL  

    return logo


#Funciones para obtener UI
def get_gracias():
    gracias = ""
    gracias += mis_clases.consolaColor.AZUL
    gracias += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"  
    gracias += mis_clases.consolaColor.MAGENTA
    gracias += "___________________________________________________________________________________________\n\n"    
    gracias += mis_clases.consolaColor.CYAN
    gracias += "                    ██████╗ ██████╗  █████╗  ██████╗██╗ █████╗ ███████╗\n"
    gracias += "                   ██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔════╝\n"
    gracias += "                   ██║  ███╗██████╔╝███████║██║     ██║███████║███████╗\n"
    gracias += "                   ██║   ██║██╔══██╗██╔══██║██║     ██║██╔══██║╚════██║\n"
    gracias += "                   ╚██████╔╝██║  ██║██║  ██║╚██████╗██║██║  ██║███████║\n"
    gracias += "                    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝\n"
    gracias += mis_clases.consolaColor.MAGENTA
    gracias += "___________________________________________________________________________________________\n" 
        
    gracias += mis_clases.consolaColor.NORMAL  

    return gracias


#Funciones para obtener UI
def get_portada():      
    portada = ""
    portada += mis_clases.consolaColor.AZUL   
    portada += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"        
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|                                        | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|             {mis_clases.consolaColor.NORMAL}Proyecto Final{mis_clases.consolaColor.AMARILLO}             | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|........................................| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|         {mis_clases.consolaColor.NORMAL}Kevin A. Murillo Rojas{mis_clases.consolaColor.AMARILLO}         | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    portada += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    portada += mis_clases.consolaColor.MAGENTA
    portada += "___________________________________________________________________________________________\n" 
    portada += mis_clases.consolaColor.NORMAL  

    return portada


#Funciones para obtener UI
def get_mensaje_salida():
    mensaje_salida = ""
    mensaje_salida += mis_clases.consolaColor.AZUL   
    mensaje_salida += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"        
    mensaje_salida += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    mensaje_salida += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|                                        | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    mensaje_salida += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|   {mis_clases.consolaColor.NORMAL}Saliendo del sistema de Inventarios{mis_clases.consolaColor.AMARILLO}  | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    mensaje_salida += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    mensaje_salida += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    mensaje_salida += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    mensaje_salida += mis_clases.consolaColor.MAGENTA
    mensaje_salida += "___________________________________________________________________________________________\n" 
    mensaje_salida += mis_clases.consolaColor.NORMAL  

    return mensaje_salida


#Funciones para obtener UI
def get_login():   
    login = "" 
    login += mis_clases.consolaColor.AZUL   
    login += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"     
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|                                        | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|            {mis_clases.consolaColor.NORMAL}Inicio de sesión{mis_clases.consolaColor.AMARILLO}            | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"        
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    login += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    login += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    login += mis_clases.consolaColor.MAGENTA
    login += "___________________________________________________________________________________________\n" 
    login += mis_clases.consolaColor.NORMAL 
    return login


#Funcion para hacer la carga del archivo y devolver un diccionario
def cargar_archivo(opcion):
    path = os.getcwd()

    if opcion == 'usuarios':
        path += '\\datafiles\\users.txt'
    elif opcion == 'inventario':
        path += '\\datafiles\\inventario.txt'        
    file = open(path, "r", encoding='utf-8')
    content = file.read()
    file.close()

    return ast.literal_eval(content)


#Funcion para hacer la escritura del archivo y devolver un diccionario
def escritura_archivo(opcion, diccionario):
    path = os.getcwd()

    if opcion == 'usuarios':
        path += '\\datafiles\\users.txt'
    elif opcion == 'inventario':
        path += '\\datafiles\\inventario.txt'        
    file = open(path, "w", encoding='utf-8')
    file.write(str(diccionario))
    file.close()    


#Funcion para el login de un usuario contra una contraseña cifrada irreversible
def encontrar_usuario(usuarios, nombre_usuario, password):
    
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)       
    
    for usuario in usuarios:
        if nombre_usuario == usuario['usuario']:
            if dk.hex() == usuario['password']:
                return usuario
            else:
                return usuario

#Funcion para cifrar una contraseña
def generar_hash(password):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000) 
    return dk.hex()


#Funciones para obtener UI
def get_departamento():   
    depa = ""
    depa += mis_clases.consolaColor.AZUL  
    depa += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"   
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|       Seleccione un departamento       | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|........................................| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 1. Damas                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"           
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 2. Caballeros                          | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 3. Niños                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 4. Salir                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    depa += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    depa += mis_clases.consolaColor.MAGENTA
    depa += "___________________________________________________________________________________________\n" 
    depa += mis_clases.consolaColor.NORMAL 

    return depa


#Funcion para generar la linea dependiendo del departamento
def generar_linea(departamento):
    if departamento == 'Damas':
        return "..................Damas................."
    elif departamento == 'Caballeros':
        return "...............Caballeros..............."
    elif departamento == 'Niños':
        return "..................Niños................."


#Funciones para obtener Menu
def get_menu(usuario_actual, departamento):    
    menu = ""
    menu += mis_clases.consolaColor.AZUL  
    menu += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"   
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|   Menú de productos del departamento   | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|{generar_linea(departamento)}| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 1. Consultar                           | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    if usuario_actual['role'] == 'admin':        
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 2. Ingresar                            | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 3. Actualizar                          | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 4. Eliminar                            | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 5. Guardar                             | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 6. Volver                              | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 7. Salir                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    elif usuario_actual['role'] == 'invitado':        
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 2. Volver                              | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 3. Salir                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    menu += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    menu += mis_clases.consolaColor.MAGENTA
    menu += "___________________________________________________________________________________________\n" 
    menu += mis_clases.consolaColor.NORMAL 
    
    return menu


#Función para definir las opciones del menu dependiendo del rol del usuario
def get_cantidad_opciones(usuario_actual):
    if usuario_actual['role'] == 'admin':
        return OPT_ADMIN
    elif usuario_actual['role'] == 'invitado':
        return OPT_GUEST
    else:
        return 0


#Función para limitar a solo las opciones disponibles del menú
def opcion_menu(cantidad_opciones):
    bandera = 0
    opcion = 0
    while bandera == 0:
        respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Opción: {mis_clases.consolaColor.NORMAL}")
        es_numero = respuesta.isdigit()
        if es_numero == True:                    
            opcion = int(respuesta)
            if opcion > 0 and opcion <= cantidad_opciones:                
                break          
                            
        print(f"{mis_clases.consolaColor.ROJO}¡Por favor ingresar un número válido!{mis_clases.consolaColor.NORMAL}")   
               
    return opcion


#Función para ingreso solo de números
def menu_ingreso_numero(texto_input):
    bandera = 0    
    while bandera == 0:
        respuesta = input(f"{texto_input}")
        es_numero = respuesta.isdigit()
        if es_numero == True:         
            numero_ingresado = respuesta
            break          
                            
        print(f"¡Por favor ingresar un número!")   
               
    return numero_ingresado


#Función genérica para mostrar un item
def mostrar_item(item):
    columnas = list(item.keys())
    respuesta = ""
    respuesta += "---------------------------------------------------------------------------------------------\n"
    for columna in columnas:
        respuesta += f"| {columna}: {item[columna]} "
    respuesta += "\n---------------------------------------------------------------------------------------------\n"
    return respuesta


#Función genérica para mostrar diccionarios
def ver_diccionario(lista, titulo):    
    respuesta = ""
    numero = 1
    respuesta += f"{mis_clases.consolaColor.MAGENTA}"
    respuesta += "*********************************************************************************************\n"
    respuesta += f"{titulo}\n"
    respuesta += "*********************************************************************************************\n"
    respuesta += f"{mis_clases.consolaColor.NORMAL}"
    respuesta += "---------------------------------------------------------------------------------------------\n"
       
    if len(lista) > 0:         
        columnas = list(lista[0].keys())
        for item in lista:     
            respuesta += f"| {numero}. "
            for columna in columnas:
                respuesta += f"| {columna}: {item[columna]} "
            respuesta += '\n---------------------------------------------------------------------------------------------\n'
            numero += 1
    else:
        respuesta += f"No hay objetos en la lista\n"  
        respuesta += '\n---------------------------------------------------------------------------------------------\n'  
    
    respuesta += f"{mis_clases.consolaColor.MAGENTA}"
    respuesta += "*********************************************************************************************\n"   
    respuesta += f"{mis_clases.consolaColor.NORMAL}"

    return respuesta


#Función para la consulta de productos
def consulta_productos(productos, nombre_departamento):
    return ver_diccionario(productos, f"Productos del departamento de {nombre_departamento}")


#Función para el ingreso de productos
def ingresar_producto(productos, codigo, nombre, precio_unitario, cantidad):
    nuevo_producto = {
        'Codigo': codigo,
        'Nombre': nombre,
        'Precio_Unitario': precio_unitario,
        'Cantidad': cantidad
    }
    productos.append(nuevo_producto)


#Función para actualizar un producto
def encontrar_producto(codigo_producto, productos):      
    for producto in productos:        
        if producto['Codigo'] == codigo_producto:
            return producto
        

#Función para titulos de cada opcion del menú
def get_titulo(opcion_menu):
    titulo = ""
    titulo += mis_clases.consolaColor.AZUL  
    titulo += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"   
    titulo += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    if opcion_menu.lower() == 'consulta':
        titulo += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|          Consulta de productos         | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    elif opcion_menu.lower() == 'ingreso':
        titulo += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|          Ingreso de productos          | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    elif opcion_menu.lower() == 'actualizar':
        titulo += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|           Actualizar producto          | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    elif opcion_menu.lower() == 'eliminar':
        titulo += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|            Eliminar producto           | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    elif opcion_menu.lower() == 'guardar':
        titulo += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|            Guardar productos           | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    titulo += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    titulo += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    titulo += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    titulo += mis_clases.consolaColor.MAGENTA
    titulo += "___________________________________________________________________________________________\n" 
    titulo += mis_clases.consolaColor.NORMAL 
    return titulo


#Función para dar los menús dependendiendo del rol del usuario 
def menu_por_departamento(usuario_actual, inventario, nombre_departamento):
    departamento = inventario['departamentos'][nombre_departamento]
    bandera = 0
    while bandera == 0:        
        limpiar_consola()    
        
        print(get_menu(usuario_actual, departamento['nombre']))

        opcion = opcion_menu(get_cantidad_opciones(usuario_actual))
                            
        if usuario_actual['role'] == 'admin':
            if opcion == 1:#Consulta de productos

                limpiar_consola()
                print(get_titulo('consulta'))
                print(consulta_productos(departamento['productos'], departamento['nombre']))

            elif opcion == 2:#Ingrese el producto
                
                limpiar_consola()
                print(get_titulo('ingreso'))
                codigo = int(menu_ingreso_numero('Código: '))
                nombre = input("Nombre: ")
                precio_unitario = float(menu_ingreso_numero('Precio Unitario: '))
                cantidad = int(menu_ingreso_numero('Cantidad: '))
                
                ingresar_producto(departamento['productos'], codigo, nombre, precio_unitario, cantidad)
                print(f"{mis_clases.consolaColor.MAGENTA}>< >< >< >< >< Producto ingresado >< >< >< >< ><{mis_clases.consolaColor.NORMAL}") 


            elif opcion == 3:#Actualice el producto
                if len(departamento['productos']) > 0:
                    while bandera == 0:
                        limpiar_consola()
                        print(get_titulo('actualizar'))
                        print(consulta_productos(departamento['productos'], departamento['nombre']))
                        codigo_producto = int(menu_ingreso_numero('Código de producto: '))              
                    
                        limpiar_consola()
                        print(get_titulo('actualizar'))
                        producto_encontrado = encontrar_producto(codigo_producto, departamento['productos'])

                        if producto_encontrado == None: 

                            print(f"{mis_clases.consolaColor.ROJO}¡No hay ningún producto con ese código!{mis_clases.consolaColor.NORMAL}")
                            respuesta = input(f"{mis_clases.consolaColor.AMARILLO}¿Desea buscar de nuevo un producto?(Si/No) {mis_clases.consolaColor.NORMAL}\n")

                            if respuesta.lower().strip() == 'no':
                                break

                        else:
                            print(mostrar_item(producto_encontrado))
                            producto_encontrado['Nombre'] = input("Nombre: ")
                            producto_encontrado['Precio_Unitario'] = float(menu_ingreso_numero('Precio Unitario: '))
                            producto_encontrado['Cantidad'] = int(menu_ingreso_numero('Cantidad: '))        
                            print(f"{mis_clases.consolaColor.MAGENTA}>< >< >< >< >< Producto actualizado >< >< >< >< ><{mis_clases.consolaColor.NORMAL}")                         
                            break
                else:
                    print(f"{mis_clases.consolaColor.ROJO}¡No hay ningún producto para actualizar!{mis_clases.consolaColor.NORMAL}")                
            elif opcion == 4:#Elimine el producto
                if len(departamento['productos']) > 0:
                    while bandera == 0:
                        limpiar_consola()
                        print(get_titulo('eliminar'))
                        print(consulta_productos(departamento['productos'], departamento['nombre']))
                        codigo_producto = int(menu_ingreso_numero('Código de producto: '))              
                    
                        limpiar_consola()
                        print(get_titulo('eliminar'))                        
                        producto_encontrado = encontrar_producto(codigo_producto, departamento['productos'])

                        if producto_encontrado == None: 

                            print(f"{mis_clases.consolaColor.ROJO}¡El producto que trata de eliminar no existe, intente nuevamente!{mis_clases.consolaColor.NORMAL}")
                            respuesta = input(f"{mis_clases.consolaColor.AMARILLO}¿Desea buscar de nuevo un producto?(Si/No) {mis_clases.consolaColor.NORMAL}\n")

                            if respuesta.lower().strip() == 'no':
                                break

                        else:
                            print(mostrar_item(producto_encontrado))
                            departamento['productos'].remove(producto_encontrado)       
                            print(f"{mis_clases.consolaColor.MAGENTA}>< >< >< >< >< Producto eliminado >< >< >< >< ><{mis_clases.consolaColor.NORMAL}")                         
                            break  
                else:
                    print(f"{mis_clases.consolaColor.ROJO}¡No hay ningún producto para eliminar!{mis_clases.consolaColor.NORMAL}")                
            
            elif opcion == 5:#Guardar

                limpiar_consola()
                print(get_titulo('guardar'))
                escritura_archivo('inventario', inventario)
                print(f"{mis_clases.consolaColor.MAGENTA}>< >< >< >< >< Inventario guardado >< >< >< >< ><{mis_clases.consolaColor.NORMAL}")  

            elif opcion == 7: #Salir
                bandera = 1
                return 1

            elif opcion == 6: #Volver
                break
            
                

            input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para continuar...{mis_clases.consolaColor.NORMAL}")
        elif usuario_actual['role'] == 'invitado':
            
            if opcion == 1:#Consulta de productos
                limpiar_consola()         
                print(get_titulo('consulta'))       
                print(consulta_productos(departamento['productos'], departamento['nombre']))
            if opcion == 3: #Salir
                bandera = 1
                return 1
            elif opcion == 2: #Volver
                break
                
            input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para continuar...{mis_clases.consolaColor.NORMAL}")

    return 0