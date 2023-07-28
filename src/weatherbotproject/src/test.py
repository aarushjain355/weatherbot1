import PySimpleGUI as sg

num_of_buttons_pushed = 0

def GUI():

    # Define the GUI layout
    layout = [
        [sg.Text("Number of Button Presses: ", size=(20, 1)), sg.Text("0", key="-COUNTER-", size=(10, 1))],
        [sg.Button("Press Me"), sg.Button("Reset Counter"), sg.Button("Exit")],
        [sg.Graph(canvas_size=(400, 200), graph_bottom_left=(0, 0), graph_top_right=(400, 200), key="-GRAPH-")]
    ]

    # Create the window
    window = sg.Window("Button Counter", layout)

    # Initialize the 
    # 
    # button counter
    counter = num_of_buttons_pushed 

    # Initialize the graph coordinates
    graph_coords = [(0, 0)]

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        
        window["-COUNTER-"].update(str(counter))

if __name__ == "__main__":

    for i in range(5):

        num_of_buttons_pushed += 1
        GUI()
