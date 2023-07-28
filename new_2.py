import datetime
import pyaudio
import wave
import whisper  # reconocimiento automatico de voz

nombre_archivo = 'Texto_captura.txt'

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

fechaActual = datetime.datetime.now()
fechaStrActual = datetime.datetime.strftime(fechaActual, '%d/%m/%Y %H:%M:%S')
print("Grabando a las " + fechaStrActual)

seconds = 9
frames = []
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate

print("Grabacion a terminada ")

obj = wave.open("output.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close
print("Archivo output.wav generado.")

inicio = datetime.datetime.now()

print("Analizando audio output.wav")
model = whisper.load_model('small')
Texto = model.transcribe("output.wav", language='Spanish', fp16=False)

final = datetime.datetime.now()

Tiempo = final - inicio

print(f'Transcipción finalizada en {Tiempo.seconds} segundos')
print(Texto["text"])

with open(nombre_archivo, '+a') as archivo:
    archivo.write(fechaStrActual + Texto["text"]+"\n")
print("Archivo Texto_captura.txt generado.")
