#!/usr/bin/python
# -*- coding: utf-8 -*-
# Scoowy - Juan Gahona

# Crea una clase Aplicacion para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué
# construye y muestra la ventana con todos sus widgets:


from tkinter import *
from tkinter.ttk import *
from config import *


class Vista():
    """Implementacion de la Vista de la App"""

    def __init__(self, raiz, controlador):
        """Constructor de la clase"""
        # Obtener la referencia del controlador
        self.controlador = controlador

        # Contruccion de la GUI
        # Barra de menu
        barraMenu = Menu(raiz)
        raiz['menu'] = barraMenu

        # Submenus
        self.menuFile = Menu(barraMenu)
        self.menuOptions = Menu(barraMenu)
        self.menuView = Menu(barraMenu)
        self.menuHelp = Menu(barraMenu)
        self.menuOptions.add_command(
            label='CRUD Stock', command=self.windCrud)
        self.menuView.add_command(
            label='Nueva ventana', command=self.windNewWind)

        barraMenu.add_cascade(menu=self.menuFile, label='Archivo')
        barraMenu.add_cascade(menu=self.menuOptions, label='Opciones')
        barraMenu.add_cascade(menu=self.menuView, label='Ver')
        barraMenu.add_cascade(menu=self.menuHelp, label='Ayuda')

        # Elementos de la ventana
        frame = LabelFrame(raiz, text='Stock')
        frame.grid(row=0, column=0, columnspan=3, pady=10)

        # Lista General
        self.productosStock = Treeview(raiz, height=25, columns=('name'))
        self.productosStock.grid(row=0, column=0)
        self.productosStock.heading('#0', text='ID', anchor=CENTER)
        self.productosStock.heading('name', text='Nombre', anchor=CENTER)
        self.productosStock.column('#0', width=50, stretch=True)
        self.controlador.getProducts(self.productosStock)
        self.btnReloadStock = Button(raiz, text='Actualizar', command=self.reload)
        self.btnReloadStock.grid(row=26, column=0, columnspan=2, sticky=W+E)

        # Cuadro reporte
        self.reportBox = Entry(raiz, state='readonly')
        self.reportBox.grid(row=0, column=3, rowspan=25, columnspan=15, sticky=W+E+N+S)
        self.btnGenerateReport = Button(raiz, text='Reporte', command=self.generateReport)
        self.btnGenerateReport.grid(row=26, column=3, columnspan=4, sticky=W+E)

    def windCrud(self):
        self.crud = Ventana('CRUD - Stock')
        self.crud.resizable(width=False, height=False)

        # Nuevo producto
        self.frameNP = LabelFrame(self.crud, text='Nuevo producto')
        self.frameNP.grid(row=0, column=0, columnspan=4, pady=10, padx=5)
        # Entrada Nombre
        Label(self.frameNP, text='Nombre: ').grid(row=1, column=0)
        self.entryNpName = Entry(self.frameNP)
        self.entryNpName.grid(row=1, column=1)
        # Entrada Descripcion
        Label(self.frameNP, text='Descripcion: ').grid(row=2, column=0)
        self.entryNpDescription = Entry(self.frameNP)
        self.entryNpDescription.grid(row=2, column=1)
        # Entrada Precio
        Label(self.frameNP, text='Precio: ').grid(row=1, column=2)
        self.entryNpPrice = Entry(self.frameNP)
        self.entryNpPrice.grid(row=1, column=3)
        # Entrada Stock
        Label(self.frameNP, text='Stock: ').grid(row=2, column=2)
        self.entryNpStock = Entry(self.frameNP)
        self.entryNpStock.grid(row=2, column=3)
        # Boton Crear
        self.btnNpNuevo = Button(self.frameNP, text='Crear', command=self.addProduct)
        self.btnNpNuevo.grid(row=3, column=0, columnspan=4, sticky=W+E)

        # Editar producto
        self.frameEP = LabelFrame(self.crud, text='Editar producto')
        self.frameEP.grid(row=0, column=4, columnspan=4, pady=10, padx=5)
        # Entrada Nombre
        Label(self.frameEP, text='Nombre: ').grid(row=1, column=4)
        self.entryEpName = Entry(self.frameEP)
        self.entryEpName.grid(row=1, column=5)
        # Entrada Descripcion
        Label(self.frameEP, text='Descripcion: ').grid(row=2, column=4)
        self.entryEpDescription = Entry(self.frameEP)
        self.entryEpDescription.grid(row=2, column=5)
        # Entrada Precio
        Label(self.frameEP, text='Precio: ').grid(row=1, column=6)
        self.entryEpPrice = Entry(self.frameEP)
        self.entryEpPrice.grid(row=1, column=7)
        # Entrada Stock
        Label(self.frameEP, text='Stock: ').grid(row=2, column=6)
        self.entryEpStock = Entry(self.frameEP)
        self.entryEpStock.grid(row=2, column=7)
        # Boton Editar
        self.btnEPEditar = Button(self.frameEP, text='Editar')
        self.btnEPEditar.grid(row=3, column=4, columnspan=4, sticky=W+E)

        # Eliminar producto
        self.frameDP = LabelFrame(self.crud, text='Eliminar producto')
        self.frameDP.grid(row=0, column=8, columnspan=4, pady=10, padx=5)
        # Entrada ID
        Label(self.frameDP, text='ID: ').grid(row=1, column=8)
        self.entryDpName = Entry(self.frameDP)
        self.entryDpName.grid(row=1, column=9)
        # Boton Eliminar
        self.btnDPEliminar = Button(self.frameDP, text='Eliminar')
        self.btnDPEliminar.grid(row=2, column=8, columnspan=4, sticky=W+E)

        # Label de Aviso
        self.labelMessage = Label(self.crud, text='')
        self.labelMessage.grid(row=4, column=1, columnspan=10, sticky=W+E)

        # Vista Stock
        self.frameVS = LabelFrame(self.crud, text='Stock')
        self.frameVS.grid(row=5, column=0, columnspan=12)
        self.tree = Treeview(self.frameVS, height=10, columns=(
            'name', 'description', 'price', 'stock', 'caduco'))
        self.tree.grid(row=6, column=0, columnspan=12)
        self.tree.heading('#0', text='ID', anchor=CENTER)
        self.tree.column('#0', width=50, minwidth=50)
        self.tree.heading('name', text='Nombre', anchor=CENTER)
        self.tree.heading('description', text='Descripcion', anchor=CENTER)
        self.tree.column('description', width=450, minwidth=450)
        self.tree.heading('price', text='Precio', anchor=CENTER)
        self.tree.column('price', width=80, minwidth=80)
        self.tree.heading('stock', text='Stock', anchor=CENTER)
        self.tree.column('stock', width=80, minwidth=80)
        self.tree.heading('caduco', text='Caduco', anchor=CENTER)
        self.tree.column('caduco', width=80, minwidth=80)

        self.controlador.getProducts(self.tree)

    def addProduct(self):
        self.controlador.addProducts(self.entryNpName, self.entryNpDescription, self.entryNpPrice, self.entryNpStock, self.labelMessage)
        self.controlador.getProducts(self.tree)
        self.controlador.getProducts(self.productosStock)

    def reload(self):
        self.controlador.getProducts(self.productosStock)

    def generateReport(self):
        pass

    def windNewWind(self):
        nuevaVentana = Ventana('Soy una ventana', 600, 300)


class Ventana(Toplevel):
    def __init__(self, titulo: str, ancho=0, alto=0, resizable=False):
        Toplevel.__init__(self)
        self.title(titulo)
        self.resizable(width=resizable, height=resizable)
        self.setGeometry(ancho, alto)
        self.estilos = Style()

    def setGeometry(self, ancho, alto):
        if ancho != 0 and alto != 0:
            self.geometry('{}x{}'.format(ancho, alto))
