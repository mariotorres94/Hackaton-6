from models.genero import Generos

class Genero_Controller:
    def __init__(self):
        self.genero = Generos()
        self.close = False

    def menu_genero(self):
        while True:
            try:
                print("\n\t       Generos")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Generos
        2) Registrar Generos
        3) Actualizar Generos
        4) Eliminar Generos
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_generos()
                elif opcion == 2:
                    self.registro_genero()
                elif opcion == 3:
                    self.actualizar_genero()
                elif opcion == 4:
                    self.eliminar_genero()
                elif opcion == 5:
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_generos(self):
        generos = self.genero.obtain_generos()
        if generos:
            print("Lista de Editoriales")
            print("ID GENERO         NOMBRE GENERO")
            for i in generos:
                print(f"({i[0]})\t({i[1]})")
        else:
            print("No hay ningun registro en la base de datos")

    def registro_genero(self):
        
        id_genero = int(input("Ingrese identificador de Autor: "))
        nombre_genero = input("Ingrese nombre de autor: ")

        self.genero.id_genero = id_genero
        self.genero.nombre_genero = nombre_genero

        self.genero.insert_genero()

    def actualizar_genero(self):
        self.listar_generos()

        generos = self.genero.obtain_generos()

        id_genero = int(input("Seleccione ID que actualizara datos: "))
        self.genero.id_genero = id_genero

        print("Datos que Actualizara")
        print("---------------------")

        respuesta = input("¿Esta seguro de actualizar nombre de Genero? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nombre_genero = input("Ingrese nuevo nombre de Autor: ")
            self.genero.nombre_genero = nombre_genero
        elif respuesta == 'N' or respuesta == 'n':
            for i in generos:
                if i[0] == id_genero:
                    nombre_genero = i[1]
                    self.genero.nombre_genero = nombre_genero
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre_genero)
        
        self.genero.update_genero()
        
    def eliminar_genero(self):
        self.listar_generos()

        id_genero = int(input("Seleccione que dato desea eliminar: "))
        self.genero.id_genero = id_genero

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.genero.delete_genero()
        else:
            self.menu_genero()