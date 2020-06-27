# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:44:21 2020

@author: Edwin
"""



def ultimo(num):
    return [x for x in str(num)][-1]
    
def p1(lista):
    if len(lista) == 1:
        return ultimo(lista[0])
    return ultimo(lista[0]) + p1(lista[1:])

def p2(lista):
    return [[int(y)*3 for y in str(x)] for x in lista] 

def p3(lista):
    return [(int(max(str(y))),int(min(str(y))),int(max(str(y))) +int( min(str(y)))) for y in lista] 

class Nodo():
    def __init__(self,valor,izquierda=None,derecha=None):
        self.valor=valor
        self.izquierda=izquierda
        self.derecha=derecha

def en_orden(arbol):
    if arbol ==None:
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)

def p4(lista):
    return [[int(y)  for y in str(x)] for x in lista]
print(p1([123,456,789]))
print(p2([123,456]))
print(p3([1234,5678]))
arbol= Nodo(25,Nodo(15,None,Nodo(20)),Nodo(50))
print(p4(en_orden(arbol)))
