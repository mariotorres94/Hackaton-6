from conexion.conn import Conexion

class Tipo_Lector:
    def __init__(self, id_tipo_lector='', nombre_tipo_lector=''):
        self.model1 = Conexion('tipo_lector')
        self.model = Conexion('lectores')
        self.id_tipo_lector = id_tipo_lector
        self.nombre_tipo_lector = nombre_tipo_lector
    
    def obtain_tipo_lectores(self):
        return self.model1.get_all()

    def insert_tipo_lectores(self):
        try:
            query = f"""
                INSERT INTO tipo_lector(id_tipo_lector,nombre_tipo_lector) VALUES('{self.id_tipo_lector}','{self.nombre_tipo_lector}');
            """
            self.model1.execute_query(query)
            self.model1.commit()
        except Exception as e:
            print(str(e))

    def update_tipo_lectores(self):
        try:
            query = f"""
                UPDATE tipo_lector SET id_tipo_lector='{self.id_tipo_lector}', nombre_tipo_lector='{self.nombre_tipo_lector}'
                WHERE id_tipo_lector = '{self.id_tipo_lector}';
            """
            self.model1.execute_query(query)
            self.model1.commit()
        except Exception as e:
            print(str(e))

    def delete_tipo_lectores(self):
        try:
            query = f"""
                DELETE FROM tipo_lector WHERE id_tipo_lector = '{self.id_tipo_lector}';
            """
            self.model1.execute_query(query)
            self.model1.commit()
        except Exception as e:
            print(str(e))

    def inner_join_tipo_lector(self):
        try:
            query = f"""select lectores.id_tipo_lector,lectores.id_lector,lectores.dni_lector,lectores.nombres,lectores.apellidos,lectores.correo,tipo_lector.nombre_tipo_lector 
                from lectores
                inner join tipo_lector
                on lectores.id_tipo_lector = tipo_lector.id_tipo_lector"""
            return self.model.execute_query(query)
        except Exception as e:
            print(str(e))
