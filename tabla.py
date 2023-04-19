# tabla.py
# 17/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase Tabla

import mysql.connector
import mysql.connector.errorcode


class Tabla:
    """Esta clase implementa las operaciones de consultar y actualizar una tabla de una
    base de datos
    """

    def __init__(self, user: str, password: str, host: str, database: str):
        """Constructor de la clase que inicializa todos los atributos

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
        """
        self._user = user
        self._password = password
        self._host = host
        self._database = database

    def obten(self, operacion: str):
        """Busca un renglón de una tabla de la base de datos usando la consulta del parámetro
        operacion y con los parámetros dados por el parámetro parámetros.

        Regresa una tupla con el resultado de la consulta.

        -------------------------------------------------------------------------------------
        Parameters
        ----------
        operacion: str
            Cadena con la operación
        
        Returns
        -------
        tuple
            Tupla con el resultado de la consulta
        """
        conexion = mysql.connector.connect(
            user=self._user, password=self._password, host=self._host, database=self._database)

        try:
            cursor = conexion.cursor()
            cursor.execute(operacion)
            resultado = cursor.fetchone()
            return resultado
        finally:
            if (conexion.is_connected()):
                cursor.close()
                conexion.close()

    def consulta(self, operacion: str):
        """Consulta una tabla de la base de datos usando la consulta del parámetro operación
        y con los parámetros dados por el parámetro parámetros.

        Regresa una lista de tuplas con los resultados de la consulta.

        ------------------------------------------------------------------------------------
        Parameters
        ----------
        operacion: str
            Cadena con la operación
        
        Returns
        -------
        list
            Lista con los resultados de la consulta
        """
        conexion = mysql.connector.connect(
            user=self._user, password=self._password, host=self._host, database=self._database)

        try:
            cursor = conexion.cursor()
            cursor.execute(operacion)
            resultados = cursor.fetchall()
            return resultados
        finally:
            if (conexion.is_connected()):
                cursor.close()
                conexion.close()

    def actualiza(self, operacion):
        """Actualiza la base de datos usando la consulta del parámetro operación y con
        los parámetros dados por el parámetro parámetros.

        Permite insertar, actualizar o eliminar un renglón de una tabla de la base de datos.

        ------------------------------------------------------------------------------------
        Parameters
        ----------
        operacion: str
            Cadena con la operación
        """
        conexion = mysql.connector.connect(
            user=self._user, password=self._password, host=self._host, database=self._database)

        try:
            cursor = conexion.cursor()
            cursor.execute(operacion)
            conexion.commit()
        except mysql.connector.IntegrityError:
            conexion.rollback()
            raise
        finally:
            if (conexion.is_connected()):
                cursor.close()
                conexion.close()
