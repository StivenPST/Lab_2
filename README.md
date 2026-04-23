# Laboratorio N°2

## Primer Punto
### Concideraciones Previas
Este chatbot usa la API de Gemini. Para ejecutarlo se necesita una clave propia:
1. Ingresa a [Google AI Studio](https://aistudio.google.com/).
2. Genera una API Key.
3. Abre el archivo `Codigo Bot_Arduino_V1.py`.
4. Reemplaza el texto `"API_KEY_GEMINI"` en la variable `API_KEY` por tu clave.

### Configuración Conexion IA - Gemini
En esta parte del codigo se establece la conexion con la API Gemini haciendo uso de las variables:
- `API_KEY`: Esta clave autentica las solicitudes.
-  `MODEL`: Especifica la version de lenguaje que usara Gemini.
-  `URL`: Define el enlace donde se enviaran las solicitudes.

### Segmentacion Especializada
Se define el comportamiento del ChatBot, indicando como debe responder a las solicitudes del usuario, asi como los comandos definidos para el control del Arduino.
Esta definicion se logra mediante la variable `SYSTEM_PROMPT`.

### Funcion De Pregunta IA
Envia las preguntas del usuario generando un `payload` que junta el `SYSTEM_PROMPT` con la `pregunta` del usuario. Adicionalmente si ocurre algun error en este proceso el ChatBot lo informa al usuario.

### Configuración Puerto Serial
Se establece conexion entre la maquina y un dispositivo **Arduino** mediante el puerto serial `COM4` (*El puerto varia dependiendo del sistema operativo y del conector USB que se utilice en la maquina*)
Esto permite que el ChatBot controle el Arduino.

### Funcion Control Arduino
El ChatBot interactua con el Arduino segun las ordenes que envie el usuario:
- **Encender Luz:** Envia comando  `ON` al Arduino.
- **Apagar Luz:** Envia comando  `OFF` al Arduino.
- **Temperatura:** Pide la temperatura al Arduino y la muestra al usuario.

### Interfaz Del ChatBot
Se ejecuta el ChatBot para que interactue con el usuario. Se reciben las preguntas del usuario, se procesan a traves de la funcion `preguntar_gemini` 


## Segundo Punto
### Objetivo
Desarrollar un juego interactivo sencillo utilizando una pantalla OLED y una placa Arduino UNO.

### Materiales Necesarios
<img width="926" height="478" alt="image" src="https://github.com/user-attachments/assets/0147ee6b-1b42-4393-b29e-56b2ab4a8773" />

### Montaje hardware
La pantalla OLED SSD1306 se conecta mediante el protocolo I2C:
<img width="1121" height="325" alt="image" src="https://github.com/user-attachments/assets/8ba57b71-f970-40cf-8a4e-79ef3bddb27e" />

### Codigo del juego
#### Inclusion de librerias
En Arduino IDE, instalar las siguientes librerías:
Instalar "Wire.h"
Instalar "Adafruit SSD1306"
Instalar "Adafruit GFX Library"
<img width="1142" height="90" alt="image" src="https://github.com/user-attachments/assets/6662c9a4-f778-4908-b60b-217a28707b2f" />
<img width="981" height="227" alt="image" src="https://github.com/user-attachments/assets/433007e9-a91d-479d-9504-fbf9ac8d25ec" />

### Configuración de pantalla
<img width="1153" height="128" alt="image" src="https://github.com/user-attachments/assets/ef41c6a5-7db5-44f0-bfbb-ddb2cf2c236c" />
<img width="1002" height="297" alt="image" src="https://github.com/user-attachments/assets/2f402001-d756-4805-a4e4-bbf200b213a9" />



## Tercer Punto
