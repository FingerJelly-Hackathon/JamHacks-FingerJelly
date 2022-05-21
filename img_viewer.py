#img_viewr.py

import PySimpleGUI as sg
import os.path

#first the winow layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size = (25,1), enable_events = True, key = "-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values = [],enable_events = True, size = (40,20), key = "-FILE LIST-"
        )

    ],

]

#for now will only show the name of the file that was chosen

image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size = (40,1), key = "-TOUT-")],
    [sg.Image(key = "-IMAGE-")],
]

#----Full Layout-----

layout = [
    [
        sg.Column(file_list_column),
        sg.Vsperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

#Run The Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event ==sg.WIN_CLOSED:    # act of pressing the close button or exit button       
        break

    #Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            #Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png",".gif"))
        ]
        window["-FILE LIST-"].update(fnmaes)
    elif event=="-FILE LIST-": #A file was chosen from the LISTBOX
        try:
            filename = os.path.join(
                values ["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename = filename)
        
        except:
            pass
window.close()
            