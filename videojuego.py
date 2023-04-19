# videojuego.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Este es el módulo de la clase Videojuego

import articulo


class Videojuego(articulo.Articulo):
    """Clase que representa un Videojuego en un tienda de renta de películas y videojuegos
    """

    def __init__(self, numCatalogo=None, titulo=None, genero=None, clasificacion=None, consola=None, fabricante=None, version=None):
        """Constructor de la clase que inicializa todos sus atributos

        -------------------------------------------------------------
        Parameters
        ----------
        numCatalogo: str
            Número de catálogo del videojuego
        titulo: str
            Título del videojuego
        genero: str
            Género del videojuego
        clasificacion: str
            Clasificación del videojuego
        consola: str
            Consola del videojuego
        fabricante: str
            Fabricante del videojuego
        version: str
            Versión del videojuego
        """
        super().__init__(numCatalogo, titulo, genero, clasificacion)
        self.__consola = consola
        self.__fabricante = fabricante
        self.__version = version

    @property
    def consola(self):
        """Regresa la consola del videojuego

        @returns Consola del videojuego
        """
        return self.__consola

    @consola.setter
    def consola(self, consola: str):
        """Establece un nuevo valor para la consola del videojuego
        
        @param consola Consola del videojuego
        """
        self.__consola = consola

    @property
    def fabricante(self):
        """Regresa el fabricante del videojuego

        @returns Fabricante del videojuego
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante: str):
        """Establece un nuevo valor para el fabricante del videojuego
        
        @param fabricante Fabricante del videojuego
        """
        self.__fabricante = fabricante

    @property
    def version(self):
        """Regresa la versión del videojuego

        @returns Versión del videojuego
        """
        return self.__version

    @version.setter
    def version(self, version: str):
        """Establece un nuevo valor para la versión del videojuego
        
        @param version Versión del videojuego
        """
        self.__version = version

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return (f'Videojuego({super().__str__()}, {self.__consola}, {self.__fabricante}, {self.__version})')

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return (f'Videojuego({super().__repr__()}, {self.__consola}, {self.__fabricante}, {self.__version})')


if (__name__ == '__main__'):
    videojuego1 = Videojuego('V00001', 'Superman Returns',
                             'Acción', 'T-Teen', 'XBox 360', 'Electronic Arts', '01.01')
    videojuego2 = Videojuego('V00002', 'Tomb Raider',
                             'Acción', 'T-Teen', 'PS2', 'Eidos', '02.11')
    videojuego3 = Videojuego('V00003', 'Super Smash Bros. Brawl',
                             'Acción', 'T-Teen', 'Nintendo Wii', 'Nintendo', '01.05')

    print(videojuego1)
    print(videojuego2)
    print(videojuego3)

    print(f'\nFabricante de videojuego2: {videojuego2.fabricante}\n')

    print(
        f'¿Son videojuego1 y videojuego1 diferentes? {videojuego1.__ne__(videojuego1)}')
