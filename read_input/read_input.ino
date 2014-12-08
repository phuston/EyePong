int hashPin = 7;
int delayTime = 20;

void setup()
{
  Serial.begin(9600);
  pinMode(hashPin, INPUT);
}

void loop()
{
  int l_trigger = -1;
  int r_trigger = 1;
  
  int eyeIn = digitalRead(hashPin);
  
  if(eyeIn < l_trigger){
    Serial.println(1);
  }
  else if(eyeIn > r_trigger){
    Serial.println(0);
  }
}

