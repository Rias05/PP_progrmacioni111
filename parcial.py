from package_input.input import *
# peso = get_float("ingrese su peso","error, ingrese nuevamnete su peso",300,10,5)

def sangre():
    grupos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    pido_sangre= input( "ingrese su sangre:").upper()
    
    for i in grupos_sanguineos:
        print(i)
        
        if i==pido_sangre:
                retorno = i
                break
        else:
            while True:
                pido_sangre =input("error ingrese nuevamnte el tipo de sangre")
                if i==pido_sangre:
                    retorno = i
                    break

            
    return retorno
def dar_de_alta(id:int,lista:list):
    '''
    esta funcion dar_de_alta pide los datos y los guarda en un dict propio del paciente, con sus recpectivos pacientes
    '''
    id= id
    nombre = get_string("ingrese su nombre:","error ingrese nuevamente el nombre",5)
    apellidos =get_string("ingrese su apellido:","error ingrese nuevamente el apellido",5)
    edad= get_int("ingrese su edad","error, ingrese nuevamnete",120,1,5,False)
    altura= get_int("ingrese su altura","error, ingrese nuevamnete",300,10,5,False)
    dni= get_int("ingrese, su dni","error ingrese nuevamnete",99999999,40000000,5,True)
    peso = get_float("ingrese su peso","error, ingrese nuevamnete su peso",300,10,5)
    grupo_sanguineo=sangre()
    dicc_paciente ={
                    "nombre":nombre,
                    "apellido":apellidos,
                    "edad":edad,
                    "altura":altura,
                    "peso":peso,
                    "dni":dni,
                    "grupo sanguineo":grupo_sanguineo,
                    "id":id}
    lista.append(dicc_paciente)
    return lista
def buscar(lista:list,clave:str,valor:str)->dict:
    '''
    recibo la lista con la clvae y el valor de esta para validar la busqueda del valor recibido retornara el diccioanrio si es que lo encuntra de lo contrario none
    '''
    retorno= None
    for i in lista:
        if i[clave]== valor:
            retorno = i
            print("encontrado")
            break  
    if retorno== None:
        print("no encontrado")     
    return retorno

def confimar_cambios(nueva_dato_modificado,empleado:dict,dato_a_cambiar:str):
    '''
    valido la entrada con mi get string, cpn el if y el dato ingresado por el usuario depende la modificacion que ha soliciditado
    '''
    pregunto = get_string("ingrese si o no para confirmar","error, solo es si o no",5,2).lower()
    if pregunto == "si": # confirmo cambios
        empleado[dato_a_cambiar] = nueva_dato_modificado
        retorno = empleado
    elif pregunto=="no":
            print("operecion confirmada") # cancelo cambios
    return retorno
def modificar(lista_empleados)  :
    '''
    validamos que el dni con el cual se le permitira modificar el dato que desea.
    
    que se le pedida en dato a cambiar dependiendo del dato se le pedira el el nuevo dato que cambiara con sus respectivos validaciones para cumplir con el formato con la funcion confirmar_cambios se hara dicha modificaion y retornara la lista conn sus diccionnarios y eldato neuvo modificado.
    '''
    pido_id= get_int("ingrese su dni","error ingrese nuevamnte:",1000,0,5,True)
    empleado= buscar(lista_empleados,"Id",pido_id)

    dato_a_cambiar = input("¿Qué datos desea modificar? Solo puede modificar estos datos\n.Nombre\n.Apellido\n.dni\n.altura\n.peso\ngrupo sanguineo\nescriba el dato que desea modificar:").lower()
    if dato_a_cambiar == "nombre" or dato_a_cambiar == "apellido":
            nueva_dato_modificado = get_string(f"Ingrese su {dato_a_cambiar}:",f"Hubo un error, ingrese nuevamente el {dato_a_cambiar}. No debe superar los 20 caracteres.",5,20)
    elif dato_a_cambiar == "dni":
            nueva_dato_modificado = get_int("Ingrese el valor nuevo de DNI:", "Error, ingrese nuevamente el DNI:",99999999,40000000,5,True)
    elif dato_a_cambiar == "grupo sanguineo":
            nueva_dato_modificado = sangre().lower()
    elif dato_a_cambiar == "altura":
            nueva_dato_modificado = get_int("Ingrese el salario que desea modificar:","Error, ingrese nuevamente el salario:",234315, 0, 5,False)
    elif dato_a_cambiar == "peso":
        nueva_dato_modificado= get_float("ingrese el peso que desea  modificar:","error, ingrese nuevamanete el peso:",300,10,5,)
    # Actualizar el valor en el diccionario del empleado
    confimar_cambios(nueva_dato_modificado,empleado,dato_a_cambiar)
    return lista_empleados

def eliminar_empleado(lista_empleados:list[dict],pido_dni:int):
    eliminado=""
    for i in lista_empleados:
        if i["dni"]== pido_dni:
            eliminado= i
            print(f"datos del empleado a eliminar:{eliminado}")
            lista_empleados.remove(eliminado)
        else:
            print("el dni ingresao no esta entre nuestros pacientes")

    return lista_empleados
def mostrar_todos(lista_empleados):
    '''
    imprimo el encabezado uno por uno y seperao cad uno al lado del otro con un espacio determinado especificado, tambien ocurre con los datos con lo que corresponde itero en la lista y hago el mismo procedimiento
    '''
    encabezado = ["nombre", "apellido", "edad", "altura", "peso", "dni", "grupo sanguineo"]
    print("-"*95)
    print("| {:<10} | {:<10} | {:<5} | {:<7} | {:<8} | {:<15} | {:<18} |".format(*encabezado))
    print("-"*95)

    # Imprimir datos de cada empleado
    for empleado in lista_empleados:
        print("| {:<10} | {:<10} | {:<5} | {:<7}cm | {:<8}kg | {:<15} | {:<14} |".format(empleado["nombre"], empleado["apellido"], empleado["edad"], empleado["altura"], empleado["peso"], empleado["dni"], empleado["grupo sanguineo"]))

    # Separador final
    print("-"*95)

def ordenar_lista(lista:list[dict], valor:str, ascendente:bool):
    '''
    recibo la lista con los diccionarios un valor que sera el criterio a ordenar y el ascendente se recorrer la lista la cantidad de de elemntos de la lista recorre  con el primer for la cantidad de veces que lo hara el segundo  es para recorrer las posiciones lo siguinte es la parte que ordenadara mediante la psocion y la clave compara el elemento con el que esta despues de el si es ascendente intercambia los valores derecha  izq
    
    '''
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if ascendente :
                    if lista[j][valor] > lista[j+1][valor]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                    if lista[j][valor] < lista[j+1][valor]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenar_lista_dato(lista_empleados:list[dict], forma:str, dato_ordenar:str):
    if forma == "ascendente":
        lista_empleados = ordenar_lista(lista_empleados, dato_ordenar, True)
    elif forma == "descendente":
        lista_empleados = ordenar_lista(lista_empleados, dato_ordenar, False)

    return lista_empleados

def buscar_paciente_dni(lista:list,dni:int):
    '''
    itero en la lista, si coincide con el dni retorno los datos del paciente
    '''
    for dato in lista:
            if dato["Dni"]== dni:
                empleado =print (dato["nombre"],dato["apellido"])
    return empleado
# def calcular_promedio(lista:list,dato_a_promediar:str):
def calcular_salario_promedio(lista_empleados:list[dict]):
        '''
        recibo la lista con sus respectivos diccionarios
        le pido al usario el dato que se desea promodiar, me dara la clave itero la lista con la clave pedida y acumulo los numeros y un contador con la cantidad de coincidencias de numeros con  dato a promediar
        '''
        print("datos que se podra promediar\nedad\naltura\npeso")
        dato_a_promediar=input("ingrese el dato que desea promediar:").lower()
        acumulador_salarios = 0
        contador = 0
        for i in lista_empleados:
            acumulador_salarios+= i[dato_a_promediar]
            contador+=1
        promedio = acumulador_salarios/ contador
        return promedio
import json
import re
def generar_csv_pacientes(path:str, lista:list):
    with open(path, "w", encoding="utf8") as archivo:
        # Escribir datos de los pacientes
        for paciente in lista:
            linea = f"{paciente['nombre']},{paciente['apellido']},{paciente['edad']},{paciente['altura']},{paciente['dni']},{paciente['peso']},{paciente['grupo sanguineo']},{paciente['id']}\n"
            archivo.write(linea)
def parser_csv_pacientes(path:str)-> list:
    lista = []
    with open(path, "r", encoding="utf8") as archivo:
        for linea in archivo:
            registro = re.split(",|\n",linea)  # Dividir la línea en los datos del paciente
            diccionario={}
            diccionario["nombre"]=registro[0]
            diccionario["apellido"]= registro[1]
            diccionario["edad"]= int(registro[2])
            diccionario["altura"]=int(registro[3])
            diccionario["dni"]= int(registro[4])
            diccionario["peso"]=float (registro[5])
            diccionario["grupo sanguineo"] = (registro[6])
            diccionario["id"] = int(registro[7])
            lista.append(diccionario)
        
    return lista

def generar_json(path: str, lista: list):
    # Abre el archivo especificado por la ruta en modo escritura ("w"),
    # utilizando la codificación UTF-8 para manejar caracteres especiales.
    with open(path, "w", encoding="utf8") as archivo:
        # Esta línea escribe el contenido de la lista en formato JSON en el archivo,
        # utilizando una sangría de 4 espacios para una mejor legibilidad.
        json.dump(lista, archivo, indent=4)
def actualizar_id(lista:list):
    lista_id=[1]
    for empleado in lista:
        lista_id.append(int(empleado["Id"]))

    # for i in lista_eliminados:
    #     lista_id.append(int(i["Id"]))
    # sacamos el ultimo id
    for i in lista_id:
        pass
    guardo = i
    return guardo
# def mostrar_tabla(puede_donanr,puede_recibir):
#      for i in puede_donar:

def mostrar_todos(lista_empleados,puede_dar,puede_recibir):
    # Encabezado de la tabla
    encabezado = ["tipo sangre", "puede donar", "puede recibir de"]
    print("-------------------------------------------------------")
    print("| {:<10} | {:<10} | {:<15} |  |".format(*encabezado))
    for i in puede_dar:

    # Imprimir datos de cada empleado
    # for empleado in lista_empleados:
        # print("| {:<10} | {:<10} | {:<15} | ${:<9} |".format(empleado["Nombre"], empleado["Apellido"], empleado["Puesto"], empleado["Salario"]))

    # Separador final
        pass

def determinar_compatibilidad(lista:list):
    pido_dni = get_int("ingrese su dni","error ingrese nuevamente el dni:",99999999,40000000,5,True)
    for i in lista:
        if pido_dni == i["dni"]:
            paciente = i
            puede_donar_a=[]
            puede_recibir=[]
            su_grupo_sanguineo=paciente["grupo sanguineo"]
            print("paciente encontrado")
            if paciente["grupo sanguineo"]=="A+":
                puede_donar_a=["A+","B+"]

                puede_recibir=["O+","O","-A","+A"]
            elif su_grupo_sanguineo=="A-":
                    puede_donar_a=["A+","A-","AB+","AB-"]
                    puede_recibir =["0-","A-"]
            elif su_grupo_sanguineo=="B+":
                    puede_donar_a=["B+","AB+"]
                    puede_recibir=["O+","O-","B+","B-"]
            elif su_grupo_sanguineo=="B-":
                    puede_donar_a=["B+","B-","AB+","AB-"]
                    puede_recibir=["O-","B-"]
            elif su_grupo_sanguineo=="AB+":
                    puede_donar_a=["AB+"]
                    puede_recibir=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
            elif su_grupo_sanguineo =="AB-":
                    puede_donar_a=["AB+","AB-"]
                    puede_recibir=["O-","A+","B+","AB+"]
            puede_donar_a_str=",".join(puede_donar_a)
            puede_recibir_str=",".join(puede_recibir)
        encabezado = ["tipo sangre", "puede donar", "puede recibir de"]
        print("-------------------------------------------------------")
        print("| {:<10} | {:<10} | {:<15} |  |".format(*encabezado))
        print(f"{su_grupo_sanguineo:<15}|{puede_donar_a_str:<10}|{puede_recibir_str:<14}")
    

# lista_pacientes = parser_csv_pacientes("pacientes.csv")

# determinar_compatibilidad(lista_pacientes)

