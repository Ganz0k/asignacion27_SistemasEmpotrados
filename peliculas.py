# peliculas.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase Peliculas

import mysql.connector
from pelicula import Pelicula
from persistenciaException import PersistenciaException
from tabla import Tabla


class Peliculas(Tabla):
    """Esta clase permite agregar, modificar, eliminar y listar películas al catálogo de películas.

    El catálogo de películas se almacena en la tabla peliculas de la base de datos videocentro.
    """

    def __init__(self, user: str, password: str, host: str, database: str, nomTablaPeliculas: str):
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
        nomTablaPeliculas: str
            Nombre de la tabla en la base de datos para el catálogo de películas
        """
        super().__init__(user, password, host, database)
        self.__nomTablaPeliculas = nomTablaPeliculas

    def obten(self, pelicula: Pelicula):
        """Busca en el catálogo de películas (la tabla peliculas) la película cuyo número de catálogo está en el parámetro pelicula.

        Regresa la película si la encuentra, None en caso contrario.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la película del catálogo de películas.

        ----------------------------------------------------------------------------------------------------------------------------
        
        Parameters
        ----------
        pelicula: Pelicula
            Película a buscar en el catálogo de películas
        
        Returns
        -------
        Pelicula
            La película si la encuentra
        None
            None en caso contrario

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la película del catálogo de películas
        """
        operacion = f"SELECT * FROM {self.__nomTablaPeliculas}"
        operacion += f" WHERE num_catalogo = '{pelicula.numCatalogo}';"

        try:
            renglon = super().obten(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

        if (renglon is not None):
            pelicula = Pelicula(*renglon)
            return pelicula

        return None

    def agrega(self, pelicula: Pelicula):
        """Agrega la película del parámetro al catálogo de películas.
        
        Lanza una excepción del tipo PersistenciaException si la película ya existe o 
        no se puede agregar la película al catálogo de películas.

        -----------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Película a agregar al catálogo de películas
        
        Throws
        ------
        PersistenciaException
            Si la película ya existe o no se puede agregar la película al catálogo de películas
        """
        operacion = f"INSERT {self.__nomTablaPeliculas}"
        operacion += f" SET num_catalogo = '{pelicula.numCatalogo}'"
        operacion += f", titulo = '{pelicula.titulo}'"
        operacion += f", genero = '{pelicula.genero}'"
        operacion += f", clasificacion = '{pelicula.clasificacion}'"
        operacion += f", actor1 = '{pelicula.actor1}'"
        operacion += f", actor2 = '{pelicula.actor2}'"
        operacion += f", productora = '{pelicula.productora}';"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

    def actualiza(self, pelicula: Pelicula):
        """Actualiza la película del parámetro del catálogo de películas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede actualizar la película del catálogo de películas.

        -------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Película a actualizar al catálogo de películas
        
        Throws
        ------
        PersistenciaException
            Si no se puede actualizar la película del catálogo de películas
        """
        operacion = f"UPDATE {self.__nomTablaPeliculas}"
        operacion += f" SET num_catalogo = '{pelicula.numCatalogo}'"
        operacion += f", titulo = '{pelicula.titulo}'"
        operacion += f", genero = '{pelicula.genero}'"
        operacion += f", clasificacion = '{pelicula.clasificacion}'"
        operacion += f", actor1 = '{pelicula.actor1}'"
        operacion += f", actor2 = '{pelicula.actor2}'"
        operacion += f", productora = '{pelicula.productora}'"
        operacion += f" WHERE num_catalogo = '{pelicula.numCatalogo}';"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

    def elimina(self, pelicula: Pelicula):
        """Elimina la película del parámetro del catálogo de películas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede eliminar la película del catálogo de películas.

        -----------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Pelicula a eliminar del catálogo de películas

        Throws
        ------
        PersistenciaException
            Si no se puede eliminar la película del catálogo de películas
        """
        operacion = f"DELETE FROM {self.__nomTablaPeliculas}"
        operacion += f" WHERE num_catalogo = '{pelicula.numCatalogo}';"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

    def lista(self):
        """Regresa la lista de todas las películas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Returns
        -------
        list
            lista de todas las películas
        
        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        listaPeliculas = []

        operacion = f"SELECT * FROM {self.__nomTablaPeliculas};"

        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

        for renglon in renglones:
            pelicula = Pelicula(*renglon)
            listaPeliculas.append(pelicula)

        return listaPeliculas

    def listaGenero(self, genero: str):
        """Regresa la lista de todas las películas del género del parámetro.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        genero: str
            Género de las películas a listar del catálogo de películas
        
        Returns
        -------
        list
            Lista de todas las películas del género del parámetro

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        listaPeliculas = []

        operacion = f"SELECT * FROM {self.__nomTablaPeliculas}"
        operacion += f" WHERE genero = '{genero}';"

        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

        for renglon in renglones:
            pelicula = Pelicula(*renglon)
            listaPeliculas.append(pelicula)

        return listaPeliculas

    def listaActor(self, actor: str):
        """Regresa la lista de todas las películas del actor del parámetro.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        actor: str
            Actor por el cual listar el catálogo de películas
        
        Returns
        -------
        list
            Lista de todas las películas del actor del parámetro

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        listaPeliculas = []

        operacion = f"SELECT * FROM {self.__nomTablaPeliculas}"
        operacion += f" WHERE actor1 = '{actor}' OR actor2 = '{actor}';"

        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

        for renglon in renglones:
            pelicula = Pelicula(*renglon)
            listaPeliculas.append(pelicula)

        return listaPeliculas

    def listaProductora(self, productora: str):
        """Regresa la lista de todas las películas de la productora del parámetro.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        prodcutora: str
            Prodcutora de películas por la cual listar el catálogo de películas
        
        Returns
        -------
        list
            Lista de todas las películas de la productora del parámetro

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        listaPeliculas = []

        operacion = f"SELECT * FROM {self.__nomTablaPeliculas}"
        operacion += f" WHERE productora = '{productora}';"

        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error en la tabla {self.__nomTablaPeliculas} de la base de datos {self._database}') from e

        for renglon in renglones:
            pelicula = Pelicula(*renglon)
            listaPeliculas.append(pelicula)

        return listaPeliculas
