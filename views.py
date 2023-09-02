from django.shortcuts import render

# Create your views here.

def sumar(request, num1, num2):
    resul = num1 + num2
    return render(request, 'calculadora/operaciones.html',{'num1':num1, 'num2':num2, 'resul':resul, 'nombre': 'suma', 'operacion':'+'})

def restar(request, num1, num2):
    resul = num1 - num2
    return render(request, 'calculadora/operaciones.html',{'num1':num1, 'num2':num2, 'resul':resul, 'nombre': 'resta', 'operacion':'-'})

def multiplicar(request, num1, num2):
    resul = num1 * num2
    return render(request, 'calculadora/operaciones.html',{'num1':num1, 'num2':num2, 'resul':resul, 'nombre':'nultplicacion', 'operacion':'*'})
