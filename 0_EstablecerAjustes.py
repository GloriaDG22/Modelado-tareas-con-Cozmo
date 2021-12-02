
import pyttsx3
import pycozmo

rate = 150
voice = ""

def establecerAjustes(rate, voice):
    with pycozmo.connect(enable_procedural_face=False) as cli:

    audio.setProperty('rate', rate)
    
    audio.setProperty('voice', voice)


establecerAjustes(rate, voice)