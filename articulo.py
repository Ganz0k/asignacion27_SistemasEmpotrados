# articulo.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Este es el módulo de la clase Articulo

class Articulo:
    """Clase que representa un Artículo en un tienda de renta de películas y videojuegos
    """

    def __init__(self, numCatalogo=None, titulo=None, genero=None, clasificacion=None):
        """Constructor de la clase que inicializa todos sus atributos

        -------------------------------------------------------------
        Parameters
        ----------
        numCatalogo: str
            Número de catálogo del artículo
        titulo: str
            Título del artículo
        genero: str
            Género del artículo
        clasificacion: str
            Clasificación del artículo
        """
        self._numCatalogo = numCatalogo
        self._titulo = titulo
        self._genero = genero
        self._clasificacion = clasificacion

    @property
    def numCatalogo(self):
        """Regresa el número de catálogo del artículo

        @returns Número de catálogo del artículo
        """
        return self._numCatalogo

    @property
    def titulo(self):
        """Regresa el título del artículo

        @returns Título del artículo
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        """Establece un nuevo valor para el título del artículo
        
        @param titulo Título para el artículo
        """
        self._titulo = titulo

    @property
    def genero(self):
        """Regresa el género del artículo

        @returns Género del artículo
        """
        return self._genero

    @genero.setter
    def genero(self, genero: str):
        """Establece un nuevo valor para el género del artículo
        
        @param genero Género para el artículo
        """
        self._genero = genero

    @property
    def clasificacion(self):
        """Regresa la clasificación del artículo

        @returns Clasificación del artículo
        """
        return self._clasificacion

    @clasificacion.setter
    def clasificacion(self, clasificacion: str):
        """Establece un nuevo valor para la clasificación del artículo
        
        @param clasificacion Clasificación para el artículo
        """
        self._clasificacion = clasificacion

    def __eq__(self, articulo):
        """Compara por igualdad la instancia de esta clase con la del artículo del parámetro.

        Se considera que dos artículos son iguales si sus números de catálogo son iguales.

        -------------------------------------------------------------------------------------
        Parameters
        ----------
        articulo: Articulo
            Artículo a comparar con la instancia de esta clase
        
        Returns
        -------
        bool
            True en caso de que ambos sean iguales, False en caso contrario
        """
        return self._numCatalogo == articulo.numCatalogo

    def __ne__(self, articulo):
        """Compara por desigualdad la instancia de esta clase con la del artículo del parámetro.

        Se considera que dos artículos son diferentes si sus números de catálogo son diferentes.

        -------------------------------------------------------------------------------------
        Parameters
        ----------
        articulo: Articulo
            Artículo a comparar con la instancia de esta clase
        
        Returns
        -------
        bool
            True en caso de que ambos sean diferentes, False en caso contrario
        """
        return self._numCatalogo != articulo.numCatalogo

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return f'{self._numCatalogo}, {self._titulo}, {self._genero}, {self._clasificacion}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return f'{self.__class__.__module__}, {self.__class__.__name__}, {self._numCatalogo}, {self._titulo}, {self._genero}, {self._clasificacion}'
