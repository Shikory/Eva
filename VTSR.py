#Codigo para escuchar y repetir instrucciones pero solo con internet
import speech_recognition as sr
import pyttsx3

name = 'chico'

# the flag help us to turn off the program
flag = 1

listener = sr.Recognizer()
engine =pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

# editing default configuration
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.8)

# Para ver que voces estan instaladas en mi lap.
"""
for voice in voices:
    print(voice)
"""

def talk(text):
    engine.say(text)
    engine.runAndWait()

#Para que funcione correctamente de sebe de hablar claro y pausadamente
def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name,'')
                flag = run(rec)
                
            else:
                talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag

def run(rec):
    
    if 'reproduce' in rec:
       #print('Reproduciendo')
       music = rec.replace('reproduce','')
       # talk('Reproduciendo' + music)
       talk(rec)
       print(rec)

while flag:
    flag = listen()