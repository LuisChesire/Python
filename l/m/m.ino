void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(A0);
  int  value1=100*value*5/1023;
  Serial.println(value1);
  delay(2000);
}
