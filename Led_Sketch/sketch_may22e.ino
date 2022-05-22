int lr =  8;
int ly =  9;
int lg =  10;

int rr = 11;
int ry = 12;
int rg = 13;

int datafromUser = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9000);
  pinMode( lr, OUTPUT );
  pinMode( lg, OUTPUT );
  pinMode( ly, OUTPUT );

  pinMode( rr, OUTPUT );
  pinMode( rg, OUTPUT );
  pinMode( ry, OUTPUT );
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
    //Serial.print(datafromUser);
  }
  //led
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
    digitalWrite( ly, LOW);
    digitalWrite( lr, HIGH );
  }                                                                          
  else if(datafromUser == '4')
  {
    digitalWrite( rr, LOW);
    digitalWrite( rg, HIGH );
  }
  else if(datafromUser == '5')
  {
    digitalWrite( ry, LOW);
    digitalWrite( rr, HIGH );
  }
  else if(datafromUser == '6')
  {
    digitalWrite( lg, LOW);
    digitalWrite( ly, HIGH );
  }

  else if(datafromUser == '7')
  {
    digitalWrite( rg, LOW);
    digitalWrite( ry, HIGH );
  }
  
}
