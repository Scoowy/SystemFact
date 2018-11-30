#!/usr/bin/python
# -*- coding: utf-8 -*-
# Scoowy - Juan Gahona


import abc


class Producto(metaclass=abc.ABCMeta):
    """Clase Producto"""

    def __init__(self, code, name, description, price, amount, stock):
        self.code = code
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
        self.stock = stock

    @abc.abstractmethod
    def __str__(self):
        pass


class ProductoCaduco(Producto):
    """Clase ProductoCaduco hereda de Producto"""

    def __init__(self, code, name, description, price, amount, stock, expiration):
        super().__init__(code, name, description, price, amount, stock)
        self.expiration = expiration

    def __str__(self):
        return '| {:6} | {:.20} | {:.40} | {:>4.2f} | {:2d} | Expira el: {}'.format(self.cod, self.name, self.description, self.price, self.amount, self.expiration)


class ProductoNoCaduco(Producto):
    """Clase ProductoNoCaduco hereda de Producto"""

    def __init__(self, code, name, description, price, amount, stock):
        super().__init__(code, name, description, price, amount, stock)

    def __str__(self):
        return '| {:6} | {:.20} | {:.40} | {:>4.2f} | {:2d} |'.format(self.cod, self.name, self.description, self.price, self.amount)


class Factura:
    """Clase Factura"""

    def __init__(self, productList=[]):
        self.productList = productList
        self.subTotal = 0
        self.iva = 12
        self.total = 0
        self.ivaValue = 0

    def calcSubTotal(self):
        for product in self.productList:
            self.subTotal += product.price * product.amount

    def calcIva(self):
        self.ivaValue = self.subTotal * (self.iva/100)

    def calcTotal(self):
        self.total = self.subTotal + self.ivaValue

    def addProcucto(self, product):
        self.productList.append(product)

    def delProducto(self, code):
        index = 0
        for product in self.productList:
            if product.code == code:
                self.productList.pop(index)
                break
            index += 1


class Stock:
    def __init__(self):
        self.stock = {}
        self.numProducts = 0

    def addProduco(self):
        pass

    def delProducto(self):
        pass

    def refreshStock(self):
        pass


class Persona(metaclass=abc.ABCMeta):
    """Clase Abstracta Persona"""

    def __init__(self, id, name, lastName, telephone, mail, address):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.telephone = telephone
        self.mail = mail
        self.address = address

    def getFullName(self):
        return '{} {}'.format(self.name, self.lastName)

    @abc.abstractmethod
    def __str__(self):
        pass


class Cliente(Persona):
    """Clase Cliente hereda de Persona"""

    def __init__(self, id, name, lastName, telephone, mail, address, typeClient):
        super(Cliente, self).__init__(
            id, name, lastName, telephone, mail, address)
        self.typeClient = typeClient

    def __str__(self):
        title = '=== Cliente ==='
        return '{:^45}\n Nombre: {:20} CI: {:0>10}\n Tel: {:0>10} Mail: {:21}\n Direccion: {:32}'.format(title, self.getFullName, self.id, self.telephone, self.mail, self.address)


class Usuario(Persona):
    """Clase Usuario hereda de Persona"""

    def __init__(self, id, name, lastName, telephone, mail, address, typeUser, position):
        super(Usuario, self).__init__(
            id, name, lastName, telephone, mail, address)
        self.typeUser = typeUser
        self.position = position
