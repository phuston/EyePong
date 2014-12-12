void setup()
{
  Serial.begin(9600);

}

void loop()
{
  int r_trigger = 400;
  int l_trigger = 625;
  int eyeIn = analogRead(A5);
  
//  Serial.println(eyeIn);
  if(eyeIn < l_trigger && eyeIn > r_trigger){
    Serial.println(0);
  }
  if(eyeIn > l_trigger){
    Serial.println(1);
  }
  else if(eyeIn < r_trigger){
    Serial.println(-1);
  }
  delay(100);
}

