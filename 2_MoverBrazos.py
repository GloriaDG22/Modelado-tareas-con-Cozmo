import pyttsx3
import pycozmo

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
    with pycozmo.connect(enable_procedural_face=False) as cli:
        
        cli.set_lift_height(pycozmo.robot.MAX_LIFT_HEIGHT)
        
        #pycozmo.robot.LiftPosition(origen)
        cli.move_lift(100)

moverBrazos(origen, destino, n_veces)