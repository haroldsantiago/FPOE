import threading
import datetime
import logging
import time
from hilo4 import Hilo4
from hilo5 import Hilo5
from hilo6 import Hilo6

logging.basicConfig(level=logging.DEBUG)

tiempoinicial1 = datetime.datetime.now()
def consultar(nombre):
    logging.debug('consultando: ' + nombre )
    time.sleep(0)
    return

def letras():
    list = ['a','b','c','d','e']
    for elemento in list:
        logging.debug(elemento)
        time.sleep(2)
    return

def numeros():
    list = [1,2,3,4,5]
    for elemento in list:
        logging.debug(elemento)
        time.sleep(1)
    return

hilo_1 = threading.Thread(name='hilo_1', target=consultar,  args=('Raul', ))
hilo_2 = threading.Thread(name='hilo_2', target=numeros)
hilo_3 = threading.Thread(name='hilo_3', target=letras)
hilo_4 = Hilo4('hilo_4', 'Juan')
hilo_5 = Hilo5('hilo_5')

nombre_archivo = "nombres.txt"
hilo_6 = Hilo6(nombre_archivo)


#hilo_1.start()
#hilo_1.join()

#hilo_2.start()
#hilo_2.join()

#hilo_3.start()
#hilo_3.join()

#hilo_4.start()
#hilo_4.join()

hilo_5.start()
#hilo_5.join()

hilo_6.start()
#hilo_6.join()


tiempofinal1 = datetime.datetime.now()

logging.debug('tiempo trancurrido: ' + str(tiempofinal1.second - tiempoinicial1.second) + '\n')
