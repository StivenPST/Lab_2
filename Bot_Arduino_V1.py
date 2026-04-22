import requests #Instalar -> pip install requests
import json
import serial #Instalar -> pip install pyserial
import time

# CONFIGURACION CONEXION IA - GEMINI
API_KEY = "AIzaSyClxsZpwrXlm5cSDh3_cfIU45E9Y1jEoYo" # Se debe generar una API KEY propia en el enlace https://aistudio.google.com/
MODELO = "models/gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/{MODELO}:generateContent?key={API_KEY}"

# SEGMENTACION ESPECIALIZADA
SYSTEM_PROMPT = """
Eres un asistente que puede responder preguntas y además controlar un Arduino:
- Si el usuario dice 'encender luz', envías comando ON.
- Si el usuario dice 'apagar luz', envías comando OFF.
- Si el usuario pregunta por la temperatura, envías comando TEMP y devuelves el valor recibido.
Tu comportamiento debe ser amigable y cordial:
- Si el usuario te saluda (ej. 'hola', 'buenas', 'qué tal'), responde saludando y explicando que eres un asistente para controlar arduino.
- Si el usuario pregunta '¿en qué me puedes ayudar?' o algo similar, responde indicando que puedes explicar y resolver dudas sobre:
 El control del arduino y le diras que puedes encender luz, apagar luz, medir temperatura.
- Si el usuario pregunta sobre otros temas, responde amablemente que solo asesoras y controlar arduino.
"""

# FUNCION DE PREGUNTA IA - GEMINI
def preguntar_gemini(mensaje_usuario):
    payload = {
        "contents": [{
            "parts": [
                {"text": SYSTEM_PROMPT},
                {"text": f"Pregunta: {mensaje_usuario}"}
            ]
        }]
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        res_json = response.json()

        if response.status_code == 200:
            # Gemini devuelve candidatos, se toma el primero
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"❌ Error {response.status_code}: {res_json.get('error', {}).get('message', 'Error desconocido')}"
    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"
    
# CONFIGURACION PUERTO SERIAL (ajustar port según tu sistema)
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)  # Windows

# FUNCION CONTROL ARDUINO
def controlar_arduino(mensaje_usuario):
    if "encender" in mensaje_usuario.lower():
        arduino.write(b'ON\n')
        return "✅ Luz encendida"
    elif "apagar" in mensaje_usuario.lower():
        arduino.write(b'OFF\n')
        return "✅ Luz apagada"
    elif "temperatura" in mensaje_usuario.lower():
        arduino.write(b'TEMP\n')
        temp = arduino.readline().decode().strip()
        return f"🌡️ La temperatura actual es {temp} °C"
    else:
        return None
    

# INTERFAZ DEL CHATBOT
print("🤖 Chatbot Sistemas Digitales (Gemini API)")
print("Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "chau", "chao", "adios", "terminar", "gracias", "eso es todo"]:
        print("Fue un placer ayudarte.\n 👋 Chat finalizado.")
        break
    respuesta = preguntar_gemini(user_input)


    print(f"\n🤖 Bot: {respuesta}\n")
