# juego de fantasmas
from random import randint
print('Juego de fantasmas')
te_sientes_valiente=True
puntuacion=0;

while te_sientes_valiente:
    puerta_fantasma=randint(1,3)
    #print(puerta_fantasma)
    print('Tres puertas ante ti....')
    print('Un fantasma detrás de una.')
    print('¿Qué puerta abres?')
    puerta= input('1,2 o 3?')
    #print(puerta)
    num_puerta= int(puerta)
    #print(num_puerta)
    if num_puerta == puerta_fantasma:
        print('FANTASMA')
        te_sientes_valiente=False
    else:
            print('¡No hay fantasma!')
            print('Entras en la habitación siguiente.')
            puntuacion=puntuacion +1
print('¡Huye!')
print('Game over! Tu puntuación es', puntuacion)
    
          
          
