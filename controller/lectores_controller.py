from models.lectores import Lectores

class Lectores_Controller:
    def __init__(self):
        self.lector = Lectores()
        self.close = False
    
    def menu_lector(self):
        while True:
            try:
                print("\n\t       Clientes")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Lectores
        2) Registro Lectores
        3) Actualizar datos de Lector
        4) Eliminar datos de Lector
        5) Registro de Prestamo
        6) Registro de Devolucion
        7) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_lectores()
                elif opcion == 2:
                    self.registro_lectores()
                elif opcion == 3:
                    self.actualizar_datos_lectores()
                elif opcion == 4:
                    self.eliminar_datos_lectores()
                elif opcion == 5:
                    "self.prestamo.registro_fecha_prestamo()"
                    pass
                elif opcion == 6:
                    "self.prestamo.actualizar_prestamo()"
                    pass
                elif opcion == 7:
                    "self.menu_principal()"
                    pass
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_lectores(self):
        lectores = self.lector.obtain_lectores()
        if lectores:
            print("Lista de Clientes")
            print("ID LECTOR          DNI             NOMBRES         APELLIDOS        CORREO           DIRECCION")
            for i in lectores:
                print(f"({i[0]})\t({i[1]})\t({i[2]})\t({i[3]})\t({i[4]})\t({i[5]})")
        else:
            print("No se encuentra ningun cliente registrado en la base de datos")

    def registro_lectores(self):

        print("Registro de Clientes")
        dni_lector = input("Ingrese dni de cliente: ")
        nombres = input("Ingrese nombres completo: ")
        apellidos = input("Ingrese apellidos completo: ")                
        correo = input("Ingrese correo de cliente: ")
        direccion = input("Ingrese direccion de cliente: ")

        print("\nTipo de Lector")
        print("-----------------")
        print("""
            1. Universitario
            2. Docentes
            3. Escolar
            4. Publico en General
        """)
        id_tipo_lector = int(input("¿Que tipo de lector es?"))                

        self.lector.dni_lector = dni_lector
        self.lector.nombres = nombres
        self.lector.apellidos = apellidos
        self.lector.correo = correo
        self.lector.direccion = direccion
        self.lector.id_tipo_lector = id_tipo_lector

        self.lector.insert_lectores()

    def actualizar_datos_lectores(self):
        self.listar_lectores()
        lectores = self.lector.obtain_lectores()

        id_lector = int(input("Seleccione un alumno de la lista: "))
        self.lector.id_lector = id_lector

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar dni de Lector? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            dni_lector = input("Ingrese dni: ")
            self.lector.dni_lector = dni_lector
        elif respuesta == 'N' or respuesta == 'n':
            for i in lectores:
                if i[0] == id_lector:
                    dni_lector = i[1]
                    self.lector.dni_lector = dni_lector
                    print(f"({i[0]})\t({i[1]})")
                    print(dni_lector)

        respuesta = input("¿Esta seguro de actualizar nombres? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            nombres = input("Ingrese nombre completo: ")
            self.lector.nombres = nombres
        elif respuesta == 'N' or respuesta == 'n':
            for i in lectores:
                if i[0] == id_lector:
                    nombres = i[2]
                    self.lector.nombres = nombres
                    print(f"({i[0]})\t({i[2]})")
                    print(nombres)

        respuesta = input("¿Esta seguro de actualizar apellidos? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            apellidos = input("Ingrese apellidos completos: ")
            self.lector.apellidos = apellidos
        elif respuesta == 'N' or respuesta == 'n':
            for i in lectores:
                if i[0] == id_lector:
                    apellidos = i[3]
                    self.lector.apellidos = apellidos
                    print(f"({i[0]})\t({i[3]})")
                    print(apellidos)

        respuesta = input("¿Esta seguro de actualizar correo? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            correo = input("Ingrese correo: ")
            self.lector.correo = correo
        elif respuesta == 'N' or respuesta == 'n':
            for i in lectores:
                if i[0] == id_lector:
                    correo = i[4]
                    self.lector.correo = correo
                    print(f"({i[0]})\t({i[4]})")
                    print(correo)

        respuesta = input("¿Esta seguro de actualizar direccion? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            direccion = input("Ingrese direccion: ")
            self.lector.direccion = direccion
        elif respuesta == 'N' or respuesta == 'n':
            for i in lectores:
                if i[0] == id_lector:
                    direccion = i[5]
                    self.lector.direccion = direccion
                    print(f"({i[0]})\t({i[5]})")
                    print(direccion)
        
        self.lector.update_lectores()
        
    def eliminar_datos_lectores(self):
        self.listar_lectores()

        id_lector = int(input("Seleccione alumno que desea eliminar sus datos: "))
        self.lector.id_lector = id_lector

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.lector.delete_lectores()
        else:
            self.menu_lector()