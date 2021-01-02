from models.estados import Estados

class Estados_Controller:
    def __init__(self):
        self.estado = Estados()
        self.close = False
    
    def menu_estados(self):
        while True:
            try:
                print("\n\t       Estados de Libro")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Estados - Libros
        2) Registro Estados
        3) Actualizar Estado - Libro
        4) Eliminar Estado - Libro
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_estados()
                elif opcion == 2:
                    self.registro_estado()
                elif opcion == 3:
                    self.actualizar_estado()
                elif opcion == 4:
                    self.eliminar_genero()
                elif opcion == 5:
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_estados(self):
        estados = self.estado.obtain_estados()
        if estados:
            print("Lista de Editoriales")
            print("ID ESTADO         NOMBRE ESTADO")
            for i in estados:
                print(f"({i[0]})\t({i[1]})")
        else:
            print("No hay ningun registro en la base de datos")

    def registro_estado(self):
        
        id_estado_libro = int(input("Ingrese identificador de Autor: "))
        nombres_estado = input("Ingrese nombre de autor: ")

        self.estado.id_estado_libro = id_estado_libro
        self.estado.nombre_estado = nombres_estado

        self.estado.insert_estado()

    def actualizar_estado(self):
        self.listar_estados()

        estados = self.estado.obtain_estados()

        id_estado_libro = int(input("Seleccione ID que actualizara datos: "))
        self.estado.id_estado_libro = id_estado_libro

        print("Datos que Actualizara")
        print("---------------------")

        respuesta = input("¿Esta seguro de actualizar nombre de Genero? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nombre_estado = input("Ingrese nuevo nombre de Autor: ")
            self.estado.nombre_estado = nombre_estado
        elif respuesta == 'N' or respuesta == 'n':
            for i in estados:
                if i[0] == id_estado_libro:
                    nombre_estado = i[1]
                    self.estado.nombre_estado = nombre_estado
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre_estado)
        
        self.estado.update_estado()
        
    def eliminar_genero(self):
        self.listar_estados()

        id_estado_libro = int(input("Seleccione que dato desea eliminar: "))
        self.estado.id_estado_libro = id_estado_libro

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.estado.delete_estado()
        else:
            self.menu_estados()