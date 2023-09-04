#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/UInt32.h>
#include <std_msgs/String.h>
#include <Servo.h>
#include "ButtonPush.h"


ros::NodeHandle nh;
std_msgs::Float32MultiArray Sensor_Values;
ros::Publisher pub1("Sensor_values", &Sensor_Values);
const int MotorPinA1 = 11;
const int MotorPinA2 = 12;
const int EnablePinA = 10;
const int MotorPinB1 = 8;
const int MotorPinB2 = 9;
const int EnablePinB = 6;
Servo myServo;
bool Flag;
const int ServoPin = 13;
const int ButtonPin = A0;
const int BuzzerPin = A1;
const int ledPin = A2;
bool buzzer = false;
bool led = false;
bool servo = false;
const int NUM_OF_SENSORS = 5;
const int STARTING_SPEED = 255;
bool off = true;
const int irSensorPins[] = {2, 3, 4, 5, 7};
std_msgs::Float32MultiArray stop;

std_msgs::Float32MultiArray arr;

void readSensorData() {

    for (int i = 0; i < NUM_OF_SENSORS; i++) {
        arr.data[i] = digitalRead(irSensorPins[i]);   
    }
    pub1.publish(&arr);

}

void action_callback(const std_msgs::String& action) {


  if (action.data == "fire") {
    buzzer = true;
  } else if (action.data == "hot") {
    servo = true;
  } else if (action.data == "cold") {
    led = true;
  } else if (action.data == "neutral") {
    led = false;
    buzzer = false;
    servo = false;
  }
}

void subscriber_callback1(const std_msgs::Float32MultiArray& Motor_Commands) {

  if (Flag) {
    float motor_speed = Motor_Commands.data[0];
    bool rotate_right = Motor_Commands.data[2];

    if (rotate_right) {
        
    } else {

      if (Motor_Commands.data[1] == 1) {
        analogWrite(EnablePinA, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinA1, HIGH);
        digitalWrite(MotorPinA2, LOW);
        analogWrite(EnablePinB, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinB1, LOW);
        digitalWrite(MotorPinB2, HIGH);

      } else if (Motor_Commands.data[1] == -1) {
        analogWrite(EnablePinA, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinA1, LOW);
        digitalWrite(MotorPinA2, HIGH);
        analogWrite(EnablePinB, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinB1, HIGH);
        digitalWrite(MotorPinB2, LOW);
      } else {

        analogWrite(EnablePinA, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinA1, HIGH);
        digitalWrite(MotorPinA2, LOW);
        analogWrite(EnablePinB, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinB1, HIGH);
        digitalWrite(MotorPinB2, LOW);
      }
    }
  }
}

ros::Subscriber<std_msgs::Float32MultiArray> sub1 ("Motor_Commands", &subscriber_callback1);
ros::Subscriber<std_msgs::String> motion_sub ("position", &action_callback);
ros::ServiceClient<ButtonPush::Request, ButtonPush::Response> serviceClient("ButtonPush");



void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  nh.initNode();
  nh.getHardware()->setBaud(9600);
  nh.advertise(pub1);
  nh.subscribe(sub1);
  for (int i = 0; i < NUM_OF_SENSORS; i++) {
    pinMode(irSensorPins[i], INPUT);
  }
  pinMode(MotorPinA1, OUTPUT);
  pinMode(MotorPinA2, OUTPUT);
  pinMode(EnablePinA, OUTPUT);
  pinMode(MotorPinB1, OUTPUT);
  pinMode(MotorPinB2, OUTPUT);
  pinMode(EnablePinB, OUTPUT);
  pinMode(ButtonPin, INPUT);
  pinMode(BuzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  myServo.attach(ServoPin);


  
  while (!nh.connected()) {
    nh.spinOnce();
  }
}

void loop() {
  // put your main code here, to run repeatedly:

    myServo.write(0);
    delay(1000);

    if (servo) {

        myServo.write(90);
        delay(1000); 
        myServo.write(180);
        delay(1000); 
    }

    if (buzzer) {

        analogWrite(BuzzerPin, 128);
    } else {
        analogWrite(BuzzerPin, 0);
    }

    if (led) {
        analogWrite(ledPin, 128);
    } else {
        analogWrite(BuzzerPin, 0);
    }

    if (digitalRead(ButtonPin) == LOW) {

      if (off) {
        off = false;

      } else {
        off = true;
      }
    }
    if (off == false) {

        ButtonPush::Request request;
        ButtonPush::Response response;
        request.push = 1;

        if (serviceClient.call(request)) {
            Flag = true;
            readSensorData();

        }
    } else {
        stop.data_length = 1;
        stop.data[0] = -1;
        pub1.publish(&stop);
        Flag = false;
        analogWrite(EnablePinA, 0);
        digitalWrite(MotorPinA1, LOW);
        digitalWrite(MotorPinA2, LOW);
        analogWrite(EnablePinB, 0);
        digitalWrite(MotorPinB1, LOW);
        digitalWrite(MotorPinB2, LOW);

      
    } 

    delay(100);
}
