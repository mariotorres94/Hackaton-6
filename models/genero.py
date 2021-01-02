from conexion.conn import Conexion

class Generos:
    def __init__(self, id_genero='', nombre_genero=''):
        self.model = Conexion('genero')
        self.id_genero = id_genero
        self.nombre_genero = nombre_genero

    def obtain_generos(self):
        return self.model.get_all()

    def insert_genero(self):
        query = f"""
            INSERT INTO genero(id_genero,nombre_genero) VALUES('{self.id_genero}','{self.nombre_genero}');
        """
        self.model.execute_query(query)
        self.model.commit()

    def update_genero(self):
        query = f"""
            UPDATE genero SET nombre_genero='{self.nombre_genero}'
            WHERE id_genero = '{self.id_genero}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def delete_genero(self):
        query = f"""
            DELETE FROM genero WHERE id_genero = '{self.id_genero}';
        """
        self.model.execute_query(query)
        self.model.commit()