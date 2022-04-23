int datafromUser=0;

int lr =  8;
int lg =  10;

int rr = 11;
int rg = 12;

void setup() {
  // put your setup code here, to run once:
  pinMode( lr, OUTPUT );
  pinMode( lg, OUTPUT );

  pinMode( rr, OUTPUT );
  pinMode( rg, OUTPUT );
  
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
  }

  if(datafromUser == '1')
  {
    digitalWrite( lr , HIGH );
    digitalWrite( rr , HIGH );
  }
  else if(datafromUser == '2')
  {
    digitalWrite( lr, LOW);
    digitalWrite( lg, HIGH );
  }
  else if(datafromUser == '3')
  {
    digitalWrite( lg, LOW);
    digitalWrite( lr, HIGH );
  }
  else if(datafromUser == '4')
  {
    digitalWrite( rr, LOW);
    digitalWrite( rg, HIGH );
  }
  else if(datafromUser == '5')
  {
    digitalWrite( rg, LOW);
    digitalWrite( rr, HIGH );
  }
  
}
