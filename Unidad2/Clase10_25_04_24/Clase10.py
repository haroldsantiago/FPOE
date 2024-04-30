import threading
import datetime
import time 
import logging
from hilo4 import Hilo4
from hilo5 import Hilo5
from hilo6 import Hilo6

logging.basicConfig(level=logging.DEBUG)

tiempo_inicial = datetime.datetime.now()


def consultar(nombre):
    logging.debug('Consultando: '+ nombre)
    time.sleep(5)
    return

def numeros():
    list = [1,2,3,4,5]
    for element in list:
        logging.debug(element)
        time.sleep(1)
    return

def letras():
    list = ['a','b','c','d','e']
    for element in list:
        logging.debug(element)
        time.sleep(2)
    return



hilo_1 = threading.Thread(name='hilo_1',target=numeros)
hilo_2 = threading.Thread(name='hilo_2',target=letras)
hilo_3 = threading.Thread(name='hilo_3',target=consultar,args=('Sergio', ) )
hilo_4 = Hilo4('hilo_4','Sergio')
hilo_5 = Hilo5('hilo_5')
hilo_6 = Hilo6('hilo_6')



#Iniciar hilos
#hilo_1.start()
#hilo_1.join()
#hilo_2.start()
#hilo_2.join()
#hilo_3.start()
#hilo_3.join()
#hilo_4.start()
hilo_5.start()
hilo_6.start()




tiempo_final = datetime.datetime.now()

logging.debug('Tiempo transcurrido ' + str(tiempo_final.second -tiempo_inicial.second) + '\n')
