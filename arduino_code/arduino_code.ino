#include<Servo.h>

Servo x;

int width = 640, height = 480;  // total resolution of the video
int xpos = 90, ypos = 90;  // initial positions of both Servos
void setup() {

  Serial.begin(9600);
  x.attach(9);
  pinMode(13, OUTPUT);
  x.write(0);
  digitalWrite(8, LOW);
  
}

int angle = 45;
int increment = 5; 
int decrement = -5;

void loop() {
  if (Serial.available() > 0)
  {
    auto letter = Serial.read();
    if (letter == 'L') {
        x.write(angle+=decrement);
    }
    else if (letter == 'R') {  
        x.write(angle+=increment);
    }
    else if (letter == 'S') {
      digitalWrite(8, HIGH);
    }
  }
}
