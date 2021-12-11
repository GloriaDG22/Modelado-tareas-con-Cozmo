import pycozmo
import time

'''
1. Arriba
2. Medio
3. Bajo
'''

origen = 1
destino = 2
n_veces = 3

def moverCabeza (origen, destino, n_veces):    
    with pycozmo.connect() as cli:
        trayecto = [origen, destino]
        
        for i in range(n_veces):

            for mov in trayecto:
                if mov == 1:
                    cli.set_head_angle(pycozmo.MAX_HEAD_ANGLE.radians) #44,5º
                    time.sleep(1)
                elif mov == 2:
                    cli.set_head_angle(pycozmo.MAX_HEAD_ANGLE.radians/2) #22º
                    time.sleep(1)
                elif mov == 3:
                    cli.set_head_angle(pycozmo.MIN_HEAD_ANGLE.radians) #-25º
                    time.sleep(1)

moverCabeza(origen, destino, n_veces)

time.sleep(2)
moverCabeza(1, 3, 3)