#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

int playerY = 50;
int obstacleX = 120;
int score = 0;
const int buttonPin = 2; // Conecta un pulsador aquí para saltar

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Dirección 0x3C es la común
    for(;;);
  }
  display.clearDisplay();
}

void loop() {
  display.clearDisplay();
  
  // Dibujar "Suelo"
  display.drawLine(0, 60, 128, 60, WHITE);

  // Leer botón para saltar
  if (digitalRead(buttonPin) == LOW && playerY == 50) {
    playerY = 20; // Salto
  }
  if (playerY < 50) playerY += 2; // Gravedad simple

  // Movimiento del obstáculo
  obstacleX -= 4;
  if (obstacleX < 0) {
    obstacleX = 120;
    score++;
  }

  // Dibujar Jugador y Obstáculo
  display.fillRect(10, playerY, 8, 8, WHITE);     // Jugador
  display.fillRect(obstacleX, 50, 6, 10, WHITE); // Obstáculo

  // Mostrar puntaje
  display.setCursor(0,0);
  display.setTextColor(WHITE);
  display.print("Score: "); display.print(score);

  // Colisión simple
  if (obstacleX < 18 && obstacleX > 2 && playerY > 40) {
    display.clearDisplay();
    display.setCursor(20, 30);
    display.print("GAME OVER");
    display.display();
    delay(2000);
    score = 0;
    obstacleX = 120;
  }

  display.display();
  delay(10);
}