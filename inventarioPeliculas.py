# inventarioPeliculas.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase InventarioPeliculas

import mysql.connector
from pelicula import Pelicula
from peliculaED import PeliculaED
from persistenciaException import PersistenciaException
from tabla import Tabla


class InventarioPeliculas(Tabla):
    """Esta clase permite agregar, modificar, eliminar y listar películas al inventario de películas.

    El inventario de películas se almacena en la tabla inventario_peliculas de la base de datos videocentro.
    """

    def __init__(self, user: str, password: str, host: str, database: str, nomTablaInventarioPeliculas: str, nomTablaPeliculas: str):
        """Constructor de la clase que inicializa todos sus atributos

        -------------------------------------------------------------
        Parameters
        ----------
        user: str
            Nombre del usuario de la base de datos
        password: str
            Contraseña del usuario de la base de datos
        host: str
            Dirección IP de la computadora con la base de datos
        database: str
            Base de datos
        nomTablaInventarioPeliculas: str
            Nombre de la tabla en la base de datos para el inventario de películas
        nomTablaPeliculas: str
            Nombre de la tabla en la base de datos para el catálogo de películas
        """
        super().__init__(user, password, host, database)
        self.__nomTablaInventarioPeliculas = nomTablaInventarioPeliculas
        self.__nomTablaPeliculas = nomTablaPeliculas

    def obten(self, peliculaED: PeliculaED):
        """Busca en el inventario de películas la películaED cuyo número de catálogo está en el parámetro peliculaED.
        
        Regresa la peliculaED si la encuentra, None en caso contrario.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la películaED del inventario de películas.

        --------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        peliculaED: PeliculaED
            peliculaED a obtener en la base de datos
        
        Returns
        -------
        PeliculaED
            peliculaED de la base de datos
        None
            En caso de que no se encuentre
        
        Throws
        ------
        PersistenciaException
            Si no se puede obtener la películaED del inventario de películas.
        """
        operacion = f"SELECT p.num_catalogo, p.titulo, p.genero, p.clasificacion, p.actor1, p.actor2, p.productora, ip.existencia, ip.disponibilidad"
        operacion += f" FROM {self.__nomTablaInventarioPeliculas} as ip INNER JOIN {self.__nomTablaPeliculas} as p"
        operacion += f" ON ip.num_catalogo = p.num_catalogo"
        operacion += f" WHERE ip.num_catalogo = '{peliculaED.pelicula.numCatalogo}';"

        try:
            renglon = super().obten(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaInventarioPeliculas} de la base de datos {self._database}') from e

        if (renglon is not None):
            numCatalogo, titulo, genero, clasificacion, actor1, actor2, productora, existencia, disponibilidad = renglon

            pelicula = Pelicula(numCatalogo, titulo, genero,
                                clasificacion, actor1, actor2, productora)
            peliculaED = PeliculaED(pelicula, existencia, disponibilidad)
            return peliculaED

        return None

    def agrega(self, peliculaED: PeliculaED):
        """Agrega la películaED del parámetro al inventario de películas.

        Lanza una excepción del tipo PersistenciaException si la películaED ya existe o no se puede agregar la películaED al inventario de películas.

        ---------------------------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        peliculaED: PeliculaED
            peliculaED a agregar en la base de datos
        
        Throws
        ------
        PersistenciaException
            Si la películaED ya existe o no se puede agregar la películaED al inventario de películas
        """
        operacion = f"INSERT {self.__nomTablaInventarioPeliculas}"
        operacion += f" SET num_catalogo = '{peliculaED.pelicula.numCatalogo}'"
        operacion += f", existencia = {peliculaED.existencia}"
        operacion += f", disponibilidad = {peliculaED.disponibilidad};"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaInventarioPeliculas} de la base de datos {self._database}') from e

    def actualiza(self, peliculaED: PeliculaED):
        """Actualiza la películaED del parámetro del inventario de películas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede actualizar la películaED del inventario de películas.

        -----------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        peliculaED: PeliculaED
            peliculaED a actualizar en la base de datos
        
        Throws
        ------
        PersistenciaException
            Si no se puede actualizar la películaED del inventario de películas
        """
        operacion = f"UPDATE {self.__nomTablaInventarioPeliculas}"
        operacion += f" SET existencia = '{peliculaED.existencia}'"
        operacion += f", disponibilidad = '{peliculaED.disponibilidad}'"
        operacion += f" WHERE num_catalogo = '{peliculaED.pelicula.numCatalogo}';"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaInventarioPeliculas} de la base de datos {self._database}') from e

    def elimina(self, peliculaED: PeliculaED):
        """Elimina la películaED del parámetro del inventario de películas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede eliminar la películaED del inventario de películas.

        ---------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        peliculaED: PeliculaED
            peliculaED a eliminar de la base de datos
        
        Throws
        ------
        PersistenciaException
            Si no se puede eliminar la películaED del inventario de películas
        """
        operacion = f"DELETE FROM {self.__nomTablaInventarioPeliculas}"
        operacion += f" WHERE num_catalogo = '{peliculaED.pelicula.numCatalogo}';"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaInventarioPeliculas} de la base de datos {self._database}') from e

    def lista(self):
        """Regresa la lista de todas las películasED.

        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películasED del inventario de películas.

        ------------------------------------------------------------------------------------------------------------------------------
        Returns
        -------
        list
            Lista de todas las películasED

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películasED del inventario de películas
        """
        inventario = []

        operacion = f"SELECT p.num_catalogo, p.titulo, p.genero, p.clasificacion, p.actor1, p.actor2, p.productora, ip.existencia, ip.disponibilidad"
        operacion += f" FROM {self.__nomTablaInventarioPeliculas} as ip INNER JOIN {self.__nomTablaPeliculas} as p"
        operacion += f" ON ip.num_catalogo = p.num_catalogo"

        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaInventarioPeliculas} de la base de datos {self._database}') from e

        for numCatalogo, titulo, genero, clasificacion, actor1, actor2, productora, existencia, disponibilidad in renglones:
            pelicula = Pelicula(numCatalogo, titulo, genero,
                                clasificacion, actor1, actor2, productora)
            peliculaED = PeliculaED(pelicula, existencia, disponibilidad)

            inventario.append(peliculaED)

        return inventario
