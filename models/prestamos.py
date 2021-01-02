from conexion.conn import Conexion

class Prestamos:
    def __init__(self,id_prestamo='',fecha_prestamo='',fecha_devolucion='',id_lector='',id_tipo_lector=''):
        self.model = Conexion('prestamos')
        self.model1 = Conexion('lectores')
        self.model2 = Conexion('tipo_lector')
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.id_lector = id_lector
        self.id_tipo_lector = id_tipo_lector

    def obtain_prestamos(self):
        return self.model.get_all()

    def insert_prestamos(self):
        query = f"""
            INSERT INTO prestamos(fecha_prestamo,fecha_devolucion,id_lector,id_tipo_lector) VALUES('{self.fecha_prestamo}','{self.fecha_devolucion}',{self.id_lector},{self.id_tipo_lector});
        """
        self.model.execute_query(query)
        self.model.commit()

    def update_prestamos(self):
        query = f"""
            UPDATE prestamos SET fecha_prestamo = '{self.fecha_prestamo}', fecha_devolucion = '{self.fecha_devolucion}'
            WHERE id_prestamo = '{self.id_prestamo}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def delete_prestamos(self):
        query = f"""
            DELETE FROM prestamos WHERE id_prestamo = '{self.id_prestamo}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def inner_join_prestamo(self):
        query = """
                select pr.id_prestamo,l.dni_lector,l.nombres,l.apellidos,l.correo,tp.nombre_tipo_lector,pr.fecha_prestamo,pr.fecha_devolucion 
                from lectores l
                inner join tipo_lector tp
                on l.id_tipo_lector = tp.id_tipo_lector
                inner join prestamos pr
                on pr.id_lector = l.id_lector
        """
        return self.model1.execute_query(query)