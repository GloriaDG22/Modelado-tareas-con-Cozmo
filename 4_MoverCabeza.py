import pyttsx3
import pycozmo
import time

'''
1. Arriba
2. Medio Alto
3. Medio
4. Medio Bajo
5. Bajo
'''

origen = 1
destino = 2
n_veces = 4

def moverBrazos (origen, destino, n_veces):    
    with pycozmo.connect() as cli:

        cli.set_head_angle(pycozmo.MAX_HEAD_ANGLE.radians)
        time.sleep(1)
        cli.set_head_angle(pycozmo.MIN_HEAD_ANGLE.radians)
        time.sleep(1)
       

moverBrazos(origen, destino, n_veces)