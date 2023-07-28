#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/UInt32.h>
#include <weatherbotproject/ButtonPush.h>


ros::NodeHandle nh;
std_msgs::Float32MultiArray Sensor_Values;
ros::Publisher pub1("Sensor_values", &Sensor_Values);
ros::Subscriber<std_msgs::Float32MultiArray> sub1 ("Motor_Commands", &subscriber_callback1);
ros::ServiceClient<ButtonPush::Request, ButtonPush::Response> serviceClient("weatherbotproject/ButtonPush");
const int MotorPinA1 = 10;
const int MotorPinA2 = 11;
const int EnablePinA = 9;
const int MotorPinB1 = 12;
const int MotorPinB2 = 8;
const int EnablePinB = 6;
const int ButtonPin = 12;
const int NUM_OF_SENSORS = 5;
const int STARTING_SPEED = 255;
bool off = true;
const int irSensorPins[] = {2, 3, 4, 5, 7};
const int stop[] = {-1};
int arr[NUM_OF_SENSORS];

void readSensorData() {

    for (int i = 0; i < NUM_OF_SENSORS; i++) {
        arr[i] = digitalRead(irSensorPins[i]);   
    }
    pub1.publish(&arr[0], NUM_OF_SENSORS);

}
void subscriber_callback1(const std_msgs::Float32MultiArray& Motor_Commands) {

    motor_speed = Motor_Commands[0];
    direction = Motor_Commands[1];
    rotate_right = Motor_Commands[2];

    if (rotate_right) {
        
    } else {

      if (direction == 1) {
        analogWrite(EnablePinA, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinA1, HIGH);
        digitalWrite(MotorPinA2, LOW);
        analogWrite(EnablePinB, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinB1, LOW);
        digitalWrite(MotorPInB2, HIGH);

      } else if (direction == -1) {
        analogWrite(EnablePinA, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinA1, LOW);
        digitalWrite(MotorPinA2, HIGH);
        analogWrite(EnablePinB, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinB1, HIGH);
        digitalWrite(MotorPInB2, LOW);
      } else {

        analogWrite(EnablePinA, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinA1, HIGH);
        digitalWrite(MotorPinA2, LOW);
        analogWrite(EnablePinB, STARTING_SPEED - motor_speed);
        digitalWrite(MotorPinB1, HIGH);
        digitalWrite(MotorPInB2, LOW);
      }
    }

}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  nh.initNode();
  motor_subscribe = nh.subscribe("Motor_Commands", &subscriber_callback1);
  nh.advertise(pub1);
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
  
  while (!nh.connected()) {
    nh.spinOnce();
  }
}

void loop() {
  // put your main code here, to run repeatedly:

    weatherbotproject::ButtonPush::Request req;
    weatherbotproject::ButtonPush::Response res;


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
            response.check = true;
            nh.subscribe(motor_subscribe);
            readSensorData();

        }
    } else {
        pub1.publish(stop);
        nh.unsubscribe(motor_subscribe);
        analogWrite(EnablePinA, 0);
        digitalWrite(MotorPinA1, LOW);
        digitalWrite(MotorPinA2, LOW);
        analogWrite(EnablePinB, 0);
        digitalWrite(MotorPinB1, LOW);
        digitalWrite(MotorPInB2, LOW);

      
    } 

    delay(100);
}
