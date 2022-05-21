import PySimpleGUI as sg
layout = [[sg.Text("Hello from PySimpleGUI")],[sg.Button("OK")]] #add button and Text on screen

#create the window
window = sg.Window("Demo",layout)

# Create an Event Loop
while True:
    event, values = window.read()
    #End program if user closes window or presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break   #break out of the loop

window.close()   #close the window