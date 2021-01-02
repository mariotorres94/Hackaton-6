from models.prestamos import Prestamos
from models.tipo_lector import Tipo_Lector
from controller.tipo_lector_controller import Tipo_Lector_Controller
from models.lectores import Lectores

class Prestamos_Controller:
    def __init__(self):
        self.prestamo = Prestamos()
        self.tipo_lector = Tipo_Lector()
        self.lector = Lectores()
        self.tipo_controller = Tipo_Lector_Controller()
        self.close = False

    def menu_prestamo(self):
        while True:
            try:
                print("\n\t       Prestamos")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar
        2) Registrar
        3) Actualizar
        4) Eliminar
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listado_inner()
                elif opcion == 2:
                    self.registro_fecha_prestamo()
                elif opcion == 3:
                    self.actualizar_prestamo()
                elif opcion == 4:
                    self.eliminar_datos_lectores()
                elif opcion == 5:
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_prestamos(self):
        prestamos = self.prestamo.obtain_prestamos()
        if prestamos:
            print("Lista de Clientes")
            print("ID PRESTAMO          FECHA PRESTAMO             FECHA DEVOLUCION")
            for i in prestamos:
                print(f"({i[0]})\t({i[1]})\t({i[2]})")
        else:
            print("No hay ningun registro en la base de datos")

    def registro_fecha_prestamo(self):
        self.tipo_controller.listado_tipo_lector()
        tipo_lectores = self.tipo_lector.inner_join_tipo_lector()
        prestamos = self.prestamo.inner_join_prestamo()

        id_lector = int(input("Seleccione por ID-LECTOR, lector que adquirira prestamo: "))
        self.lector.id_lector = id_lector

        for i in tipo_lectores:
            if i[1] == id_lector:
                id_lector = i[1]
                self.prestamo.id_lector = id_lector
                print(id_lector)
            
                id_tipo_lector = i[0]
                self.prestamo.id_tipo_lector = id_tipo_lector
                print(id_tipo_lector)

        print("Registro de Prestamo")
        respuesta = input("¿Ingresara fecha de prestamo? Y/N: ")
        if respuesta == 'Y' or respuesta == 'y':
            fecha_prestamo = input("Ingrese fecha de prestamo: ")
            self.prestamo.fecha_prestamo = fecha_prestamo
        elif respuesta == 'N' or respuesta == 'n':
            for i in prestamos:
                if i[0] == id_lector:
                    fecha_prestamo = i[6]
                    self.prestamo.fecha_prestamo = fecha_prestamo

        self.prestamo.insert_prestamos()

    def listado_inner(self):
        listado_prestamos = self.prestamo.inner_join_prestamo()
        if listado_prestamos:
            print("Listado de Prestamos")
            print("ID PRESTAMO  DNI LECTOR          NOMBRES          APELLIDOS                CORREO               TIPO LECTOR             FECHA PRESTAMO     FECHA DEVOLUCION")
            for i in listado_prestamos:
                print(f"({i[0]})\t   ({i[1]})\t   ({i[2]})\t        ({i[3]})\t   ({i[4]})\t    ({i[5]})     ({i[6]})\t  ({i[7]})\t")
        else:
            print("No se encuentra registro en la base de datos")

    def actualizar_prestamo(self):
        self.listado_inner()

        prestamos = self.prestamo.inner_join_prestamo()

        id_prestamo = int(input("Seleccione ID PRESTAMO que ingresara fecha de devolucion: "))
        self.prestamo.id_prestamo = id_prestamo

        print("Datos que Actualizara")
        print("---------------------")

        respuesta = input("¿Esta seguro de ingresar fecha de prestamo de Lector? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            fecha_prestamo = input("Ingrese nueva fecha de devolucion: ")
            self.prestamo.fecha_prestamo = fecha_prestamo
        elif respuesta == 'N' or respuesta == 'n':
            for i in prestamos:
                if i[0] == id_prestamo:
                    fecha_prestamo = i[6]
                    self.prestamo.fecha_prestamo = fecha_prestamo
                    print(f"({i[1]})\t({i[6]})")
                    print(fecha_prestamo)

        respuesta = input("¿Esta seguro de ingresar fecha de devolucion de Lector? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            fecha_devolucion = input("Ingrese nueva fecha de devolucion: ")
            self.prestamo.fecha_devolucion = fecha_devolucion
        elif respuesta == 'N' or respuesta == 'n':
            for i in prestamos:
                if i[0] == id_prestamo:
                    fecha_devolucion = i[7]
                    self.prestamo.fecha_devolucion = fecha_devolucion
                    print(f"({i[1]})\t({i[7]})")
                    print(fecha_devolucion)
        
        self.prestamo.update_prestamos()
        
    def eliminar_datos_lectores(self):
        self.listar_prestamos()

        id_prestamo = int(input("Seleccione que dato desea eliminar: "))
        self.prestamo.id_prestamo = id_prestamo

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.prestamo.delete_prestamos()
        else:
            self.menu_prestamo()