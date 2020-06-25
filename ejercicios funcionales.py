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
print(p1([123,456,789]))
print(p2([123,456]))
print(p3([1234,5678]))
