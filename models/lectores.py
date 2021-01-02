from conexion.conn import Conexion

class Lectores:
    def __init__(self, id_lector='', dni_lector='', nombres='', apellidos='', correo='', direccion='',id_tipo_lector='',id_estado_libro=''):
        self.model = Conexion('lectores')
        self.id_lector = id_lector
        self.dni_lector = dni_lector
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo 
        self.direccion = direccion 
        self.id_tipo_lector = id_tipo_lector
        self.id_estado_libro = id_estado_libro
    
    def obtain_lectores(self):
        return self.model.get_all()

    def insert_lectores(self):
        try:
            query = f"""
                INSERT INTO lectores(dni_lector,nombres,apellidos,correo,direccion,id_tipo_lector) VALUES('{self.dni_lector}','{self.nombres}','{self.apellidos}',
                '{self.correo}','{self.direccion}','{self.id_tipo_lector}');
            """
            self.model.execute_query(query)
            self.model.commit()
        except Exception as e:
            print(str(e))

    def update_lectores(self):
        try:
            query = f"""
                UPDATE lectores SET dni_lector='{self.dni_lector}', nombres='{self.nombres}', apellidos='{self.apellidos}', correo='{self.correo}', direccion='{self.direccion}'
                WHERE id_lector = '{self.id_lector}';
            """
            self.model.execute_query(query)
            self.model.commit()
        except Exception as e:
            print(str(e))

    def delete_lectores(self):
        try:
            query = f"""
                DELETE FROM lectores WHERE id_lector = '{self.id_lector}';
            """
            self.model.execute_query(query)
            self.model.commit()
        except Exception as e:
            print(str(e))
