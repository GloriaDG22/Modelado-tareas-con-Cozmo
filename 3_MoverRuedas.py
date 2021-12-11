import pycozmo
import time

'''
1. Rápido
2. Medio
3. Lento
4. Marcha atrás
'''

n_velocidad = 1
tiempo = 2.0      # En segundo
girar = True

def moverRuedas(n_velocidad, tiempo, girar):
    with pycozmo.connect() as cli:

        # Establecer velocidad
        if n_velocidad == 1:
            velocidad = 100.00
            
        elif n_velocidad == 2:
            velocidad = 50.00

        elif n_velocidad == 3:
            velocidad = 30.00

        elif n_velocidad == 4:
            velocidad = -50.00

        #Establecer si ambas ruedas van en la misma dirección o no
        if girar:
            Rvelocidad = 0 - velocidad
        else:
            Rvelocidad = velocidad
        
        cli.wait_for_robot()
        #time.sleep(15)    
        #cli.drive_wheels(lwheel_speed=100.0, rwheel_speed=100.0, duration=5.0)

        print("velocidad " + str(velocidad))
        print("Rvelocidad " + str(Rvelocidad))
        print("tiempo " + str(tiempo))
        cli.drive_wheels(lwheel_speed=velocidad, rwheel_speed=Rvelocidad, duration=tiempo)

#moverRuedas(n_velocidad, tiempo, girar)

moverRuedas(1, 2, False)
time.sleep(3)  
moverRuedas(2, 3, True)
time.sleep(3)  
moverRuedas(4, 2, False)
