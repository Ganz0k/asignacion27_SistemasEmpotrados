# videojuegoED.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Este es el módulo de la clase VideojuegoED

import videojuego as vi


class VideojuegoED:
    def __init__(self, videojuego: vi.Videojuego, existencia: int, disponibilidad: int):
        self.__videojuego = videojuego
        self.__existencia = existencia
        self.__disponibilidad = disponibilidad

    @property
    def videojuego(self):
        """Regresa el videojuego

        @returns Videojuego
        """
        return self.__videojuego

    @videojuego.setter
    def videojuego(self, videojuego: vi.Videojuego):
        """Establece un nuevo valor para el videojuego
        
        @param videojuego Videojuego
        """
        self.__videojuego = videojuego

    @property
    def existencia(self):
        """Regresa la cantidad del videojuego en existencia en la tienda

        @returns Cantidad del videojuego en existencia en la tienda
        """
        return self.__existencia

    @existencia.setter
    def existencia(self, existencia: int):
        """Establece un nuevo valor para la existencia del videojuego
        
        @param existencia Existencia del videojuego
        """
        self.__existencia = existencia

    @property
    def disponibilidad(self):
        """Regresa la cantidad del videojuego en disponibilidad en la tienda

        @returns Cantidad del videojuego en disponibilidad en la tienda
        """
        return self.__disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, disponibilidad: int):
        """Establece un nuevo valor para la disponibilidad del videojuego
        
        @param disponibilidad Disponibilidad del videojuego
        """
        self.__disponibilidad = disponibilidad

    def __eq__(self, videojuegoED):
        """Compara por igualdad la instancia de esta clase con la instancia de VideojuegoED del parámetro.

        Se considera que dos instancias de VideojuegoED son iguales si sus videojuegos son iguales.

        --------------------------------------------------------------------------------------------------
        Parameters
        ----------
        videojuegoED: VideojuegoED
            Instancia de la clase VideojuegoED a comparar con ésta.
        
        Returns
        -------
        bool
            True en caso de que ambos sean iguales, False en caso contrario
        """
        return self.__videojuego == videojuegoED.videojuego

    def __ne__(self, videojuegoED):
        """Compara por desigualdad la instancia de esta clase con la instancia de VideojuegoED del parámetro.

        Se considera que dos instancias de VideojuegoED son diferentes si sus videojuegos no son iguales.

        -----------------------------------------------------------------------------------------------------
        Parameters
        ----------
        videojuegoED: VideojuegoED
            Instancia de la clase VideojuegoED a comparar con ésta.
        
        Returns
        -------
        bool
            True en caso de que ambos sean diferentes, False en caso contrario
        """
        return self.__videojuego != videojuegoED.videojuego

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return f'{self.__videojuego}, {self.__existencia}, {self.__disponibilidad}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return f'{self.__class__.__module__}, {self.__class__.__name__}, {self.__videojuego}, {self.__existencia}, {self.__disponibilidad}'


if (__name__ == '__main__'):
    videojuego1 = vi.Videojuego('V00001', 'Superman Returns',
                                'Acción', 'T-Teen', 'XBox 360', 'Electronic Arts', '01.01')
    videojuego2 = vi.Videojuego('V00002', 'Tomb Raider',
                                'Acción', 'T-Teen', 'PS2', 'Eidos', '02.11')
    videojuego3 = vi.Videojuego('V00003', 'Super Smash Bros. Brawl',
                                'Acción', 'T-Teen', 'Nintendo Wii', 'Nintendo', '01.05')

    videojuegoED1 = VideojuegoED(videojuego1, 5, 3)
    videojuegoED2 = VideojuegoED(videojuego2, 7, 4)
    videojuegoED3 = VideojuegoED(videojuego3, 8, 5)

    print(videojuegoED1)
    print(videojuegoED2)
    print(videojuegoED3)

    print(f'\nVideojuego de videojuegoED2: {videojuegoED2.videojuego}')

    print(
        f'\nExistencia del videojuego de videojuegoED3: {videojuegoED3.existencia}')

    print(
        f'\nDisponibilidad del videojuego de videojuegoED1: {videojuegoED1.disponibilidad}')

    print(
        f'\n¿Son videojuegoED2 y videojuegoED3 diferentes? {videojuegoED2.__ne__(videojuegoED3)}')
