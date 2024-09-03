import threading  # para usar varios hilos al mismo tiempo
import sys        # para salir del programa
import datetime   # usar hora y fecha
import pyaudio    # grabación de audio
import wave       # generación de archivo de audio
import winsound   # producir sonido Beep de windows
import whisper    # reconocimiento automatico de voz
import time       # activar el sleep en segundos y (t/1000) para milisegundos
import msvcrt     # para esperar ENTER para continuar
import keyboard   # para utilizar las teclas del keyborad

nombre_archivo = 'Texto_captura2.txt'      # Nombre del archivo donde se guardaran las transcripciones
n = 1  # número de la grabaciones REC A
m = 1  # número de fragmento analizado con whisper  
chico = 16 # tiempo de espera para obtener el primer archivo de audio .wav
infinity = 0 # variable para 

def REC_A():    # GRABACIÓN #####################################################

    global n  # comando para utlizar la variable global n desiganda para las grabaciones A

    # CONFIGURACIÓN DEL ARCHIVO DE GRABACIÓN
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

    # INICIANDO GRABACIÓN
    """winsound.Beep(2000, 200)
    time.sleep(100/1000)
    winsound.Beep(2000, 200)"""

    fechaActual = datetime.datetime.now()
    fechaStrActual = datetime.datetime.strftime(
        fechaActual, '%d/%m/%Y %H:%M:%S')
    print(fechaStrActual + f" Grabando lado A número: {n}")

    seconds = 15    # tiempo de grabación en 10 segundos
    frames = []
    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate

    # FINALIZANDO GRABACIÓN
    """winsound.Beep(500, 300)
    time.sleep(100/1000)
    winsound.Beep(500, 300)"""

    fechaActual = datetime.datetime.now()
    fechaStrActual = datetime.datetime.strftime(
        fechaActual, '%d/%m/%Y %H:%M:%S')
    print(fechaStrActual + f" Grabación lado A numero: {n} terminada.")

    # GENERACION DE ARCHIVO DE AUDIO
    obj = wave.open(f"outputA{n}.wav", "wb")
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(RATE)
    obj.writeframes(b"".join(frames))
    obj.close
    print(f"Archivo outputA_{n}.wav generado.")
    n += 1
    if keyboard.is_pressed('q'):
            print("Dejando de grabar, se procede a solo transcribir..."+"\n")
            Whis_Infi()

def REC_B():    # GRABACIÓN #####################################################

    global n  # comando para utlizar la variable global n desiganda para las grabaciones B

    time.sleep(10)
    # CONFIGURACIÓN DEL ARCHIVO DE GRABACIÓN
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

    # INICIANDO GRABACIÓN
    """winsound.Beep(2000, 200)
    time.sleep(100/1000)
    winsound.Beep(2000, 200)"""

    fechaActual = datetime.datetime.now()
    fechaStrActual = datetime.datetime.strftime(
        fechaActual, '%d/%m/%Y %H:%M:%S')
    print(fechaStrActual + f" Grabando lado A numero: {n}")

    seconds = 15    # tiempo de grabación en 10 segundos
    frames = []
    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate

    # FINALIZANDO GRABACIÓN
    """winsound.Beep(500, 300)
    time.sleep(100/1000)
    winsound.Beep(500, 300)"""

    fechaActual = datetime.datetime.now()
    fechaStrActual = datetime.datetime.strftime(
        fechaActual, '%d/%m/%Y %H:%M:%S')
    print(fechaStrActual + f" Grabación lado A numero: {n} terminada.")

    # GENERACION DE ARCHIVO DE AUDIO
    obj = wave.open(f"outputA{n}.wav", "wb")
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(RATE)
    obj.writeframes(b"".join(frames))
    obj.close
    print(f"Archivo outputA_{n}.wav generado.")
    n += 1
    if keyboard.is_pressed('q'):
         print("Dejando de grabar, se procede a solo transcribir..."+"\n")
         Whis_Infi()
            

def Whis():  # WHISPER ##############################################################
    
    global m  # la variable global m desiganda para analizar los fragmentos de las grabaciones A

    fechaActual = datetime.datetime.now()
    fechaStrActual = datetime.datetime.strftime(
        fechaActual, '%d/%m/%Y %H:%M:%S')

    inicio = datetime.datetime.now()

    print(f"Analizando audio output{m}.wav")
    # SELECCIÓN DE MODELO small PARA RAPIDO, medium PARA PRECISIÓN, large PARA MAXIMA PRECISIÖN
    model = whisper.load_model('small')
    Texto = model.transcribe(f"outputA{m}.wav", language='Spanish', fp16=False)

    final = datetime.datetime.now()

    Tiempo = final - inicio

    print(f'Transcipción finalizada en {Tiempo.seconds} segundos'+"\n")
    print("''" + Texto["text"] + "''"+"\n")

    with open(nombre_archivo, '+a') as archivo:
        archivo.write(fechaStrActual + f" Audio#{m} " + Texto["text"]+"\n")
    print("Texto agregado a Texto_captura2.txt")
    m +=1


def Whis_Infi(): #Blucle hasta terminar traduccion de todos los audios.
     global m  # la variable global m desiganda para analizar los fragmentos de las grabaciones A
     global n  # la variable global m desiganda para analizar los fragmentos de las grabaciones A

     while m<n:
           
           fechaActual = datetime.datetime.now()
           fechaStrActual = datetime.datetime.strftime(
           fechaActual, '%d/%m/%Y %H:%M:%S')

           inicio = datetime.datetime.now()
           print(f"Analizando audio output{m}.wav")
           # SELECCIÓN DE MODELO small PARA RAPIDO, medium PARA PRECISIÓN, large PARA MAXIMA PRECISIÖN
           model = whisper.load_model('small')
           Texto = model.transcribe(f"outputA{m}.wav", language='Spanish', fp16=False)
           final = datetime.datetime.now()

           Tiempo = final - inicio

           print(f'Transcipción finalizada en {Tiempo.seconds} segundos'+"\n")
           print("''" + Texto["text"] + "''"+"\n")

           with open(nombre_archivo, '+a') as archivo:
                archivo.write(fechaStrActual + f" Audio#{m} " + Texto["text"]+"\n")
           print("Texto agregado a Texto_captura2.txt")
           m +=1
           if m == n:
                print("Transcripción COMPLETADA en Texto_captura2.txt")
                exit()
                

# MAIN ###################principal############################################
if __name__ == '__main__':
    # REC_A()
    # Whis()
    global chicom  # la variable global chico desiganda para esperar los fragmentos de las grabaciones A
    while True:

        h1 = threading.Thread(name="REC_A", target=REC_A)
        h2 = threading.Thread(name="REC_B", target=REC_B)
        h3 = threading.Thread(name="Whis", target=Whis)

        h1.start()
        h2.start()
        time.sleep(chico)
        h3.start()

        h1.join()
        h2.join()
        h3.join()

        chico = 0

        #print("Presione la tecla ""q"" para detener el programa.")
        #time.sleep(3)
        #if keyboard.is_pressed('q'):
            #break

    #print("Presione una tecla para continuar...")
    #msvcrt.getch()
