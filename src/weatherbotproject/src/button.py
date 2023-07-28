#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt32, String
from weatherbotproject.srv import ButtonPush, ButtonPushResponse
import PySimpleGUI as sg


num_of_times_button_pushed = 0
window = None  # Global window variable


def display_GUI():
    global window

    # Define the GUI layout
    layout = [
        [sg.Text("Number of Button Presses: ", size=(20, 1)), sg.Text("0", key="-COUNTER-", size=(10, 1))],
        [sg.Button("Press Me"), sg.Button("Reset Counter"), sg.Button("Exit")],
        [sg.Graph(canvas_size=(400, 200), graph_bottom_left=(0, 0), graph_top_right=(400, 200), key="-GRAPH-")]
    ]

    # Create the window if it doesn't exist
    if window is None:
        window = sg.Window("Button Counter", layout)

    # Initialize the button counter
    counter = num_of_times_button_pushed

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            window.close()
            break


def callback(request):
    global num_of_times_button_pushed

    response = ButtonPushResponse()
    response.vel = True
    num_of_times_button_pushed += 1

    if window is not None:
        window["-COUNTER-"].update(str(num_of_times_button_pushed))


    return response


if __name__ == "__main__":
    rospy.init_node("Button_Node")
    Button_Service = rospy.Service("Button Pressed", ButtonPush, callback)
    display_GUI() 
    rospy.spin()
