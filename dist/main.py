#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# name:        main.py (Python 3.x).
# description: Sin definir
# purpose:     Sin definir
# author:      Scoowy - Juan Gahona
#
# ------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *

from controlador import Controlador
from config import *

'''SystemFact: Sin definir '''

__author__ = 'Scoowy - Juan Gahona'
__title__ = TITULO
__date__ = '19/11/2018'
__version__ = VERSION
__license__ = 'GNU GPLv3'

# SYSTEMFACT: Sin definir


def main():
    # Definir ventana de la aplicacion
    raiz = Tk()

    # Propiedades de la ventana App
    # raiz.geometry('{}x{}'.format(ANCHO, ALTO))
    # raiz.minsize(ANCHO, ALTO)
    raiz.title(TITULO)
    # raiz.attributes('-fullscreen', True)

    # Configuracion de Estilos
    estilos = Style()

    controlador = Controlador(raiz)

    # Ciclo Principal
    raiz.mainloop()


if __name__ == '__main__':
    main()
