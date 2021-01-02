from controller.lectores_controller import Lectores_Controller
from controller.libros_controller import Libros_Controller
from controller.autores_controller import Autores_Controller
from controller.editorial_controller import Editoriales_Controller
from controller.genero_controller import Genero_Controller
from controller.estados_controller import Estados_Controller
from controller.tipo_lector_controller import Tipo_Lector_Controller
from controller.prestamos_controller import Prestamos_Controller

lector = Lectores_Controller()
libro = Libros_Controller()
autor = Autores_Controller()
editorial = Editoriales_Controller()
genero = Genero_Controller()
estado = Estados_Controller()
tipo_lector = Tipo_Lector_Controller()
prestamo = Prestamos_Controller()

while True:
    try:

        print("\n")
        print("\t|****************************|")
        print("\t|**|      Bienvenidos     |**|")
        print("\t|**|         Menu         |**|")
        print("\t|****************************|")
        print("")
        print("""
            1. Menu Lectores
            2. Menu Libros
            3. Menu Autores
            4. Menu Editorial
            5. Menu Genero
            6. Menu Estado
            7. Tipos de Lectores
            8. Regitro Prestamos y Devoluciones
            9. Salir
        """)

        opcion = int(input("Seleccione una opcion del menu: "))

        if opcion == 1:
            lector.menu_lector()
        elif opcion == 2:
            libro.menu_libros()
        elif opcion == 3:
            autor.menu_autores()
        elif opcion == 4:
            editorial.menu_editorial()
        elif opcion == 5:
            genero.menu_genero()
        elif opcion == 6:
            estado.menu_estados()
        elif opcion == 7:
            tipo_lector.menu_tipo_lector()
        elif opcion == 8:
            prestamo.menu_prestamo()
        elif opcion == 9:
            print("Saliendo ...")
            exit()
        else:
            print("Opcion digitada no se encuentra en el menu, Intentelo nuevamente...")
    
    except Exception:
        print("Solo puede ingresar numeros enteros, Intentelo nuevamente")