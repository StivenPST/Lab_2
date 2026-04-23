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

### Materiales Necesarios
<img width="461" height="378" alt="image" src="https://github.com/user-attachments/assets/c033335f-8cca-4db6-b1bf-068668fffd28" />

### Montaje hardware
La pantalla OLED SSD1306 se conecta mediante el protocolo I2C:
<img width="260" height="262" alt="image" src="https://github.com/user-attachments/assets/80018b04-c9dc-40f1-81da-edc92bd7818d" />

### Librerias para el codigo
En Arduino IDE, instalar las siguientes librerías
<img width="487" height="88" alt="image" src="https://github.com/user-attachments/assets/f0e8c3cc-f451-4f91-9ed9-ca2e3d23550b" />
<img width="522" height="132" alt="image" src="https://github.com/user-attachments/assets/5b6ec102-010e-4351-8db3-ad270a93a847" />

### Codigo del juego


## Tercer Punto
