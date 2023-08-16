def pedir_prestado(usuario_idx, libro_idx):
    if libros[libro_idx][1] == "disponible" and usuarios[usuario_idx][1] is None:
        libros[libro_idx][1] = "prestado"
        usuarios[usuario_idx][1] = libro_idx
        print(f"{usuarios[usuario_idx][0]} ha pedido prestado el libro '{libros[libro_idx][0]}'")
    else:
        print("No es posible pedir prestado el libro.")

def devolver(usuario_idx):
    libro_prestado_idx = usuarios[usuario_idx][1]
    if libro_prestado_idx is not None:
        libros[libro_prestado_idx][1] = "disponible"
        usuarios[usuario_idx][1] = None
        print(f"{usuarios[usuario_idx][0]} ha devuelto el libro '{libros[libro_prestado_idx][0]}'")
    else:
        print("El usuario no tiene ningún libro prestado.")

def mostrar_libros():
    print("Libros en la biblioteca:")
    for i, libro in enumerate(libros):
        print(f"{i + 1}. Título: {libro[0]} - Estado: {libro[1]}")

def mostrar_usuarios():
    print("Usuarios y libros prestados:")
    for i, usuario in enumerate(usuarios):
        libro_prestado_idx = usuario[1]
        libro = libros[libro_prestado_idx][0] if libro_prestado_idx is not None else "Ninguno"
        print(f"{i + 1}. Usuario: {usuario[0]} - Libro prestado: {libro}")

def insertar_libro(titulo):
    libros.append([titulo, "disponible"])
    print(f"Se ha insertado el libro '{titulo}' en la biblioteca.")

libros = [["Cien años de soledad", "disponible"], ["1984", "disponible"], ["Don Quijote de la Mancha", "disponible"]]
usuarios = [["Juan", None], ["María", None]]

while True:
    print("Menú de opciones:")
    print("1. Pedir prestado")
    print("2. Devolver")
    print("3. Mostrar libros")
    print("4. Mostrar usuarios")
    print("5. Insertar libro")
    print("6. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        mostrar_usuarios()
        usuario_idx = int(input("Seleccione el número de usuario: ")) - 1
        mostrar_libros()
        libro_idx = int(input("Seleccione el número de libro: ")) - 1
        pedir_prestado(usuario_idx, libro_idx)
    
    elif opcion == 2:
        mostrar_usuarios()
        usuario_idx = int(input("Seleccione el número de usuario: ")) - 1
        devolver(usuario_idx)
    
    elif opcion == 3:
        mostrar_libros()
    
    elif opcion == 4:
        mostrar_usuarios()
    
    elif opcion == 5:
        titulo_libro = input("Ingrese el título del nuevo libro: ")
        insertar_libro(titulo_libro)
    
    elif opcion == 6:
        break
