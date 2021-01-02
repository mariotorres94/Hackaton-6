from conexion.conn import Conexion

class Editoriales:
    def __init__(self, id_editorial='', nombre_editorial=''):
        self.model = Conexion('editorial')
        self.id_editorial = id_editorial
        self.nombre_editorial = nombre_editorial

    def obtain_editoriales(self):
        return self.model.get_all()

    def insert_editorial(self):
        query = f"""
            INSERT INTO editorial(id_editorial,nombre_editorial) VALUES('{self.id_editorial}','{self.nombre_editorial}');
        """
        self.model.execute_query(query)
        self.model.commit()

    def update_editorial(self):
        query = f"""
            UPDATE editorial SET nombre_editorial='{self.nombre_editorial}'
            WHERE id_editorial = '{self.id_editorial}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def delete_editorial(self):
        query = f"""
            DELETE FROM editorial WHERE id_editorial = '{self.id_editorial}';
        """
        self.model.execute_query(query)
        self.model.commit()