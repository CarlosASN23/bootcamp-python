from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, n1, n2):
    resultado = n1 + n2
    return HttpResponse('<h1>A soma de {} + {} = {}</h1>'.format(n1, n2, resultado))


def sub(request, n1, n2):

    subtracao = n1 - n2
    return HttpResponse('<h1>A subtração de {} - {} = {}</h1>'.format(n1, n2, subtracao))

def mult(request, n1, n2):

    multiplicacao = n1 * n2
    return HttpResponse('<h1>A multiplicação de {} x {} = {}</h1>'.format(n1, n2, multiplicacao))

def divi(request, n1, n2):

    if n2 > 0:
        divisao = n1 / n2
        return HttpResponse('<h1>O resultado da divisão entre {} e {} = {}</h1>'.format(n1, n2, divisao))
    else:
        return HttpResponse('Error... \nNão existe divisão por zero')