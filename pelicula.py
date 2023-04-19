# pelicula.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Este es el módulo de la clase Pelicula

import articulo


class Pelicula(articulo.Articulo):
    """Clase que representa una Película en un tienda de renta de películas y videojuegos
    """

    def __init__(self, numCatalogo=None, titulo=None, genero=None, clasificacion=None, actor1=None, actor2=None, productora=None):
        """Constructor de la clase que inicializa todos sus atributos

        -------------------------------------------------------------
        Parameters
        ----------
        numCatalogo: str
            Número de catálogo de la película
        titulo: str
            Título de la película
        genero: str
            Género de la película
        clasificacion: str
            Clasificación de la película
        actor1: str
            1° Actor de la película
        actor2: str
            2° Actor de la película
        productora: str
            Productora de la película
        """
        super().__init__(numCatalogo, titulo, genero, clasificacion)
        self.__actor1 = actor1
        self.__actor2 = actor2
        self.__productora = productora

    @property
    def actor1(self):
        """Regresa el 1° actor de la película

        @returns 1° actor de la pleícula
        """
        return self.__actor1

    @actor1.setter
    def actor1(self, actor1: str):
        """Establece un nuevo valor para el 1° de la película
        
        @param actor1 1° actor para la película
        """
        self.__actor1 = actor1

    @property
    def actor2(self):
        """Regresa el 2° actor de la película

        @returns 2° actor de la pleícula
        """
        return self.__actor2

    @actor2.setter
    def actor2(self, actor2: str):
        """Establece un nuevo valor para el 2° de la película
        
        @param actor2 2° actor para la película
        """
        self.__actor2 = actor2

    @property
    def productora(self):
        """Regresa la prodcutora de la película

        @returns Productora de la pleícula
        """
        return self.__productora

    @productora.setter
    def productora(self, productora: str):
        """Establece un nuevo valor para la productora de la película
        
        @param productora Productora para la película
        """
        self.__productora = productora

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return (f'Pelicula({super().__str__()}, {self.__actor1}, {self.__actor2}, {self.__productora})')

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return (f'Pelicula({super().__repr__()}, {self.__actor1}, {self.__actor2}, {self.__productora})')


if (__name__ == '__main__'):
    pelicula1 = Pelicula('P00001', 'Orgullo y prejuicio',
                         'Drama', 'A', 'Colin Firth', 'Anna Chancellor', 'BBC')
    pelicula2 = Pelicula('P00002', 'El diablo se viste a la moda', 'Comedia',
                         'B15', 'Anne Hathaway', 'Meryl Streep', '20 Century Fox')
    pelicula3 = Pelicula('P00003', 'El ilusionista', 'Misterio',
                         'A', 'Rufus Sewell', 'Edward Norton', 'Quality Films')

    print(pelicula1)
    print(pelicula2)
    print(pelicula3)

    print(f'\nProductora de pelicula1: {pelicula1.productora}\n')

    tituloCorrectoPelicula3 = pelicula2.titulo
    tituloCorrectoPelicula2 = pelicula3.titulo
    pelicula2.titulo = tituloCorrectoPelicula2
    pelicula3.titulo = tituloCorrectoPelicula3

    print(pelicula2)
    print(pelicula3)

    print(f'\n¿Son la película 2 y 3 iguales? {pelicula2.__eq__(pelicula3)}')
