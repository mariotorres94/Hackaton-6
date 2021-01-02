from models.libros import Libros
from models.autores import Autores

class Libros_Controller:
    def __init__(self):
        self.libro = Libros()
        self.autor = Autores()
        self.close = False
    
    def menu_libros(self):
        while True:
            try:
                print("\n\t       Libros")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Libro - Autor
        2) Listar Libros
        3) Registrar Libro
        4) Actualizar Libro
        5) Eliminar Libro
        6) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_libro_autor()
                elif opcion == 2:
                    self.listar_libros()
                elif opcion == 3:
                    self.registro_libros()
                elif opcion == 4:
                    self.actualizar_datos_libro()
                elif opcion == 5:
                    self.eliminar_datos_libro()
                elif opcion == 6:
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listado_libro_estado(self):
        estado_libro = self.libro.inner_join_libro_estado()
        if estado_libro:
            print("Lista Libro - Estado")
            print("ID LIBRO         NOMBRE DE LIBRO           NOMBRE AUTOR          APELLIDO AUTOR      AÑO DE PUBLICACION       EDITORIAL         GENERO       ESTADO")
            for i in estado_libro:
                print(f"({i[0]})\t    ({i[1]})\t({i[2]})\t({i[3]})\t        ({i[4]})\t              ({i[5]})\t      ({i[6]})\t ({i[7]})\t")
        else:
            print("No se encuentra ningun Libro o Autor registrado en la base de datos")

    def listar_libro_autor(self):
        libros = self.libro.inner_join_libros()

        if libros:
            print("Lista Libro - Autor")
            print("ID LIBRO         NOMBRE DE LIBRO           NOMBRE AUTOR          APELLIDO AUTOR      AÑO DE PUBLICACION       EDITORIAL         GENERO")
            for i in libros:
                print(f"({i[0]})\t    ({i[1]})\t({i[2]})\t({i[3]})\t        ({i[4]})\t              ({i[5]})\t      ({i[6]})\t")
        else:
            print("No se encuentra ningun Libro o Autor registrado en la base de datos")

    def listar_libros(self):
        libros = self.libro.obtain_libros()
        if libros:
            print("Lista de Libros")
            print("ID LIBRO             NOMBRE             FECHA PUBLICACION         ID AUTOR      ID EDITORIAL        ID GENERO")
            for i in libros:
                print(f"({i[0]})\t  ({i[1]})\t({i[2]})\t({i[3]})\t({i[4]})\t({i[5]})")
        else:
            print("No se encuentra ningun cliente registrado en la base de datos")

    def listar_autores(self):
        autores = self.autor.obtain_autores()
        if autores:
            print("Lista de Clientes")
            print("ID AUTOR          NOMBRES             APELLIDOS         NACIONALIDAD")
            for i in autores:
                print(f"({i[0]})\t({i[1]})\t({i[2]})\t({i[3]})")
        else:
            print("No se encuentra ningun cliente registrado en la base de datos")

    def registro_libros(self):

        print("Registro de Libros")
        nombre = input("Ingrese nombre de Libro: ")
        fecha_publicacion = input("Ingrese fecha de publicacion: ")

        self.listar_autores()
        autores = self.autor.obtain_autores()
        print("Seleccione autor que publico libro registrado: ")
        id_autor = int(input("Seleccione ID AUTOR: "))

        for i in autores:
            if i[0] == id_autor:
                id_libro = i[0]
                self.libro.id_libro = id_libro
                self.libro.id_autor = id_autor
                print(id_autor)
                print(id_libro)

        print("\nEditoriales")
        print("-----------------")
        print("""
            1. Acantilado
            2. Aguilar
            3. Almadía
            4. Alfaguara
        """)
        id_editorial = int(input("¿A que editorial pertenece?: ")) 
        self.libro.id_editorial = id_editorial

        print("\nGeneros")
        print("-----------------")
        print("""
            1. Aventura
            2. Ciencia Ficcion
            3. Cuentos de Hadas
            4. Piliciaca
        """)
        id_genero = int(input("¿A que editorial pertenece?: "))      

        print("\nEstados")
        print("-----------------")
        print("""
            1. Prestado
            2. No Prestado
        """)
        id_estado_libro = int(input("¿A que editorial pertenece?: "))    
        if id_estado_libro == "":
            self.libro.id_estado_libro = id_estado_libro
            

        self.libro.nombre = nombre
        self.libro.fecha_publicacion = fecha_publicacion
        self.libro.id_genero = id_genero
        self.libro.id_estado_libro = id_estado_libro

        self.libro.insert_libros()
    def actualizar_datos_libro(self):
        self.listar_libros()
        libros = self.libro.obtain_libros()

        id_libro = int(input("Seleccione un alumno de la lista: "))
        self.libro.id_libro = id_libro

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar nombre de Libro? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nombre = input("Ingrese el nuevo nombre de Libro: ")
            self.libro.nombre = nombre
        elif respuesta == 'N' or respuesta == 'n':
            for i in libros:
                if i[0] == id_libro:
                    nombre = i[1]
                    self.libro.nombre = nombre
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre)

        respuesta = input("¿Esta seguro de actualizar fecha_publicacion de Libro? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            fecha_publicacion = input("Ingrese nombre completo: ")
            self.libro.fecha_publicacion = fecha_publicacion
        elif respuesta == 'N' or respuesta == 'n':
            for i in libros:
                if i[0] == id_libro:
                    fecha_publicacion = i[2]
                    self.libro.fecha_publicacion = fecha_publicacion
                    print(f"({i[0]})\t({i[2]})")
                    print(fecha_publicacion)
        
        self.libro.update_libro()
        
    def eliminar_datos_libro(self):
        self.listar_libros()

        id_libro = int(input("Seleccione alumno que desea eliminar sus datos: "))
        self.libro.id_libro = id_libro

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.libro.delete_libro()
        else:
            self.menu_libros()