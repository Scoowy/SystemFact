#!/usr/bin/python
# -*- coding: utf-8 -*-
# Scoowy - Juan Gahona

from tkinter import END

from vista import Vista
from modelo import Producto
from funciones import *


class Controlador(object):
    """Implementacion del Controlador de la App"""

    def __init__(self, raiz):
        """Constructor de la clase"""
        # Crear la Vista y el Modelo dentro del Controlador (Composición)
        # Pasar una referencia del Controlador a la Vista
        self.vista = Vista(raiz, self)
        # self.producto = Producto()

    def getProducts(self, tree):
        records = tree.get_children()
        for record in records:
            tree.delete(record)
        query = "SELECT * FROM producto ORDER BY id DESC"
        rows = runQuery(query)
        for row in rows:
            tree.insert('', 0, text=row[0], values=row[1:])

    def addProducts(self, name, description, price, stock, message):
        valueName = name.get()
        valueDescription = description.get()
        valuePrice = parseToFloat(price.get())
        valueStock = stock.get()

        if validar(valueName) and validar(valuePrice):
            query = 'INSERT INTO producto VALUES(NULL, ?, ?, ?, ?)'
            parametros = (valueName, valueDescription, valuePrice, valueStock)
            runQuery(query, parametros)
            name.delete(0, END)
            description.delete(0, END)
            price.delete(0, END)
            stock.delete(0, END)
            message['text'] = 'Nuevo producto añadido - {}'.format(valueName)
            print('Nuevo producto creado')
        else:
            message['text'] = 'Faltan parametros!!!'

    def editProduct(self, id, name, description, price, stock):
        pass
