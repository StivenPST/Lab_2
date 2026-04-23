# Laboratorio N°2

## ► Primer Punto ◄
### Codigo ChatBot
#### Concideraciones Previas
Este chatbot usa la API de Gemini. Para ejecutarlo se necesita una clave propia:
1. Ingresa a [Google AI Studio](https://aistudio.google.com/).
2. Genera una API Key.
3. Abre el archivo `chatbot_arduino.py`.
4. Reemplaza el texto `"API_KEY_GEMINI"` en la variable `API_KEY` por tu clave.

#### Configuración Conexion IA - Gemini
En esta parte del codigo se establece la conexion con la API Gemini haciendo uso de las variables:
- `API_KEY`: Esta clave autentica las solicitudes.
-  `MODEL`: Especifica la version de lenguaje que usara Gemini.
-  `URL`: Define el enlace donde se enviaran las solicitudes.

#### Segmentacion Especializada
Se define el comportamiento del ChatBot, indicando como debe responder a las solicitudes del usuario, asi como los comandos definidos para el control del Arduino.
Esta definicion se logra mediante la variable `SYSTEM_PROMPT`.

#### Funcion De Pregunta IA
Envia las preguntas del usuario generando un `payload` que junta el `SYSTEM_PROMPT` con la `pregunta` del usuario. Adicionalmente si ocurre algun error en este proceso el ChatBot lo informa al usuario.

#### Configuración Puerto Serial
Se establece conexion entre la maquina y un dispositivo **Arduino** mediante el puerto serial `COM4` (*El puerto varia dependiendo del sistema operativo y del conector USB que se utilice en la maquina*)
Esto permite que el ChatBot controle el Arduino.

#### Funcion Control Arduino
El ChatBot interactua con el Arduino segun las ordenes que envie el usuario:
- **encender verde:** Envia comando  `ON_VERDE` al Arduino.
- **encender rojo:** Envia comando  `ON_ROJO` al Arduino.
- **apagar verde:** Envia comando  `OFF_VERDE` al Arduino.
- **apagar rojo:** Envia comando  `OFF_ROJO` al Arduino.
- **Temperatura:** Envia el comando  `TEMP` para pedir la temperatura al Arduino y muestrarla al usuario.

#### Interfaz Del ChatBot
Se ejecuta el ChatBot para que interactue con el usuario. Se reciben las preguntas del usuario, se procesan a traves de la funcion `preguntar_gemini` mientras que procesa los comandos predefinidos con la funcion `controlar_arduino`.

### Materiales

### Montaje


## ► Segundo Punto ◄
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
<img width="1142" height="90" alt="image" src="https://github.com/user-attachments/assets/6662c9a4-f778-4908-b60b-217a28707b2f" /> \
<img width="981" height="227" alt="image" src="https://github.com/user-attachments/assets/433007e9-a91d-479d-9504-fbf9ac8d25ec" />

#### Configuración de pantalla
<img width="1153" height="128" alt="image" src="https://github.com/user-attachments/assets/ef41c6a5-7db5-44f0-bfbb-ddb2cf2c236c" /> \
<img width="1002" height="297" alt="image" src="https://github.com/user-attachments/assets/2f402001-d756-4805-a4e4-bbf200b213a9" />

#### Variables de juego
<img width="1116" height="122" alt="image" src="https://github.com/user-attachments/assets/0b91eaee-4720-4708-9a4f-5e334a413af7" /> \
<img width="801" height="219" alt="image" src="https://github.com/user-attachments/assets/e4121dd4-7438-4bbe-bbcc-acc1cc63adf3" />

#### Setup - Configuracion inicial
<img width="1187" height="512" alt="image" src="https://github.com/user-attachments/assets/f6fcd077-92a5-4c2e-94b1-415442cc9069" />

#### Dibujar elementos y mostrar puntuacion
<img width="1303" height="257" alt="image" src="https://github.com/user-attachments/assets/3c5b0b3f-fd73-48a3-a54b-9c3fc85582e0" />

#### Detección de colisión
<img width="1079" height="303" alt="image" src="https://github.com/user-attachments/assets/4f01d2c4-4dd4-4e50-bacd-e12c343e214d" />

#### Imagenes Laboratorio
<img width="1394" height="811" alt="image" src="https://github.com/user-attachments/assets/0547ecdf-8a6a-438f-b30b-fe477cc3017c" />

NOTA: Se anexa un video de funcionamiento


## ► Tercer Punto ◄
### Objetivo
### Materiales Necesarios
### Montaje hardware
### Codigo 
### Imagenes Laboratorio
<img width="1600" height="522" alt="image" src="https://github.com/user-attachments/assets/1f44a127-2bdd-455b-9d4b-92a0358ecbdb" />
