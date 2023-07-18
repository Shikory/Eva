# pip install pyaudio  ==> para instalar pyaudio
# Autor : Marco Jhoel Churata Torres.
# Titulo:Grabacion_de_audio_con_Python

import whisper  # reconocimiento automatico de voz
import pyaudio  # grabacion y reproducción de audio
import wave  # manejo de archivos de audio.wav
# Codigo para escuchar y repetir instrucciones pero solo con internet
# import speech_recognition as sr
# biblioteca de conversión de texto a voz en Python. A diferencia de las bibliotecas alternativas, funciona sin conexión y es compatible con Python 2 y 3.
import pyttsx3


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# editando configuración por defecto de lavoz que repetira las instrucciones
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.8)

duracion = 10
archivo = "ejemplo2.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=2,
                    rate=44100, input=True, frames_per_buffer=1024)

# codigo para que hable la computadora


def talk(Oido):
    engine.say(Oido)
    engine.runAndWait()


print("Grabando ...")
frames = []

for i in range(0, int(44100/1024*duracion)):
    data = stream.read(1024)
    frames.append(data)

print("Grabacion a terminado ")

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(archivo, 'wb')
waveFile.setnchannels(2)
waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
waveFile.setframerate(44100)
waveFile.writeframes(b''.join(frames))
waveFile.close()

model = whisper.load_model('small')
Oido = model.transcribe("ejemplo2.wav", language='Spanish', fp16=False)
print(Oido["text"])
talk(Oido)
