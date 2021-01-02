from conexion.conn import Conexion

class Estados:
    def __init__(self, id_estado_libro='', nombre_estado=''):
        self.model = Conexion('estado_libro')
        self.id_estado_libro = id_estado_libro
        self.nombre_estado = nombre_estado

    def obtain_estados(self):
        return self.model.get_all()

    def insert_estado(self):
        query = f"""
            INSERT INTO estado_libro(id_estado_libro,nombre_estado) 
            VALUES('{self.id_estado_libro}','{self.nombre_estado}');
        """
        self.model.execute_query(query)
        self.model.commit()

    def update_estado(self):
        query = f"""
            UPDATE estado_libro SET id_estado_libro='{self.id_estado_libro}',nombre_estado='{self.nombre_estado}'
            WHERE id_estado_libro = '{self.id_estado_libro}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def delete_estado(self):
        query = f"""
            DELETE FROM estado_libro WHERE id_estado_libro = '{self.id_estado_libro}';
        """
        self.model.execute_query(query)
        self.model.commit()