//#define gasSensor A0
#define smokeDetector 12
#define beeper 10
//String msgGas = "Gas Sensor: "
int gasSensorOutput, smokeDetectorOutput;

void setup() {
  // put your setup code here, to run once:
  //Start Serial
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  gasSensorOutput = analogRead(A0);
//  Serial.print("Gas Sensor : ");
  Serial.println(gasSensorOutput);
//  Serial.print(",");
//  delay(1000);
  smokeDetectorOutput = digitalRead(smokeDetector);
//  Serial.print("Smoke Detector : ");
//  Serial.println(smokeDetectorOutput);
  if (gasSensorOutput > 100) {
    digitalWrite(beeper, HIGH);
    delay(1000);
    digitalWrite(beeper, LOW);
    delay(100);
    digitalWrite(beeper, HIGH);
    delay(1000);
    digitalWrite(beeper, LOW);
    delay(100);
    digitalWrite(beeper, HIGH);
    delay(1000);
    digitalWrite(beeper, LOW);
    }
  delay(1000);
}
