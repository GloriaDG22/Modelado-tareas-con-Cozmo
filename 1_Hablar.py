
# Mirar hacia arriba 
# Pasar texto por parámetro
import os
import time

from PIL import Image
import numpy as np
import pyttsx3
import pycozmo

import librosa

text = "Hola, Glowinn. Soy Cozmo y vengo a jugar contigo."

def talk(text):
    with pycozmo.connect() as cli:

            #Put face
        # Raise head.
        angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
        cli.set_head_angle(angle)

        # Render a 128x64 procedural face with default parameters.
        f = pycozmo.procedural_face.ProceduralFace()
        im = f.render()

        # The Cozmo protocol expects a 128x32 image, so take only the even lines.
        np_im = np.array(im)
        np_im2 = np_im[::2]
        im2 = Image.fromarray(np_im2)

            # Initialize the Pyttsx3 engine
        audio = pyttsx3.init()
            #Set Rate. Defaults to 200 word per minute.
        audio.setProperty('rate', 150) 
            # We can use file extension as mp3 and wav, both will work
        audio.save_to_file(text, 'audio.wav')
            # Wait until above command is not finished.
        audio.runAndWait()

        # Set volume to maximum.
        #cli.set_volume(65535)

        # A 22 kHz, 16-bit, mono file is required.
        cli.play_audio("audio.wav")
        
        
        duration = librosa.get_duration(filename='audio.wav')
        print("La duración es: " + str(duration))
        #cli.display_image(im2)
        cli.wait_for(pycozmo.event.EvtAudioCompleted)
        
talk(text)