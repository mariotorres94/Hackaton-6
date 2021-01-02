from models.tipo_lector import Tipo_Lector

class Tipo_Lector_Controller:
    def __init__(self):
        self.tipo_lector = Tipo_Lector()
        self.close = False
    
    def menu_tipo_lector(self):
        while True:
            try:
                print("\n\t       Tipo Lector")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar
        2) Lista de Tipos-Lectores
        3) Registrar
        4) Actualizar
        5) Eliminar
        6) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_tipo_lector()
                elif opcion == 2:
                    self.listado_tipo_lector()
                elif opcion == 3:
                    self.registro_tipo_lector()
                elif opcion == 4:
                    self.actualizar_datos_tipo_lector()
                elif opcion == 5:
                    self.eliminar_datos_lectores()
                elif opcion == 6:
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))
    
    def listar_tipo_lector(self):
        tipo_lectores = self.tipo_lector.obtain_tipo_lectores()
        if tipo_lectores:
            print("Lista de Tipo de Lectores")
            for i in tipo_lectores:
                print(f"({i[0]})\t({i[1]})")
        else:
            print("No se encuentra registro en la base de datos")

    def listado_tipo_lector(self):
        tipo_lectores = self.tipo_lector.inner_join_tipo_lector()
        if tipo_lectores:
            print("Lista de Clientes")
            print("ID TIPO LECTOR      ID LECTOR    DNI LECTOR             NOMBRES         APELLIDOS            CORREO           TIPO LECTOR")
            for i in tipo_lectores:
                print(f"({i[0]})                \t({i[1]})  \t({i[2]})        \t({i[3]})      \t({i[4]})  \t({i[5]}) \t({i[6]})")
        else:
            print("No se encuentra registro en la base de datos")

    def registro_tipo_lector(self):

        print("Registro de Clientes")
        id_tipo_lector = int(input("Ingrese id de tipo de lector: "))
        nombre_tipo_lector = input("Ingrese nombre de tipo de lector: ")

        self.tipo_lector.id_tipo_lector = id_tipo_lector
        self.tipo_lector.nombre_tipo_lector = nombre_tipo_lector

        self.tipo_lector.insert_tipo_lectores()
    
    def actualizar_datos_tipo_lector(self):
        self.listar_tipo_lector()
        tipo_lectores = self.tipo_lector.obtain_tipo_lectores()

        id_tipo_lector = int(input("Seleccione un alumno de la lista: "))
        self.tipo_lector.id_tipo_lector = id_tipo_lector

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar nombre de tipo lector? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nombre_tipo_lector = input("Ingrese dni: ")
            self.tipo_lector.nombre_tipo_lector = nombre_tipo_lector
        elif respuesta == 'N' or respuesta == 'n':
            for i in tipo_lectores:
                if i[0] == id_tipo_lector:
                    nombre_tipo_lector = i[1]
                    self.tipo_lector.nombre_tipo_lector = nombre_tipo_lector
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre_tipo_lector)
        
        self.tipo_lector.update_tipo_lectores()
        
    def eliminar_datos_lectores(self):
        self.listar_tipo_lector()

        id_tipo_lector = int(input("Seleccione que dato desea eliminar: "))
        self.tipo_lector.id_tipo_lector = id_tipo_lector

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.tipo_lector.delete_tipo_lectores()
        else:
            self.menu_tipo_lector()