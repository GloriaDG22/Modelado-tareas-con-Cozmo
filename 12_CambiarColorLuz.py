import time

import pycozmo

#¿cambiar a poner color de error (rojo) color de acierto (verde)?????? 
'''
0. Green
1. Red
2. Blue
3. White
4. Off
'''

n_luz = 2

def cambiarColorLuz(n_luz):
    with pycozmo.connect() as cli:

        lights = [
            pycozmo.lights.red_light,
            pycozmo.lights.green_light,
            pycozmo.lights.blue_light,
            pycozmo.lights.white_light,
            pycozmo.lights.off_light,
        ]
        
        cli.set_all_backpack_lights(lights[n_luz])
        time.sleep(2)


cambiarColorLuz(n_luz)
