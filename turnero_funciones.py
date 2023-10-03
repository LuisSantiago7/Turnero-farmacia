'''#Este modulo tendra el funcionamiento principal del software, es decir su estructura y logica'''
import generadoresydecoradores
from os import system

'''Funcion de bienvenida'''
def welcome():
    '''imprime binevenida'''
    system('cls')
    print('''               FARMACIA MX
Bienvenido, ¿A que area te diriges?''')

#Funcion para elegir el area
def choice_area():
    '''loop por si el usuario ingresa una opcion invalida'''
    while True:
        #Intentara obtener una respuesta del usuario
        try:
            area = int(input('''
    Perfumeria  [1]
    Farmacia    [2]
    Cosmeticos  [3]
'''))
            #Retornara y almacenara la respuesta del usuario
            return area
        #respuesta user diferente a int, captura error y regresando al loop para elegir respuesta
        except ValueError:
            system('cls')
            print('No es una opcion, intenta de nuevo')

#funciom para otro turno
def tanks():
    '''funcion para retornar al menu inicial para preguntar el area'''
    input('''Gracias por su preferencia, que disfrute su visita.
          (Press Enter to continue)''')
#loop que lleva el control del programa
while True:
    welcome()
    area = choice_area()
    if area == 1:
        #si el suario elige 1, llamara al generador de turno perfumeria
        system('cls')
        generadoresydecoradores.texto_perfumeria = generadoresydecoradores.text_turno(generadoresydecoradores.text_perfumeria(generadoresydecoradores.turno_perfumeria))
    elif area == 2:
        #si el suario elige 2, llamara al generador de turno farmacia
        system('cls')
        generadoresydecoradores.texto_farmacia = generadoresydecoradores.text_turno(generadoresydecoradores.text_farmacia(generadoresydecoradores.turno_farmacia))
    elif area == 3:
        #si el suario elige 3, llamara al generador de turno cosmeticos
        system('cls')
        generadoresydecoradores.texto_cosmeticos = generadoresydecoradores.text_turno(generadoresydecoradores.text_cosmeticos(generadoresydecoradores.turno_cosmeticos))
    tanks()
