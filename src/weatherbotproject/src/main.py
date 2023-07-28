#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt32, Float32MultiArray, String
from weatherbotproject.srv import WeatherService, WeatherServiceResponse

kP = 0
kI = 0
kD = 0
previous_error = 0
integral = 0
value = None
current_value = 0
clear_and_sunny = ["Clear Sky", "Sunny"]
cloudy_and_overcast = ["Partly cloudy", "Cloudy", "Overcast"]
precipitation = ["Light rain", "Moderate rain", "Heavy rain", "Showers", "Light snow", "Moderate snow", "Heavy snow", "Snow showers"]
severe_weather = ["Mist", "Foggy", "Hazy", "Thunderstorms", "Tornado", "Dust storm", "Sandstorm"]


def generate_PID_LOOP(direction, rotateright):

    global current_value, previous_error, current_value, integral
    motor_publisher = rospy.Publisher ("Motor Commands", Float32MultiArray, queue_size=10)
    list1 = []
    if direction == "straight":
        setpoint = 255
    else:
        setpoint = 155


    error = setpoint - current_value
    proportional = kP * error
    integral = integral + kI * error
    derivative = kD * (error - previous_error)
    motor_speed = proportional + integral + derivative
    previous_error = error 
    current_value = current_value + motor_speed
    
    list1.append(motor_speed)
    if direction == "right":
        list1.append(1)
    elif direction == "left":
        list1.append(-1)
    else:
        list1.append(0)
    if rotateright:
        list1.append(1)
    else:
        list1.append(0)
    
    motor_publisher.publish(list1)        


def sensor_callback(sensor_values):
    
    if sensor_values.data[0] == -1:
        current_value = 0
    else: 
        left = 0
        right = 0
        for i in range(2):
            if sensor_values.data[i] == 0:
                left += 1
            if sensor_values.data[4 - i] == 0:
                right += 1
        
        if left == 0 and right == 0 and sensor_values.data[2] == 1:

            generate_PID_LOOP("straight", False)

        else:
            if left > right:
                generate_PID_LOOP("right", False)
            elif right > left:
                generate_PID_LOOP("left", False)
            else:
                if sensor_values.data[2] == 0:
                    generate_PID_LOOP("right", True)
                
                else:
                    generate_PID_LOOP("straight", False)

    
        

def status_code(request):

    global kP, kI, kD, previous_error, integral_sum 
    response = WeatherServiceResponse()
    try:

        value = request.Weather
        response.ok = 1
    except AttributeError:

        response.ok = 0

    if value in clear_and_sunny:
        kP = 0.9
        kI = 0.6
        kD = 0.2

    elif value in cloudy_and_overcast:
        kP = 1.1
        kI = 0.9
        kD = 0.4

    elif value in precipitation:
        kP = 1.3
        kI = 1.2
        kD = 0.6

    else:
        kP = 1.8
        kI = 1.6
        kD = 1.0

    previous_error = 0
    integral_sum = 0
    rospy.Subscriber("Sensor_values", Float32MultiArray, sensor_callback)
    
    return response 

if __name__ == "__main__":

    rospy.init_node("Main_Node")
    Weather_Service = rospy.Service("Weather_Update", WeatherService, status_code)
   

    rospy.spin()
