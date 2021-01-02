from conexion.conn import Conexion

class Autores:
    def __init__(self, id_autor='', nombres='', apellidos='', nacionalidad=''):
        self.model = Conexion('autores')
        self.id_autor = id_autor
        self.nombres = nombres
        self.apellidos = apellidos
        self.nacionalidad = nacionalidad

    def obtain_autores(self):
        return self.model.get_all()

    def insert_autores(self):
        query = f"""
            INSERT INTO autores(id_autor,nombres,apellidos,nacionalidad) VALUES('{self.id_autor}','{self.nombres}','{self.apellidos}','{self.nacionalidad}');
        """
        self.model.execute_query(query)
        self.model.commit()

    def update_autores(self):
        query = f"""
            UPDATE autores SET nombres='{self.nombres}', apellidos='{self.apellidos}', nacionalidad='{self.nacionalidad}'
            WHERE id_autor = '{self.id_autor}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def delete_autor(self):
        query = f"""
            DELETE FROM autores WHERE id_autor = '{self.id_autor}';
        """
        self.model.execute_query(query)
        self.model.commit()