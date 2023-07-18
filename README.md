# Eva

El objetivo de este proyecto es convertir texto a voz para posteriormente utilizar Procesamiento Natural de lenguaje y poder utilizarlo como asistente virtual pero desde la computadora y no desde la nube.

El código VTSR.py esta basado en el codigo del Youtuber AMV (https://www.youtube.com/watch?v=8WKjX0dbh4E&t=976s&ab_channel=AVM) el cual es para la creación de un asistente virtual y su enlace de Github (https://github.com/avmmodules/virtual_assistant/tree/version1) utiliza dos librerias **speech_recognition** y **pyttsx3** funciona bien, solo que **speech_recognition** necesita conexión a internet para su correcto funcionamiento, la conversión a texto es aceptable, aunque el ruido debe de ser minimo y la dicción al hablar debe ser clara para obtener buenos resultados, por lo que para este proyecto no es apto este codigo. **pyttsx3** sin embargo convierte el texto a voz utilizando las voces instaladas en Windows por lo que es util esta libreria.

El codigo audio.py es del canal Sin Sentido (https://www.youtube.com/watch?v=gbVRIcVrnI0&ab_channel=SinSentido) con enlace a Github (https://github.com/metalheah2/grabacion_audio_python/tree/main) del Autor : Marco Jhoel Churata Torres. Utiliza tres librerias para realizar la conversión de audio a texto primero **pyaudio** lo utiliza para reproducir y grabar audio en una variedad de plataformas, como GNU/Linux, Microsoft Windows y Apple macOS. **wave** es un modulo que proporciona una interfaz conveniente para el formato de archivo Waveform Audio «WAVE» (o «WAV») y **Whisper** es un sistema de reconocimiento automático de voz (ASR) entrenado en 680.000 horas de datos supervisados ​​multilingües y multitarea recopilados de la web. Mostramos que el uso de un conjunto de datos tan grande y diverso conduce a una mayor solidez a los acentos, el ruido de fondo y el lenguaje técnico. Además, permite la transcripción en varios idiomas, así como la traducción de esos idiomas al inglés. Modelos de código abierto y código de inferencia que sirven como base para crear aplicaciones útiles y para futuras investigaciones sobre procesamiento de voz sólido. Estas librerias cumplen con el objetivo de ejecutarse en el pc pero consumen más recursos del sistema y es mas lento que el Speech Recognition aunque esto se puede mejorar con una GPU nvidia, por lo pronto es lo que más se acerca a nuestro sistema ideal. 

El próximo paso es usar el codigo audio.py y tratar de mezclarlo con el codigo VTSR.py para que repita las instrucciones que escuche.
El archivo todo.py graba un audio con extención *.wav y lo guarda luego lo procesa **Whisper** arrojando un texto que es leido por la libreria **pyttsx3**,se debe de ordenar el código porque repite dos veces la grabación, el tiempo de escucha es de 10 segundos aproximadamente y el de procesamiento unos 20 o 30 segundos, se debe de investigar como modificar estos tiempos para que el procesamiento sean en tiempo real. Por lo pronto estoysatisfecho con el avance. :)

