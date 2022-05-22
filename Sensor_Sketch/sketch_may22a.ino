#include <Wire.h> 
#include <LiquidCrystal_I2C.h>


int datafromUser = 0;
int x1 = 0;
int input1 = A0;
int state1= 0;

int x2 = 0;
int input2 = A1;
int state2 = 0;

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup()
{
  // initialize the LCD
  Serial.begin(9600);
  lcd.begin();
  lcd.clear();

  // Turn on the blacklight and print a message.
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print(x1);
  lcd.print(" Sensor 1 ");
  
  lcd.setCursor(0, 1);
  lcd.print(x2);
  lcd.print(" Sensor 2 ");
}

void loop()
{

 int counter1 = digitalRead(A0);
 int counter2 = digitalRead(A1);

 if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
    //Serial.print(datafromUser);
  }

  // sensor
  if(datafromUser == '1'){
    
      Serial.println(x1);
      
      delay(10);
      
      Serial.println(x2);
      datafromUser = 0;      
    }

    if(datafromUser == '2'){
      x1=0;
      x2=0;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(x1);
      lcd.print(" Sensor 1 ");
      
      lcd.setCursor(0, 1);
      lcd.print(x2);
      lcd.print(" Sensor 2 ");
      
      datafromUser = 0;      
    }

    

  // Sensor 1
  if (state1 == 0)
  {
    switch (counter1) {

      case 1 : state1 = 1; lcd.setCursor (0, 0); x1 = x1 + 1; lcd.print(x1); break;
      case 0 : state1 = 0; break;

    }
  }

  // Sensor 2
  if (state2 == 0)
  {
    switch (counter2) {

      case 1 : state2 = 1; lcd.setCursor (0, 1); x2 = x2 + 1; lcd.print(x2); break;
      case 0 : state2 = 0; break;

    }
  }

  // Reseting Sensor 1 State
  if (counter1 == LOW) {
    state1 = 0;
  }

  // Reseting Sensor 2 State
  if (counter2 == LOW) {
    state2 = 0;
  }
}
