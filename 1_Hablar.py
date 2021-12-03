
import os
import time

import pyttsx3
import pycozmo

text = "Hola, Glowinn. Soy Cozmo y vengo a jugar contigo."

def talk(text):
    with pycozmo.connect() as cli:

            #Put face
        # Raise head.
        angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
        cli.set_head_angle(angle)

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
        
        cli.wait_for(pycozmo.event.EvtAudioCompleted)
        
talk(text)