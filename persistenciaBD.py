# persistenciaBD.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase PersistenciaBD

from inventarioPeliculas import InventarioPeliculas
from pelicula import Pelicula
from peliculaED import PeliculaED
from peliculas import Peliculas
from persistenciaException import PersistenciaException


class PersistenciaBD:
    """Clase que implementa todos las funciones para operaciones con BDs
    """

    def __init__(self):
        """Constructor que inicializa todos los atributos de la clase
        """
        self.__user = 'root'
        self.__password = 'Luisgon10$'
        self.__host = 'localhost'
        self.__database = 'videocentro'

        self.__catalogoPeliculas = Peliculas(
            self.__user, self.__password, self.__host, self.__database, 'peliculas')
        self.__inventarioPeliculas = InventarioPeliculas(
            self.__user, self.__password, self.__host, self.__database, 'inventario_peliculas', 'peliculas')

    def obtenPelicula(self, pelicula: Pelicula):
        """Busca en el catálogo de películas la película cuyo número de catálogo está en el parámetro pelicula.
        
        Regresa la película si la encuentra, None en caso contrario.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la película del catálogo de películas.

        ----------------------------------------------------------------------------------------------------------------
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
        return self.__catalogoPeliculas.obten(pelicula)

    def agregaPelicula(self, pelicula: Pelicula):
        """Agrega la película del parámetro al catálogo de películas.
        
        Lanza una excepción del tipo PersistenciaException si la película ya existe o no se puede agregar la película al catálogo de películas.

        ---------------------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Película a agregar en el catálogo de películas
        
        Throws
        ------
        PersistenciaException
            Si la película ya existe o no se puede agregar la película al catálogo de películas
        """
        self.__catalogoPeliculas.agrega(pelicula)

    def actualizaPelicula(self, pelicula: Pelicula):
        """Actualiza la película del parámetro del catálogo de películas.
        
        Lanza una excepción del tipo PersistenciaException si la película no existe o no se puede actualizar la película del catálogo de películas.

        -------------------------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Película a actualizar en el catálogo de películas
        
        Throws
        ------
        PersistenciaException
            Si la película no existe o no se puede actualizar la película del catálogo de películas
        """
        peliculaBuscada = self.__catalogoPeliculas.obten(pelicula)

        if (peliculaBuscada is None):
            raise PersistenciaException(
                f'Error: La película de número de catálogo {pelicula.numCatalogo} no existe')

        self.__catalogoPeliculas.actualiza(pelicula)

    def eliminaPelicula(self, pelicula: Pelicula):
        """Elimina la película del parámetro del catálogo de películas.
        
        Lanza una excepción del tipo PersistenciaException si la película no existe o no se puede eliminar la película del catálogo de películas.
        
        -----------------------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Película a eliminar en el catálogo de películas

        Throws
        ------
        PersistenciaException
            Si la película no existe o no se puede eliminar la película del catálogo de películas
        """
        peliculaBuscada = self.__catalogoPeliculas.obten(pelicula)

        if (peliculaBuscada is None):
            raise PersistenciaException(
                f'Error: La película de número de catálogo {pelicula.numCatalogo} no existe')

        self.__catalogoPeliculas.elimina(pelicula)

    def consultaPeliculas(self):
        """Regresa la lista de todas las películas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Returns
        -------
        list
            Lista de todas las películas
        
        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        return self.__catalogoPeliculas.lista()

    def consultaPeliculasGenero(self, genero: str):
        """Regresa la lista de todas las películas del género del parámetro.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        genero: str
            Género por el cual filtrar las películas
        
        Returns
        -------
        list
            Lista de todas las películas del género del parámetro

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        return self.__catalogoPeliculas.listaGenero(genero)

    def consultaPeliculasActor(self, actor: str):
        """Regresa la lista de todas las películas del actor del parámetro.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        actor: str
            Actor por el cual filtrar las películas
        
        Returns
        -------
        list
            Lista de todas las películas del actor del parámetro
        
        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        return self.__catalogoPeliculas.listaActor(actor)

    def consultaPeliculasProductora(self, productora: str):
        """Regresa la lista de todas las películas de la productora del parámetro.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del catálogo de películas.

        --------------------------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        productora: str
            Productora por la cual filtrar las películas
        
        Returns
        -------
        list
            Lista de todas las películas de la productora del parámetro

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del catálogo de películas
        """
        return self.__catalogoPeliculas.listaProductora(productora)

    def inventariarPelicula(self, pelicula: Pelicula, cantidad: int):
        """Inventaría una película en el inventario de películas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede inventariar la película.

        ------------------------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Película a inventariar
        cantidad: int
            Cantidad por la cual inventariar

        Throws
        ------
        PersitenciaException
            Si no se puede inventariar la película
        """
        peliculaED = PeliculaED(pelicula, cantidad, cantidad)
        peliculaInventario = self.__inventarioPeliculas.obten(peliculaED)

        if (peliculaInventario is not None):
            peliculaInventario.disponibilidad = peliculaInventario.disponibilidad + cantidad
            peliculaInventario.existencia = peliculaInventario.existencia + cantidad

            self.__inventarioPeliculas.actualiza(peliculaInventario)
        else:
            self.__inventarioPeliculas.agrega(peliculaED)

    def desinventariarPelicula(self, pelicula: Pelicula, cantidad: int):
        """Desinventaría una película en el inventario de películas, se actualiza la película restándole a los
        atributos existencia y disponibilidad el valor del parámetro cantidad.

        Lanza una excepción del tipo PersistenciaException si no se puede desinventariar la película.

        -------------------------------------------------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Película a desinventariar
        cantidad: int
            Cantidad por la cual desinventariar
        
        Throws
        ------
        PersistenciaException
            Si no se puede desinventariar la película
        """
        peliculaED = PeliculaED(pelicula, cantidad, cantidad)
        peliculaInventario = self.__inventarioPeliculas.obten(peliculaED)

        if (peliculaInventario is not None):
            peliculaInventario.disponibilidad = peliculaInventario.disponibilidad - cantidad
            peliculaInventario.existencia = peliculaInventario.existencia - cantidad

            self.__inventarioPeliculas.actualiza(peliculaInventario)

    def consultarInventarioPeliculas(self):
        """Regresa la lista de todas las películas en el inventario de peliculas.
        
        Lanza una excepción del tipo PersistenciaException si no se puede obtener la lista de películas del inventario de películas.

        ----------------------------------------------------------------------------------------------------------------------------
        Returns
        -------
        list
            Lista de todas las películas en el inventario de peliculas

        Throws
        ------
        PersistenciaException
            Si no se puede obtener la lista de películas del inventario de películas
        """
        return self.__inventarioPeliculas.lista()
