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
destino = 4
n_veces = 3

def moverBrazos (origen, destino, n_veces):    
    with pycozmo.connect() as cli:
        trayecto = [origen, destino]
        
        
        cli.wait_for_robot() # se puede sustituir por la siguiente linea??????????
        #Necesita esperar unos segundos para realizar los primeros movimientos
        #time.sleep(5) 
        for i in range(n_veces):

            for mov in trayecto:
                if mov == 1:
                    cli.set_lift_height(pycozmo.MAX_LIFT_HEIGHT.mm) #92mm
                    time.sleep(1)
                elif mov == 2:
                    cli.set_lift_height(75.00) #75mm
                    time.sleep(1)
                elif mov == 3:
                    cli.set_lift_height(pycozmo.MIN_LIFT_HEIGHT.mm*2) #64mm
                    time.sleep(1)
                elif mov == 4:
                    cli.set_lift_height(pycozmo.LIFT_PIVOT_HEIGHT.mm) #45mm
                    time.sleep(1)
                elif mov == 5:
                    cli.set_lift_height(pycozmo.MIN_LIFT_HEIGHT.mm) #32mm
                    time.sleep(1)

moverBrazos(origen, destino, n_veces)