import os
import time

from PIL import Image
import pycozmo

imagen = "Glowinn_logo.png"

def mostrarImagen (imagen):
    with pycozmo.connect(enable_procedural_face=False) as cli:

        # Raise head.
        angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
        cli.set_head_angle(angle)
        time.sleep(1)

        # Load image
        im = Image.open(os.path.join(os.path.dirname(__file__), "Recursos", imagen))
       
        # Resize from 320x240 to 68x17. Larger image sometime are too big for the robot receive buffer.
        im = im.resize((128, 32)) # Convert to binary image.

        im = im.convert('1')

        cli.display_image(im, 7.0)


mostrarImagen(imagen)