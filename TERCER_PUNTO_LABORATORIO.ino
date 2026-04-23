void setup() {
  // Iniciamos la comunicación serial a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Leemos el valor analógico del pin A0
  int sensorcny = analogRead(A0); // Almacena el valor

  // Lógica de detección según tu imagen:
  // Si el valor está entre 50 y 150, se considera negro
  if (sensorcny > 50 && sensorcny < 150) {
    Serial.print("Es negro ");
  } 
  // Si el valor es mayor a 150, se considera blanco
  else if (sensorcny > 150) {
    Serial.print("Blanco ");
  }

  // Muestra el valor numérico actual para ayudar a la calibración
  Serial.println(sensorcny); 
  
  // Pequeña pausa de 100 milisegundos
  delay(100);
}