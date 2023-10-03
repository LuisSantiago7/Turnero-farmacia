'''Modulo para generadores de turno y decoradores de impresion de turno'''

'''Generador de turno de perfumeria'''
def generator_perfumeria():
    #Empieza con el turno 1
    turn_perf = 1
    #Produce el turno
    yield turn_perf
    #bucle para hacer que sean turnos indeterminados, se generara un turno por cada llamada
    while True:
        turn_perf += 1
        yield turn_perf
turno_perfumeria = generator_perfumeria()

'''Generador de turno de perfumeria'''
def generator_farmacia():
    #Empieza con el turno 1
    turn_farm = 1
    #Produce el turno
    yield turn_farm
    #bucle para hacer que sean turnos indeterminados, se generara un turno por cada llamada
    while True:
        turn_farm += 1
        yield turn_farm
turno_farmacia = generator_farmacia()

'''Generador de turno de cosmeticos'''
def generator_cosmeticos():
    #Empieza con el turno 1
    turn_cosm = 1
    #Produce el turno
    yield turn_cosm
    #bucle para hacer que sean turnos indeterminados, se generara un turno por cada llamada
    while True:
        turn_cosm += 1
        yield turn_cosm
turno_cosmeticos = generator_cosmeticos()

#DECORADOR
#funcion que recibe como argumento la funcion que se va a decorar
def text_turno(funcion):
    #funcion que recibe como argumento el mismo argumento la funcion que se va a decorar
    def text_new_function(turno):
        #decoraciones
        print('Su turno es: ')
        funcion(turno)
        print('''Aguarde y será atendido''')
    #retorna la funcion que decora una funcion
    return text_new_function

#Decorando funcion
@text_turno
def text_perfumeria(turn_perf):
    print(f'    P-{next(turn_perf)}')

#Decorando funcion
@text_turno
def text_farmacia(turn_frma):
    print(f'    F-{next(turn_frma)}')

#Decorando funcion
@text_turno
def text_cosmeticos(turn_cosmet):
    print(f'    C-{next(turn_cosmet)}')





