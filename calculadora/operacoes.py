# operacoes.py

import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero!"

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    return math.sqrt(a)

def logaritmo(a):
    return math.log(a)
