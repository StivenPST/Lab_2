import requests  # Instalar -> pip install requests
import json
import serial    # Instalar -> pip install pyserial
import time

# CONFIGURACION CONEXION IA - GEMINI
API_KEY = "API_KEY_GEMINI"  # Genera tu propia API KEY en https://aistudio.google.com/
MODELO = "models/gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/{MODELO}:generateContent?key={API_KEY}"

# PROMPT DEL CHATBOT
SYSTEM_PROMPT = """
Eres un asistente que puede responder preguntas y además controlar un Arduino:
- Si el usuario dice 'encender verde', envías comando ON_VERDE.
- Si el usuario dice 'apagar verde', envías comando OFF_VERDE.
- Si el usuario dice 'encender rojo', envías comando ON_ROJO.
- Si el usuario dice 'apagar rojo', envías comando OFF_ROJO.
- Si el usuario pregunta por la temperatura, envías comando TEMP y devuelves el valor recibido.
Tu comportamiento debe ser amigable y cordial:
- Si el usuario te saluda (ej. 'hola', 'buenas', 'qué tal'), responde saludando y explicando que eres un asistente para controlar Arduino.
- Si el usuario pregunta '¿en qué me puedes ayudar?' o algo similar, responde indicando que puedes encender/apagar luces y medir temperatura.
Adicionalmente le muestras la lista de comandos definidos para dichas funciones.
- Si el usuario pregunta sobre otros temas, responde amablemente que solo asesoras en el control de Arduino.
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
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"❌ Error {response.status_code}: {res_json.get('error', {}).get('message', 'Error desconocido')}"
    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"

# CONFIGURACION PUERTO SERIAL (ajustar port según tu sistema)
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)  # Windows
time.sleep(2)  # espera inicial para que Arduino reinicie

# FUNCION CONTROL ARDUINO
def controlar_arduino(mensaje_usuario):
    msg = mensaje_usuario.lower()

    if "encender verde" in msg:
        arduino.write(b'ON_VERDE\n')
        return "✅ Luz verde encendida"
    elif "apagar verde" in msg:
        arduino.write(b'OFF_VERDE\n')
        return "✅ Luz verde apagada"
    elif "encender rojo" in msg:
        arduino.write(b'ON_ROJO\n')
        return "✅ Luz roja encendida"
    elif "apagar rojo" in msg:
        arduino.write(b'OFF_ROJO\n')
        return "✅ Luz roja apagada"
    elif "temperatura" in msg or "medir temperatura" in msg:
        arduino.write(b'TEMP\n')
        temp = arduino.readline().decode().strip()
        return f"🌡️ La temperatura actual es {temp} °C"
    else:
        return None

# INTERFAZ DEL CHATBOT
print("🤖 Chatbot Sistemas Digitales (Gemini API + Arduino)")
print("Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "chau", "chao", "adios", "terminar", "gracias", "eso es todo"]:
        print("Fue un placer ayudarte.\n 👋 Chat finalizado.")
        break

    respuesta_local = controlar_arduino(user_input)
    if respuesta_local:
        print(f"\n🤖 Bot: {respuesta_local}\n")
        continue

    respuesta = preguntar_gemini(user_input)
    print(f"\n🤖 Bot: {respuesta}\n")



