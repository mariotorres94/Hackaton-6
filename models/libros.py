from conexion.conn import Conexion

class Libros:
    def __init__(self, id_libro='', nombre='',fecha_publicacion='',estado_libro=''):
        self.model = Conexion('libros')
        self.id_libro = id_libro
        self.nombre = nombre
        self.fecha_publicacion = fecha_publicacion
        self.estado_libro = estado_libro
        """self.id_autor = id_autor
        self.id_editorial = id_editorial
        self.id_genero = id_genero
        self.id_estado_libro = id_estado_libro"""

    def obtain_libros(self):
        return self.model.get_all()

    def insert_libros(self):
        query = f"""
            INSERT INTO libros(id_libro,nombre,fecha_publicacion,id_autor,id_editorial,id_genero,id_estado_libro) 
            VALUES('{self.id_libro}','{self.nombre}','{self.fecha_publicacion}');
        """
        self.model.execute_query(query)
        self.model.commit()

    def update_libro(self):
        query = f"""
            UPDATE libros SET nombre='{self.nombre}', fecha_publicacion='{self.fecha_publicacion}'
            WHERE id_libro = '{self.id_libro}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def delete_libro(self):
        query = f"""
            DELETE FROM libros WHERE id_libro = '{self.id_libro}';
        """
        self.model.execute_query(query)
        self.model.commit()

    def inner_join_libros(self):
        query = """
            select li.id_libro,li.nombre as LIBRO,au.nombres,au.apellidos,li.fecha_publicacion,ed.nombre_editorial as EDITORIAL, ge.nombre_genero as GENERO
            from libros li
            inner join autores au
            on li.id_autor = au.id_autor
            inner join editorial ed
            on li.id_editorial = ed.id_editorial
            inner join genero ge
            on li.id_genero = ge.id_genero
        """
        return self.model.execute_query(query)

    def inner_join_libro_estado(self):
        query = """
            select li.id_libro,li.nombre as LIBRO,au.nombres,au.apellidos,li.fecha_publicacion,ed.nombre_editorial as EDITORIAL, 
            ge.nombre_genero as GENERO, el.nombre_estado as ESTADO
            from libros li
            inner join autores au
            on li.id_autor = au.id_autor
            inner join editorial ed
            on li.id_editorial = ed.id_editorial
            inner join genero ge
            on li.id_genero = ge.id_genero
            inner join estado_libro el
            on li.id_estado_libro = el.id_estado_libro
        """
        return self.model.execute_query(query)