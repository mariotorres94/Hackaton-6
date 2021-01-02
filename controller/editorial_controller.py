from models.editoriales import Editoriales

class Editoriales_Controller:
    def __init__(self):
        self.editorial = Editoriales()
        self.close = False

    def menu_editorial(self):
        while True:
            try:
                print("\n\t       Editoriales")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Editoriales
        2) Registrar Editorial
        3) Actualizar Editorial
        4) Eliminar Editorial
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_editoriales()
                elif opcion == 2:
                    self.registro_editorial()
                elif opcion == 3:
                    self.actualizar_editorial()
                elif opcion == 4:
                    self.eliminar_editorial()
                elif opcion == 5:
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_editoriales(self):
        editoriales = self.editorial.obtain_editoriales()
        if editoriales:
            print("Lista de Editoriales")
            print("ID EDITORIAL         NOMBRE EDITORIAL")
            for i in editoriales:
                print(f"({i[0]})\t({i[1]})")
        else:
            print("No hay ningun registro en la base de datos")

    def registro_editorial(self):
        
        id_editorial = int(input("Ingrese identificador de Autor: "))
        nombre_editorial = input("Ingrese nombre de autor: ")

        self.editorial.id_editorial = id_editorial
        self.editorial.nombre_editorial = nombre_editorial

        self.editorial.insert_editorial()

    def actualizar_editorial(self):
        self.listar_editoriales()

        editoriales = self.editorial.obtain_editoriales()

        id_editorial = int(input("Seleccione ID que actualizara datos: "))
        self.editorial.id_editorial = id_editorial

        print("Datos que Actualizara")
        print("---------------------")

        respuesta = input("¿Esta seguro de actualizar nombre de Editorial? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nombre_editorial = input("Ingrese nuevo nombre de Autor: ")
            self.editorial.nombre_editorial = nombre_editorial
        elif respuesta == 'N' or respuesta == 'n':
            for i in editoriales:
                if i[0] == id_editorial:
                    nombre_editorial = i[1]
                    self.editorial.nombre_editorial = nombre_editorial
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre_editorial)
        
        self.editorial.update_editorial()
        
    def eliminar_editorial(self):
        self.listar_editoriales()

        id_editorial = int(input("Seleccione que dato desea eliminar: "))
        self.editorial.id_editorial = id_editorial

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.editorial.delete_editorial()
        else:
            self.menu_editorial()