#!/usr/bin/python
# -*- coding: utf-8 -*-
# Scoowy - Juan Gahona

import os
from tkinter import *
from tkinter import ttk

# Info general
VERSION = '0.0.1'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dimensiones de la ventana principal
ANCHO = 800
ALTO = 600
TITULO = 'SYSTEMFACT - v{}'.format(VERSION)

# Configuracion de la DB
DBNAME = os.path.join(BASE_DIR, 'dbSystemFact.db')
