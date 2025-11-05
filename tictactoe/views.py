from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from controller.tablaJuego import TablaJuego
from controller.numeroAleatorio import numeroRandom
from django.views.decorators.csrf import csrf_exempt
import json
tablajuego = TablaJuego()

class Partida(View):
    
    #Obtiene y genera la tabla 3 x 3
    def get(self, request):
        rango = range(3)

        return render(request, 'juego.html',{
            'tablero': tablajuego.obtener_tablero(), 
            'rango':rango
        })

    def post(self, request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                posicion = int(data.get('posicion'))
                print(posicion)
            except Exception as e:
                return JsonResponse({'error': f'Datos inválidos: {e}'}, status=400)

            #Movimiento del usuario (X)
            exito = tablajuego.movimiento(numero=posicion, simbolo='X')
            if not exito:
                return JsonResponse({'error': 'Posición ocupada'}, status=409)

            #Verifica si hay ganador 
            ganador = tablajuego.verificar_ganador()
            if ganador:
                return JsonResponse({
                    'jugador': {'posicion': posicion, 'simbolo': 'X'},
                    'ganador': ganador,
                    'tablero': tablajuego.obtener_tablero()
                })

            #Movimiento de la máquina (O)
            libres = tablajuego.posiciones_libres()
            numerorandom = numeroRandom()
            pos_maquina = numerorandom.verificarNumero(libres)
            print(pos_maquina)

            if pos_maquina:
                tablajuego.movimiento(numero=pos_maquina, simbolo='O')
            #Respuesta JSON para actualizar el tablero
            return JsonResponse({
                'jugador': {'posicion': posicion, 'simbolo': 'X'},
                'maquina': {'posicion': pos_maquina, 'simbolo': 'O'} if pos_maquina else None,
                'ganador': ganador,
                'tablero': tablajuego.obtener_tablero()
            })
        

#Reinicia el juego si hay ganador o empate
def reiniciar(request):
    if request.method == 'POST':
        global tablajuego
        tablajuego = TablaJuego()
        return JsonResponse({'tablero':tablajuego.obtener_tablero()})
    return JsonResponse({'error':'Metodo no permitido'}, status =405)