import ast

# Funcion para registrar a un nuevo usuario
def registrarUsuario():
    nombre = input("Ingrese un nombre de usuario: ")
    contrasenia = input("Ingrese su contrasenia: ")

    usuario = {}
    usuario["Nombre"] = nombre
    usuario["Contrasenia"] = contrasenia

    baseDeDatos.append(usuario)
    print(f"\n***** El usuario {nombre} ha sido registrado exitosamente *****\n")


# Funcion para iniciar sesion
def iniciarSesion():
    nombre = input("Ingrese un nombre de usuario: ")
    contrasenia = input("Ingrese su contrasenia: ")
    
    logeado = False

    for usuario in baseDeDatos:
        if(usuario["Nombre"] == nombre and usuario["Contrasenia"] == contrasenia):
            logeado = True

    if(logeado == False):
        print("\n!!! Usuario o contrasenia invalidos !!!\n")
    else:
        print(f"\n***** Bienvenido {nombre} *****\n")


# Funcion para mostrar los usuarios registrados
def mostrarUsuarios():
    print("*** Los usuarios actuales son: ***\n")
    for usuario in baseDeDatos:
        print(usuario["Nombre"])

    print("\n *** fin de la lista de usuarios *** \n")

# inicio del programa principal

# definimos la "base de datos" para almacenar nuestros usuarios
baseDeDatos = []

# Revisamos si existe el archivo txt, en caso de que no exista lo creamos
if(not open("./data.txt" , "r")):
    f = open("./data.txt" , "w")
    f.write("")
    f.close()

# buscamos la base de datos y la almacenamos en texto plano
f = open("./data.txt", "r")
textoPlano = f.read()
f.close()

# dividimos el texto plano separando los diccionarios
textoListado =  textoPlano.split("|")

# Convertimos los textos planos a diccionarios y los metemos dentro de nuestra base de datos
for diccionario in textoListado:
    
    if(diccionario != ""):
        dictionary = ast.literal_eval(diccionario)
        baseDeDatos.append(dictionary)

# Menu de seleccion de opciones
control = 1

while control != 0:
    # diferentes opciones dependiendo el numero ingresado por el usuario
    control = int(input("Para registrar un nuevo usuario presiona 1 \nPara iniciar sesion presiona 2 \nPara mostrar los usuarios registrados presiona 3 \nPara salir presiona 0\n"))
    if control == 1:
        registrarUsuario()
    elif control == 2:
        iniciarSesion()
    elif control == 3:
        mostrarUsuarios()
    else:
        print("\n !!! Opcion no valida, vuelve a intentarlo !!! \n")

    # Escribimos cualquier cambio hecho en la base de datos
    f = open("./data.txt" , "w")

    for usuario in baseDeDatos:
        f.write("{")
        for clave, valor in usuario.items():
            f.write(f"'{clave}' : '{valor}',")
        f.write("}|")

    f.close()
