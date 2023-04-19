# peliculaED.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Este es el módulo de la clase PeliculaED

import pelicula as pe


class PeliculaED:
    """Clase que representa la cantidad de una Película en existencia y disponibilidad en la tienda
    """

    def __init__(self, pelicula: pe.Pelicula, existencia: int, disponibilidad: int):
        """Constructor de la clase que inicializa todos sus atributos

        -------------------------------------------------------------
        Parameters
        ----------
        pelicula: Pelicula
            Pelicula de la tienda
        existencia: int
            Existencia de la película en la tienda
        disponibilidad: int
            Disponibilidad de la película en la tienda
        """
        self.__pelicula = pelicula
        self.__existencia = existencia
        self.__disponibilidad = disponibilidad

    @property
    def pelicula(self):
        """Regresa la película

        @returns Película
        """
        return self.__pelicula

    @pelicula.setter
    def pelicula(self, pelicula: pe.Pelicula):
        """Establece un nuevo valor para la película
        
        @param pelicula Película
        """
        self.__pelicula = pelicula

    @property
    def existencia(self):
        """Regresa la cantidad de la película en existencia en la tienda

        @returns Cantidad de la película en existencia en la tienda
        """
        return self.__existencia

    @existencia.setter
    def existencia(self, existencia: int):
        """Establece un nuevo valor para la existencia de la película
        
        @param existencia Existencia de la película
        """
        self.__existencia = existencia

    @property
    def disponibilidad(self):
        """Regresa la cantidad de la película en disponibilidad en la tienda

        @returns Cantidad de la película en disponibilidad en la tienda
        """
        return self.__disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, disponibilidad: int):
        """Establece un nuevo valor para la disponibilidad de la película
        
        @param disponibilidad Disponibilidad de la película
        """
        self.__disponibilidad = disponibilidad

    def __eq__(self, peliculaED):
        """Compara por igualdad la instancia de esta clase con la instancia de PeliculaED del parámetro.

        Se considera que dos instancias de PeliculaED son iguales si sus películas son iguales.

        ------------------------------------------------------------------------------------------------
        Parameters
        ----------
        peliculaED: PeliculaED
            Instancia de la clase PeliculaED a comparar con ésta.
        
        Returns
        -------
        bool
            True en caso de que ambos sean iguales, False en caso contrario
        """
        return self.__pelicula == peliculaED.pelicula

    def __ne__(self, peliculaED):
        """Compara por desigualdad la instancia de esta clase con la instancia de PeliculaED del parámetro.

        Se considera que dos instancias de PeliculaED son diferentes si sus películas no son iguales.

        ---------------------------------------------------------------------------------------------------
        Parameters
        ----------
        peliculaED: PeliculaED
            Instancia de la clase PeliculaED a comparar con ésta.
        
        Returns
        -------
        bool
            True en caso de que ambos sean diferentes, False en caso contrario
        """
        return self.__pelicula != peliculaED.pelicula

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return f'{self.__pelicula}, {self.__existencia}, {self.__disponibilidad}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return f'{self.__class__.__module__}, {self.__class__.__name__}, {self.__pelicula}, {self.__existencia}, {self.__disponibilidad}'


if (__name__ == '__main__'):
    pelicula1 = pe.Pelicula('P00001', 'Orgullo y prejuicio',
                            'Drama', 'A', 'Colin Firth', 'Anna Chancellor', 'BBC')
    pelicula2 = pe.Pelicula('P00002', 'El diablo se viste a la moda', 'Comedia',
                            'B15', 'Anne Hathaway', 'Meryl Streep', '20 Century Fox')
    pelicula3 = pe.Pelicula('P00003', 'El ilusionista', 'Misterio',
                            'A', 'Rufus Sewell', 'Edward Norton', 'Quality Films')

    peliculaED1 = PeliculaED(pelicula1, 10, 8)
    peliculaED2 = PeliculaED(pelicula2, 10, 6)
    peliculaED3 = PeliculaED(pelicula3, 15, 5)

    print(peliculaED1)
    print(peliculaED2)
    print(peliculaED3)

    print(f'\nPelícula de peliculaED2: {peliculaED2.pelicula}')

    print(
        f'\nExistencia de la película de peliculaED3: {peliculaED3.existencia}')

    print(
        f'\nDisponibilidad de la película de peliculaED1: {peliculaED1.disponibilidad}')

    print(
        f'\n¿Son peliculaED2 y peliculaED3 iguales? {peliculaED2.__eq__(peliculaED3)}')
