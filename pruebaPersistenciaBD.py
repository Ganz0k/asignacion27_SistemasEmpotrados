# pruebaPersistenciaBD.py
# 18/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo de pruebas para PersistenciaBD

from pelicula import Pelicula
from peliculaED import PeliculaED
from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException

persistencia = PersistenciaBD()

pelicula1 = Pelicula('P00001', 'Orgullo y prejuicio', 'Drama', 'A', 'Colin Firth', 'Anna Chancellor', 'BBC')
pelicula2 = Pelicula('P00002', 'El diablo viste a la moda', 'Comedia', 'B15', 'Anne Hathaway', 'Meryl Streep', '20 Century Fox')
pelicula3 = Pelicula('P00003', 'El ilusionista', 'Misterio', 'A', 'Rufus Sewell', 'Edward Norton', 'Quality Films')
pelicula4 = Pelicula('P00004', 'Star Treck', 'Ciencia Ficción', 'A', 'Chris Pine', 'Zachary Quinto', 'Paramount Pictures')

try:
    persistencia.agregaPelicula(pelicula1)
    print(f'Se agregó la película {pelicula1}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.agregaPelicula(pelicula2)
    print(f'Se agregó la película {pelicula2}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.agregaPelicula(pelicula3)
    print(f'Se agregó la película {pelicula3}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.agregaPelicula(pelicula4)
    print(f'Se agregó la película {pelicula4}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.agregaPelicula(pelicula2)
    print(f'\nSe agregó la película {pelicula2}\n')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()
    peliculas = persistencia.consultaPeliculas()

    for pelicula in peliculas:
        print(pelicula)
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    pelicula = persistencia.obtenPelicula(pelicula3)
    print(f'\nSe obtuvo la película {pelicula}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    pelicula1.genero = 'Romance'
    persistencia.actualizaPelicula(pelicula1)
    print(f'\nSe actualizó la película {pelicula1}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    pelicula7 = Pelicula('P00007', '', 'Comedia', '', '', '', '')
    persistencia.actualizaPelicula(pelicula7)
    print(f'\nSe actualizó la película {pelicula7}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.eliminaPelicula(pelicula2)
    print('\nPelícula eliminada')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    pelicula9 = Pelicula('P00009', '', '', '', '', '', '')
    persistencia.eliminaPelicula(pelicula9)
    print('\nPelícula eliminada')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()
    peliculas = persistencia.consultaPeliculas()

    for pelicula in peliculas:
        print(pelicula)
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()

    peliculasMisterio = persistencia.consultaPeliculasGenero('Misterio')

    for pelicula in peliculasMisterio:
        print(pelicula)
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()

    peliculasChrisPine = persistencia.consultaPeliculasActor('Chris Pine')

    for pelicula in peliculasChrisPine:
        print(pelicula)
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()

    peliculasBBC = persistencia.consultaPeliculasProductora('BBC')

    for pelicula in peliculasBBC:
        print(pelicula)
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.inventariarPelicula(pelicula1, 3)
    print(f'\nSe inventariaron 3 unidades de la película {pelicula1}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.inventariarPelicula(pelicula3, 10)
    print(f'\nSe inventariaron 10 unidades de la película {pelicula3}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.inventariarPelicula(pelicula4, 5)
    print(f'\nSe inventariaron 5 unidades de la película {pelicula4}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()

    inventario = persistencia.consultarInventarioPeliculas()

    for item in inventario:
        print(item)
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.inventariarPelicula(pelicula3, 2)
    print(f'\nSe inventariaron 2 unidades de la película {pelicula3}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    pelicula6 = Pelicula('P00006', '', '', '', '', '', '')
    persistencia.inventariarPelicula(pelicula6, 4)
    print(f'\nSe inventariaron 4 unidades de la película {pelicula6}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    persistencia.desinventariarPelicula(pelicula4, 2)
    print(f'\nSe desinventariaron 2 unidades de la pelicula {pelicula4}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()

    inventario = persistencia.consultarInventarioPeliculas()

    for item in inventario:
        print(item)
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)

try:
    print()

    inventario = persistencia.consultarInventarioPeliculas()

    for item in inventario:
        if (item.pelicula.numCatalogo == 'P00003'):
            print(f'Existencia de la película 3 = {item.existencia}')
        
        if (item.pelicula.numCatalogo == 'P00004'):
            print(f'Disponibilidad de la película 4 = {item.disponibilidad}')
except PersistenciaException as pe:
    print()
    print(pe.msj)
    print(pe.cause)