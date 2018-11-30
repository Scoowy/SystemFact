#!/usr/bin/python
# -*- coding: utf-8 -*-
# Scoowy - Juan Gahona

import sqlite3

from config import DBNAME


def runQuery(query, parameters=()):
    with sqlite3.connect(DBNAME) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result


def validar(value):
    return value != ''


def parseToFloat(value: str):
    if validar(value):
        try:
            value = float(value)
        except ValueError:
            if value.find(','):
                entero, dec = value.split(',')
                value = float('{}.{}'.format(entero, dec))
            else:
                value = ''
    return value
