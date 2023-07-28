# ![GitHubEVA](https://github.com/Shikory/Eva/assets/42322745/574282f3-d2a1-4e4d-9676-6e4e7c1d020a)

El objetivo de este proyecto es convertir texto a voz para posteriormente utilizar Procesamiento Natural de lenguaje y poder utilizarlo como asistente virtual pero desde la computadora y no desde la nube.

El código **VTSR.py** esta basado en el codigo del Youtuber AMV (https://www.youtube.com/watch?v=8WKjX0dbh4E&t=976s&ab_channel=AVM) el cual es para la creación de un asistente virtual y su enlace de Github (https://github.com/avmmodules/virtual_assistant/tree/version1) utiliza dos librerias **speech_recognition** y **pyttsx3** funciona bien, solo que **speech_recognition** necesita conexión a internet para su correcto funcionamiento, la conversión a texto es aceptable, aunque el ruido debe de ser minimo y la dicción al hablar debe ser clara para obtener buenos resultados, por lo que para este proyecto no es apto este codigo. **pyttsx3** sin embargo convierte el texto a voz utilizando las voces instaladas en Windows por lo que es util esta libreria.

El codigo **audio.py** es del canal Sin Sentido (https://www.youtube.com/watch?v=gbVRIcVrnI0&ab_channel=SinSentido) con enlace a Github (https://github.com/metalheah2/grabacion_audio_python/tree/main) del Autor : Marco Jhoel Churata Torres. Utiliza tres librerias para realizar la conversión de audio a texto primero **pyaudio** lo utiliza para reproducir y grabar audio en una variedad de plataformas, como GNU/Linux, Microsoft Windows y Apple macOS. **wave** es un modulo que proporciona una interfaz conveniente para el formato de archivo Waveform Audio «WAVE» (o «WAV») y **Whisper** es un sistema de reconocimiento automático de voz (ASR) entrenado en 680.000 horas de datos supervisados ​​multilingües y multitarea recopilados de la web. Mostramos que el uso de un conjunto de datos tan grande y diverso conduce a una mayor solidez a los acentos, el ruido de fondo y el lenguaje técnico. Además, permite la transcripción en varios idiomas, así como la traducción de esos idiomas al inglés. Modelos de código abierto y código de inferencia que sirven como base para crear aplicaciones útiles y para futuras investigaciones sobre procesamiento de voz sólido. Estas librerias cumplen con el objetivo de ejecutarse en el pc pero consumen más recursos del sistema y es mas lento que el Speech Recognition aunque esto se puede mejorar con una GPU nvidia, por lo pronto es lo que más se acerca a nuestro sistema ideal. 

El enlace de Github para instalar Whisper (https://github.com/openai/whisper).

El próximo paso es usar el codigo **audio.py** y tratar de mezclarlo con el codigo **VTSR.py** para que repita las instrucciones que escuche.
El archivo todo.py graba un audio con extención *.wav y lo guarda luego lo procesa **Whisper** arrojando un texto que es leido por la libreria **pyttsx3**,se debe de ordenar el código porque repite dos veces la grabación, el tiempo de escucha es de 10 segundos aproximadamente y el de procesamiento unos 20 o 30 segundos, se debe de investigar como modificar estos tiempos para que el procesamiento sean en tiempo real. Por lo pronto estoysatisfecho con el avance. :)

Se anexa otro archivo **texvox.py** con un codigo simple que muestra como funciona la libreria **pyttsx3**.

En el canal de AMP Tech (https://www.youtube.com/watch?v=SaoDps2QBsI&ab_channel=AMPTech) dice los siguiente: "... el problema es que whisper no procesa streams de audio sino que procesa archivos que ya fueron grabados y salvados y para un asistente virtual pues si necesitamos que sea esto en tiempo real así que la manera en la que le voy a dar la vuelta a esto al menos por ahorita es que voy a hacer un código el cual esté grabando audio y cada 10 o 15 segundos corte la grabación salve el archivo procese eso utilizando whisper y vaya generando un transcript entonces si bien no va a ser en tiempo real al menos va a estar procesando en bloques de 10 o 15 segundos para grabar audio desde python la verdad es que no sabía muy bien qué era lo que tenía que hacer investigando vi una paquetería que se llama sound device la cual nos da esta posibilidad y lo único que tenemos que hacer es correr estos comandos el primero es para instalar sound device después el segundo es para instalar libport audio 2 que lo necesita sound device y por último vamos a hacer una grabación de sound device"

Los archivos **main.py** y **recorder.py** son los codigos que muestra AMP Tech en su video, sin embargo en mi caso al correr el programa no hace lo que se supone que debería hacer, aclarando que tampoco mostraba error.

En vista de que este ultimo código no me funcionó lo tomé como base y escribí un programa que si pudiera transribir lo que yo diga. El código se llama **todo.py** el inconveniente es que al momento de repetir mi dicción, menciona los parametros del archivo de audio, cosa que no es necesaria saber y que posteriormente modificaré para crear un archivo de texto donde se guarde solo lo que yo mencione.

Tomando como referencia los programas anteiores escribí otró código que graba 9 segundos de audio en formato **.wav** despúes lo guarda con nombre de **output.wav** posteriomente lo analiza con whisper e imprime en pantalla la trancripción y guarda la misma en un archivo de texto con nombre **Texto_captura.txt** en el cual se irán guardado las posteriores transcripciones.
