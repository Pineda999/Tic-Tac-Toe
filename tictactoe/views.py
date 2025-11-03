from django.shortcuts import render
from controller.tablaJuego import TablaJuego
from controller.numeroAleatorio import numeroRandom

def juego(request):
    tablajuego = TablaJuego()
    tablero = tablajuego.mostrarTablero

    numerorandom= numeroRandom()
    random = numerorandom.verificarNumero

    return render(request, 'juego.html', {'tablero': tablero, 'random':random})