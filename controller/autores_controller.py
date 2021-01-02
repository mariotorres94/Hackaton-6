from models.autores import Autores

class Autores_Controller:
    def __init__(self):
        self.autor = Autores()
        self.close = False

    def menu_autores(self):
        while True:
            try:
                print("\n\t       Autores")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar
        2) Registrar Autor
        3) Actualizar Autor
        4) Eliminar Autor
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_autores()
                elif opcion == 2:
                    self.registro_autores()
                elif opcion == 3:
                    self.actualizar_autor()
                elif opcion == 4:
                    self.eliminar_autor()
                elif opcion == 5:
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_autores(self):
        autores = self.autor.obtain_autores()
        if autores:
            print("Lista de Autores")
            print("ID AUTOR         NOMBRES         APELLIDOS       NACIONALIDAD")
            for i in autores:
                print(f"({i[0]})\t({i[1]})\t({i[2]})\t({i[3]})")
        else:
            print("No hay ningun registro en la base de datos")

    def registro_autores(self):
        
        id_autor = int(input("Ingrese identificador de Autor: "))
        nombres = input("Ingrese nombre de autor: ")
        apellidos = input("Ingrese apellido de autor: ")
        nacionalidad = input("Ingrese nacionalidad: ")

        self.autor.id_autor = id_autor
        self.autor.nombres = nombres
        self.autor.apellidos = apellidos
        self.autor.nacionalidad = nacionalidad

        self.autor.insert_autores()

    def actualizar_autor(self):
        self.listar_autores()

        autores = self.autor.obtain_autores()

        id_autor = int(input("Seleccione ID que actualizara datos: "))
        self.autor.id_autor = id_autor

        print("Datos que Actualizara")
        print("---------------------")

        respuesta = input("¿Esta seguro de actualizar nombres del Autor? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nombres = input("Ingrese nuevo nombre de Autor: ")
            self.autor.nombres = nombres
        elif respuesta == 'N' or respuesta == 'n':
            for i in autores:
                if i[0] == id_autor:
                    nombres = i[1]
                    self.autor.nombres = nombres
                    print(f"({i[0]})\t({i[1]})")
                    print(nombres)

        respuesta = input("¿Esta seguro de actualizar apellidos del Autor? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            apellidos = input("Ingrese nuevo apellido de Autor: ")
            self.autor.apellidos = apellidos
        elif respuesta == 'N' or respuesta == 'n':
            for i in autores:
                if i[0] == id_autor:
                    apellidos = i[2]
                    self.autor.apellidos = apellidos
                    print(f"({i[1]})\t({i[2]})")
                    print(apellidos)

        respuesta = input("¿Esta seguro de actualizar nacionalidad del Autor? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nacionalidad = input("Ingrese nueva nacionalidad de Autor: ")
            self.autor.nacionalidad = nacionalidad
        elif respuesta == 'N' or respuesta == 'n':
            for i in autores:
                if i[0] == id_autor:
                    nacionalidad = i[3]
                    self.autor.nacionalidad = nacionalidad
                    print(f"({i[1]})\t({i[3]})")
                    print(nacionalidad)
        
        self.autor.update_autores()
        
    def eliminar_autor(self):
        self.listar_autores()

        id_autor = int(input("Seleccione que dato desea eliminar: "))
        self.autor.id_autor = id_autor

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.autor.delete_autor()
        else:
            self.menu_autores()