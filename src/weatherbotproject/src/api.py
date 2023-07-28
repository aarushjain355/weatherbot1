#!/usr/bin/env python3
import requests
import rospy
import PySimpleGUI as sg
from std_msgs.msg import String
from weatherbotproject.srv import WeatherService

if __name__ == "__main__":

    rospy.init_node("Service Client")
    rospy.wait_for_service("Weather_Update")
    weather_fetcher = rospy.ServiceProxy("Weather_Update", WeatherService)
    sg.theme('DarkBlue6')
    sg.set_options(font='verdana 15')

    layout = [
        [sg.Text('Weather Condition')],
        [sg.Button('Toronto'), sg.Button('Los Angeles'), sg.Button('Miami'), sg.Button('New York')],
        [sg.Text('Country:'), sg.Text(key='-COUNTRY-', size=15), sg.Push(), sg.Text('Local Time:'), sg.Text(key='-TIME-', size=15)],
        [sg.Text('Weather Now:'), sg.Text(key='-WEATHER-', size=15), sg.Push(), sg.Text('Feels Like:'), sg.Text(key='-FEELS_LIKE-', size=15)],
        [sg.Text('Condition:'), sg.Text(key='-CONDITION-', size=15), sg.Push(), sg.Text('Rain Chance:'), sg.Text(key='-RAIN-', size=15)],
        [sg.Text('Max:'), sg.Text(key='-MAX-', size=15), sg.Push(), sg.Text('Min:'), sg.Text(key='-MIN-', size=15)]
    ]
    window = sg.Window('Weather Condition', layout)

    def fetch_weather_data(city):
        url = f"http://api.weatherapi.com/v1/current.json?key=d20e61cc5f5545a1b1b155340232405&q={city}"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
        else:
            data = 0

        return data

    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event in ['Toronto', 'Los Angeles', 'Miami', 'New York']:
            city = event
            res = fetch_weather_data(city)

     
            weather_now = res['current']['temp_c']
            feels_like = res['current']['feelslike_c']
            condition_now = res['current']['condition']['text']
            status = weather_fetcher(condition_now)

            if status == 0:
                print("Service is not available, please try again")

            window['-WEATHER-'].update(weather_now)
            window['-FEELS_LIKE-'].update(feels_like)
            window['-CONDITION-'].update(condition_now)
           

    window.close()
